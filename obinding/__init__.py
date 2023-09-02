"""
OBinding
This must be a short description of the project
"""

# versioningit
from ._version import __version__

__doc_web__ = 'https://www.uibcdf.org/OBinding'
__github_web__ = 'https://github.com/uibcdf/OBinding'
__github_issues_web__ = __github_web__ + '/issues'

from ._pyunitwizard import puw as pyunitwizard

from . import config

from .molecular_complex import MolecularComplex

from . import topology
from . import structure
from . import potential_energy
from . import free_energy

from . import systems
from . import report

# With the following list sphinx can document de methods in the api section without adding the
# module files names explicitly:

__all__ = []

