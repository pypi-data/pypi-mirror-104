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
    from . import _itkLaplacianOperatorPython
else:
    import _itkLaplacianOperatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkLaplacianOperatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkLaplacianOperatorPython.SWIG_PyStaticMethod_New

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
class itkLaplacianOperatorD2(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2):
    r"""


    A NeighborhoodOperator for use in calculating the Laplacian at a
    pixel.

    A NeighborhoodOperator for use in calculating the Laplacian at a
    pixel. The LaplacianOperator's coefficients are a tightest-fitting
    convolution kernel.

    The LaplacianOperator is a non-directional NeighborhoodOperator that
    should be applied to a Neighborhood or NeighborhoodIterator using an
    inner product method (itkNeighborhoodInnerProduct). To initialize the
    operator, you need call CreateOperator() before using it.

    By default the operator will be created for an isotropic image, but
    you can modify the operator to handle different pixel spacings by
    calling SetDerivativeScalings. The argument to SetDerivativeScalings
    is an array of doubles that is of length VDimension (the
    dimensionality of the image). Make sure to use 1/pixel_spacing to
    properly scale derivatives.

    LaplacianOperator does not have any user-declared "special member
    function" for copy, move, or destruction, following the C++ Rule of
    Zero: the compiler will generate them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    CreateOperator = _swig_new_instance_method(_itkLaplacianOperatorPython.itkLaplacianOperatorD2_CreateOperator)
    SetDerivativeScalings = _swig_new_instance_method(_itkLaplacianOperatorPython.itkLaplacianOperatorD2_SetDerivativeScalings)
    __swig_destroy__ = _itkLaplacianOperatorPython.delete_itkLaplacianOperatorD2

    def __init__(self, *args):
        r"""
        __init__(self) -> itkLaplacianOperatorD2
        __init__(self, arg0) -> itkLaplacianOperatorD2

        Parameters
        ----------
        arg0: itkLaplacianOperatorD2 const &



        A NeighborhoodOperator for use in calculating the Laplacian at a
        pixel.

        A NeighborhoodOperator for use in calculating the Laplacian at a
        pixel. The LaplacianOperator's coefficients are a tightest-fitting
        convolution kernel.

        The LaplacianOperator is a non-directional NeighborhoodOperator that
        should be applied to a Neighborhood or NeighborhoodIterator using an
        inner product method (itkNeighborhoodInnerProduct). To initialize the
        operator, you need call CreateOperator() before using it.

        By default the operator will be created for an isotropic image, but
        you can modify the operator to handle different pixel spacings by
        calling SetDerivativeScalings. The argument to SetDerivativeScalings
        is an array of doubles that is of length VDimension (the
        dimensionality of the image). Make sure to use 1/pixel_spacing to
        properly scale derivatives.

        LaplacianOperator does not have any user-declared "special member
        function" for copy, move, or destruction, following the C++ Rule of
        Zero: the compiler will generate them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood 
        """
        _itkLaplacianOperatorPython.itkLaplacianOperatorD2_swiginit(self, _itkLaplacianOperatorPython.new_itkLaplacianOperatorD2(*args))

# Register itkLaplacianOperatorD2 in _itkLaplacianOperatorPython:
_itkLaplacianOperatorPython.itkLaplacianOperatorD2_swigregister(itkLaplacianOperatorD2)

class itkLaplacianOperatorD3(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3):
    r"""


    A NeighborhoodOperator for use in calculating the Laplacian at a
    pixel.

    A NeighborhoodOperator for use in calculating the Laplacian at a
    pixel. The LaplacianOperator's coefficients are a tightest-fitting
    convolution kernel.

    The LaplacianOperator is a non-directional NeighborhoodOperator that
    should be applied to a Neighborhood or NeighborhoodIterator using an
    inner product method (itkNeighborhoodInnerProduct). To initialize the
    operator, you need call CreateOperator() before using it.

    By default the operator will be created for an isotropic image, but
    you can modify the operator to handle different pixel spacings by
    calling SetDerivativeScalings. The argument to SetDerivativeScalings
    is an array of doubles that is of length VDimension (the
    dimensionality of the image). Make sure to use 1/pixel_spacing to
    properly scale derivatives.

    LaplacianOperator does not have any user-declared "special member
    function" for copy, move, or destruction, following the C++ Rule of
    Zero: the compiler will generate them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    CreateOperator = _swig_new_instance_method(_itkLaplacianOperatorPython.itkLaplacianOperatorD3_CreateOperator)
    SetDerivativeScalings = _swig_new_instance_method(_itkLaplacianOperatorPython.itkLaplacianOperatorD3_SetDerivativeScalings)
    __swig_destroy__ = _itkLaplacianOperatorPython.delete_itkLaplacianOperatorD3

    def __init__(self, *args):
        r"""
        __init__(self) -> itkLaplacianOperatorD3
        __init__(self, arg0) -> itkLaplacianOperatorD3

        Parameters
        ----------
        arg0: itkLaplacianOperatorD3 const &



        A NeighborhoodOperator for use in calculating the Laplacian at a
        pixel.

        A NeighborhoodOperator for use in calculating the Laplacian at a
        pixel. The LaplacianOperator's coefficients are a tightest-fitting
        convolution kernel.

        The LaplacianOperator is a non-directional NeighborhoodOperator that
        should be applied to a Neighborhood or NeighborhoodIterator using an
        inner product method (itkNeighborhoodInnerProduct). To initialize the
        operator, you need call CreateOperator() before using it.

        By default the operator will be created for an isotropic image, but
        you can modify the operator to handle different pixel spacings by
        calling SetDerivativeScalings. The argument to SetDerivativeScalings
        is an array of doubles that is of length VDimension (the
        dimensionality of the image). Make sure to use 1/pixel_spacing to
        properly scale derivatives.

        LaplacianOperator does not have any user-declared "special member
        function" for copy, move, or destruction, following the C++ Rule of
        Zero: the compiler will generate them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood 
        """
        _itkLaplacianOperatorPython.itkLaplacianOperatorD3_swiginit(self, _itkLaplacianOperatorPython.new_itkLaplacianOperatorD3(*args))

# Register itkLaplacianOperatorD3 in _itkLaplacianOperatorPython:
_itkLaplacianOperatorPython.itkLaplacianOperatorD3_swigregister(itkLaplacianOperatorD3)

class itkLaplacianOperatorD4(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD4):
    r"""


    A NeighborhoodOperator for use in calculating the Laplacian at a
    pixel.

    A NeighborhoodOperator for use in calculating the Laplacian at a
    pixel. The LaplacianOperator's coefficients are a tightest-fitting
    convolution kernel.

    The LaplacianOperator is a non-directional NeighborhoodOperator that
    should be applied to a Neighborhood or NeighborhoodIterator using an
    inner product method (itkNeighborhoodInnerProduct). To initialize the
    operator, you need call CreateOperator() before using it.

    By default the operator will be created for an isotropic image, but
    you can modify the operator to handle different pixel spacings by
    calling SetDerivativeScalings. The argument to SetDerivativeScalings
    is an array of doubles that is of length VDimension (the
    dimensionality of the image). Make sure to use 1/pixel_spacing to
    properly scale derivatives.

    LaplacianOperator does not have any user-declared "special member
    function" for copy, move, or destruction, following the C++ Rule of
    Zero: the compiler will generate them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    CreateOperator = _swig_new_instance_method(_itkLaplacianOperatorPython.itkLaplacianOperatorD4_CreateOperator)
    SetDerivativeScalings = _swig_new_instance_method(_itkLaplacianOperatorPython.itkLaplacianOperatorD4_SetDerivativeScalings)
    __swig_destroy__ = _itkLaplacianOperatorPython.delete_itkLaplacianOperatorD4

    def __init__(self, *args):
        r"""
        __init__(self) -> itkLaplacianOperatorD4
        __init__(self, arg0) -> itkLaplacianOperatorD4

        Parameters
        ----------
        arg0: itkLaplacianOperatorD4 const &



        A NeighborhoodOperator for use in calculating the Laplacian at a
        pixel.

        A NeighborhoodOperator for use in calculating the Laplacian at a
        pixel. The LaplacianOperator's coefficients are a tightest-fitting
        convolution kernel.

        The LaplacianOperator is a non-directional NeighborhoodOperator that
        should be applied to a Neighborhood or NeighborhoodIterator using an
        inner product method (itkNeighborhoodInnerProduct). To initialize the
        operator, you need call CreateOperator() before using it.

        By default the operator will be created for an isotropic image, but
        you can modify the operator to handle different pixel spacings by
        calling SetDerivativeScalings. The argument to SetDerivativeScalings
        is an array of doubles that is of length VDimension (the
        dimensionality of the image). Make sure to use 1/pixel_spacing to
        properly scale derivatives.

        LaplacianOperator does not have any user-declared "special member
        function" for copy, move, or destruction, following the C++ Rule of
        Zero: the compiler will generate them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood 
        """
        _itkLaplacianOperatorPython.itkLaplacianOperatorD4_swiginit(self, _itkLaplacianOperatorPython.new_itkLaplacianOperatorD4(*args))

# Register itkLaplacianOperatorD4 in _itkLaplacianOperatorPython:
_itkLaplacianOperatorPython.itkLaplacianOperatorD4_swigregister(itkLaplacianOperatorD4)

class itkLaplacianOperatorF2(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2):
    r"""


    A NeighborhoodOperator for use in calculating the Laplacian at a
    pixel.

    A NeighborhoodOperator for use in calculating the Laplacian at a
    pixel. The LaplacianOperator's coefficients are a tightest-fitting
    convolution kernel.

    The LaplacianOperator is a non-directional NeighborhoodOperator that
    should be applied to a Neighborhood or NeighborhoodIterator using an
    inner product method (itkNeighborhoodInnerProduct). To initialize the
    operator, you need call CreateOperator() before using it.

    By default the operator will be created for an isotropic image, but
    you can modify the operator to handle different pixel spacings by
    calling SetDerivativeScalings. The argument to SetDerivativeScalings
    is an array of doubles that is of length VDimension (the
    dimensionality of the image). Make sure to use 1/pixel_spacing to
    properly scale derivatives.

    LaplacianOperator does not have any user-declared "special member
    function" for copy, move, or destruction, following the C++ Rule of
    Zero: the compiler will generate them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    CreateOperator = _swig_new_instance_method(_itkLaplacianOperatorPython.itkLaplacianOperatorF2_CreateOperator)
    SetDerivativeScalings = _swig_new_instance_method(_itkLaplacianOperatorPython.itkLaplacianOperatorF2_SetDerivativeScalings)
    __swig_destroy__ = _itkLaplacianOperatorPython.delete_itkLaplacianOperatorF2

    def __init__(self, *args):
        r"""
        __init__(self) -> itkLaplacianOperatorF2
        __init__(self, arg0) -> itkLaplacianOperatorF2

        Parameters
        ----------
        arg0: itkLaplacianOperatorF2 const &



        A NeighborhoodOperator for use in calculating the Laplacian at a
        pixel.

        A NeighborhoodOperator for use in calculating the Laplacian at a
        pixel. The LaplacianOperator's coefficients are a tightest-fitting
        convolution kernel.

        The LaplacianOperator is a non-directional NeighborhoodOperator that
        should be applied to a Neighborhood or NeighborhoodIterator using an
        inner product method (itkNeighborhoodInnerProduct). To initialize the
        operator, you need call CreateOperator() before using it.

        By default the operator will be created for an isotropic image, but
        you can modify the operator to handle different pixel spacings by
        calling SetDerivativeScalings. The argument to SetDerivativeScalings
        is an array of doubles that is of length VDimension (the
        dimensionality of the image). Make sure to use 1/pixel_spacing to
        properly scale derivatives.

        LaplacianOperator does not have any user-declared "special member
        function" for copy, move, or destruction, following the C++ Rule of
        Zero: the compiler will generate them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood 
        """
        _itkLaplacianOperatorPython.itkLaplacianOperatorF2_swiginit(self, _itkLaplacianOperatorPython.new_itkLaplacianOperatorF2(*args))

# Register itkLaplacianOperatorF2 in _itkLaplacianOperatorPython:
_itkLaplacianOperatorPython.itkLaplacianOperatorF2_swigregister(itkLaplacianOperatorF2)

class itkLaplacianOperatorF3(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3):
    r"""


    A NeighborhoodOperator for use in calculating the Laplacian at a
    pixel.

    A NeighborhoodOperator for use in calculating the Laplacian at a
    pixel. The LaplacianOperator's coefficients are a tightest-fitting
    convolution kernel.

    The LaplacianOperator is a non-directional NeighborhoodOperator that
    should be applied to a Neighborhood or NeighborhoodIterator using an
    inner product method (itkNeighborhoodInnerProduct). To initialize the
    operator, you need call CreateOperator() before using it.

    By default the operator will be created for an isotropic image, but
    you can modify the operator to handle different pixel spacings by
    calling SetDerivativeScalings. The argument to SetDerivativeScalings
    is an array of doubles that is of length VDimension (the
    dimensionality of the image). Make sure to use 1/pixel_spacing to
    properly scale derivatives.

    LaplacianOperator does not have any user-declared "special member
    function" for copy, move, or destruction, following the C++ Rule of
    Zero: the compiler will generate them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    CreateOperator = _swig_new_instance_method(_itkLaplacianOperatorPython.itkLaplacianOperatorF3_CreateOperator)
    SetDerivativeScalings = _swig_new_instance_method(_itkLaplacianOperatorPython.itkLaplacianOperatorF3_SetDerivativeScalings)
    __swig_destroy__ = _itkLaplacianOperatorPython.delete_itkLaplacianOperatorF3

    def __init__(self, *args):
        r"""
        __init__(self) -> itkLaplacianOperatorF3
        __init__(self, arg0) -> itkLaplacianOperatorF3

        Parameters
        ----------
        arg0: itkLaplacianOperatorF3 const &



        A NeighborhoodOperator for use in calculating the Laplacian at a
        pixel.

        A NeighborhoodOperator for use in calculating the Laplacian at a
        pixel. The LaplacianOperator's coefficients are a tightest-fitting
        convolution kernel.

        The LaplacianOperator is a non-directional NeighborhoodOperator that
        should be applied to a Neighborhood or NeighborhoodIterator using an
        inner product method (itkNeighborhoodInnerProduct). To initialize the
        operator, you need call CreateOperator() before using it.

        By default the operator will be created for an isotropic image, but
        you can modify the operator to handle different pixel spacings by
        calling SetDerivativeScalings. The argument to SetDerivativeScalings
        is an array of doubles that is of length VDimension (the
        dimensionality of the image). Make sure to use 1/pixel_spacing to
        properly scale derivatives.

        LaplacianOperator does not have any user-declared "special member
        function" for copy, move, or destruction, following the C++ Rule of
        Zero: the compiler will generate them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood 
        """
        _itkLaplacianOperatorPython.itkLaplacianOperatorF3_swiginit(self, _itkLaplacianOperatorPython.new_itkLaplacianOperatorF3(*args))

# Register itkLaplacianOperatorF3 in _itkLaplacianOperatorPython:
_itkLaplacianOperatorPython.itkLaplacianOperatorF3_swigregister(itkLaplacianOperatorF3)

class itkLaplacianOperatorF4(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF4):
    r"""


    A NeighborhoodOperator for use in calculating the Laplacian at a
    pixel.

    A NeighborhoodOperator for use in calculating the Laplacian at a
    pixel. The LaplacianOperator's coefficients are a tightest-fitting
    convolution kernel.

    The LaplacianOperator is a non-directional NeighborhoodOperator that
    should be applied to a Neighborhood or NeighborhoodIterator using an
    inner product method (itkNeighborhoodInnerProduct). To initialize the
    operator, you need call CreateOperator() before using it.

    By default the operator will be created for an isotropic image, but
    you can modify the operator to handle different pixel spacings by
    calling SetDerivativeScalings. The argument to SetDerivativeScalings
    is an array of doubles that is of length VDimension (the
    dimensionality of the image). Make sure to use 1/pixel_spacing to
    properly scale derivatives.

    LaplacianOperator does not have any user-declared "special member
    function" for copy, move, or destruction, following the C++ Rule of
    Zero: the compiler will generate them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    CreateOperator = _swig_new_instance_method(_itkLaplacianOperatorPython.itkLaplacianOperatorF4_CreateOperator)
    SetDerivativeScalings = _swig_new_instance_method(_itkLaplacianOperatorPython.itkLaplacianOperatorF4_SetDerivativeScalings)
    __swig_destroy__ = _itkLaplacianOperatorPython.delete_itkLaplacianOperatorF4

    def __init__(self, *args):
        r"""
        __init__(self) -> itkLaplacianOperatorF4
        __init__(self, arg0) -> itkLaplacianOperatorF4

        Parameters
        ----------
        arg0: itkLaplacianOperatorF4 const &



        A NeighborhoodOperator for use in calculating the Laplacian at a
        pixel.

        A NeighborhoodOperator for use in calculating the Laplacian at a
        pixel. The LaplacianOperator's coefficients are a tightest-fitting
        convolution kernel.

        The LaplacianOperator is a non-directional NeighborhoodOperator that
        should be applied to a Neighborhood or NeighborhoodIterator using an
        inner product method (itkNeighborhoodInnerProduct). To initialize the
        operator, you need call CreateOperator() before using it.

        By default the operator will be created for an isotropic image, but
        you can modify the operator to handle different pixel spacings by
        calling SetDerivativeScalings. The argument to SetDerivativeScalings
        is an array of doubles that is of length VDimension (the
        dimensionality of the image). Make sure to use 1/pixel_spacing to
        properly scale derivatives.

        LaplacianOperator does not have any user-declared "special member
        function" for copy, move, or destruction, following the C++ Rule of
        Zero: the compiler will generate them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood 
        """
        _itkLaplacianOperatorPython.itkLaplacianOperatorF4_swiginit(self, _itkLaplacianOperatorPython.new_itkLaplacianOperatorF4(*args))

# Register itkLaplacianOperatorF4 in _itkLaplacianOperatorPython:
_itkLaplacianOperatorPython.itkLaplacianOperatorF4_swigregister(itkLaplacianOperatorF4)



