# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKIOMetaPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkMetaImageIOPython
else:
    import _itkMetaImageIOPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMetaImageIOPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMetaImageIOPython.SWIG_PyStaticMethod_New

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
import itk.ITKIOImageBaseBasePython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython

def itkMetaImageIO_New():
    return itkMetaImageIO.New()

class itkMetaImageIO(itk.ITKIOImageBaseBasePython.itkImageIOBase):
    r"""


    Read MetaImage file format.

    For a detailed description of using this format, please
    seehttps://www.itk.org/Wiki/ITK/MetaIO/Documentation 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMetaImageIOPython.itkMetaImageIO___New_orig__)
    Clone = _swig_new_instance_method(_itkMetaImageIOPython.itkMetaImageIO_Clone)
    GetMetaImagePointer = _swig_new_instance_method(_itkMetaImageIOPython.itkMetaImageIO_GetMetaImagePointer)
    SetDataFileName = _swig_new_instance_method(_itkMetaImageIOPython.itkMetaImageIO_SetDataFileName)
    SetDoublePrecision = _swig_new_instance_method(_itkMetaImageIOPython.itkMetaImageIO_SetDoublePrecision)
    SetSubSamplingFactor = _swig_new_instance_method(_itkMetaImageIOPython.itkMetaImageIO_SetSubSamplingFactor)
    GetSubSamplingFactor = _swig_new_instance_method(_itkMetaImageIOPython.itkMetaImageIO_GetSubSamplingFactor)
    SetDefaultDoublePrecision = _swig_new_static_method(_itkMetaImageIOPython.itkMetaImageIO_SetDefaultDoublePrecision)
    GetDefaultDoublePrecision = _swig_new_static_method(_itkMetaImageIOPython.itkMetaImageIO_GetDefaultDoublePrecision)
    __swig_destroy__ = _itkMetaImageIOPython.delete_itkMetaImageIO
    cast = _swig_new_static_method(_itkMetaImageIOPython.itkMetaImageIO_cast)

    def New(*args, **kargs):
        """New() -> itkMetaImageIO

        Create a new object of the class itkMetaImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMetaImageIO.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMetaImageIO.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMetaImageIO.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMetaImageIO in _itkMetaImageIOPython:
_itkMetaImageIOPython.itkMetaImageIO_swigregister(itkMetaImageIO)
itkMetaImageIO___New_orig__ = _itkMetaImageIOPython.itkMetaImageIO___New_orig__
itkMetaImageIO_SetDefaultDoublePrecision = _itkMetaImageIOPython.itkMetaImageIO_SetDefaultDoublePrecision
itkMetaImageIO_GetDefaultDoublePrecision = _itkMetaImageIOPython.itkMetaImageIO_GetDefaultDoublePrecision
itkMetaImageIO_cast = _itkMetaImageIOPython.itkMetaImageIO_cast


def itkMetaImageIOFactory_New():
    return itkMetaImageIOFactory.New()

class itkMetaImageIOFactory(itk.ITKCommonBasePython.itkObjectFactoryBase):
    r"""


    Create instances of MetaImageIO objects using an object factory. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMetaImageIOPython.itkMetaImageIOFactory___New_orig__)
    RegisterOneFactory = _swig_new_static_method(_itkMetaImageIOPython.itkMetaImageIOFactory_RegisterOneFactory)
    __swig_destroy__ = _itkMetaImageIOPython.delete_itkMetaImageIOFactory
    cast = _swig_new_static_method(_itkMetaImageIOPython.itkMetaImageIOFactory_cast)

    def New(*args, **kargs):
        """New() -> itkMetaImageIOFactory

        Create a new object of the class itkMetaImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMetaImageIOFactory.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMetaImageIOFactory.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMetaImageIOFactory.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMetaImageIOFactory in _itkMetaImageIOPython:
_itkMetaImageIOPython.itkMetaImageIOFactory_swigregister(itkMetaImageIOFactory)
itkMetaImageIOFactory___New_orig__ = _itkMetaImageIOPython.itkMetaImageIOFactory___New_orig__
itkMetaImageIOFactory_RegisterOneFactory = _itkMetaImageIOPython.itkMetaImageIOFactory_RegisterOneFactory
itkMetaImageIOFactory_cast = _itkMetaImageIOPython.itkMetaImageIOFactory_cast



