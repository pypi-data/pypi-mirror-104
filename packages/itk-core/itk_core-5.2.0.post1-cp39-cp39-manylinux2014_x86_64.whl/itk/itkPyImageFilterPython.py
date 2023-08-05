# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKPyUtilsPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkPyImageFilterPython
else:
    import _itkPyImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkPyImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkPyImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkImageToImageFilterAPython
import itk.itkImageRegionPython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkImageSourcePython
import itk.itkImagePython
import itk.itkMatrixPython
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkRGBPixelPython
import itk.itkRGBAPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterCommonPython

def itkPyImageFilterIUC2IUC2_New():
    return itkPyImageFilterIUC2IUC2.New()

class itkPyImageFilterIUC2IUC2(itk.itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    r"""


    ImageToImageFilter subclass that calls a Python callable object, e.g.
    a Python function. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPyImageFilterPython.itkPyImageFilterIUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_Clone)
    SetPyGenerateData = _swig_new_instance_method(_itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_SetPyGenerateData)
    __swig_destroy__ = _itkPyImageFilterPython.delete_itkPyImageFilterIUC2IUC2
    cast = _swig_new_static_method(_itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkPyImageFilterIUC2IUC2

        Create a new object of the class itkPyImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPyImageFilterIUC2IUC2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPyImageFilterIUC2IUC2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPyImageFilterIUC2IUC2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPyImageFilterIUC2IUC2 in _itkPyImageFilterPython:
_itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_swigregister(itkPyImageFilterIUC2IUC2)
itkPyImageFilterIUC2IUC2___New_orig__ = _itkPyImageFilterPython.itkPyImageFilterIUC2IUC2___New_orig__
itkPyImageFilterIUC2IUC2_cast = _itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_cast


def itkPyImageFilterIUC3IUC3_New():
    return itkPyImageFilterIUC3IUC3.New()

class itkPyImageFilterIUC3IUC3(itk.itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUC3):
    r"""


    ImageToImageFilter subclass that calls a Python callable object, e.g.
    a Python function. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPyImageFilterPython.itkPyImageFilterIUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_Clone)
    SetPyGenerateData = _swig_new_instance_method(_itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_SetPyGenerateData)
    __swig_destroy__ = _itkPyImageFilterPython.delete_itkPyImageFilterIUC3IUC3
    cast = _swig_new_static_method(_itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkPyImageFilterIUC3IUC3

        Create a new object of the class itkPyImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPyImageFilterIUC3IUC3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPyImageFilterIUC3IUC3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPyImageFilterIUC3IUC3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPyImageFilterIUC3IUC3 in _itkPyImageFilterPython:
_itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_swigregister(itkPyImageFilterIUC3IUC3)
itkPyImageFilterIUC3IUC3___New_orig__ = _itkPyImageFilterPython.itkPyImageFilterIUC3IUC3___New_orig__
itkPyImageFilterIUC3IUC3_cast = _itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_cast


def itkPyImageFilterIUC4IUC4_New():
    return itkPyImageFilterIUC4IUC4.New()

class itkPyImageFilterIUC4IUC4(itk.itkImageToImageFilterAPython.itkImageToImageFilterIUC4IUC4):
    r"""


    ImageToImageFilter subclass that calls a Python callable object, e.g.
    a Python function. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPyImageFilterPython.itkPyImageFilterIUC4IUC4___New_orig__)
    Clone = _swig_new_instance_method(_itkPyImageFilterPython.itkPyImageFilterIUC4IUC4_Clone)
    SetPyGenerateData = _swig_new_instance_method(_itkPyImageFilterPython.itkPyImageFilterIUC4IUC4_SetPyGenerateData)
    __swig_destroy__ = _itkPyImageFilterPython.delete_itkPyImageFilterIUC4IUC4
    cast = _swig_new_static_method(_itkPyImageFilterPython.itkPyImageFilterIUC4IUC4_cast)

    def New(*args, **kargs):
        """New() -> itkPyImageFilterIUC4IUC4

        Create a new object of the class itkPyImageFilterIUC4IUC4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPyImageFilterIUC4IUC4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPyImageFilterIUC4IUC4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPyImageFilterIUC4IUC4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPyImageFilterIUC4IUC4 in _itkPyImageFilterPython:
_itkPyImageFilterPython.itkPyImageFilterIUC4IUC4_swigregister(itkPyImageFilterIUC4IUC4)
itkPyImageFilterIUC4IUC4___New_orig__ = _itkPyImageFilterPython.itkPyImageFilterIUC4IUC4___New_orig__
itkPyImageFilterIUC4IUC4_cast = _itkPyImageFilterPython.itkPyImageFilterIUC4IUC4_cast


def itkPyImageFilterIUS2IUS2_New():
    return itkPyImageFilterIUS2IUS2.New()

class itkPyImageFilterIUS2IUS2(itk.itkImageToImageFilterAPython.itkImageToImageFilterIUS2IUS2):
    r"""


    ImageToImageFilter subclass that calls a Python callable object, e.g.
    a Python function. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPyImageFilterPython.itkPyImageFilterIUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkPyImageFilterPython.itkPyImageFilterIUS2IUS2_Clone)
    SetPyGenerateData = _swig_new_instance_method(_itkPyImageFilterPython.itkPyImageFilterIUS2IUS2_SetPyGenerateData)
    __swig_destroy__ = _itkPyImageFilterPython.delete_itkPyImageFilterIUS2IUS2
    cast = _swig_new_static_method(_itkPyImageFilterPython.itkPyImageFilterIUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkPyImageFilterIUS2IUS2

        Create a new object of the class itkPyImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPyImageFilterIUS2IUS2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPyImageFilterIUS2IUS2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPyImageFilterIUS2IUS2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPyImageFilterIUS2IUS2 in _itkPyImageFilterPython:
_itkPyImageFilterPython.itkPyImageFilterIUS2IUS2_swigregister(itkPyImageFilterIUS2IUS2)
itkPyImageFilterIUS2IUS2___New_orig__ = _itkPyImageFilterPython.itkPyImageFilterIUS2IUS2___New_orig__
itkPyImageFilterIUS2IUS2_cast = _itkPyImageFilterPython.itkPyImageFilterIUS2IUS2_cast


def itkPyImageFilterIUS3IUS3_New():
    return itkPyImageFilterIUS3IUS3.New()

class itkPyImageFilterIUS3IUS3(itk.itkImageToImageFilterAPython.itkImageToImageFilterIUS3IUS3):
    r"""


    ImageToImageFilter subclass that calls a Python callable object, e.g.
    a Python function. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPyImageFilterPython.itkPyImageFilterIUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkPyImageFilterPython.itkPyImageFilterIUS3IUS3_Clone)
    SetPyGenerateData = _swig_new_instance_method(_itkPyImageFilterPython.itkPyImageFilterIUS3IUS3_SetPyGenerateData)
    __swig_destroy__ = _itkPyImageFilterPython.delete_itkPyImageFilterIUS3IUS3
    cast = _swig_new_static_method(_itkPyImageFilterPython.itkPyImageFilterIUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkPyImageFilterIUS3IUS3

        Create a new object of the class itkPyImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPyImageFilterIUS3IUS3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPyImageFilterIUS3IUS3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPyImageFilterIUS3IUS3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPyImageFilterIUS3IUS3 in _itkPyImageFilterPython:
_itkPyImageFilterPython.itkPyImageFilterIUS3IUS3_swigregister(itkPyImageFilterIUS3IUS3)
itkPyImageFilterIUS3IUS3___New_orig__ = _itkPyImageFilterPython.itkPyImageFilterIUS3IUS3___New_orig__
itkPyImageFilterIUS3IUS3_cast = _itkPyImageFilterPython.itkPyImageFilterIUS3IUS3_cast


def itkPyImageFilterIUS4IUS4_New():
    return itkPyImageFilterIUS4IUS4.New()

class itkPyImageFilterIUS4IUS4(itk.itkImageToImageFilterAPython.itkImageToImageFilterIUS4IUS4):
    r"""


    ImageToImageFilter subclass that calls a Python callable object, e.g.
    a Python function. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPyImageFilterPython.itkPyImageFilterIUS4IUS4___New_orig__)
    Clone = _swig_new_instance_method(_itkPyImageFilterPython.itkPyImageFilterIUS4IUS4_Clone)
    SetPyGenerateData = _swig_new_instance_method(_itkPyImageFilterPython.itkPyImageFilterIUS4IUS4_SetPyGenerateData)
    __swig_destroy__ = _itkPyImageFilterPython.delete_itkPyImageFilterIUS4IUS4
    cast = _swig_new_static_method(_itkPyImageFilterPython.itkPyImageFilterIUS4IUS4_cast)

    def New(*args, **kargs):
        """New() -> itkPyImageFilterIUS4IUS4

        Create a new object of the class itkPyImageFilterIUS4IUS4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPyImageFilterIUS4IUS4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPyImageFilterIUS4IUS4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPyImageFilterIUS4IUS4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPyImageFilterIUS4IUS4 in _itkPyImageFilterPython:
_itkPyImageFilterPython.itkPyImageFilterIUS4IUS4_swigregister(itkPyImageFilterIUS4IUS4)
itkPyImageFilterIUS4IUS4___New_orig__ = _itkPyImageFilterPython.itkPyImageFilterIUS4IUS4___New_orig__
itkPyImageFilterIUS4IUS4_cast = _itkPyImageFilterPython.itkPyImageFilterIUS4IUS4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def py_image_filter(*args: itkt.ImageLike,  py_generate_data=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for PyImageFilter"""
    import itk

    kwarg_typehints = { 'py_generate_data':py_generate_data }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.PyImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def py_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKPyUtils.PyImageFilter
    py_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    py_image_filter.__doc__ = filter_object.__doc__




