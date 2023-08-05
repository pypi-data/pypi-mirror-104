# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKImageFunctionPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkExtrapolateImageFunctionPython
else:
    import _itkExtrapolateImageFunctionPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkExtrapolateImageFunctionPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkExtrapolateImageFunctionPython.SWIG_PyStaticMethod_New

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
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkSizePython
import itk.pyBasePython
import itk.itkOffsetPython
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.ITKCommonBasePython
import itk.itkImageFunctionBasePython
import itk.itkFunctionBasePython
import itk.itkRGBPixelPython
import itk.itkImagePython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkImageRegionPython
import itk.itkRGBAPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkArrayPython
class itkExtrapolateImageFunctionID2D(itk.itkImageFunctionBasePython.itkImageFunctionID2DD):
    r"""


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionID2D
    cast = _swig_new_static_method(_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionID2D_cast)

# Register itkExtrapolateImageFunctionID2D in _itkExtrapolateImageFunctionPython:
_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionID2D_swigregister(itkExtrapolateImageFunctionID2D)
itkExtrapolateImageFunctionID2D_cast = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionID2D_cast

class itkExtrapolateImageFunctionID3D(itk.itkImageFunctionBasePython.itkImageFunctionID3DD):
    r"""


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionID3D
    cast = _swig_new_static_method(_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionID3D_cast)

# Register itkExtrapolateImageFunctionID3D in _itkExtrapolateImageFunctionPython:
_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionID3D_swigregister(itkExtrapolateImageFunctionID3D)
itkExtrapolateImageFunctionID3D_cast = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionID3D_cast

class itkExtrapolateImageFunctionID4D(itk.itkImageFunctionBasePython.itkImageFunctionID4DD):
    r"""


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionID4D
    cast = _swig_new_static_method(_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionID4D_cast)

# Register itkExtrapolateImageFunctionID4D in _itkExtrapolateImageFunctionPython:
_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionID4D_swigregister(itkExtrapolateImageFunctionID4D)
itkExtrapolateImageFunctionID4D_cast = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionID4D_cast

class itkExtrapolateImageFunctionIF2D(itk.itkImageFunctionBasePython.itkImageFunctionIF2DD):
    r"""


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionIF2D
    cast = _swig_new_static_method(_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIF2D_cast)

# Register itkExtrapolateImageFunctionIF2D in _itkExtrapolateImageFunctionPython:
_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIF2D_swigregister(itkExtrapolateImageFunctionIF2D)
itkExtrapolateImageFunctionIF2D_cast = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIF2D_cast

class itkExtrapolateImageFunctionIF3D(itk.itkImageFunctionBasePython.itkImageFunctionIF3DD):
    r"""


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionIF3D
    cast = _swig_new_static_method(_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIF3D_cast)

# Register itkExtrapolateImageFunctionIF3D in _itkExtrapolateImageFunctionPython:
_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIF3D_swigregister(itkExtrapolateImageFunctionIF3D)
itkExtrapolateImageFunctionIF3D_cast = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIF3D_cast

class itkExtrapolateImageFunctionIF4D(itk.itkImageFunctionBasePython.itkImageFunctionIF4DD):
    r"""


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionIF4D
    cast = _swig_new_static_method(_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIF4D_cast)

# Register itkExtrapolateImageFunctionIF4D in _itkExtrapolateImageFunctionPython:
_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIF4D_swigregister(itkExtrapolateImageFunctionIF4D)
itkExtrapolateImageFunctionIF4D_cast = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIF4D_cast

class itkExtrapolateImageFunctionISS2D(itk.itkImageFunctionBasePython.itkImageFunctionISS2DD):
    r"""


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionISS2D
    cast = _swig_new_static_method(_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionISS2D_cast)

# Register itkExtrapolateImageFunctionISS2D in _itkExtrapolateImageFunctionPython:
_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionISS2D_swigregister(itkExtrapolateImageFunctionISS2D)
itkExtrapolateImageFunctionISS2D_cast = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionISS2D_cast

class itkExtrapolateImageFunctionISS3D(itk.itkImageFunctionBasePython.itkImageFunctionISS3DD):
    r"""


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionISS3D
    cast = _swig_new_static_method(_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionISS3D_cast)

# Register itkExtrapolateImageFunctionISS3D in _itkExtrapolateImageFunctionPython:
_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionISS3D_swigregister(itkExtrapolateImageFunctionISS3D)
itkExtrapolateImageFunctionISS3D_cast = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionISS3D_cast

class itkExtrapolateImageFunctionISS4D(itk.itkImageFunctionBasePython.itkImageFunctionISS4DD):
    r"""


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionISS4D
    cast = _swig_new_static_method(_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionISS4D_cast)

# Register itkExtrapolateImageFunctionISS4D in _itkExtrapolateImageFunctionPython:
_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionISS4D_swigregister(itkExtrapolateImageFunctionISS4D)
itkExtrapolateImageFunctionISS4D_cast = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionISS4D_cast

class itkExtrapolateImageFunctionIUC2D(itk.itkImageFunctionBasePython.itkImageFunctionIUC2DD):
    r"""


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionIUC2D
    cast = _swig_new_static_method(_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUC2D_cast)

# Register itkExtrapolateImageFunctionIUC2D in _itkExtrapolateImageFunctionPython:
_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUC2D_swigregister(itkExtrapolateImageFunctionIUC2D)
itkExtrapolateImageFunctionIUC2D_cast = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUC2D_cast

class itkExtrapolateImageFunctionIUC3D(itk.itkImageFunctionBasePython.itkImageFunctionIUC3DD):
    r"""


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionIUC3D
    cast = _swig_new_static_method(_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUC3D_cast)

# Register itkExtrapolateImageFunctionIUC3D in _itkExtrapolateImageFunctionPython:
_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUC3D_swigregister(itkExtrapolateImageFunctionIUC3D)
itkExtrapolateImageFunctionIUC3D_cast = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUC3D_cast

class itkExtrapolateImageFunctionIUC4D(itk.itkImageFunctionBasePython.itkImageFunctionIUC4DD):
    r"""


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionIUC4D
    cast = _swig_new_static_method(_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUC4D_cast)

# Register itkExtrapolateImageFunctionIUC4D in _itkExtrapolateImageFunctionPython:
_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUC4D_swigregister(itkExtrapolateImageFunctionIUC4D)
itkExtrapolateImageFunctionIUC4D_cast = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUC4D_cast

class itkExtrapolateImageFunctionIUS2D(itk.itkImageFunctionBasePython.itkImageFunctionIUS2DD):
    r"""


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionIUS2D
    cast = _swig_new_static_method(_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUS2D_cast)

# Register itkExtrapolateImageFunctionIUS2D in _itkExtrapolateImageFunctionPython:
_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUS2D_swigregister(itkExtrapolateImageFunctionIUS2D)
itkExtrapolateImageFunctionIUS2D_cast = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUS2D_cast

class itkExtrapolateImageFunctionIUS3D(itk.itkImageFunctionBasePython.itkImageFunctionIUS3DD):
    r"""


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionIUS3D
    cast = _swig_new_static_method(_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUS3D_cast)

# Register itkExtrapolateImageFunctionIUS3D in _itkExtrapolateImageFunctionPython:
_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUS3D_swigregister(itkExtrapolateImageFunctionIUS3D)
itkExtrapolateImageFunctionIUS3D_cast = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUS3D_cast

class itkExtrapolateImageFunctionIUS4D(itk.itkImageFunctionBasePython.itkImageFunctionIUS4DD):
    r"""


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionIUS4D
    cast = _swig_new_static_method(_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUS4D_cast)

# Register itkExtrapolateImageFunctionIUS4D in _itkExtrapolateImageFunctionPython:
_itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUS4D_swigregister(itkExtrapolateImageFunctionIUS4D)
itkExtrapolateImageFunctionIUS4D_cast = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUS4D_cast



