# -*- coding: utf-8 -*-

try:
    # Declare this a namespace package if pkg_resources is available.
    import pkg_resources
    pkg_resources.declare_namespace('kooaba')
except ImportError:
    pass
