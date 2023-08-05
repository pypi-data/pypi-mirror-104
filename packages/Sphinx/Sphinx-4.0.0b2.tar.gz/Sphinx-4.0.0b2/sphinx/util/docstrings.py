"""
    sphinx.util.docstrings
    ~~~~~~~~~~~~~~~~~~~~~~

    Utilities for docstring processing.

    :copyright: Copyright 2007-2021 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re
import sys
import warnings
from typing import Dict, List

from docutils.parsers.rst.states import Body

from sphinx.deprecation import RemovedInSphinx50Warning

field_list_item_re = re.compile(Body.patterns['field_marker'])


def extract_metadata(s: str) -> Dict[str, str]:
    """Extract metadata from docstring."""
    in_other_element = False
    metadata: Dict[str, str] = {}

    if not s:
        return metadata

    for line in prepare_docstring(s):
        if line.strip() == '':
            in_other_element = False
        else:
            matched = field_list_item_re.match(line)
            if matched and not in_other_element:
                field_name = matched.group()[1:].split(':', 1)[0]
                if field_name.startswith('meta '):
                    name = field_name[5:].strip()
                    metadata[name] = line[matched.end():].strip()
            else:
                in_other_element = True

    return metadata


def prepare_docstring(s: str, ignore: int = None, tabsize: int = 8) -> List[str]:
    """Convert a docstring into lines of parseable reST.  Remove common leading
    indentation, where the indentation of a given number of lines (usually just
    one) is ignored.

    Return the docstring as a list of lines usable for inserting into a docutils
    ViewList (used as argument of nested_parse().)  An empty line is added to
    act as a separator between this docstring and following content.
    """
    if ignore is None:
        ignore = 1
    else:
        warnings.warn("The 'ignore' argument to prepare_docstring() is deprecated.",
                      RemovedInSphinx50Warning, stacklevel=2)

    lines = s.expandtabs(tabsize).splitlines()
    # Find minimum indentation of any non-blank lines after ignored lines.
    margin = sys.maxsize
    for line in lines[ignore:]:
        content = len(line.lstrip())
        if content:
            indent = len(line) - content
            margin = min(margin, indent)
    # Remove indentation from ignored lines.
    for i in range(ignore):
        if i < len(lines):
            lines[i] = lines[i].lstrip()
    if margin < sys.maxsize:
        for i in range(ignore, len(lines)):
            lines[i] = lines[i][margin:]
    # Remove any leading blank lines.
    while lines and not lines[0]:
        lines.pop(0)
    # make sure there is an empty line at the end
    if lines and lines[-1]:
        lines.append('')
    return lines


def prepare_commentdoc(s: str) -> List[str]:
    """Extract documentation comment lines (starting with #:) and return them
    as a list of lines.  Returns an empty list if there is no documentation.
    """
    result = []
    lines = [line.strip() for line in s.expandtabs().splitlines()]
    for line in lines:
        if line.startswith('#:'):
            line = line[2:]
            # the first space after the comment is ignored
            if line and line[0] == ' ':
                line = line[1:]
            result.append(line)
    if result and result[-1]:
        result.append('')
    return result
