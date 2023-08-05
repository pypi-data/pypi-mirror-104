# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKTransformPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkCenteredAffineTransformPython
else:
    import _itkCenteredAffineTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkCenteredAffineTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkCenteredAffineTransformPython.SWIG_PyStaticMethod_New

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
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkArray2DPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.itkTransformBasePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.itkPointPython
import itk.itkVariableLengthVectorPython
import itk.itkDiffusionTensor3DPython
import itk.itkArrayPython
import itk.itkOptimizerParametersPython
import itk.itkAffineTransformPython
import itk.itkMatrixOffsetTransformBasePython

def itkCenteredAffineTransformD2_New():
    return itkCenteredAffineTransformD2.New()

class itkCenteredAffineTransformD2(itk.itkAffineTransformPython.itkAffineTransformD2):
    r"""


    Affine transformation with a specified center of rotation.

    This class implements an Affine transform in which the rotation center
    can be explicitly selected. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCenteredAffineTransformPython.itkCenteredAffineTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkCenteredAffineTransformPython.itkCenteredAffineTransformD2_Clone)
    GetInverse = _swig_new_instance_method(_itkCenteredAffineTransformPython.itkCenteredAffineTransformD2_GetInverse)
    __swig_destroy__ = _itkCenteredAffineTransformPython.delete_itkCenteredAffineTransformD2
    cast = _swig_new_static_method(_itkCenteredAffineTransformPython.itkCenteredAffineTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkCenteredAffineTransformD2

        Create a new object of the class itkCenteredAffineTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCenteredAffineTransformD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCenteredAffineTransformD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCenteredAffineTransformD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCenteredAffineTransformD2 in _itkCenteredAffineTransformPython:
_itkCenteredAffineTransformPython.itkCenteredAffineTransformD2_swigregister(itkCenteredAffineTransformD2)
itkCenteredAffineTransformD2___New_orig__ = _itkCenteredAffineTransformPython.itkCenteredAffineTransformD2___New_orig__
itkCenteredAffineTransformD2_cast = _itkCenteredAffineTransformPython.itkCenteredAffineTransformD2_cast


def itkCenteredAffineTransformD3_New():
    return itkCenteredAffineTransformD3.New()

class itkCenteredAffineTransformD3(itk.itkAffineTransformPython.itkAffineTransformD3):
    r"""


    Affine transformation with a specified center of rotation.

    This class implements an Affine transform in which the rotation center
    can be explicitly selected. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCenteredAffineTransformPython.itkCenteredAffineTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkCenteredAffineTransformPython.itkCenteredAffineTransformD3_Clone)
    GetInverse = _swig_new_instance_method(_itkCenteredAffineTransformPython.itkCenteredAffineTransformD3_GetInverse)
    __swig_destroy__ = _itkCenteredAffineTransformPython.delete_itkCenteredAffineTransformD3
    cast = _swig_new_static_method(_itkCenteredAffineTransformPython.itkCenteredAffineTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkCenteredAffineTransformD3

        Create a new object of the class itkCenteredAffineTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCenteredAffineTransformD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCenteredAffineTransformD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCenteredAffineTransformD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCenteredAffineTransformD3 in _itkCenteredAffineTransformPython:
_itkCenteredAffineTransformPython.itkCenteredAffineTransformD3_swigregister(itkCenteredAffineTransformD3)
itkCenteredAffineTransformD3___New_orig__ = _itkCenteredAffineTransformPython.itkCenteredAffineTransformD3___New_orig__
itkCenteredAffineTransformD3_cast = _itkCenteredAffineTransformPython.itkCenteredAffineTransformD3_cast


def itkCenteredAffineTransformD4_New():
    return itkCenteredAffineTransformD4.New()

class itkCenteredAffineTransformD4(itk.itkAffineTransformPython.itkAffineTransformD4):
    r"""


    Affine transformation with a specified center of rotation.

    This class implements an Affine transform in which the rotation center
    can be explicitly selected. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCenteredAffineTransformPython.itkCenteredAffineTransformD4___New_orig__)
    Clone = _swig_new_instance_method(_itkCenteredAffineTransformPython.itkCenteredAffineTransformD4_Clone)
    GetInverse = _swig_new_instance_method(_itkCenteredAffineTransformPython.itkCenteredAffineTransformD4_GetInverse)
    __swig_destroy__ = _itkCenteredAffineTransformPython.delete_itkCenteredAffineTransformD4
    cast = _swig_new_static_method(_itkCenteredAffineTransformPython.itkCenteredAffineTransformD4_cast)

    def New(*args, **kargs):
        """New() -> itkCenteredAffineTransformD4

        Create a new object of the class itkCenteredAffineTransformD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCenteredAffineTransformD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCenteredAffineTransformD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCenteredAffineTransformD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCenteredAffineTransformD4 in _itkCenteredAffineTransformPython:
_itkCenteredAffineTransformPython.itkCenteredAffineTransformD4_swigregister(itkCenteredAffineTransformD4)
itkCenteredAffineTransformD4___New_orig__ = _itkCenteredAffineTransformPython.itkCenteredAffineTransformD4___New_orig__
itkCenteredAffineTransformD4_cast = _itkCenteredAffineTransformPython.itkCenteredAffineTransformD4_cast



