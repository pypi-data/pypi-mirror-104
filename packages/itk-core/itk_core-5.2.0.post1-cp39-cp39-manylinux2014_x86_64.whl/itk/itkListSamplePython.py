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
    from . import _itkListSamplePython
else:
    import _itkListSamplePython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkListSamplePython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkListSamplePython.SWIG_PyStaticMethod_New

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
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.itkFixedArrayPython
import itk.ITKCommonBasePython
import itk.itkSamplePython
import itk.itkArrayPython

def itkListSampleVF2_New():
    return itkListSampleVF2.New()

class itkListSampleVF2(itk.itkSamplePython.itkSampleVF2):
    r"""


    This class is the native implementation of the a Sample with an STL
    container.

    ListSample stores measurements in a list type structure (as opposed to
    a Histogram, etc.). ListSample allows duplicate measurements.
    ListSample is not sorted.

    ListSample does not allow the user to specify the frequency of a
    measurement directly. The GetFrequency() methods returns 1 if the
    measurement exists in the list, 0 otherwise.

    See:   Sample, Histogram 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkListSamplePython.itkListSampleVF2___New_orig__)
    Clone = _swig_new_instance_method(_itkListSamplePython.itkListSampleVF2_Clone)
    Resize = _swig_new_instance_method(_itkListSamplePython.itkListSampleVF2_Resize)
    Clear = _swig_new_instance_method(_itkListSamplePython.itkListSampleVF2_Clear)
    PushBack = _swig_new_instance_method(_itkListSamplePython.itkListSampleVF2_PushBack)
    SetMeasurement = _swig_new_instance_method(_itkListSamplePython.itkListSampleVF2_SetMeasurement)
    SetMeasurementVector = _swig_new_instance_method(_itkListSamplePython.itkListSampleVF2_SetMeasurementVector)
    __swig_destroy__ = _itkListSamplePython.delete_itkListSampleVF2
    cast = _swig_new_static_method(_itkListSamplePython.itkListSampleVF2_cast)

    def New(*args, **kargs):
        """New() -> itkListSampleVF2

        Create a new object of the class itkListSampleVF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkListSampleVF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkListSampleVF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkListSampleVF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkListSampleVF2 in _itkListSamplePython:
_itkListSamplePython.itkListSampleVF2_swigregister(itkListSampleVF2)
itkListSampleVF2___New_orig__ = _itkListSamplePython.itkListSampleVF2___New_orig__
itkListSampleVF2_cast = _itkListSamplePython.itkListSampleVF2_cast


def itkListSampleVF3_New():
    return itkListSampleVF3.New()

class itkListSampleVF3(itk.itkSamplePython.itkSampleVF3):
    r"""


    This class is the native implementation of the a Sample with an STL
    container.

    ListSample stores measurements in a list type structure (as opposed to
    a Histogram, etc.). ListSample allows duplicate measurements.
    ListSample is not sorted.

    ListSample does not allow the user to specify the frequency of a
    measurement directly. The GetFrequency() methods returns 1 if the
    measurement exists in the list, 0 otherwise.

    See:   Sample, Histogram 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkListSamplePython.itkListSampleVF3___New_orig__)
    Clone = _swig_new_instance_method(_itkListSamplePython.itkListSampleVF3_Clone)
    Resize = _swig_new_instance_method(_itkListSamplePython.itkListSampleVF3_Resize)
    Clear = _swig_new_instance_method(_itkListSamplePython.itkListSampleVF3_Clear)
    PushBack = _swig_new_instance_method(_itkListSamplePython.itkListSampleVF3_PushBack)
    SetMeasurement = _swig_new_instance_method(_itkListSamplePython.itkListSampleVF3_SetMeasurement)
    SetMeasurementVector = _swig_new_instance_method(_itkListSamplePython.itkListSampleVF3_SetMeasurementVector)
    __swig_destroy__ = _itkListSamplePython.delete_itkListSampleVF3
    cast = _swig_new_static_method(_itkListSamplePython.itkListSampleVF3_cast)

    def New(*args, **kargs):
        """New() -> itkListSampleVF3

        Create a new object of the class itkListSampleVF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkListSampleVF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkListSampleVF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkListSampleVF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkListSampleVF3 in _itkListSamplePython:
_itkListSamplePython.itkListSampleVF3_swigregister(itkListSampleVF3)
itkListSampleVF3___New_orig__ = _itkListSamplePython.itkListSampleVF3___New_orig__
itkListSampleVF3_cast = _itkListSamplePython.itkListSampleVF3_cast


def itkListSampleVF4_New():
    return itkListSampleVF4.New()

class itkListSampleVF4(itk.itkSamplePython.itkSampleVF4):
    r"""


    This class is the native implementation of the a Sample with an STL
    container.

    ListSample stores measurements in a list type structure (as opposed to
    a Histogram, etc.). ListSample allows duplicate measurements.
    ListSample is not sorted.

    ListSample does not allow the user to specify the frequency of a
    measurement directly. The GetFrequency() methods returns 1 if the
    measurement exists in the list, 0 otherwise.

    See:   Sample, Histogram 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkListSamplePython.itkListSampleVF4___New_orig__)
    Clone = _swig_new_instance_method(_itkListSamplePython.itkListSampleVF4_Clone)
    Resize = _swig_new_instance_method(_itkListSamplePython.itkListSampleVF4_Resize)
    Clear = _swig_new_instance_method(_itkListSamplePython.itkListSampleVF4_Clear)
    PushBack = _swig_new_instance_method(_itkListSamplePython.itkListSampleVF4_PushBack)
    SetMeasurement = _swig_new_instance_method(_itkListSamplePython.itkListSampleVF4_SetMeasurement)
    SetMeasurementVector = _swig_new_instance_method(_itkListSamplePython.itkListSampleVF4_SetMeasurementVector)
    __swig_destroy__ = _itkListSamplePython.delete_itkListSampleVF4
    cast = _swig_new_static_method(_itkListSamplePython.itkListSampleVF4_cast)

    def New(*args, **kargs):
        """New() -> itkListSampleVF4

        Create a new object of the class itkListSampleVF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkListSampleVF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkListSampleVF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkListSampleVF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkListSampleVF4 in _itkListSamplePython:
_itkListSamplePython.itkListSampleVF4_swigregister(itkListSampleVF4)
itkListSampleVF4___New_orig__ = _itkListSamplePython.itkListSampleVF4___New_orig__
itkListSampleVF4_cast = _itkListSamplePython.itkListSampleVF4_cast



