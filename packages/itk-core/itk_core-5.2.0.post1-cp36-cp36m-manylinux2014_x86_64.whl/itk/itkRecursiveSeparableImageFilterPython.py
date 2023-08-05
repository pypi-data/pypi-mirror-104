# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKImageFilterBasePython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkRecursiveSeparableImageFilterPython
else:
    import _itkRecursiveSeparableImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkRecursiveSeparableImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkRecursiveSeparableImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkInPlaceImageFilterAPython
import itk.itkImageToImageFilterBPython
import itk.itkImagePython
import itk.stdcomplexPython
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
import itk.itkSymmetricSecondRankTensorPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageToImageFilterAPython
class itkRecursiveSeparableImageFilterID2ID2(itk.itkInPlaceImageFilterAPython.itkInPlaceImageFilterID2ID2):
    r"""


    Base class for recursive convolution with a kernel.

    RecursiveSeparableImageFilter is the base class for recursive filters
    that are applied in each dimension separately. If multi-component
    images are specified, the filtering operation works on each component
    independently.

    This class implements the recursive filtering method proposed by
    R.Deriche in IEEE-PAMI Vol.12, No.1, January 1990, pp 78-87.

    Details of the implementation are described in the technical report:
    R. Deriche, "Recursively Implementing The Gaussian and Its
    Derivatives", INRIA, 1993,ftp://ftp.inria.fr/INRIA/tech-
    reports/RR/RR-1893.ps.gz

    Further improvements of the algorithm are described in: G. Farnebäck &
    C.-F. Westin, "Improving Deriche-style Recursive Gaussian Filters".
    J Math Imaging Vis 26, 293–299
    (2006).https://doi.org/10.1007/s10851-006-8464-z 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    GetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID2ID2_GetDirection)
    SetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID2ID2_SetDirection)
    SetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID2ID2_SetInputImage)
    GetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID2ID2_GetInputImage)
    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterID2ID2
    cast = _swig_new_static_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID2ID2_cast)

# Register itkRecursiveSeparableImageFilterID2ID2 in _itkRecursiveSeparableImageFilterPython:
_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID2ID2_swigregister(itkRecursiveSeparableImageFilterID2ID2)
itkRecursiveSeparableImageFilterID2ID2_cast = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID2ID2_cast

class itkRecursiveSeparableImageFilterID3ID3(itk.itkInPlaceImageFilterAPython.itkInPlaceImageFilterID3ID3):
    r"""


    Base class for recursive convolution with a kernel.

    RecursiveSeparableImageFilter is the base class for recursive filters
    that are applied in each dimension separately. If multi-component
    images are specified, the filtering operation works on each component
    independently.

    This class implements the recursive filtering method proposed by
    R.Deriche in IEEE-PAMI Vol.12, No.1, January 1990, pp 78-87.

    Details of the implementation are described in the technical report:
    R. Deriche, "Recursively Implementing The Gaussian and Its
    Derivatives", INRIA, 1993,ftp://ftp.inria.fr/INRIA/tech-
    reports/RR/RR-1893.ps.gz

    Further improvements of the algorithm are described in: G. Farnebäck &
    C.-F. Westin, "Improving Deriche-style Recursive Gaussian Filters".
    J Math Imaging Vis 26, 293–299
    (2006).https://doi.org/10.1007/s10851-006-8464-z 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    GetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID3ID3_GetDirection)
    SetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID3ID3_SetDirection)
    SetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID3ID3_SetInputImage)
    GetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID3ID3_GetInputImage)
    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterID3ID3
    cast = _swig_new_static_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID3ID3_cast)

# Register itkRecursiveSeparableImageFilterID3ID3 in _itkRecursiveSeparableImageFilterPython:
_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID3ID3_swigregister(itkRecursiveSeparableImageFilterID3ID3)
itkRecursiveSeparableImageFilterID3ID3_cast = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID3ID3_cast

class itkRecursiveSeparableImageFilterID4ID4(itk.itkInPlaceImageFilterAPython.itkInPlaceImageFilterID4ID4):
    r"""


    Base class for recursive convolution with a kernel.

    RecursiveSeparableImageFilter is the base class for recursive filters
    that are applied in each dimension separately. If multi-component
    images are specified, the filtering operation works on each component
    independently.

    This class implements the recursive filtering method proposed by
    R.Deriche in IEEE-PAMI Vol.12, No.1, January 1990, pp 78-87.

    Details of the implementation are described in the technical report:
    R. Deriche, "Recursively Implementing The Gaussian and Its
    Derivatives", INRIA, 1993,ftp://ftp.inria.fr/INRIA/tech-
    reports/RR/RR-1893.ps.gz

    Further improvements of the algorithm are described in: G. Farnebäck &
    C.-F. Westin, "Improving Deriche-style Recursive Gaussian Filters".
    J Math Imaging Vis 26, 293–299
    (2006).https://doi.org/10.1007/s10851-006-8464-z 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    GetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID4ID4_GetDirection)
    SetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID4ID4_SetDirection)
    SetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID4ID4_SetInputImage)
    GetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID4ID4_GetInputImage)
    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterID4ID4
    cast = _swig_new_static_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID4ID4_cast)

# Register itkRecursiveSeparableImageFilterID4ID4 in _itkRecursiveSeparableImageFilterPython:
_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID4ID4_swigregister(itkRecursiveSeparableImageFilterID4ID4)
itkRecursiveSeparableImageFilterID4ID4_cast = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterID4ID4_cast

class itkRecursiveSeparableImageFilterIF2IF2(itk.itkInPlaceImageFilterAPython.itkInPlaceImageFilterIF2IF2):
    r"""


    Base class for recursive convolution with a kernel.

    RecursiveSeparableImageFilter is the base class for recursive filters
    that are applied in each dimension separately. If multi-component
    images are specified, the filtering operation works on each component
    independently.

    This class implements the recursive filtering method proposed by
    R.Deriche in IEEE-PAMI Vol.12, No.1, January 1990, pp 78-87.

    Details of the implementation are described in the technical report:
    R. Deriche, "Recursively Implementing The Gaussian and Its
    Derivatives", INRIA, 1993,ftp://ftp.inria.fr/INRIA/tech-
    reports/RR/RR-1893.ps.gz

    Further improvements of the algorithm are described in: G. Farnebäck &
    C.-F. Westin, "Improving Deriche-style Recursive Gaussian Filters".
    J Math Imaging Vis 26, 293–299
    (2006).https://doi.org/10.1007/s10851-006-8464-z 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    GetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF2IF2_GetDirection)
    SetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF2IF2_SetDirection)
    SetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF2IF2_SetInputImage)
    GetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF2IF2_GetInputImage)
    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterIF2IF2
    cast = _swig_new_static_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF2IF2_cast)

# Register itkRecursiveSeparableImageFilterIF2IF2 in _itkRecursiveSeparableImageFilterPython:
_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF2IF2_swigregister(itkRecursiveSeparableImageFilterIF2IF2)
itkRecursiveSeparableImageFilterIF2IF2_cast = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF2IF2_cast

class itkRecursiveSeparableImageFilterIF3IF3(itk.itkInPlaceImageFilterAPython.itkInPlaceImageFilterIF3IF3):
    r"""


    Base class for recursive convolution with a kernel.

    RecursiveSeparableImageFilter is the base class for recursive filters
    that are applied in each dimension separately. If multi-component
    images are specified, the filtering operation works on each component
    independently.

    This class implements the recursive filtering method proposed by
    R.Deriche in IEEE-PAMI Vol.12, No.1, January 1990, pp 78-87.

    Details of the implementation are described in the technical report:
    R. Deriche, "Recursively Implementing The Gaussian and Its
    Derivatives", INRIA, 1993,ftp://ftp.inria.fr/INRIA/tech-
    reports/RR/RR-1893.ps.gz

    Further improvements of the algorithm are described in: G. Farnebäck &
    C.-F. Westin, "Improving Deriche-style Recursive Gaussian Filters".
    J Math Imaging Vis 26, 293–299
    (2006).https://doi.org/10.1007/s10851-006-8464-z 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    GetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF3IF3_GetDirection)
    SetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF3IF3_SetDirection)
    SetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF3IF3_SetInputImage)
    GetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF3IF3_GetInputImage)
    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterIF3IF3
    cast = _swig_new_static_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF3IF3_cast)

# Register itkRecursiveSeparableImageFilterIF3IF3 in _itkRecursiveSeparableImageFilterPython:
_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF3IF3_swigregister(itkRecursiveSeparableImageFilterIF3IF3)
itkRecursiveSeparableImageFilterIF3IF3_cast = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF3IF3_cast

class itkRecursiveSeparableImageFilterIF4IF4(itk.itkInPlaceImageFilterAPython.itkInPlaceImageFilterIF4IF4):
    r"""


    Base class for recursive convolution with a kernel.

    RecursiveSeparableImageFilter is the base class for recursive filters
    that are applied in each dimension separately. If multi-component
    images are specified, the filtering operation works on each component
    independently.

    This class implements the recursive filtering method proposed by
    R.Deriche in IEEE-PAMI Vol.12, No.1, January 1990, pp 78-87.

    Details of the implementation are described in the technical report:
    R. Deriche, "Recursively Implementing The Gaussian and Its
    Derivatives", INRIA, 1993,ftp://ftp.inria.fr/INRIA/tech-
    reports/RR/RR-1893.ps.gz

    Further improvements of the algorithm are described in: G. Farnebäck &
    C.-F. Westin, "Improving Deriche-style Recursive Gaussian Filters".
    J Math Imaging Vis 26, 293–299
    (2006).https://doi.org/10.1007/s10851-006-8464-z 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    GetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF4IF4_GetDirection)
    SetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF4IF4_SetDirection)
    SetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF4IF4_SetInputImage)
    GetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF4IF4_GetInputImage)
    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterIF4IF4
    cast = _swig_new_static_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF4IF4_cast)

# Register itkRecursiveSeparableImageFilterIF4IF4 in _itkRecursiveSeparableImageFilterPython:
_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF4IF4_swigregister(itkRecursiveSeparableImageFilterIF4IF4)
itkRecursiveSeparableImageFilterIF4IF4_cast = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIF4IF4_cast

class itkRecursiveSeparableImageFilterISS2ISS2(itk.itkInPlaceImageFilterAPython.itkInPlaceImageFilterISS2ISS2):
    r"""


    Base class for recursive convolution with a kernel.

    RecursiveSeparableImageFilter is the base class for recursive filters
    that are applied in each dimension separately. If multi-component
    images are specified, the filtering operation works on each component
    independently.

    This class implements the recursive filtering method proposed by
    R.Deriche in IEEE-PAMI Vol.12, No.1, January 1990, pp 78-87.

    Details of the implementation are described in the technical report:
    R. Deriche, "Recursively Implementing The Gaussian and Its
    Derivatives", INRIA, 1993,ftp://ftp.inria.fr/INRIA/tech-
    reports/RR/RR-1893.ps.gz

    Further improvements of the algorithm are described in: G. Farnebäck &
    C.-F. Westin, "Improving Deriche-style Recursive Gaussian Filters".
    J Math Imaging Vis 26, 293–299
    (2006).https://doi.org/10.1007/s10851-006-8464-z 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    GetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS2ISS2_GetDirection)
    SetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS2ISS2_SetDirection)
    SetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS2ISS2_SetInputImage)
    GetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS2ISS2_GetInputImage)
    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterISS2ISS2
    cast = _swig_new_static_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS2ISS2_cast)

# Register itkRecursiveSeparableImageFilterISS2ISS2 in _itkRecursiveSeparableImageFilterPython:
_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS2ISS2_swigregister(itkRecursiveSeparableImageFilterISS2ISS2)
itkRecursiveSeparableImageFilterISS2ISS2_cast = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS2ISS2_cast

class itkRecursiveSeparableImageFilterISS3ISS3(itk.itkInPlaceImageFilterAPython.itkInPlaceImageFilterISS3ISS3):
    r"""


    Base class for recursive convolution with a kernel.

    RecursiveSeparableImageFilter is the base class for recursive filters
    that are applied in each dimension separately. If multi-component
    images are specified, the filtering operation works on each component
    independently.

    This class implements the recursive filtering method proposed by
    R.Deriche in IEEE-PAMI Vol.12, No.1, January 1990, pp 78-87.

    Details of the implementation are described in the technical report:
    R. Deriche, "Recursively Implementing The Gaussian and Its
    Derivatives", INRIA, 1993,ftp://ftp.inria.fr/INRIA/tech-
    reports/RR/RR-1893.ps.gz

    Further improvements of the algorithm are described in: G. Farnebäck &
    C.-F. Westin, "Improving Deriche-style Recursive Gaussian Filters".
    J Math Imaging Vis 26, 293–299
    (2006).https://doi.org/10.1007/s10851-006-8464-z 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    GetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS3ISS3_GetDirection)
    SetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS3ISS3_SetDirection)
    SetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS3ISS3_SetInputImage)
    GetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS3ISS3_GetInputImage)
    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterISS3ISS3
    cast = _swig_new_static_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS3ISS3_cast)

# Register itkRecursiveSeparableImageFilterISS3ISS3 in _itkRecursiveSeparableImageFilterPython:
_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS3ISS3_swigregister(itkRecursiveSeparableImageFilterISS3ISS3)
itkRecursiveSeparableImageFilterISS3ISS3_cast = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS3ISS3_cast

class itkRecursiveSeparableImageFilterISS4ISS4(itk.itkInPlaceImageFilterAPython.itkInPlaceImageFilterISS4ISS4):
    r"""


    Base class for recursive convolution with a kernel.

    RecursiveSeparableImageFilter is the base class for recursive filters
    that are applied in each dimension separately. If multi-component
    images are specified, the filtering operation works on each component
    independently.

    This class implements the recursive filtering method proposed by
    R.Deriche in IEEE-PAMI Vol.12, No.1, January 1990, pp 78-87.

    Details of the implementation are described in the technical report:
    R. Deriche, "Recursively Implementing The Gaussian and Its
    Derivatives", INRIA, 1993,ftp://ftp.inria.fr/INRIA/tech-
    reports/RR/RR-1893.ps.gz

    Further improvements of the algorithm are described in: G. Farnebäck &
    C.-F. Westin, "Improving Deriche-style Recursive Gaussian Filters".
    J Math Imaging Vis 26, 293–299
    (2006).https://doi.org/10.1007/s10851-006-8464-z 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    GetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS4ISS4_GetDirection)
    SetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS4ISS4_SetDirection)
    SetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS4ISS4_SetInputImage)
    GetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS4ISS4_GetInputImage)
    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterISS4ISS4
    cast = _swig_new_static_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS4ISS4_cast)

# Register itkRecursiveSeparableImageFilterISS4ISS4 in _itkRecursiveSeparableImageFilterPython:
_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS4ISS4_swigregister(itkRecursiveSeparableImageFilterISS4ISS4)
itkRecursiveSeparableImageFilterISS4ISS4_cast = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterISS4ISS4_cast

class itkRecursiveSeparableImageFilterIUC2IUC2(itk.itkInPlaceImageFilterAPython.itkInPlaceImageFilterIUC2IUC2):
    r"""


    Base class for recursive convolution with a kernel.

    RecursiveSeparableImageFilter is the base class for recursive filters
    that are applied in each dimension separately. If multi-component
    images are specified, the filtering operation works on each component
    independently.

    This class implements the recursive filtering method proposed by
    R.Deriche in IEEE-PAMI Vol.12, No.1, January 1990, pp 78-87.

    Details of the implementation are described in the technical report:
    R. Deriche, "Recursively Implementing The Gaussian and Its
    Derivatives", INRIA, 1993,ftp://ftp.inria.fr/INRIA/tech-
    reports/RR/RR-1893.ps.gz

    Further improvements of the algorithm are described in: G. Farnebäck &
    C.-F. Westin, "Improving Deriche-style Recursive Gaussian Filters".
    J Math Imaging Vis 26, 293–299
    (2006).https://doi.org/10.1007/s10851-006-8464-z 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    GetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC2IUC2_GetDirection)
    SetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC2IUC2_SetDirection)
    SetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC2IUC2_SetInputImage)
    GetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC2IUC2_GetInputImage)
    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterIUC2IUC2
    cast = _swig_new_static_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC2IUC2_cast)

# Register itkRecursiveSeparableImageFilterIUC2IUC2 in _itkRecursiveSeparableImageFilterPython:
_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC2IUC2_swigregister(itkRecursiveSeparableImageFilterIUC2IUC2)
itkRecursiveSeparableImageFilterIUC2IUC2_cast = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC2IUC2_cast

class itkRecursiveSeparableImageFilterIUC3IUC3(itk.itkInPlaceImageFilterAPython.itkInPlaceImageFilterIUC3IUC3):
    r"""


    Base class for recursive convolution with a kernel.

    RecursiveSeparableImageFilter is the base class for recursive filters
    that are applied in each dimension separately. If multi-component
    images are specified, the filtering operation works on each component
    independently.

    This class implements the recursive filtering method proposed by
    R.Deriche in IEEE-PAMI Vol.12, No.1, January 1990, pp 78-87.

    Details of the implementation are described in the technical report:
    R. Deriche, "Recursively Implementing The Gaussian and Its
    Derivatives", INRIA, 1993,ftp://ftp.inria.fr/INRIA/tech-
    reports/RR/RR-1893.ps.gz

    Further improvements of the algorithm are described in: G. Farnebäck &
    C.-F. Westin, "Improving Deriche-style Recursive Gaussian Filters".
    J Math Imaging Vis 26, 293–299
    (2006).https://doi.org/10.1007/s10851-006-8464-z 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    GetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC3IUC3_GetDirection)
    SetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC3IUC3_SetDirection)
    SetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC3IUC3_SetInputImage)
    GetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC3IUC3_GetInputImage)
    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterIUC3IUC3
    cast = _swig_new_static_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC3IUC3_cast)

# Register itkRecursiveSeparableImageFilterIUC3IUC3 in _itkRecursiveSeparableImageFilterPython:
_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC3IUC3_swigregister(itkRecursiveSeparableImageFilterIUC3IUC3)
itkRecursiveSeparableImageFilterIUC3IUC3_cast = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC3IUC3_cast

class itkRecursiveSeparableImageFilterIUC4IUC4(itk.itkInPlaceImageFilterAPython.itkInPlaceImageFilterIUC4IUC4):
    r"""


    Base class for recursive convolution with a kernel.

    RecursiveSeparableImageFilter is the base class for recursive filters
    that are applied in each dimension separately. If multi-component
    images are specified, the filtering operation works on each component
    independently.

    This class implements the recursive filtering method proposed by
    R.Deriche in IEEE-PAMI Vol.12, No.1, January 1990, pp 78-87.

    Details of the implementation are described in the technical report:
    R. Deriche, "Recursively Implementing The Gaussian and Its
    Derivatives", INRIA, 1993,ftp://ftp.inria.fr/INRIA/tech-
    reports/RR/RR-1893.ps.gz

    Further improvements of the algorithm are described in: G. Farnebäck &
    C.-F. Westin, "Improving Deriche-style Recursive Gaussian Filters".
    J Math Imaging Vis 26, 293–299
    (2006).https://doi.org/10.1007/s10851-006-8464-z 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    GetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC4IUC4_GetDirection)
    SetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC4IUC4_SetDirection)
    SetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC4IUC4_SetInputImage)
    GetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC4IUC4_GetInputImage)
    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterIUC4IUC4
    cast = _swig_new_static_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC4IUC4_cast)

# Register itkRecursiveSeparableImageFilterIUC4IUC4 in _itkRecursiveSeparableImageFilterPython:
_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC4IUC4_swigregister(itkRecursiveSeparableImageFilterIUC4IUC4)
itkRecursiveSeparableImageFilterIUC4IUC4_cast = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUC4IUC4_cast

class itkRecursiveSeparableImageFilterIUS2IUS2(itk.itkInPlaceImageFilterAPython.itkInPlaceImageFilterIUS2IUS2):
    r"""


    Base class for recursive convolution with a kernel.

    RecursiveSeparableImageFilter is the base class for recursive filters
    that are applied in each dimension separately. If multi-component
    images are specified, the filtering operation works on each component
    independently.

    This class implements the recursive filtering method proposed by
    R.Deriche in IEEE-PAMI Vol.12, No.1, January 1990, pp 78-87.

    Details of the implementation are described in the technical report:
    R. Deriche, "Recursively Implementing The Gaussian and Its
    Derivatives", INRIA, 1993,ftp://ftp.inria.fr/INRIA/tech-
    reports/RR/RR-1893.ps.gz

    Further improvements of the algorithm are described in: G. Farnebäck &
    C.-F. Westin, "Improving Deriche-style Recursive Gaussian Filters".
    J Math Imaging Vis 26, 293–299
    (2006).https://doi.org/10.1007/s10851-006-8464-z 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    GetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS2IUS2_GetDirection)
    SetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS2IUS2_SetDirection)
    SetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS2IUS2_SetInputImage)
    GetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS2IUS2_GetInputImage)
    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterIUS2IUS2
    cast = _swig_new_static_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS2IUS2_cast)

# Register itkRecursiveSeparableImageFilterIUS2IUS2 in _itkRecursiveSeparableImageFilterPython:
_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS2IUS2_swigregister(itkRecursiveSeparableImageFilterIUS2IUS2)
itkRecursiveSeparableImageFilterIUS2IUS2_cast = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS2IUS2_cast

class itkRecursiveSeparableImageFilterIUS3IUS3(itk.itkInPlaceImageFilterAPython.itkInPlaceImageFilterIUS3IUS3):
    r"""


    Base class for recursive convolution with a kernel.

    RecursiveSeparableImageFilter is the base class for recursive filters
    that are applied in each dimension separately. If multi-component
    images are specified, the filtering operation works on each component
    independently.

    This class implements the recursive filtering method proposed by
    R.Deriche in IEEE-PAMI Vol.12, No.1, January 1990, pp 78-87.

    Details of the implementation are described in the technical report:
    R. Deriche, "Recursively Implementing The Gaussian and Its
    Derivatives", INRIA, 1993,ftp://ftp.inria.fr/INRIA/tech-
    reports/RR/RR-1893.ps.gz

    Further improvements of the algorithm are described in: G. Farnebäck &
    C.-F. Westin, "Improving Deriche-style Recursive Gaussian Filters".
    J Math Imaging Vis 26, 293–299
    (2006).https://doi.org/10.1007/s10851-006-8464-z 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    GetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS3IUS3_GetDirection)
    SetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS3IUS3_SetDirection)
    SetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS3IUS3_SetInputImage)
    GetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS3IUS3_GetInputImage)
    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterIUS3IUS3
    cast = _swig_new_static_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS3IUS3_cast)

# Register itkRecursiveSeparableImageFilterIUS3IUS3 in _itkRecursiveSeparableImageFilterPython:
_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS3IUS3_swigregister(itkRecursiveSeparableImageFilterIUS3IUS3)
itkRecursiveSeparableImageFilterIUS3IUS3_cast = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS3IUS3_cast

class itkRecursiveSeparableImageFilterIUS4IUS4(itk.itkInPlaceImageFilterAPython.itkInPlaceImageFilterIUS4IUS4):
    r"""


    Base class for recursive convolution with a kernel.

    RecursiveSeparableImageFilter is the base class for recursive filters
    that are applied in each dimension separately. If multi-component
    images are specified, the filtering operation works on each component
    independently.

    This class implements the recursive filtering method proposed by
    R.Deriche in IEEE-PAMI Vol.12, No.1, January 1990, pp 78-87.

    Details of the implementation are described in the technical report:
    R. Deriche, "Recursively Implementing The Gaussian and Its
    Derivatives", INRIA, 1993,ftp://ftp.inria.fr/INRIA/tech-
    reports/RR/RR-1893.ps.gz

    Further improvements of the algorithm are described in: G. Farnebäck &
    C.-F. Westin, "Improving Deriche-style Recursive Gaussian Filters".
    J Math Imaging Vis 26, 293–299
    (2006).https://doi.org/10.1007/s10851-006-8464-z 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    GetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS4IUS4_GetDirection)
    SetDirection = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS4IUS4_SetDirection)
    SetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS4IUS4_SetInputImage)
    GetInputImage = _swig_new_instance_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS4IUS4_GetInputImage)
    __swig_destroy__ = _itkRecursiveSeparableImageFilterPython.delete_itkRecursiveSeparableImageFilterIUS4IUS4
    cast = _swig_new_static_method(_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS4IUS4_cast)

# Register itkRecursiveSeparableImageFilterIUS4IUS4 in _itkRecursiveSeparableImageFilterPython:
_itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS4IUS4_swigregister(itkRecursiveSeparableImageFilterIUS4IUS4)
itkRecursiveSeparableImageFilterIUS4IUS4_cast = _itkRecursiveSeparableImageFilterPython.itkRecursiveSeparableImageFilterIUS4IUS4_cast



