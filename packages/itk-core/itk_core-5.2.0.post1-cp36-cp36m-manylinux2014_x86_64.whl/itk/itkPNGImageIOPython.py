# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKIOPNGPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkPNGImageIOPython
else:
    import _itkPNGImageIOPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkPNGImageIOPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkPNGImageIOPython.SWIG_PyStaticMethod_New

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
import itk.ITKIOImageBaseBasePython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_matrixPython
import itk.ITKCommonBasePython
import itk.itkRGBPixelPython
import itk.itkFixedArrayPython

def itkPNGImageIO_New():
    return itkPNGImageIO.New()

class itkPNGImageIO(itk.ITKIOImageBaseBasePython.itkImageIOBase):
    r"""


    ImageIO object for reading and writing PNG images.

    Compression is support with only the default compressor. The
    compression level option is supported in the range 0-9. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPNGImageIOPython.itkPNGImageIO___New_orig__)
    Clone = _swig_new_instance_method(_itkPNGImageIOPython.itkPNGImageIO_Clone)
    GetColorPalette = _swig_new_instance_method(_itkPNGImageIOPython.itkPNGImageIO_GetColorPalette)
    SetColorPalette = _swig_new_instance_method(_itkPNGImageIOPython.itkPNGImageIO_SetColorPalette)
    ReadVolume = _swig_new_instance_method(_itkPNGImageIOPython.itkPNGImageIO_ReadVolume)
    __swig_destroy__ = _itkPNGImageIOPython.delete_itkPNGImageIO
    cast = _swig_new_static_method(_itkPNGImageIOPython.itkPNGImageIO_cast)

    def New(*args, **kargs):
        """New() -> itkPNGImageIO

        Create a new object of the class itkPNGImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPNGImageIO.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPNGImageIO.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPNGImageIO.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPNGImageIO in _itkPNGImageIOPython:
_itkPNGImageIOPython.itkPNGImageIO_swigregister(itkPNGImageIO)
itkPNGImageIO___New_orig__ = _itkPNGImageIOPython.itkPNGImageIO___New_orig__
itkPNGImageIO_cast = _itkPNGImageIOPython.itkPNGImageIO_cast


def itkPNGImageIOFactory_New():
    return itkPNGImageIOFactory.New()

class itkPNGImageIOFactory(itk.ITKCommonBasePython.itkObjectFactoryBase):
    r"""


    Create instances of PNGImageIO objects using an object factory. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPNGImageIOPython.itkPNGImageIOFactory___New_orig__)
    FactoryNew = _swig_new_static_method(_itkPNGImageIOPython.itkPNGImageIOFactory_FactoryNew)
    RegisterOneFactory = _swig_new_static_method(_itkPNGImageIOPython.itkPNGImageIOFactory_RegisterOneFactory)
    __swig_destroy__ = _itkPNGImageIOPython.delete_itkPNGImageIOFactory
    cast = _swig_new_static_method(_itkPNGImageIOPython.itkPNGImageIOFactory_cast)

    def New(*args, **kargs):
        """New() -> itkPNGImageIOFactory

        Create a new object of the class itkPNGImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPNGImageIOFactory.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPNGImageIOFactory.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPNGImageIOFactory.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPNGImageIOFactory in _itkPNGImageIOPython:
_itkPNGImageIOPython.itkPNGImageIOFactory_swigregister(itkPNGImageIOFactory)
itkPNGImageIOFactory___New_orig__ = _itkPNGImageIOPython.itkPNGImageIOFactory___New_orig__
itkPNGImageIOFactory_FactoryNew = _itkPNGImageIOPython.itkPNGImageIOFactory_FactoryNew
itkPNGImageIOFactory_RegisterOneFactory = _itkPNGImageIOPython.itkPNGImageIOFactory_RegisterOneFactory
itkPNGImageIOFactory_cast = _itkPNGImageIOPython.itkPNGImageIOFactory_cast



