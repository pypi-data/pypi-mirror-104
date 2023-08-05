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
    from . import _itkOptimizerParametersPython
else:
    import _itkOptimizerParametersPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkOptimizerParametersPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkOptimizerParametersPython.SWIG_PyStaticMethod_New

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
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.itkArrayPython
import itk.ITKCommonBasePython
class itkOptimizerParametersD(itk.itkArrayPython.itkArrayD):
    r"""


    Class to hold and manage different parameter types used during
    optimization. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkOptimizerParametersD
        __init__(self, rhs) -> itkOptimizerParametersD

        Parameters
        ----------
        rhs: itkOptimizerParametersD const &

        __init__(self, dimension) -> itkOptimizerParametersD

        Parameters
        ----------
        dimension: unsigned long

        __init__(self, array) -> itkOptimizerParametersD

        Parameters
        ----------
        array: itkArrayD const &

        __init__(self, dimension, value) -> itkOptimizerParametersD

        Parameters
        ----------
        dimension: unsigned long const
        value: double const &

        __init__(self, inputData, dimension) -> itkOptimizerParametersD

        Parameters
        ----------
        inputData: double const *const
        dimension: unsigned long const



        Class to hold and manage different parameter types used during
        optimization. 
        """
        _itkOptimizerParametersPython.itkOptimizerParametersD_swiginit(self, _itkOptimizerParametersPython.new_itkOptimizerParametersD(*args))
    Initialize = _swig_new_instance_method(_itkOptimizerParametersPython.itkOptimizerParametersD_Initialize)
    MoveDataPointer = _swig_new_instance_method(_itkOptimizerParametersPython.itkOptimizerParametersD_MoveDataPointer)
    SetParametersObject = _swig_new_instance_method(_itkOptimizerParametersPython.itkOptimizerParametersD_SetParametersObject)
    SetHelper = _swig_new_instance_method(_itkOptimizerParametersPython.itkOptimizerParametersD_SetHelper)
    GetHelper = _swig_new_instance_method(_itkOptimizerParametersPython.itkOptimizerParametersD_GetHelper)
    __swig_destroy__ = _itkOptimizerParametersPython.delete_itkOptimizerParametersD

# Register itkOptimizerParametersD in _itkOptimizerParametersPython:
_itkOptimizerParametersPython.itkOptimizerParametersD_swigregister(itkOptimizerParametersD)

class itkOptimizerParametersF(itk.itkArrayPython.itkArrayF):
    r"""


    Class to hold and manage different parameter types used during
    optimization. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkOptimizerParametersF
        __init__(self, rhs) -> itkOptimizerParametersF

        Parameters
        ----------
        rhs: itkOptimizerParametersF const &

        __init__(self, dimension) -> itkOptimizerParametersF

        Parameters
        ----------
        dimension: unsigned long

        __init__(self, array) -> itkOptimizerParametersF

        Parameters
        ----------
        array: itkArrayF const &

        __init__(self, dimension, value) -> itkOptimizerParametersF

        Parameters
        ----------
        dimension: unsigned long const
        value: float const &

        __init__(self, inputData, dimension) -> itkOptimizerParametersF

        Parameters
        ----------
        inputData: float const *const
        dimension: unsigned long const



        Class to hold and manage different parameter types used during
        optimization. 
        """
        _itkOptimizerParametersPython.itkOptimizerParametersF_swiginit(self, _itkOptimizerParametersPython.new_itkOptimizerParametersF(*args))
    Initialize = _swig_new_instance_method(_itkOptimizerParametersPython.itkOptimizerParametersF_Initialize)
    MoveDataPointer = _swig_new_instance_method(_itkOptimizerParametersPython.itkOptimizerParametersF_MoveDataPointer)
    SetParametersObject = _swig_new_instance_method(_itkOptimizerParametersPython.itkOptimizerParametersF_SetParametersObject)
    SetHelper = _swig_new_instance_method(_itkOptimizerParametersPython.itkOptimizerParametersF_SetHelper)
    GetHelper = _swig_new_instance_method(_itkOptimizerParametersPython.itkOptimizerParametersF_GetHelper)
    __swig_destroy__ = _itkOptimizerParametersPython.delete_itkOptimizerParametersF

# Register itkOptimizerParametersF in _itkOptimizerParametersPython:
_itkOptimizerParametersPython.itkOptimizerParametersF_swigregister(itkOptimizerParametersF)

class itkOptimizerParametersHelperD(object):
    r"""


    Basic helper class to manage parameter data as an Array type, the
    default type. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    MoveDataPointer = _swig_new_instance_method(_itkOptimizerParametersPython.itkOptimizerParametersHelperD_MoveDataPointer)
    SetParametersObject = _swig_new_instance_method(_itkOptimizerParametersPython.itkOptimizerParametersHelperD_SetParametersObject)
    __swig_destroy__ = _itkOptimizerParametersPython.delete_itkOptimizerParametersHelperD

    def __init__(self, *args):
        r"""
        __init__(self) -> itkOptimizerParametersHelperD
        __init__(self, arg0) -> itkOptimizerParametersHelperD

        Parameters
        ----------
        arg0: itkOptimizerParametersHelperD const &



        Basic helper class to manage parameter data as an Array type, the
        default type. 
        """
        _itkOptimizerParametersPython.itkOptimizerParametersHelperD_swiginit(self, _itkOptimizerParametersPython.new_itkOptimizerParametersHelperD(*args))

# Register itkOptimizerParametersHelperD in _itkOptimizerParametersPython:
_itkOptimizerParametersPython.itkOptimizerParametersHelperD_swigregister(itkOptimizerParametersHelperD)

class itkOptimizerParametersHelperF(object):
    r"""


    Basic helper class to manage parameter data as an Array type, the
    default type. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    MoveDataPointer = _swig_new_instance_method(_itkOptimizerParametersPython.itkOptimizerParametersHelperF_MoveDataPointer)
    SetParametersObject = _swig_new_instance_method(_itkOptimizerParametersPython.itkOptimizerParametersHelperF_SetParametersObject)
    __swig_destroy__ = _itkOptimizerParametersPython.delete_itkOptimizerParametersHelperF

    def __init__(self, *args):
        r"""
        __init__(self) -> itkOptimizerParametersHelperF
        __init__(self, arg0) -> itkOptimizerParametersHelperF

        Parameters
        ----------
        arg0: itkOptimizerParametersHelperF const &



        Basic helper class to manage parameter data as an Array type, the
        default type. 
        """
        _itkOptimizerParametersPython.itkOptimizerParametersHelperF_swiginit(self, _itkOptimizerParametersPython.new_itkOptimizerParametersHelperF(*args))

# Register itkOptimizerParametersHelperF in _itkOptimizerParametersPython:
_itkOptimizerParametersPython.itkOptimizerParametersHelperF_swigregister(itkOptimizerParametersHelperF)



