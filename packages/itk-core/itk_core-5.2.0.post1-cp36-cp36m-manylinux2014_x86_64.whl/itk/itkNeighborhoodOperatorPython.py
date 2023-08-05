# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKCommonPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkNeighborhoodOperatorPython
else:
    import _itkNeighborhoodOperatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkNeighborhoodOperatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkNeighborhoodOperatorPython.SWIG_PyStaticMethod_New

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
import itk.itkNeighborhoodPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.pyBasePython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.itkRGBPixelPython
import itk.ITKCommonBasePython
class itkNeighborhoodOperatorD2(itk.itkNeighborhoodPython.itkNeighborhoodD2):
    r"""


    Virtual class that defines a common interface to all neighborhood
    operator subtypes.

    A NeighborhoodOperator is a set of pixel values that can be applied to
    a Neighborhood to perform a user-defined operation (i.e. convolution
    kernel, morphological structuring element). A NeighborhoodOperator is
    itself a specialized Neighborhood, with functionality to generate its
    coefficients according to user- defined parameters. Because the
    operator is a subclass of Neighborhood, it is a valid operand in any
    of the operations defined on the Neighborhood object (convolution,
    inner product, etc.).

    NeighborhoodOperator is a pure virtual object that must be subclassed
    to be used. A user's subclass must implement two methods:

    (1) GenerateCoefficients the algorithm that computes the scalar
    coefficients of the operator.

    (2) Fill the algorithm that places the scalar coefficients into the
    memory buffer of the operator (arranges them spatially in the
    neighborhood).

    NeighborhoodOperator supports the concept of a "directional
    operator." A directional operator is defined in this context to be an
    operator that is applied along a single dimension. Examples of this
    type of operator are directional derivatives and the individual,
    directional components of separable processes such as Gaussian
    smoothing.

    How a NeighborhoodOperator is applied to data is up to the user who
    defines it. One possible use of an operator would be to take its inner
    product with a neighborhood of values to produce a scalar result. This
    process effects convolution when applied to successive neighborhoods
    across a region of interest in an image.

    NeighborhoodOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetDirection = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2_SetDirection)
    GetDirection = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2_GetDirection)
    CreateDirectional = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2_CreateDirectional)
    CreateToRadius = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2_CreateToRadius)
    FlipAxes = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2_FlipAxes)
    PrintSelf = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2_PrintSelf)
    ScaleCoefficients = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2_ScaleCoefficients)
    __swig_destroy__ = _itkNeighborhoodOperatorPython.delete_itkNeighborhoodOperatorD2

# Register itkNeighborhoodOperatorD2 in _itkNeighborhoodOperatorPython:
_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2_swigregister(itkNeighborhoodOperatorD2)

class itkNeighborhoodOperatorD3(itk.itkNeighborhoodPython.itkNeighborhoodD3):
    r"""


    Virtual class that defines a common interface to all neighborhood
    operator subtypes.

    A NeighborhoodOperator is a set of pixel values that can be applied to
    a Neighborhood to perform a user-defined operation (i.e. convolution
    kernel, morphological structuring element). A NeighborhoodOperator is
    itself a specialized Neighborhood, with functionality to generate its
    coefficients according to user- defined parameters. Because the
    operator is a subclass of Neighborhood, it is a valid operand in any
    of the operations defined on the Neighborhood object (convolution,
    inner product, etc.).

    NeighborhoodOperator is a pure virtual object that must be subclassed
    to be used. A user's subclass must implement two methods:

    (1) GenerateCoefficients the algorithm that computes the scalar
    coefficients of the operator.

    (2) Fill the algorithm that places the scalar coefficients into the
    memory buffer of the operator (arranges them spatially in the
    neighborhood).

    NeighborhoodOperator supports the concept of a "directional
    operator." A directional operator is defined in this context to be an
    operator that is applied along a single dimension. Examples of this
    type of operator are directional derivatives and the individual,
    directional components of separable processes such as Gaussian
    smoothing.

    How a NeighborhoodOperator is applied to data is up to the user who
    defines it. One possible use of an operator would be to take its inner
    product with a neighborhood of values to produce a scalar result. This
    process effects convolution when applied to successive neighborhoods
    across a region of interest in an image.

    NeighborhoodOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetDirection = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3_GetDirection)
    CreateDirectional = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3_CreateDirectional)
    CreateToRadius = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3_CreateToRadius)
    FlipAxes = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3_FlipAxes)
    PrintSelf = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3_PrintSelf)
    ScaleCoefficients = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3_ScaleCoefficients)
    __swig_destroy__ = _itkNeighborhoodOperatorPython.delete_itkNeighborhoodOperatorD3

# Register itkNeighborhoodOperatorD3 in _itkNeighborhoodOperatorPython:
_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3_swigregister(itkNeighborhoodOperatorD3)

class itkNeighborhoodOperatorD4(itk.itkNeighborhoodPython.itkNeighborhoodD4):
    r"""


    Virtual class that defines a common interface to all neighborhood
    operator subtypes.

    A NeighborhoodOperator is a set of pixel values that can be applied to
    a Neighborhood to perform a user-defined operation (i.e. convolution
    kernel, morphological structuring element). A NeighborhoodOperator is
    itself a specialized Neighborhood, with functionality to generate its
    coefficients according to user- defined parameters. Because the
    operator is a subclass of Neighborhood, it is a valid operand in any
    of the operations defined on the Neighborhood object (convolution,
    inner product, etc.).

    NeighborhoodOperator is a pure virtual object that must be subclassed
    to be used. A user's subclass must implement two methods:

    (1) GenerateCoefficients the algorithm that computes the scalar
    coefficients of the operator.

    (2) Fill the algorithm that places the scalar coefficients into the
    memory buffer of the operator (arranges them spatially in the
    neighborhood).

    NeighborhoodOperator supports the concept of a "directional
    operator." A directional operator is defined in this context to be an
    operator that is applied along a single dimension. Examples of this
    type of operator are directional derivatives and the individual,
    directional components of separable processes such as Gaussian
    smoothing.

    How a NeighborhoodOperator is applied to data is up to the user who
    defines it. One possible use of an operator would be to take its inner
    product with a neighborhood of values to produce a scalar result. This
    process effects convolution when applied to successive neighborhoods
    across a region of interest in an image.

    NeighborhoodOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetDirection = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD4_SetDirection)
    GetDirection = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD4_GetDirection)
    CreateDirectional = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD4_CreateDirectional)
    CreateToRadius = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD4_CreateToRadius)
    FlipAxes = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD4_FlipAxes)
    PrintSelf = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD4_PrintSelf)
    ScaleCoefficients = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD4_ScaleCoefficients)
    __swig_destroy__ = _itkNeighborhoodOperatorPython.delete_itkNeighborhoodOperatorD4

# Register itkNeighborhoodOperatorD4 in _itkNeighborhoodOperatorPython:
_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD4_swigregister(itkNeighborhoodOperatorD4)

class itkNeighborhoodOperatorF2(itk.itkNeighborhoodPython.itkNeighborhoodF2):
    r"""


    Virtual class that defines a common interface to all neighborhood
    operator subtypes.

    A NeighborhoodOperator is a set of pixel values that can be applied to
    a Neighborhood to perform a user-defined operation (i.e. convolution
    kernel, morphological structuring element). A NeighborhoodOperator is
    itself a specialized Neighborhood, with functionality to generate its
    coefficients according to user- defined parameters. Because the
    operator is a subclass of Neighborhood, it is a valid operand in any
    of the operations defined on the Neighborhood object (convolution,
    inner product, etc.).

    NeighborhoodOperator is a pure virtual object that must be subclassed
    to be used. A user's subclass must implement two methods:

    (1) GenerateCoefficients the algorithm that computes the scalar
    coefficients of the operator.

    (2) Fill the algorithm that places the scalar coefficients into the
    memory buffer of the operator (arranges them spatially in the
    neighborhood).

    NeighborhoodOperator supports the concept of a "directional
    operator." A directional operator is defined in this context to be an
    operator that is applied along a single dimension. Examples of this
    type of operator are directional derivatives and the individual,
    directional components of separable processes such as Gaussian
    smoothing.

    How a NeighborhoodOperator is applied to data is up to the user who
    defines it. One possible use of an operator would be to take its inner
    product with a neighborhood of values to produce a scalar result. This
    process effects convolution when applied to successive neighborhoods
    across a region of interest in an image.

    NeighborhoodOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetDirection = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2_SetDirection)
    GetDirection = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2_GetDirection)
    CreateDirectional = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2_CreateDirectional)
    CreateToRadius = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2_CreateToRadius)
    FlipAxes = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2_FlipAxes)
    PrintSelf = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2_PrintSelf)
    ScaleCoefficients = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2_ScaleCoefficients)
    __swig_destroy__ = _itkNeighborhoodOperatorPython.delete_itkNeighborhoodOperatorF2

# Register itkNeighborhoodOperatorF2 in _itkNeighborhoodOperatorPython:
_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2_swigregister(itkNeighborhoodOperatorF2)

class itkNeighborhoodOperatorF3(itk.itkNeighborhoodPython.itkNeighborhoodF3):
    r"""


    Virtual class that defines a common interface to all neighborhood
    operator subtypes.

    A NeighborhoodOperator is a set of pixel values that can be applied to
    a Neighborhood to perform a user-defined operation (i.e. convolution
    kernel, morphological structuring element). A NeighborhoodOperator is
    itself a specialized Neighborhood, with functionality to generate its
    coefficients according to user- defined parameters. Because the
    operator is a subclass of Neighborhood, it is a valid operand in any
    of the operations defined on the Neighborhood object (convolution,
    inner product, etc.).

    NeighborhoodOperator is a pure virtual object that must be subclassed
    to be used. A user's subclass must implement two methods:

    (1) GenerateCoefficients the algorithm that computes the scalar
    coefficients of the operator.

    (2) Fill the algorithm that places the scalar coefficients into the
    memory buffer of the operator (arranges them spatially in the
    neighborhood).

    NeighborhoodOperator supports the concept of a "directional
    operator." A directional operator is defined in this context to be an
    operator that is applied along a single dimension. Examples of this
    type of operator are directional derivatives and the individual,
    directional components of separable processes such as Gaussian
    smoothing.

    How a NeighborhoodOperator is applied to data is up to the user who
    defines it. One possible use of an operator would be to take its inner
    product with a neighborhood of values to produce a scalar result. This
    process effects convolution when applied to successive neighborhoods
    across a region of interest in an image.

    NeighborhoodOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetDirection = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3_GetDirection)
    CreateDirectional = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3_CreateDirectional)
    CreateToRadius = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3_CreateToRadius)
    FlipAxes = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3_FlipAxes)
    PrintSelf = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3_PrintSelf)
    ScaleCoefficients = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3_ScaleCoefficients)
    __swig_destroy__ = _itkNeighborhoodOperatorPython.delete_itkNeighborhoodOperatorF3

# Register itkNeighborhoodOperatorF3 in _itkNeighborhoodOperatorPython:
_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3_swigregister(itkNeighborhoodOperatorF3)

class itkNeighborhoodOperatorF4(itk.itkNeighborhoodPython.itkNeighborhoodF4):
    r"""


    Virtual class that defines a common interface to all neighborhood
    operator subtypes.

    A NeighborhoodOperator is a set of pixel values that can be applied to
    a Neighborhood to perform a user-defined operation (i.e. convolution
    kernel, morphological structuring element). A NeighborhoodOperator is
    itself a specialized Neighborhood, with functionality to generate its
    coefficients according to user- defined parameters. Because the
    operator is a subclass of Neighborhood, it is a valid operand in any
    of the operations defined on the Neighborhood object (convolution,
    inner product, etc.).

    NeighborhoodOperator is a pure virtual object that must be subclassed
    to be used. A user's subclass must implement two methods:

    (1) GenerateCoefficients the algorithm that computes the scalar
    coefficients of the operator.

    (2) Fill the algorithm that places the scalar coefficients into the
    memory buffer of the operator (arranges them spatially in the
    neighborhood).

    NeighborhoodOperator supports the concept of a "directional
    operator." A directional operator is defined in this context to be an
    operator that is applied along a single dimension. Examples of this
    type of operator are directional derivatives and the individual,
    directional components of separable processes such as Gaussian
    smoothing.

    How a NeighborhoodOperator is applied to data is up to the user who
    defines it. One possible use of an operator would be to take its inner
    product with a neighborhood of values to produce a scalar result. This
    process effects convolution when applied to successive neighborhoods
    across a region of interest in an image.

    NeighborhoodOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetDirection = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF4_SetDirection)
    GetDirection = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF4_GetDirection)
    CreateDirectional = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF4_CreateDirectional)
    CreateToRadius = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF4_CreateToRadius)
    FlipAxes = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF4_FlipAxes)
    PrintSelf = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF4_PrintSelf)
    ScaleCoefficients = _swig_new_instance_method(_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF4_ScaleCoefficients)
    __swig_destroy__ = _itkNeighborhoodOperatorPython.delete_itkNeighborhoodOperatorF4

# Register itkNeighborhoodOperatorF4 in _itkNeighborhoodOperatorPython:
_itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF4_swigregister(itkNeighborhoodOperatorF4)



