"""
    sphinx.ext.githubpages
    ~~~~~~~~~~~~~~~~~~~~~~

    To publish HTML docs at GitHub Pages, create .nojekyll file.

    :copyright: Copyright 2007-2021 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import os
import urllib
from typing import Any, Dict

import sphinx
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment


def create_nojekyll_and_cname(app: Sphinx, env: BuildEnvironment) -> None:
    if app.builder.format == 'html':
        open(os.path.join(app.builder.outdir, '.nojekyll'), 'wt').close()

        html_baseurl = app.config.html_baseurl
        if html_baseurl:
            domain = urllib.parse.urlparse(html_baseurl).hostname
            if domain and not domain.endswith(".github.io"):
                with open(os.path.join(app.builder.outdir, 'CNAME'), 'wt') as f:
                    # NOTE: don't write a trailing newline. The `CNAME` file that's
                    # auto-generated by the Github UI doesn't have one.
                    f.write(domain)


def setup(app: Sphinx) -> Dict[str, Any]:
    app.connect('env-updated', create_nojekyll_and_cname)
    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
