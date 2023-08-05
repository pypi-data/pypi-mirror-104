# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKCommonPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkTriangleHelperPython
else:
    import _itkTriangleHelperPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkTriangleHelperPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkTriangleHelperPython.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import collections.abc
import itk.itkPointPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
class itkTriangleHelperPD2(object):
    r"""


    A convenience class for computation of various triangle elements in 2D
    or 3D. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    IsObtuse = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD2_IsObtuse)
    ComputeNormal = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD2_ComputeNormal)
    Cotangent = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD2_Cotangent)
    ComputeBarycenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD2_ComputeBarycenter)
    ComputeAngle = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD2_ComputeAngle)
    ComputeGravityCenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD2_ComputeGravityCenter)
    ComputeCircumCenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD2_ComputeCircumCenter)
    ComputeConstrainedCircumCenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD2_ComputeConstrainedCircumCenter)
    ComputeArea = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD2_ComputeArea)
    ComputeMixedArea = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD2_ComputeMixedArea)

    def __init__(self, *args):
        r"""
        __init__(self) -> itkTriangleHelperPD2
        __init__(self, arg0) -> itkTriangleHelperPD2

        Parameters
        ----------
        arg0: itkTriangleHelperPD2 const &



        A convenience class for computation of various triangle elements in 2D
        or 3D. 
        """
        _itkTriangleHelperPython.itkTriangleHelperPD2_swiginit(self, _itkTriangleHelperPython.new_itkTriangleHelperPD2(*args))
    __swig_destroy__ = _itkTriangleHelperPython.delete_itkTriangleHelperPD2

# Register itkTriangleHelperPD2 in _itkTriangleHelperPython:
_itkTriangleHelperPython.itkTriangleHelperPD2_swigregister(itkTriangleHelperPD2)
itkTriangleHelperPD2_IsObtuse = _itkTriangleHelperPython.itkTriangleHelperPD2_IsObtuse
itkTriangleHelperPD2_ComputeNormal = _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeNormal
itkTriangleHelperPD2_Cotangent = _itkTriangleHelperPython.itkTriangleHelperPD2_Cotangent
itkTriangleHelperPD2_ComputeBarycenter = _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeBarycenter
itkTriangleHelperPD2_ComputeAngle = _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeAngle
itkTriangleHelperPD2_ComputeGravityCenter = _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeGravityCenter
itkTriangleHelperPD2_ComputeCircumCenter = _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeCircumCenter
itkTriangleHelperPD2_ComputeConstrainedCircumCenter = _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeConstrainedCircumCenter
itkTriangleHelperPD2_ComputeArea = _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeArea
itkTriangleHelperPD2_ComputeMixedArea = _itkTriangleHelperPython.itkTriangleHelperPD2_ComputeMixedArea

class itkTriangleHelperPD3(object):
    r"""


    A convenience class for computation of various triangle elements in 2D
    or 3D. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    IsObtuse = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD3_IsObtuse)
    ComputeNormal = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD3_ComputeNormal)
    Cotangent = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD3_Cotangent)
    ComputeBarycenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD3_ComputeBarycenter)
    ComputeAngle = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD3_ComputeAngle)
    ComputeGravityCenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD3_ComputeGravityCenter)
    ComputeCircumCenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD3_ComputeCircumCenter)
    ComputeConstrainedCircumCenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD3_ComputeConstrainedCircumCenter)
    ComputeArea = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD3_ComputeArea)
    ComputeMixedArea = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD3_ComputeMixedArea)

    def __init__(self, *args):
        r"""
        __init__(self) -> itkTriangleHelperPD3
        __init__(self, arg0) -> itkTriangleHelperPD3

        Parameters
        ----------
        arg0: itkTriangleHelperPD3 const &



        A convenience class for computation of various triangle elements in 2D
        or 3D. 
        """
        _itkTriangleHelperPython.itkTriangleHelperPD3_swiginit(self, _itkTriangleHelperPython.new_itkTriangleHelperPD3(*args))
    __swig_destroy__ = _itkTriangleHelperPython.delete_itkTriangleHelperPD3

# Register itkTriangleHelperPD3 in _itkTriangleHelperPython:
_itkTriangleHelperPython.itkTriangleHelperPD3_swigregister(itkTriangleHelperPD3)
itkTriangleHelperPD3_IsObtuse = _itkTriangleHelperPython.itkTriangleHelperPD3_IsObtuse
itkTriangleHelperPD3_ComputeNormal = _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeNormal
itkTriangleHelperPD3_Cotangent = _itkTriangleHelperPython.itkTriangleHelperPD3_Cotangent
itkTriangleHelperPD3_ComputeBarycenter = _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeBarycenter
itkTriangleHelperPD3_ComputeAngle = _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeAngle
itkTriangleHelperPD3_ComputeGravityCenter = _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeGravityCenter
itkTriangleHelperPD3_ComputeCircumCenter = _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeCircumCenter
itkTriangleHelperPD3_ComputeConstrainedCircumCenter = _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeConstrainedCircumCenter
itkTriangleHelperPD3_ComputeArea = _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeArea
itkTriangleHelperPD3_ComputeMixedArea = _itkTriangleHelperPython.itkTriangleHelperPD3_ComputeMixedArea

class itkTriangleHelperPD4(object):
    r"""


    A convenience class for computation of various triangle elements in 2D
    or 3D. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    IsObtuse = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD4_IsObtuse)
    ComputeNormal = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD4_ComputeNormal)
    Cotangent = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD4_Cotangent)
    ComputeBarycenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD4_ComputeBarycenter)
    ComputeAngle = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD4_ComputeAngle)
    ComputeGravityCenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD4_ComputeGravityCenter)
    ComputeCircumCenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD4_ComputeCircumCenter)
    ComputeConstrainedCircumCenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD4_ComputeConstrainedCircumCenter)
    ComputeArea = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD4_ComputeArea)
    ComputeMixedArea = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPD4_ComputeMixedArea)

    def __init__(self, *args):
        r"""
        __init__(self) -> itkTriangleHelperPD4
        __init__(self, arg0) -> itkTriangleHelperPD4

        Parameters
        ----------
        arg0: itkTriangleHelperPD4 const &



        A convenience class for computation of various triangle elements in 2D
        or 3D. 
        """
        _itkTriangleHelperPython.itkTriangleHelperPD4_swiginit(self, _itkTriangleHelperPython.new_itkTriangleHelperPD4(*args))
    __swig_destroy__ = _itkTriangleHelperPython.delete_itkTriangleHelperPD4

# Register itkTriangleHelperPD4 in _itkTriangleHelperPython:
_itkTriangleHelperPython.itkTriangleHelperPD4_swigregister(itkTriangleHelperPD4)
itkTriangleHelperPD4_IsObtuse = _itkTriangleHelperPython.itkTriangleHelperPD4_IsObtuse
itkTriangleHelperPD4_ComputeNormal = _itkTriangleHelperPython.itkTriangleHelperPD4_ComputeNormal
itkTriangleHelperPD4_Cotangent = _itkTriangleHelperPython.itkTriangleHelperPD4_Cotangent
itkTriangleHelperPD4_ComputeBarycenter = _itkTriangleHelperPython.itkTriangleHelperPD4_ComputeBarycenter
itkTriangleHelperPD4_ComputeAngle = _itkTriangleHelperPython.itkTriangleHelperPD4_ComputeAngle
itkTriangleHelperPD4_ComputeGravityCenter = _itkTriangleHelperPython.itkTriangleHelperPD4_ComputeGravityCenter
itkTriangleHelperPD4_ComputeCircumCenter = _itkTriangleHelperPython.itkTriangleHelperPD4_ComputeCircumCenter
itkTriangleHelperPD4_ComputeConstrainedCircumCenter = _itkTriangleHelperPython.itkTriangleHelperPD4_ComputeConstrainedCircumCenter
itkTriangleHelperPD4_ComputeArea = _itkTriangleHelperPython.itkTriangleHelperPD4_ComputeArea
itkTriangleHelperPD4_ComputeMixedArea = _itkTriangleHelperPython.itkTriangleHelperPD4_ComputeMixedArea

class itkTriangleHelperPF2(object):
    r"""


    A convenience class for computation of various triangle elements in 2D
    or 3D. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    IsObtuse = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF2_IsObtuse)
    ComputeNormal = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF2_ComputeNormal)
    Cotangent = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF2_Cotangent)
    ComputeBarycenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF2_ComputeBarycenter)
    ComputeAngle = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF2_ComputeAngle)
    ComputeGravityCenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF2_ComputeGravityCenter)
    ComputeCircumCenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF2_ComputeCircumCenter)
    ComputeConstrainedCircumCenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF2_ComputeConstrainedCircumCenter)
    ComputeArea = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF2_ComputeArea)
    ComputeMixedArea = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF2_ComputeMixedArea)

    def __init__(self, *args):
        r"""
        __init__(self) -> itkTriangleHelperPF2
        __init__(self, arg0) -> itkTriangleHelperPF2

        Parameters
        ----------
        arg0: itkTriangleHelperPF2 const &



        A convenience class for computation of various triangle elements in 2D
        or 3D. 
        """
        _itkTriangleHelperPython.itkTriangleHelperPF2_swiginit(self, _itkTriangleHelperPython.new_itkTriangleHelperPF2(*args))
    __swig_destroy__ = _itkTriangleHelperPython.delete_itkTriangleHelperPF2

# Register itkTriangleHelperPF2 in _itkTriangleHelperPython:
_itkTriangleHelperPython.itkTriangleHelperPF2_swigregister(itkTriangleHelperPF2)
itkTriangleHelperPF2_IsObtuse = _itkTriangleHelperPython.itkTriangleHelperPF2_IsObtuse
itkTriangleHelperPF2_ComputeNormal = _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeNormal
itkTriangleHelperPF2_Cotangent = _itkTriangleHelperPython.itkTriangleHelperPF2_Cotangent
itkTriangleHelperPF2_ComputeBarycenter = _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeBarycenter
itkTriangleHelperPF2_ComputeAngle = _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeAngle
itkTriangleHelperPF2_ComputeGravityCenter = _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeGravityCenter
itkTriangleHelperPF2_ComputeCircumCenter = _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeCircumCenter
itkTriangleHelperPF2_ComputeConstrainedCircumCenter = _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeConstrainedCircumCenter
itkTriangleHelperPF2_ComputeArea = _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeArea
itkTriangleHelperPF2_ComputeMixedArea = _itkTriangleHelperPython.itkTriangleHelperPF2_ComputeMixedArea

class itkTriangleHelperPF3(object):
    r"""


    A convenience class for computation of various triangle elements in 2D
    or 3D. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    IsObtuse = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF3_IsObtuse)
    ComputeNormal = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF3_ComputeNormal)
    Cotangent = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF3_Cotangent)
    ComputeBarycenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF3_ComputeBarycenter)
    ComputeAngle = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF3_ComputeAngle)
    ComputeGravityCenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF3_ComputeGravityCenter)
    ComputeCircumCenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF3_ComputeCircumCenter)
    ComputeConstrainedCircumCenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF3_ComputeConstrainedCircumCenter)
    ComputeArea = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF3_ComputeArea)
    ComputeMixedArea = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF3_ComputeMixedArea)

    def __init__(self, *args):
        r"""
        __init__(self) -> itkTriangleHelperPF3
        __init__(self, arg0) -> itkTriangleHelperPF3

        Parameters
        ----------
        arg0: itkTriangleHelperPF3 const &



        A convenience class for computation of various triangle elements in 2D
        or 3D. 
        """
        _itkTriangleHelperPython.itkTriangleHelperPF3_swiginit(self, _itkTriangleHelperPython.new_itkTriangleHelperPF3(*args))
    __swig_destroy__ = _itkTriangleHelperPython.delete_itkTriangleHelperPF3

# Register itkTriangleHelperPF3 in _itkTriangleHelperPython:
_itkTriangleHelperPython.itkTriangleHelperPF3_swigregister(itkTriangleHelperPF3)
itkTriangleHelperPF3_IsObtuse = _itkTriangleHelperPython.itkTriangleHelperPF3_IsObtuse
itkTriangleHelperPF3_ComputeNormal = _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeNormal
itkTriangleHelperPF3_Cotangent = _itkTriangleHelperPython.itkTriangleHelperPF3_Cotangent
itkTriangleHelperPF3_ComputeBarycenter = _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeBarycenter
itkTriangleHelperPF3_ComputeAngle = _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeAngle
itkTriangleHelperPF3_ComputeGravityCenter = _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeGravityCenter
itkTriangleHelperPF3_ComputeCircumCenter = _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeCircumCenter
itkTriangleHelperPF3_ComputeConstrainedCircumCenter = _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeConstrainedCircumCenter
itkTriangleHelperPF3_ComputeArea = _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeArea
itkTriangleHelperPF3_ComputeMixedArea = _itkTriangleHelperPython.itkTriangleHelperPF3_ComputeMixedArea

class itkTriangleHelperPF4(object):
    r"""


    A convenience class for computation of various triangle elements in 2D
    or 3D. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    IsObtuse = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF4_IsObtuse)
    ComputeNormal = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF4_ComputeNormal)
    Cotangent = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF4_Cotangent)
    ComputeBarycenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF4_ComputeBarycenter)
    ComputeAngle = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF4_ComputeAngle)
    ComputeGravityCenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF4_ComputeGravityCenter)
    ComputeCircumCenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF4_ComputeCircumCenter)
    ComputeConstrainedCircumCenter = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF4_ComputeConstrainedCircumCenter)
    ComputeArea = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF4_ComputeArea)
    ComputeMixedArea = _swig_new_static_method(_itkTriangleHelperPython.itkTriangleHelperPF4_ComputeMixedArea)

    def __init__(self, *args):
        r"""
        __init__(self) -> itkTriangleHelperPF4
        __init__(self, arg0) -> itkTriangleHelperPF4

        Parameters
        ----------
        arg0: itkTriangleHelperPF4 const &



        A convenience class for computation of various triangle elements in 2D
        or 3D. 
        """
        _itkTriangleHelperPython.itkTriangleHelperPF4_swiginit(self, _itkTriangleHelperPython.new_itkTriangleHelperPF4(*args))
    __swig_destroy__ = _itkTriangleHelperPython.delete_itkTriangleHelperPF4

# Register itkTriangleHelperPF4 in _itkTriangleHelperPython:
_itkTriangleHelperPython.itkTriangleHelperPF4_swigregister(itkTriangleHelperPF4)
itkTriangleHelperPF4_IsObtuse = _itkTriangleHelperPython.itkTriangleHelperPF4_IsObtuse
itkTriangleHelperPF4_ComputeNormal = _itkTriangleHelperPython.itkTriangleHelperPF4_ComputeNormal
itkTriangleHelperPF4_Cotangent = _itkTriangleHelperPython.itkTriangleHelperPF4_Cotangent
itkTriangleHelperPF4_ComputeBarycenter = _itkTriangleHelperPython.itkTriangleHelperPF4_ComputeBarycenter
itkTriangleHelperPF4_ComputeAngle = _itkTriangleHelperPython.itkTriangleHelperPF4_ComputeAngle
itkTriangleHelperPF4_ComputeGravityCenter = _itkTriangleHelperPython.itkTriangleHelperPF4_ComputeGravityCenter
itkTriangleHelperPF4_ComputeCircumCenter = _itkTriangleHelperPython.itkTriangleHelperPF4_ComputeCircumCenter
itkTriangleHelperPF4_ComputeConstrainedCircumCenter = _itkTriangleHelperPython.itkTriangleHelperPF4_ComputeConstrainedCircumCenter
itkTriangleHelperPF4_ComputeArea = _itkTriangleHelperPython.itkTriangleHelperPF4_ComputeArea
itkTriangleHelperPF4_ComputeMixedArea = _itkTriangleHelperPython.itkTriangleHelperPF4_ComputeMixedArea



