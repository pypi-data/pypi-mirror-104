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
    from . import _itkSobelOperatorPython
else:
    import _itkSobelOperatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkSobelOperatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkSobelOperatorPython.SWIG_PyStaticMethod_New

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
import itk.itkNeighborhoodOperatorPython
import itk.itkSizePython
import itk.itkNeighborhoodPython
import itk.itkRGBPixelPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkCovariantVectorPython
import itk.itkOffsetPython
class itkSobelOperatorD2(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2):
    r"""


    A NeighborhoodOperator for performing a directional Sobel edge-
    detection operation at a pixel location.

    SobelOperator is a directional NeighborhoodOperator that should be
    applied a NeighborhoodIterator using the NeighborhoodInnerProduct
    method. To create the operator:

    1) Set the direction by calling 2) call 3) You may optionally scale
    the coefficients of this operator using the method. This is useful if
    you want to take the spacing of the image into account when computing
    the edge strength. Apply the scaling only after calling to.

    The Sobel Operator in vertical direction for 2 dimensions is*
    -1  -2  -1 *             0    0   0 *             1    2 1 * * The
    Sobel Operator in horizontal direction is for 2 dimensions is*
    -1   0   1 *             -2   0   2 *             -1   0 1 *

    The current implementation of the Sobel operator is for 2 and 3
    dimensions only. The ND version is planned for future releases.

    The extension to 3D is from the publication "Irwin Sobel. An
    Isotropic 3x3x3 Volume Gradient Operator.   Technical report, Hewlett-
    Packard Laboratories, April 1995."

    The Sobel operator in 3D has the kernel

    * -1 -3 -1   0 0 0  1 3 1 * -3 -6 -3   0 0 0  3 6 3 * -1 -3 -1   0 0 0
    1 3 1 * *    x-1       x     x+1 *

    The x kernel is just rotated as required to obtain the kernel in the y
    and z directions.

    SobelOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood

    See:   ForwardDifferenceOperator

    See:   BackwardDifferenceOperator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkSobelOperatorPython.delete_itkSobelOperatorD2

    def __init__(self, *args):
        r"""
        __init__(self) -> itkSobelOperatorD2
        __init__(self, arg0) -> itkSobelOperatorD2

        Parameters
        ----------
        arg0: itkSobelOperatorD2 const &



        A NeighborhoodOperator for performing a directional Sobel edge-
        detection operation at a pixel location.

        SobelOperator is a directional NeighborhoodOperator that should be
        applied a NeighborhoodIterator using the NeighborhoodInnerProduct
        method. To create the operator:

        1) Set the direction by calling 2) call 3) You may optionally scale
        the coefficients of this operator using the method. This is useful if
        you want to take the spacing of the image into account when computing
        the edge strength. Apply the scaling only after calling to.

        The Sobel Operator in vertical direction for 2 dimensions is*
        -1  -2  -1 *             0    0   0 *             1    2 1 * * The
        Sobel Operator in horizontal direction is for 2 dimensions is*
        -1   0   1 *             -2   0   2 *             -1   0 1 *

        The current implementation of the Sobel operator is for 2 and 3
        dimensions only. The ND version is planned for future releases.

        The extension to 3D is from the publication "Irwin Sobel. An
        Isotropic 3x3x3 Volume Gradient Operator.   Technical report, Hewlett-
        Packard Laboratories, April 1995."

        The Sobel operator in 3D has the kernel

        * -1 -3 -1   0 0 0  1 3 1 * -3 -6 -3   0 0 0  3 6 3 * -1 -3 -1   0 0 0
        1 3 1 * *    x-1       x     x+1 *

        The x kernel is just rotated as required to obtain the kernel in the y
        and z directions.

        SobelOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood

        See:   ForwardDifferenceOperator

        See:   BackwardDifferenceOperator 
        """
        _itkSobelOperatorPython.itkSobelOperatorD2_swiginit(self, _itkSobelOperatorPython.new_itkSobelOperatorD2(*args))

# Register itkSobelOperatorD2 in _itkSobelOperatorPython:
_itkSobelOperatorPython.itkSobelOperatorD2_swigregister(itkSobelOperatorD2)

class itkSobelOperatorD3(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3):
    r"""


    A NeighborhoodOperator for performing a directional Sobel edge-
    detection operation at a pixel location.

    SobelOperator is a directional NeighborhoodOperator that should be
    applied a NeighborhoodIterator using the NeighborhoodInnerProduct
    method. To create the operator:

    1) Set the direction by calling 2) call 3) You may optionally scale
    the coefficients of this operator using the method. This is useful if
    you want to take the spacing of the image into account when computing
    the edge strength. Apply the scaling only after calling to.

    The Sobel Operator in vertical direction for 2 dimensions is*
    -1  -2  -1 *             0    0   0 *             1    2 1 * * The
    Sobel Operator in horizontal direction is for 2 dimensions is*
    -1   0   1 *             -2   0   2 *             -1   0 1 *

    The current implementation of the Sobel operator is for 2 and 3
    dimensions only. The ND version is planned for future releases.

    The extension to 3D is from the publication "Irwin Sobel. An
    Isotropic 3x3x3 Volume Gradient Operator.   Technical report, Hewlett-
    Packard Laboratories, April 1995."

    The Sobel operator in 3D has the kernel

    * -1 -3 -1   0 0 0  1 3 1 * -3 -6 -3   0 0 0  3 6 3 * -1 -3 -1   0 0 0
    1 3 1 * *    x-1       x     x+1 *

    The x kernel is just rotated as required to obtain the kernel in the y
    and z directions.

    SobelOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood

    See:   ForwardDifferenceOperator

    See:   BackwardDifferenceOperator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkSobelOperatorPython.delete_itkSobelOperatorD3

    def __init__(self, *args):
        r"""
        __init__(self) -> itkSobelOperatorD3
        __init__(self, arg0) -> itkSobelOperatorD3

        Parameters
        ----------
        arg0: itkSobelOperatorD3 const &



        A NeighborhoodOperator for performing a directional Sobel edge-
        detection operation at a pixel location.

        SobelOperator is a directional NeighborhoodOperator that should be
        applied a NeighborhoodIterator using the NeighborhoodInnerProduct
        method. To create the operator:

        1) Set the direction by calling 2) call 3) You may optionally scale
        the coefficients of this operator using the method. This is useful if
        you want to take the spacing of the image into account when computing
        the edge strength. Apply the scaling only after calling to.

        The Sobel Operator in vertical direction for 2 dimensions is*
        -1  -2  -1 *             0    0   0 *             1    2 1 * * The
        Sobel Operator in horizontal direction is for 2 dimensions is*
        -1   0   1 *             -2   0   2 *             -1   0 1 *

        The current implementation of the Sobel operator is for 2 and 3
        dimensions only. The ND version is planned for future releases.

        The extension to 3D is from the publication "Irwin Sobel. An
        Isotropic 3x3x3 Volume Gradient Operator.   Technical report, Hewlett-
        Packard Laboratories, April 1995."

        The Sobel operator in 3D has the kernel

        * -1 -3 -1   0 0 0  1 3 1 * -3 -6 -3   0 0 0  3 6 3 * -1 -3 -1   0 0 0
        1 3 1 * *    x-1       x     x+1 *

        The x kernel is just rotated as required to obtain the kernel in the y
        and z directions.

        SobelOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood

        See:   ForwardDifferenceOperator

        See:   BackwardDifferenceOperator 
        """
        _itkSobelOperatorPython.itkSobelOperatorD3_swiginit(self, _itkSobelOperatorPython.new_itkSobelOperatorD3(*args))

# Register itkSobelOperatorD3 in _itkSobelOperatorPython:
_itkSobelOperatorPython.itkSobelOperatorD3_swigregister(itkSobelOperatorD3)

class itkSobelOperatorD4(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD4):
    r"""


    A NeighborhoodOperator for performing a directional Sobel edge-
    detection operation at a pixel location.

    SobelOperator is a directional NeighborhoodOperator that should be
    applied a NeighborhoodIterator using the NeighborhoodInnerProduct
    method. To create the operator:

    1) Set the direction by calling 2) call 3) You may optionally scale
    the coefficients of this operator using the method. This is useful if
    you want to take the spacing of the image into account when computing
    the edge strength. Apply the scaling only after calling to.

    The Sobel Operator in vertical direction for 2 dimensions is*
    -1  -2  -1 *             0    0   0 *             1    2 1 * * The
    Sobel Operator in horizontal direction is for 2 dimensions is*
    -1   0   1 *             -2   0   2 *             -1   0 1 *

    The current implementation of the Sobel operator is for 2 and 3
    dimensions only. The ND version is planned for future releases.

    The extension to 3D is from the publication "Irwin Sobel. An
    Isotropic 3x3x3 Volume Gradient Operator.   Technical report, Hewlett-
    Packard Laboratories, April 1995."

    The Sobel operator in 3D has the kernel

    * -1 -3 -1   0 0 0  1 3 1 * -3 -6 -3   0 0 0  3 6 3 * -1 -3 -1   0 0 0
    1 3 1 * *    x-1       x     x+1 *

    The x kernel is just rotated as required to obtain the kernel in the y
    and z directions.

    SobelOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood

    See:   ForwardDifferenceOperator

    See:   BackwardDifferenceOperator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkSobelOperatorPython.delete_itkSobelOperatorD4

    def __init__(self, *args):
        r"""
        __init__(self) -> itkSobelOperatorD4
        __init__(self, arg0) -> itkSobelOperatorD4

        Parameters
        ----------
        arg0: itkSobelOperatorD4 const &



        A NeighborhoodOperator for performing a directional Sobel edge-
        detection operation at a pixel location.

        SobelOperator is a directional NeighborhoodOperator that should be
        applied a NeighborhoodIterator using the NeighborhoodInnerProduct
        method. To create the operator:

        1) Set the direction by calling 2) call 3) You may optionally scale
        the coefficients of this operator using the method. This is useful if
        you want to take the spacing of the image into account when computing
        the edge strength. Apply the scaling only after calling to.

        The Sobel Operator in vertical direction for 2 dimensions is*
        -1  -2  -1 *             0    0   0 *             1    2 1 * * The
        Sobel Operator in horizontal direction is for 2 dimensions is*
        -1   0   1 *             -2   0   2 *             -1   0 1 *

        The current implementation of the Sobel operator is for 2 and 3
        dimensions only. The ND version is planned for future releases.

        The extension to 3D is from the publication "Irwin Sobel. An
        Isotropic 3x3x3 Volume Gradient Operator.   Technical report, Hewlett-
        Packard Laboratories, April 1995."

        The Sobel operator in 3D has the kernel

        * -1 -3 -1   0 0 0  1 3 1 * -3 -6 -3   0 0 0  3 6 3 * -1 -3 -1   0 0 0
        1 3 1 * *    x-1       x     x+1 *

        The x kernel is just rotated as required to obtain the kernel in the y
        and z directions.

        SobelOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood

        See:   ForwardDifferenceOperator

        See:   BackwardDifferenceOperator 
        """
        _itkSobelOperatorPython.itkSobelOperatorD4_swiginit(self, _itkSobelOperatorPython.new_itkSobelOperatorD4(*args))

# Register itkSobelOperatorD4 in _itkSobelOperatorPython:
_itkSobelOperatorPython.itkSobelOperatorD4_swigregister(itkSobelOperatorD4)

class itkSobelOperatorF2(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2):
    r"""


    A NeighborhoodOperator for performing a directional Sobel edge-
    detection operation at a pixel location.

    SobelOperator is a directional NeighborhoodOperator that should be
    applied a NeighborhoodIterator using the NeighborhoodInnerProduct
    method. To create the operator:

    1) Set the direction by calling 2) call 3) You may optionally scale
    the coefficients of this operator using the method. This is useful if
    you want to take the spacing of the image into account when computing
    the edge strength. Apply the scaling only after calling to.

    The Sobel Operator in vertical direction for 2 dimensions is*
    -1  -2  -1 *             0    0   0 *             1    2 1 * * The
    Sobel Operator in horizontal direction is for 2 dimensions is*
    -1   0   1 *             -2   0   2 *             -1   0 1 *

    The current implementation of the Sobel operator is for 2 and 3
    dimensions only. The ND version is planned for future releases.

    The extension to 3D is from the publication "Irwin Sobel. An
    Isotropic 3x3x3 Volume Gradient Operator.   Technical report, Hewlett-
    Packard Laboratories, April 1995."

    The Sobel operator in 3D has the kernel

    * -1 -3 -1   0 0 0  1 3 1 * -3 -6 -3   0 0 0  3 6 3 * -1 -3 -1   0 0 0
    1 3 1 * *    x-1       x     x+1 *

    The x kernel is just rotated as required to obtain the kernel in the y
    and z directions.

    SobelOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood

    See:   ForwardDifferenceOperator

    See:   BackwardDifferenceOperator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkSobelOperatorPython.delete_itkSobelOperatorF2

    def __init__(self, *args):
        r"""
        __init__(self) -> itkSobelOperatorF2
        __init__(self, arg0) -> itkSobelOperatorF2

        Parameters
        ----------
        arg0: itkSobelOperatorF2 const &



        A NeighborhoodOperator for performing a directional Sobel edge-
        detection operation at a pixel location.

        SobelOperator is a directional NeighborhoodOperator that should be
        applied a NeighborhoodIterator using the NeighborhoodInnerProduct
        method. To create the operator:

        1) Set the direction by calling 2) call 3) You may optionally scale
        the coefficients of this operator using the method. This is useful if
        you want to take the spacing of the image into account when computing
        the edge strength. Apply the scaling only after calling to.

        The Sobel Operator in vertical direction for 2 dimensions is*
        -1  -2  -1 *             0    0   0 *             1    2 1 * * The
        Sobel Operator in horizontal direction is for 2 dimensions is*
        -1   0   1 *             -2   0   2 *             -1   0 1 *

        The current implementation of the Sobel operator is for 2 and 3
        dimensions only. The ND version is planned for future releases.

        The extension to 3D is from the publication "Irwin Sobel. An
        Isotropic 3x3x3 Volume Gradient Operator.   Technical report, Hewlett-
        Packard Laboratories, April 1995."

        The Sobel operator in 3D has the kernel

        * -1 -3 -1   0 0 0  1 3 1 * -3 -6 -3   0 0 0  3 6 3 * -1 -3 -1   0 0 0
        1 3 1 * *    x-1       x     x+1 *

        The x kernel is just rotated as required to obtain the kernel in the y
        and z directions.

        SobelOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood

        See:   ForwardDifferenceOperator

        See:   BackwardDifferenceOperator 
        """
        _itkSobelOperatorPython.itkSobelOperatorF2_swiginit(self, _itkSobelOperatorPython.new_itkSobelOperatorF2(*args))

# Register itkSobelOperatorF2 in _itkSobelOperatorPython:
_itkSobelOperatorPython.itkSobelOperatorF2_swigregister(itkSobelOperatorF2)

class itkSobelOperatorF3(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3):
    r"""


    A NeighborhoodOperator for performing a directional Sobel edge-
    detection operation at a pixel location.

    SobelOperator is a directional NeighborhoodOperator that should be
    applied a NeighborhoodIterator using the NeighborhoodInnerProduct
    method. To create the operator:

    1) Set the direction by calling 2) call 3) You may optionally scale
    the coefficients of this operator using the method. This is useful if
    you want to take the spacing of the image into account when computing
    the edge strength. Apply the scaling only after calling to.

    The Sobel Operator in vertical direction for 2 dimensions is*
    -1  -2  -1 *             0    0   0 *             1    2 1 * * The
    Sobel Operator in horizontal direction is for 2 dimensions is*
    -1   0   1 *             -2   0   2 *             -1   0 1 *

    The current implementation of the Sobel operator is for 2 and 3
    dimensions only. The ND version is planned for future releases.

    The extension to 3D is from the publication "Irwin Sobel. An
    Isotropic 3x3x3 Volume Gradient Operator.   Technical report, Hewlett-
    Packard Laboratories, April 1995."

    The Sobel operator in 3D has the kernel

    * -1 -3 -1   0 0 0  1 3 1 * -3 -6 -3   0 0 0  3 6 3 * -1 -3 -1   0 0 0
    1 3 1 * *    x-1       x     x+1 *

    The x kernel is just rotated as required to obtain the kernel in the y
    and z directions.

    SobelOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood

    See:   ForwardDifferenceOperator

    See:   BackwardDifferenceOperator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkSobelOperatorPython.delete_itkSobelOperatorF3

    def __init__(self, *args):
        r"""
        __init__(self) -> itkSobelOperatorF3
        __init__(self, arg0) -> itkSobelOperatorF3

        Parameters
        ----------
        arg0: itkSobelOperatorF3 const &



        A NeighborhoodOperator for performing a directional Sobel edge-
        detection operation at a pixel location.

        SobelOperator is a directional NeighborhoodOperator that should be
        applied a NeighborhoodIterator using the NeighborhoodInnerProduct
        method. To create the operator:

        1) Set the direction by calling 2) call 3) You may optionally scale
        the coefficients of this operator using the method. This is useful if
        you want to take the spacing of the image into account when computing
        the edge strength. Apply the scaling only after calling to.

        The Sobel Operator in vertical direction for 2 dimensions is*
        -1  -2  -1 *             0    0   0 *             1    2 1 * * The
        Sobel Operator in horizontal direction is for 2 dimensions is*
        -1   0   1 *             -2   0   2 *             -1   0 1 *

        The current implementation of the Sobel operator is for 2 and 3
        dimensions only. The ND version is planned for future releases.

        The extension to 3D is from the publication "Irwin Sobel. An
        Isotropic 3x3x3 Volume Gradient Operator.   Technical report, Hewlett-
        Packard Laboratories, April 1995."

        The Sobel operator in 3D has the kernel

        * -1 -3 -1   0 0 0  1 3 1 * -3 -6 -3   0 0 0  3 6 3 * -1 -3 -1   0 0 0
        1 3 1 * *    x-1       x     x+1 *

        The x kernel is just rotated as required to obtain the kernel in the y
        and z directions.

        SobelOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood

        See:   ForwardDifferenceOperator

        See:   BackwardDifferenceOperator 
        """
        _itkSobelOperatorPython.itkSobelOperatorF3_swiginit(self, _itkSobelOperatorPython.new_itkSobelOperatorF3(*args))

# Register itkSobelOperatorF3 in _itkSobelOperatorPython:
_itkSobelOperatorPython.itkSobelOperatorF3_swigregister(itkSobelOperatorF3)

class itkSobelOperatorF4(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF4):
    r"""


    A NeighborhoodOperator for performing a directional Sobel edge-
    detection operation at a pixel location.

    SobelOperator is a directional NeighborhoodOperator that should be
    applied a NeighborhoodIterator using the NeighborhoodInnerProduct
    method. To create the operator:

    1) Set the direction by calling 2) call 3) You may optionally scale
    the coefficients of this operator using the method. This is useful if
    you want to take the spacing of the image into account when computing
    the edge strength. Apply the scaling only after calling to.

    The Sobel Operator in vertical direction for 2 dimensions is*
    -1  -2  -1 *             0    0   0 *             1    2 1 * * The
    Sobel Operator in horizontal direction is for 2 dimensions is*
    -1   0   1 *             -2   0   2 *             -1   0 1 *

    The current implementation of the Sobel operator is for 2 and 3
    dimensions only. The ND version is planned for future releases.

    The extension to 3D is from the publication "Irwin Sobel. An
    Isotropic 3x3x3 Volume Gradient Operator.   Technical report, Hewlett-
    Packard Laboratories, April 1995."

    The Sobel operator in 3D has the kernel

    * -1 -3 -1   0 0 0  1 3 1 * -3 -6 -3   0 0 0  3 6 3 * -1 -3 -1   0 0 0
    1 3 1 * *    x-1       x     x+1 *

    The x kernel is just rotated as required to obtain the kernel in the y
    and z directions.

    SobelOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood

    See:   ForwardDifferenceOperator

    See:   BackwardDifferenceOperator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkSobelOperatorPython.delete_itkSobelOperatorF4

    def __init__(self, *args):
        r"""
        __init__(self) -> itkSobelOperatorF4
        __init__(self, arg0) -> itkSobelOperatorF4

        Parameters
        ----------
        arg0: itkSobelOperatorF4 const &



        A NeighborhoodOperator for performing a directional Sobel edge-
        detection operation at a pixel location.

        SobelOperator is a directional NeighborhoodOperator that should be
        applied a NeighborhoodIterator using the NeighborhoodInnerProduct
        method. To create the operator:

        1) Set the direction by calling 2) call 3) You may optionally scale
        the coefficients of this operator using the method. This is useful if
        you want to take the spacing of the image into account when computing
        the edge strength. Apply the scaling only after calling to.

        The Sobel Operator in vertical direction for 2 dimensions is*
        -1  -2  -1 *             0    0   0 *             1    2 1 * * The
        Sobel Operator in horizontal direction is for 2 dimensions is*
        -1   0   1 *             -2   0   2 *             -1   0 1 *

        The current implementation of the Sobel operator is for 2 and 3
        dimensions only. The ND version is planned for future releases.

        The extension to 3D is from the publication "Irwin Sobel. An
        Isotropic 3x3x3 Volume Gradient Operator.   Technical report, Hewlett-
        Packard Laboratories, April 1995."

        The Sobel operator in 3D has the kernel

        * -1 -3 -1   0 0 0  1 3 1 * -3 -6 -3   0 0 0  3 6 3 * -1 -3 -1   0 0 0
        1 3 1 * *    x-1       x     x+1 *

        The x kernel is just rotated as required to obtain the kernel in the y
        and z directions.

        SobelOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood

        See:   ForwardDifferenceOperator

        See:   BackwardDifferenceOperator 
        """
        _itkSobelOperatorPython.itkSobelOperatorF4_swiginit(self, _itkSobelOperatorPython.new_itkSobelOperatorF4(*args))

# Register itkSobelOperatorF4 in _itkSobelOperatorPython:
_itkSobelOperatorPython.itkSobelOperatorF4_swigregister(itkSobelOperatorF4)



