"""
    sphinx.ext.autodoc.directive
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2007-2021 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import warnings
from typing import Any, Callable, Dict, List, Set, Type

from docutils import nodes
from docutils.nodes import Element, Node
from docutils.parsers.rst.states import RSTState
from docutils.statemachine import StringList
from docutils.utils import Reporter, assemble_option_dict

from sphinx.config import Config
from sphinx.deprecation import RemovedInSphinx50Warning, RemovedInSphinx60Warning
from sphinx.environment import BuildEnvironment
from sphinx.ext.autodoc import Documenter, Options
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective, switch_source_input
from sphinx.util.nodes import nested_parse_with_titles

logger = logging.getLogger(__name__)


# common option names for autodoc directives
AUTODOC_DEFAULT_OPTIONS = ['members', 'undoc-members', 'inherited-members',
                           'show-inheritance', 'private-members', 'special-members',
                           'ignore-module-all', 'exclude-members', 'member-order',
                           'imported-members']

AUTODOC_EXTENDABLE_OPTIONS = ['members', 'private-members', 'special-members',
                              'exclude-members']


class DummyOptionSpec(dict):
    """An option_spec allows any options."""

    def __bool__(self) -> bool:
        """Behaves like some options are defined."""
        return True

    def __getitem__(self, key: str) -> Callable[[str], str]:
        return lambda x: x


class DocumenterBridge:
    """A parameters container for Documenters."""

    def __init__(self, env: BuildEnvironment, reporter: Reporter, options: Options,
                 lineno: int, state: Any) -> None:
        self.env = env
        self._reporter = reporter
        self.genopt = options
        self.lineno = lineno
        self.record_dependencies: Set[str] = set()
        self.result = StringList()
        self.state = state

    def warn(self, msg: str) -> None:
        warnings.warn('DocumenterBridge.warn is deprecated.  Plase use sphinx.util.logging '
                      'module instead.',
                      RemovedInSphinx60Warning, stacklevel=2)
        logger.warning(msg, location=(self.env.docname, self.lineno))

    @property
    def filename_set(self) -> Set:
        warnings.warn('DocumenterBridge.filename_set is deprecated.',
                      RemovedInSphinx60Warning, stacklevel=2)
        return self.record_dependencies

    @property
    def reporter(self) -> Reporter:
        warnings.warn('DocumenterBridge.reporter is deprecated.',
                      RemovedInSphinx50Warning, stacklevel=2)
        return self._reporter


def process_documenter_options(documenter: Type[Documenter], config: Config, options: Dict
                               ) -> Options:
    """Recognize options of Documenter from user input."""
    for name in AUTODOC_DEFAULT_OPTIONS:
        if name not in documenter.option_spec:
            continue
        else:
            negated = options.pop('no-' + name, True) is None
            if name in config.autodoc_default_options and not negated:
                if name in options and isinstance(config.autodoc_default_options[name], str):
                    # take value from options if present or extend it
                    # with autodoc_default_options if necessary
                    if name in AUTODOC_EXTENDABLE_OPTIONS:
                        if options[name] is not None and options[name].startswith('+'):
                            options[name] = ','.join([config.autodoc_default_options[name],
                                                      options[name][1:]])
                else:
                    options[name] = config.autodoc_default_options[name]

            elif options.get(name) is not None:
                # remove '+' from option argument if there's nothing to merge it with
                options[name] = options[name].lstrip('+')

    return Options(assemble_option_dict(options.items(), documenter.option_spec))


def parse_generated_content(state: RSTState, content: StringList, documenter: Documenter
                            ) -> List[Node]:
    """Parse a generated content by Documenter."""
    with switch_source_input(state, content):
        if documenter.titles_allowed:
            node: Element = nodes.section()
            # necessary so that the child nodes get the right source/line set
            node.document = state.document
            nested_parse_with_titles(state, content, node)
        else:
            node = nodes.paragraph()
            node.document = state.document
            state.nested_parse(content, 0, node)

        return node.children


class AutodocDirective(SphinxDirective):
    """A directive class for all autodoc directives. It works as a dispatcher of Documenters.

    It invokes a Documenter on running. After the processing, it parses and returns
    the generated content by Documenter.
    """
    option_spec = DummyOptionSpec()
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True

    def run(self) -> List[Node]:
        reporter = self.state.document.reporter

        try:
            source, lineno = reporter.get_source_and_line(self.lineno)  # type: ignore
        except AttributeError:
            source, lineno = (None, None)
        logger.debug('[autodoc] %s:%s: input:\n%s', source, lineno, self.block_text)

        # look up target Documenter
        objtype = self.name[4:]  # strip prefix (auto-).
        doccls = self.env.app.registry.documenters[objtype]

        # process the options with the selected documenter's option_spec
        try:
            documenter_options = process_documenter_options(doccls, self.config, self.options)
        except (KeyError, ValueError, TypeError) as exc:
            # an option is either unknown or has a wrong type
            logger.error('An option to %s is either unknown or has an invalid value: %s' %
                         (self.name, exc), location=(self.env.docname, lineno))
            return []

        # generate the output
        params = DocumenterBridge(self.env, reporter, documenter_options, lineno, self.state)
        documenter = doccls(params, self.arguments[0])
        documenter.generate(more_content=self.content)
        if not params.result:
            return []

        logger.debug('[autodoc] output:\n%s', '\n'.join(params.result))

        # record all filenames as dependencies -- this will at least
        # partially make automatic invalidation possible
        for fn in params.record_dependencies:
            self.state.document.settings.record_dependencies.add(fn)

        result = parse_generated_content(self.state, params.result, documenter)
        return result
