# https://docs.python.org/3/reference/simple_stmts.html#import

"""
Imports order
1 Standard library imports.
2 Related third party imports.
3 Local application/library specific imports.
"""

"""
import <module>
import <module> as <identifier>
from <module> import <identifier>
from <module> import <identifier> as <identifier>
from <module> import <identifier>, <identifier>
from <module> import <identifier> as <identifier>, <identifier> as <identifier>
import <package>
import <package>.(<dir>.)<module>
"""

import numpy 
import numpy as np
from numpy import pi
from numpy import pi, shape
