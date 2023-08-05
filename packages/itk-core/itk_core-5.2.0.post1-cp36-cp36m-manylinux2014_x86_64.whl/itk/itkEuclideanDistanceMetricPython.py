# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKStatisticsPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkEuclideanDistanceMetricPython
else:
    import _itkEuclideanDistanceMetricPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkEuclideanDistanceMetricPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkEuclideanDistanceMetricPython.SWIG_PyStaticMethod_New

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
import itk.itkDistanceMetricPython
import itk.itkFunctionBasePython
import itk.itkImagePython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkMatrixPython
import itk.vnl_matrixPython
import itk.vnl_vectorPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.itkPointPython
import itk.itkRGBAPixelPython
import itk.itkIndexPython
import itk.itkRGBPixelPython
import itk.itkImageRegionPython
import itk.ITKCommonBasePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkContinuousIndexPython
import itk.itkArrayPython

def itkEuclideanDistanceMetricVF2_New():
    return itkEuclideanDistanceMetricVF2.New()

class itkEuclideanDistanceMetricVF2(itk.itkDistanceMetricPython.itkDistanceMetricVF2):
    r"""


    Euclidean distance function. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF2___New_orig__)
    Clone = _swig_new_instance_method(_itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF2_Clone)
    Evaluate = _swig_new_instance_method(_itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF2_Evaluate)
    __swig_destroy__ = _itkEuclideanDistanceMetricPython.delete_itkEuclideanDistanceMetricVF2
    cast = _swig_new_static_method(_itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF2_cast)

    def New(*args, **kargs):
        """New() -> itkEuclideanDistanceMetricVF2

        Create a new object of the class itkEuclideanDistanceMetricVF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEuclideanDistanceMetricVF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkEuclideanDistanceMetricVF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkEuclideanDistanceMetricVF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEuclideanDistanceMetricVF2 in _itkEuclideanDistanceMetricPython:
_itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF2_swigregister(itkEuclideanDistanceMetricVF2)
itkEuclideanDistanceMetricVF2___New_orig__ = _itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF2___New_orig__
itkEuclideanDistanceMetricVF2_cast = _itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF2_cast


def itkEuclideanDistanceMetricVF3_New():
    return itkEuclideanDistanceMetricVF3.New()

class itkEuclideanDistanceMetricVF3(itk.itkDistanceMetricPython.itkDistanceMetricVF3):
    r"""


    Euclidean distance function. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF3___New_orig__)
    Clone = _swig_new_instance_method(_itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF3_Clone)
    Evaluate = _swig_new_instance_method(_itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF3_Evaluate)
    __swig_destroy__ = _itkEuclideanDistanceMetricPython.delete_itkEuclideanDistanceMetricVF3
    cast = _swig_new_static_method(_itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF3_cast)

    def New(*args, **kargs):
        """New() -> itkEuclideanDistanceMetricVF3

        Create a new object of the class itkEuclideanDistanceMetricVF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEuclideanDistanceMetricVF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkEuclideanDistanceMetricVF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkEuclideanDistanceMetricVF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEuclideanDistanceMetricVF3 in _itkEuclideanDistanceMetricPython:
_itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF3_swigregister(itkEuclideanDistanceMetricVF3)
itkEuclideanDistanceMetricVF3___New_orig__ = _itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF3___New_orig__
itkEuclideanDistanceMetricVF3_cast = _itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF3_cast


def itkEuclideanDistanceMetricVF4_New():
    return itkEuclideanDistanceMetricVF4.New()

class itkEuclideanDistanceMetricVF4(itk.itkDistanceMetricPython.itkDistanceMetricVF4):
    r"""


    Euclidean distance function. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF4___New_orig__)
    Clone = _swig_new_instance_method(_itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF4_Clone)
    Evaluate = _swig_new_instance_method(_itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF4_Evaluate)
    __swig_destroy__ = _itkEuclideanDistanceMetricPython.delete_itkEuclideanDistanceMetricVF4
    cast = _swig_new_static_method(_itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF4_cast)

    def New(*args, **kargs):
        """New() -> itkEuclideanDistanceMetricVF4

        Create a new object of the class itkEuclideanDistanceMetricVF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEuclideanDistanceMetricVF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkEuclideanDistanceMetricVF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkEuclideanDistanceMetricVF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEuclideanDistanceMetricVF4 in _itkEuclideanDistanceMetricPython:
_itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF4_swigregister(itkEuclideanDistanceMetricVF4)
itkEuclideanDistanceMetricVF4___New_orig__ = _itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF4___New_orig__
itkEuclideanDistanceMetricVF4_cast = _itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF4_cast



