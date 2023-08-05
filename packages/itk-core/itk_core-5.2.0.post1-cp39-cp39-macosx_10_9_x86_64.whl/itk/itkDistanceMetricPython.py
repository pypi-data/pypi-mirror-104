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
    from . import _itkDistanceMetricPython
else:
    import _itkDistanceMetricPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkDistanceMetricPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkDistanceMetricPython.SWIG_PyStaticMethod_New

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
import itk.itkFunctionBasePython
import itk.itkImagePython
import itk.itkMatrixPython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkRGBPixelPython
import itk.itkRGBAPixelPython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkArrayPython
import itk.itkContinuousIndexPython
class itkDistanceMetricVF2(itk.itkFunctionBasePython.itkFunctionBaseVF2D):
    r"""


    this class declares common interfaces for distance functions.

    As a function derived from FunctionBase, users use Evaluate method to
    get result.

    To use this function users should first set the origin by calling
    SetOrigin() function, then call Evaluate() method with a point to get
    the distance between the origin point and the evaluation point.

    See:  EuclideanSquareDistanceMetric

    See:   EuclideanDistanceMetric

    See:  ManhattanDistanceMetric 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetOrigin = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF2_SetOrigin)
    GetOrigin = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF2_GetOrigin)
    Evaluate = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF2_Evaluate)
    SetMeasurementVectorSize = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF2_SetMeasurementVectorSize)
    GetMeasurementVectorSize = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF2_GetMeasurementVectorSize)
    __swig_destroy__ = _itkDistanceMetricPython.delete_itkDistanceMetricVF2
    cast = _swig_new_static_method(_itkDistanceMetricPython.itkDistanceMetricVF2_cast)

# Register itkDistanceMetricVF2 in _itkDistanceMetricPython:
_itkDistanceMetricPython.itkDistanceMetricVF2_swigregister(itkDistanceMetricVF2)
itkDistanceMetricVF2_cast = _itkDistanceMetricPython.itkDistanceMetricVF2_cast

class itkDistanceMetricVF3(itk.itkFunctionBasePython.itkFunctionBaseVF3D):
    r"""


    this class declares common interfaces for distance functions.

    As a function derived from FunctionBase, users use Evaluate method to
    get result.

    To use this function users should first set the origin by calling
    SetOrigin() function, then call Evaluate() method with a point to get
    the distance between the origin point and the evaluation point.

    See:  EuclideanSquareDistanceMetric

    See:   EuclideanDistanceMetric

    See:  ManhattanDistanceMetric 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetOrigin = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF3_SetOrigin)
    GetOrigin = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF3_GetOrigin)
    Evaluate = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF3_Evaluate)
    SetMeasurementVectorSize = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF3_SetMeasurementVectorSize)
    GetMeasurementVectorSize = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF3_GetMeasurementVectorSize)
    __swig_destroy__ = _itkDistanceMetricPython.delete_itkDistanceMetricVF3
    cast = _swig_new_static_method(_itkDistanceMetricPython.itkDistanceMetricVF3_cast)

# Register itkDistanceMetricVF3 in _itkDistanceMetricPython:
_itkDistanceMetricPython.itkDistanceMetricVF3_swigregister(itkDistanceMetricVF3)
itkDistanceMetricVF3_cast = _itkDistanceMetricPython.itkDistanceMetricVF3_cast

class itkDistanceMetricVF4(itk.itkFunctionBasePython.itkFunctionBaseVF4D):
    r"""


    this class declares common interfaces for distance functions.

    As a function derived from FunctionBase, users use Evaluate method to
    get result.

    To use this function users should first set the origin by calling
    SetOrigin() function, then call Evaluate() method with a point to get
    the distance between the origin point and the evaluation point.

    See:  EuclideanSquareDistanceMetric

    See:   EuclideanDistanceMetric

    See:  ManhattanDistanceMetric 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetOrigin = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF4_SetOrigin)
    GetOrigin = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF4_GetOrigin)
    Evaluate = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF4_Evaluate)
    SetMeasurementVectorSize = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF4_SetMeasurementVectorSize)
    GetMeasurementVectorSize = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF4_GetMeasurementVectorSize)
    __swig_destroy__ = _itkDistanceMetricPython.delete_itkDistanceMetricVF4
    cast = _swig_new_static_method(_itkDistanceMetricPython.itkDistanceMetricVF4_cast)

# Register itkDistanceMetricVF4 in _itkDistanceMetricPython:
_itkDistanceMetricPython.itkDistanceMetricVF4_swigregister(itkDistanceMetricVF4)
itkDistanceMetricVF4_cast = _itkDistanceMetricPython.itkDistanceMetricVF4_cast



