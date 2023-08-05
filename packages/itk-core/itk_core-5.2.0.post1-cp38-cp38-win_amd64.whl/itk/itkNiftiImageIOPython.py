# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKIONIFTIPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkNiftiImageIOPython
else:
    import _itkNiftiImageIOPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkNiftiImageIOPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkNiftiImageIOPython.SWIG_PyStaticMethod_New

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
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython

def itkNiftiImageIO_New():
    return itkNiftiImageIO.New()

class itkNiftiImageIO(itk.ITKIOImageBaseBasePython.itkImageIOBase):
    r"""


    Class that defines how to read Nifti file format. Nifti IMAGE FILE
    FORMAT - As much information as I can determine from
    sourceforge.net/projects/Niftilib.

    Hans J. Johnson, The University of Iowa 2002 The specification for
    this file format is taken from the web sitehttp://analyzedirect.com/su
    pport/10.0Documents/Analyze_Resource_01.pdf 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkNiftiImageIOPython.itkNiftiImageIO___New_orig__)
    Clone = _swig_new_instance_method(_itkNiftiImageIOPython.itkNiftiImageIO_Clone)
    DetermineFileType = _swig_new_instance_method(_itkNiftiImageIOPython.itkNiftiImageIO_DetermineFileType)
    SetRescaleSlope = _swig_new_instance_method(_itkNiftiImageIOPython.itkNiftiImageIO_SetRescaleSlope)
    SetRescaleIntercept = _swig_new_instance_method(_itkNiftiImageIOPython.itkNiftiImageIO_SetRescaleIntercept)
    SetLegacyAnalyze75Mode = _swig_new_instance_method(_itkNiftiImageIOPython.itkNiftiImageIO_SetLegacyAnalyze75Mode)
    GetLegacyAnalyze75Mode = _swig_new_instance_method(_itkNiftiImageIOPython.itkNiftiImageIO_GetLegacyAnalyze75Mode)
    __swig_destroy__ = _itkNiftiImageIOPython.delete_itkNiftiImageIO
    cast = _swig_new_static_method(_itkNiftiImageIOPython.itkNiftiImageIO_cast)

    def New(*args, **kargs):
        """New() -> itkNiftiImageIO

        Create a new object of the class itkNiftiImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNiftiImageIO.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkNiftiImageIO.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkNiftiImageIO.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkNiftiImageIO in _itkNiftiImageIOPython:
_itkNiftiImageIOPython.itkNiftiImageIO_swigregister(itkNiftiImageIO)
itkNiftiImageIO___New_orig__ = _itkNiftiImageIOPython.itkNiftiImageIO___New_orig__
itkNiftiImageIO_cast = _itkNiftiImageIOPython.itkNiftiImageIO_cast

class itkNiftiImageIOEnums(object):
    r"""Proxy of C++ itkNiftiImageIOEnums class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Analyze75Flavor_AnalyzeITK4 = _itkNiftiImageIOPython.itkNiftiImageIOEnums_Analyze75Flavor_AnalyzeITK4
    
    Analyze75Flavor_AnalyzeFSL = _itkNiftiImageIOPython.itkNiftiImageIOEnums_Analyze75Flavor_AnalyzeFSL
    
    Analyze75Flavor_AnalyzeSPM = _itkNiftiImageIOPython.itkNiftiImageIOEnums_Analyze75Flavor_AnalyzeSPM
    
    Analyze75Flavor_AnalyzeITK4Warning = _itkNiftiImageIOPython.itkNiftiImageIOEnums_Analyze75Flavor_AnalyzeITK4Warning
    
    Analyze75Flavor_AnalyzeReject = _itkNiftiImageIOPython.itkNiftiImageIOEnums_Analyze75Flavor_AnalyzeReject
    
    NiftiFileEnum_TwoFileNifti = _itkNiftiImageIOPython.itkNiftiImageIOEnums_NiftiFileEnum_TwoFileNifti
    
    NiftiFileEnum_OneFileNifti = _itkNiftiImageIOPython.itkNiftiImageIOEnums_NiftiFileEnum_OneFileNifti
    
    NiftiFileEnum_Analyze75 = _itkNiftiImageIOPython.itkNiftiImageIOEnums_NiftiFileEnum_Analyze75
    
    NiftiFileEnum_OtherOrError = _itkNiftiImageIOPython.itkNiftiImageIOEnums_NiftiFileEnum_OtherOrError
    

    def __init__(self, *args):
        r"""
        __init__(self) -> itkNiftiImageIOEnums
        __init__(self, arg0) -> itkNiftiImageIOEnums

        Parameters
        ----------
        arg0: itkNiftiImageIOEnums const &

        """
        _itkNiftiImageIOPython.itkNiftiImageIOEnums_swiginit(self, _itkNiftiImageIOPython.new_itkNiftiImageIOEnums(*args))
    __swig_destroy__ = _itkNiftiImageIOPython.delete_itkNiftiImageIOEnums

# Register itkNiftiImageIOEnums in _itkNiftiImageIOPython:
_itkNiftiImageIOPython.itkNiftiImageIOEnums_swigregister(itkNiftiImageIOEnums)


def itkNiftiImageIOFactory_New():
    return itkNiftiImageIOFactory.New()

class itkNiftiImageIOFactory(itk.ITKCommonBasePython.itkObjectFactoryBase):
    r"""


    Create instances of NiftiImageIO objects using an object factory. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkNiftiImageIOPython.itkNiftiImageIOFactory___New_orig__)
    RegisterOneFactory = _swig_new_static_method(_itkNiftiImageIOPython.itkNiftiImageIOFactory_RegisterOneFactory)
    __swig_destroy__ = _itkNiftiImageIOPython.delete_itkNiftiImageIOFactory
    cast = _swig_new_static_method(_itkNiftiImageIOPython.itkNiftiImageIOFactory_cast)

    def New(*args, **kargs):
        """New() -> itkNiftiImageIOFactory

        Create a new object of the class itkNiftiImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNiftiImageIOFactory.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkNiftiImageIOFactory.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkNiftiImageIOFactory.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkNiftiImageIOFactory in _itkNiftiImageIOPython:
_itkNiftiImageIOPython.itkNiftiImageIOFactory_swigregister(itkNiftiImageIOFactory)
itkNiftiImageIOFactory___New_orig__ = _itkNiftiImageIOPython.itkNiftiImageIOFactory___New_orig__
itkNiftiImageIOFactory_RegisterOneFactory = _itkNiftiImageIOPython.itkNiftiImageIOFactory_RegisterOneFactory
itkNiftiImageIOFactory_cast = _itkNiftiImageIOPython.itkNiftiImageIOFactory_cast



