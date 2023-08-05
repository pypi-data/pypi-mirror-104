# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKIOGDCMPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkGDCMImageIOPython
else:
    import _itkGDCMImageIOPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkGDCMImageIOPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkGDCMImageIOPython.SWIG_PyStaticMethod_New

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

def itkGDCMImageIO_New():
    return itkGDCMImageIO.New()

class itkGDCMImageIO(itk.ITKIOImageBaseBasePython.itkImageIOBase):
    r"""


    ImageIO class for reading and writing DICOM V3.0 and ACR/NEMA 1&2
    uncompressed images. This class is only an adaptor to the GDCM
    library.

    GDCM can be found at:http://sourceforge.net/projects/gdcm

    To learn more about the revision shipped with ITK, call

    git log Modules/ThirdParty/GDCM/src/

    from an ITK Git checkout.

    The compressors supported include "JPEG2000" (default), and
    "JPEG". The compression level parameter is not supported.

    WARNING:  There are several restrictions to this current writer: Even
    though during the writing process you pass in a DICOM file as input
    The output file may not contains ALL DICOM field from the input file.
    In particular: The SeQuence DICOM field (SQ).

    Fields from Private Dictionary.

    Some very long (>0xfff) binary fields are not loaded (typically
    0029|0010), you need to explicitly set the maximum length of elements
    to load to be bigger (see Get/SetMaxSizeLoadEntry).

    In DICOM some fields are stored directly using their binary
    representation. When loaded into the MetaDataDictionary some fields
    are converted to ASCII (only VR: OB/OW/OF and UN are encoded as
    mime64). 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGDCMImageIOPython.itkGDCMImageIO___New_orig__)
    Clone = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_Clone)
    GetInternalComponentType = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_GetInternalComponentType)
    SetInternalComponentType = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_SetInternalComponentType)
    GetRescaleSlope = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_GetRescaleSlope)
    GetRescaleIntercept = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_GetRescaleIntercept)
    GetUIDPrefix = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_GetUIDPrefix)
    SetUIDPrefix = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_SetUIDPrefix)
    GetStudyInstanceUID = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_GetStudyInstanceUID)
    GetSeriesInstanceUID = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_GetSeriesInstanceUID)
    GetFrameOfReferenceInstanceUID = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_GetFrameOfReferenceInstanceUID)
    SetKeepOriginalUID = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_SetKeepOriginalUID)
    GetKeepOriginalUID = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_GetKeepOriginalUID)
    KeepOriginalUIDOn = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_KeepOriginalUIDOn)
    KeepOriginalUIDOff = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_KeepOriginalUIDOff)
    SetLoadPrivateTags = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_SetLoadPrivateTags)
    GetLoadPrivateTags = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_GetLoadPrivateTags)
    LoadPrivateTagsOn = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_LoadPrivateTagsOn)
    LoadPrivateTagsOff = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_LoadPrivateTagsOff)
    SetReadYBRtoRGB = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_SetReadYBRtoRGB)
    GetReadYBRtoRGB = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_GetReadYBRtoRGB)
    ReadYBRtoRGBOn = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_ReadYBRtoRGBOn)
    ReadYBRtoRGBOff = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_ReadYBRtoRGBOff)
    GetValueFromTag = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_GetValueFromTag)
    GetLabelFromTag = _swig_new_static_method(_itkGDCMImageIOPython.itkGDCMImageIO_GetLabelFromTag)
    SetCompressionType = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_SetCompressionType)
    GetCompressionType = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_GetCompressionType)
    InternalSetCompressor = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMImageIO_InternalSetCompressor)
    __swig_destroy__ = _itkGDCMImageIOPython.delete_itkGDCMImageIO
    cast = _swig_new_static_method(_itkGDCMImageIOPython.itkGDCMImageIO_cast)

    def New(*args, **kargs):
        """New() -> itkGDCMImageIO

        Create a new object of the class itkGDCMImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGDCMImageIO.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGDCMImageIO.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGDCMImageIO.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGDCMImageIO in _itkGDCMImageIOPython:
_itkGDCMImageIOPython.itkGDCMImageIO_swigregister(itkGDCMImageIO)
itkGDCMImageIO___New_orig__ = _itkGDCMImageIOPython.itkGDCMImageIO___New_orig__
itkGDCMImageIO_GetLabelFromTag = _itkGDCMImageIOPython.itkGDCMImageIO_GetLabelFromTag
itkGDCMImageIO_cast = _itkGDCMImageIOPython.itkGDCMImageIO_cast

class itkGDCMImageIOEnums(object):
    r"""Proxy of C++ itkGDCMImageIOEnums class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Compression_JPEG = _itkGDCMImageIOPython.itkGDCMImageIOEnums_Compression_JPEG
    
    Compression_JPEG2000 = _itkGDCMImageIOPython.itkGDCMImageIOEnums_Compression_JPEG2000
    
    Compression_JPEGLS = _itkGDCMImageIOPython.itkGDCMImageIOEnums_Compression_JPEGLS
    
    Compression_RLE = _itkGDCMImageIOPython.itkGDCMImageIOEnums_Compression_RLE
    

    def __init__(self, *args):
        r"""
        __init__(self) -> itkGDCMImageIOEnums
        __init__(self, arg0) -> itkGDCMImageIOEnums

        Parameters
        ----------
        arg0: itkGDCMImageIOEnums const &

        """
        _itkGDCMImageIOPython.itkGDCMImageIOEnums_swiginit(self, _itkGDCMImageIOPython.new_itkGDCMImageIOEnums(*args))
    __swig_destroy__ = _itkGDCMImageIOPython.delete_itkGDCMImageIOEnums

# Register itkGDCMImageIOEnums in _itkGDCMImageIOPython:
_itkGDCMImageIOPython.itkGDCMImageIOEnums_swigregister(itkGDCMImageIOEnums)


def itkGDCMImageIOFactory_New():
    return itkGDCMImageIOFactory.New()

class itkGDCMImageIOFactory(itk.ITKCommonBasePython.itkObjectFactoryBase):
    r"""


    Create instances of GDCMImageIO objects using an object factory. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGDCMImageIOPython.itkGDCMImageIOFactory___New_orig__)
    RegisterOneFactory = _swig_new_static_method(_itkGDCMImageIOPython.itkGDCMImageIOFactory_RegisterOneFactory)
    __swig_destroy__ = _itkGDCMImageIOPython.delete_itkGDCMImageIOFactory
    cast = _swig_new_static_method(_itkGDCMImageIOPython.itkGDCMImageIOFactory_cast)

    def New(*args, **kargs):
        """New() -> itkGDCMImageIOFactory

        Create a new object of the class itkGDCMImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGDCMImageIOFactory.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGDCMImageIOFactory.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGDCMImageIOFactory.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGDCMImageIOFactory in _itkGDCMImageIOPython:
_itkGDCMImageIOPython.itkGDCMImageIOFactory_swigregister(itkGDCMImageIOFactory)
itkGDCMImageIOFactory___New_orig__ = _itkGDCMImageIOPython.itkGDCMImageIOFactory___New_orig__
itkGDCMImageIOFactory_RegisterOneFactory = _itkGDCMImageIOPython.itkGDCMImageIOFactory_RegisterOneFactory
itkGDCMImageIOFactory_cast = _itkGDCMImageIOPython.itkGDCMImageIOFactory_cast


def itkGDCMSeriesFileNames_New():
    return itkGDCMSeriesFileNames.New()

class itkGDCMSeriesFileNames(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    Generate a sequence of filenames from a DICOM series.

    This class generates a sequence of files whose filenames point to a
    DICOM file. The ordering is based on the following strategy: Read all
    images in the directory (assuming there is only one study/series)

    Extract Image Orientation & Image Position from DICOM images, and then
    calculate the ordering based on the 3D coordinate of the slice.

    If for some reason this information is not found or failed, another
    strategy is used: the ordering is based on 'Instance Number'.

    If this strategy also failed, then the filenames are ordered by
    lexicographical order.

    If multiple volumes are being grouped as a single series for your
    DICOM objects, you may want to try calling SetUseSeriesDetails(true)
    prior to calling SetDirectory(). 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames___New_orig__)
    Clone = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_Clone)
    SetInputDirectory = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_SetInputDirectory)
    SetDirectory = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_SetDirectory)
    GetInputFileNames = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_GetInputFileNames)
    SetOutputDirectory = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_SetOutputDirectory)
    GetOutputFileNames = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_GetOutputFileNames)
    GetFileNames = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_GetFileNames)
    GetSeriesUIDs = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_GetSeriesUIDs)
    SetRecursive = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_SetRecursive)
    GetRecursive = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_GetRecursive)
    RecursiveOn = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_RecursiveOn)
    RecursiveOff = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_RecursiveOff)
    SetUseSeriesDetails = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_SetUseSeriesDetails)
    GetUseSeriesDetails = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_GetUseSeriesDetails)
    AddSeriesRestriction = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_AddSeriesRestriction)
    SetLoadSequences = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_SetLoadSequences)
    GetLoadSequences = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_GetLoadSequences)
    LoadSequencesOn = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_LoadSequencesOn)
    LoadSequencesOff = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_LoadSequencesOff)
    SetLoadPrivateTags = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_SetLoadPrivateTags)
    GetLoadPrivateTags = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_GetLoadPrivateTags)
    LoadPrivateTagsOn = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_LoadPrivateTagsOn)
    LoadPrivateTagsOff = _swig_new_instance_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_LoadPrivateTagsOff)
    __swig_destroy__ = _itkGDCMImageIOPython.delete_itkGDCMSeriesFileNames
    cast = _swig_new_static_method(_itkGDCMImageIOPython.itkGDCMSeriesFileNames_cast)

    def New(*args, **kargs):
        """New() -> itkGDCMSeriesFileNames

        Create a new object of the class itkGDCMSeriesFileNames and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGDCMSeriesFileNames.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGDCMSeriesFileNames.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGDCMSeriesFileNames.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGDCMSeriesFileNames in _itkGDCMImageIOPython:
_itkGDCMImageIOPython.itkGDCMSeriesFileNames_swigregister(itkGDCMSeriesFileNames)
itkGDCMSeriesFileNames___New_orig__ = _itkGDCMImageIOPython.itkGDCMSeriesFileNames___New_orig__
itkGDCMSeriesFileNames_cast = _itkGDCMImageIOPython.itkGDCMSeriesFileNames_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def gdcm_series_file_names(*args,  input_directory: str=..., directory: str=..., output_directory: str=..., recursive: bool=..., use_series_details: bool=..., load_sequences: bool=..., load_private_tags: bool=...,**kwargs):
    """Functional interface for GDCMSeriesFileNames"""
    import itk

    kwarg_typehints = { 'input_directory':input_directory,'directory':directory,'output_directory':output_directory,'recursive':recursive,'use_series_details':use_series_details,'load_sequences':load_sequences,'load_private_tags':load_private_tags }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.GDCMSeriesFileNames.New(*args, **kwargs)
    return instance.__internal_call__()

def gdcm_series_file_names_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKIOGDCM.GDCMSeriesFileNames
    gdcm_series_file_names.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    gdcm_series_file_names.__doc__ = filter_object.__doc__




