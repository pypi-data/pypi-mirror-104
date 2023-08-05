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
    from . import _itkDerivativeOperatorPython
else:
    import _itkDerivativeOperatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkDerivativeOperatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkDerivativeOperatorPython.SWIG_PyStaticMethod_New

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
import itk.itkNeighborhoodOperatorPython
import itk.itkNeighborhoodPython
import itk.itkCovariantVectorPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkSizePython
import itk.itkRGBPixelPython
import itk.ITKCommonBasePython
import itk.itkOffsetPython
class itkDerivativeOperatorD2(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2):
    r"""


    A NeighborhoodOperator for taking an n-th order derivative at a pixel.

    DerivativeOperator's coefficients are a tightest-fitting convolution
    kernel for calculating the n-th order directional derivative at a
    pixel. DerivativeOperator is a directional NeighborhoodOperator that
    should be applied to a Neighborhood or NeighborhoodPointer using the
    inner product method.

    An example operator to compute X derivatives of a 2D image can be
    created with: and creates a kernel that looks like:

    DerivativeOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood

    See:   ForwardDifferenceOperator

    See:   BackwardDifferenceOperator
    {Core/Common/CreateDerivativeKernel,Create Derivative Kernel} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SetOrder = _swig_new_instance_method(_itkDerivativeOperatorPython.itkDerivativeOperatorD2_SetOrder)
    GetOrder = _swig_new_instance_method(_itkDerivativeOperatorPython.itkDerivativeOperatorD2_GetOrder)
    __swig_destroy__ = _itkDerivativeOperatorPython.delete_itkDerivativeOperatorD2

    def __init__(self, *args):
        r"""
        __init__(self) -> itkDerivativeOperatorD2
        __init__(self, arg0) -> itkDerivativeOperatorD2

        Parameters
        ----------
        arg0: itkDerivativeOperatorD2 const &



        A NeighborhoodOperator for taking an n-th order derivative at a pixel.

        DerivativeOperator's coefficients are a tightest-fitting convolution
        kernel for calculating the n-th order directional derivative at a
        pixel. DerivativeOperator is a directional NeighborhoodOperator that
        should be applied to a Neighborhood or NeighborhoodPointer using the
        inner product method.

        An example operator to compute X derivatives of a 2D image can be
        created with: and creates a kernel that looks like:

        DerivativeOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood

        See:   ForwardDifferenceOperator

        See:   BackwardDifferenceOperator
        {Core/Common/CreateDerivativeKernel,Create Derivative Kernel} 
        """
        _itkDerivativeOperatorPython.itkDerivativeOperatorD2_swiginit(self, _itkDerivativeOperatorPython.new_itkDerivativeOperatorD2(*args))

# Register itkDerivativeOperatorD2 in _itkDerivativeOperatorPython:
_itkDerivativeOperatorPython.itkDerivativeOperatorD2_swigregister(itkDerivativeOperatorD2)

class itkDerivativeOperatorD3(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3):
    r"""


    A NeighborhoodOperator for taking an n-th order derivative at a pixel.

    DerivativeOperator's coefficients are a tightest-fitting convolution
    kernel for calculating the n-th order directional derivative at a
    pixel. DerivativeOperator is a directional NeighborhoodOperator that
    should be applied to a Neighborhood or NeighborhoodPointer using the
    inner product method.

    An example operator to compute X derivatives of a 2D image can be
    created with: and creates a kernel that looks like:

    DerivativeOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood

    See:   ForwardDifferenceOperator

    See:   BackwardDifferenceOperator
    {Core/Common/CreateDerivativeKernel,Create Derivative Kernel} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SetOrder = _swig_new_instance_method(_itkDerivativeOperatorPython.itkDerivativeOperatorD3_SetOrder)
    GetOrder = _swig_new_instance_method(_itkDerivativeOperatorPython.itkDerivativeOperatorD3_GetOrder)
    __swig_destroy__ = _itkDerivativeOperatorPython.delete_itkDerivativeOperatorD3

    def __init__(self, *args):
        r"""
        __init__(self) -> itkDerivativeOperatorD3
        __init__(self, arg0) -> itkDerivativeOperatorD3

        Parameters
        ----------
        arg0: itkDerivativeOperatorD3 const &



        A NeighborhoodOperator for taking an n-th order derivative at a pixel.

        DerivativeOperator's coefficients are a tightest-fitting convolution
        kernel for calculating the n-th order directional derivative at a
        pixel. DerivativeOperator is a directional NeighborhoodOperator that
        should be applied to a Neighborhood or NeighborhoodPointer using the
        inner product method.

        An example operator to compute X derivatives of a 2D image can be
        created with: and creates a kernel that looks like:

        DerivativeOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood

        See:   ForwardDifferenceOperator

        See:   BackwardDifferenceOperator
        {Core/Common/CreateDerivativeKernel,Create Derivative Kernel} 
        """
        _itkDerivativeOperatorPython.itkDerivativeOperatorD3_swiginit(self, _itkDerivativeOperatorPython.new_itkDerivativeOperatorD3(*args))

# Register itkDerivativeOperatorD3 in _itkDerivativeOperatorPython:
_itkDerivativeOperatorPython.itkDerivativeOperatorD3_swigregister(itkDerivativeOperatorD3)

class itkDerivativeOperatorD4(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD4):
    r"""


    A NeighborhoodOperator for taking an n-th order derivative at a pixel.

    DerivativeOperator's coefficients are a tightest-fitting convolution
    kernel for calculating the n-th order directional derivative at a
    pixel. DerivativeOperator is a directional NeighborhoodOperator that
    should be applied to a Neighborhood or NeighborhoodPointer using the
    inner product method.

    An example operator to compute X derivatives of a 2D image can be
    created with: and creates a kernel that looks like:

    DerivativeOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood

    See:   ForwardDifferenceOperator

    See:   BackwardDifferenceOperator
    {Core/Common/CreateDerivativeKernel,Create Derivative Kernel} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SetOrder = _swig_new_instance_method(_itkDerivativeOperatorPython.itkDerivativeOperatorD4_SetOrder)
    GetOrder = _swig_new_instance_method(_itkDerivativeOperatorPython.itkDerivativeOperatorD4_GetOrder)
    __swig_destroy__ = _itkDerivativeOperatorPython.delete_itkDerivativeOperatorD4

    def __init__(self, *args):
        r"""
        __init__(self) -> itkDerivativeOperatorD4
        __init__(self, arg0) -> itkDerivativeOperatorD4

        Parameters
        ----------
        arg0: itkDerivativeOperatorD4 const &



        A NeighborhoodOperator for taking an n-th order derivative at a pixel.

        DerivativeOperator's coefficients are a tightest-fitting convolution
        kernel for calculating the n-th order directional derivative at a
        pixel. DerivativeOperator is a directional NeighborhoodOperator that
        should be applied to a Neighborhood or NeighborhoodPointer using the
        inner product method.

        An example operator to compute X derivatives of a 2D image can be
        created with: and creates a kernel that looks like:

        DerivativeOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood

        See:   ForwardDifferenceOperator

        See:   BackwardDifferenceOperator
        {Core/Common/CreateDerivativeKernel,Create Derivative Kernel} 
        """
        _itkDerivativeOperatorPython.itkDerivativeOperatorD4_swiginit(self, _itkDerivativeOperatorPython.new_itkDerivativeOperatorD4(*args))

# Register itkDerivativeOperatorD4 in _itkDerivativeOperatorPython:
_itkDerivativeOperatorPython.itkDerivativeOperatorD4_swigregister(itkDerivativeOperatorD4)

class itkDerivativeOperatorF2(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2):
    r"""


    A NeighborhoodOperator for taking an n-th order derivative at a pixel.

    DerivativeOperator's coefficients are a tightest-fitting convolution
    kernel for calculating the n-th order directional derivative at a
    pixel. DerivativeOperator is a directional NeighborhoodOperator that
    should be applied to a Neighborhood or NeighborhoodPointer using the
    inner product method.

    An example operator to compute X derivatives of a 2D image can be
    created with: and creates a kernel that looks like:

    DerivativeOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood

    See:   ForwardDifferenceOperator

    See:   BackwardDifferenceOperator
    {Core/Common/CreateDerivativeKernel,Create Derivative Kernel} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SetOrder = _swig_new_instance_method(_itkDerivativeOperatorPython.itkDerivativeOperatorF2_SetOrder)
    GetOrder = _swig_new_instance_method(_itkDerivativeOperatorPython.itkDerivativeOperatorF2_GetOrder)
    __swig_destroy__ = _itkDerivativeOperatorPython.delete_itkDerivativeOperatorF2

    def __init__(self, *args):
        r"""
        __init__(self) -> itkDerivativeOperatorF2
        __init__(self, arg0) -> itkDerivativeOperatorF2

        Parameters
        ----------
        arg0: itkDerivativeOperatorF2 const &



        A NeighborhoodOperator for taking an n-th order derivative at a pixel.

        DerivativeOperator's coefficients are a tightest-fitting convolution
        kernel for calculating the n-th order directional derivative at a
        pixel. DerivativeOperator is a directional NeighborhoodOperator that
        should be applied to a Neighborhood or NeighborhoodPointer using the
        inner product method.

        An example operator to compute X derivatives of a 2D image can be
        created with: and creates a kernel that looks like:

        DerivativeOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood

        See:   ForwardDifferenceOperator

        See:   BackwardDifferenceOperator
        {Core/Common/CreateDerivativeKernel,Create Derivative Kernel} 
        """
        _itkDerivativeOperatorPython.itkDerivativeOperatorF2_swiginit(self, _itkDerivativeOperatorPython.new_itkDerivativeOperatorF2(*args))

# Register itkDerivativeOperatorF2 in _itkDerivativeOperatorPython:
_itkDerivativeOperatorPython.itkDerivativeOperatorF2_swigregister(itkDerivativeOperatorF2)

class itkDerivativeOperatorF3(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3):
    r"""


    A NeighborhoodOperator for taking an n-th order derivative at a pixel.

    DerivativeOperator's coefficients are a tightest-fitting convolution
    kernel for calculating the n-th order directional derivative at a
    pixel. DerivativeOperator is a directional NeighborhoodOperator that
    should be applied to a Neighborhood or NeighborhoodPointer using the
    inner product method.

    An example operator to compute X derivatives of a 2D image can be
    created with: and creates a kernel that looks like:

    DerivativeOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood

    See:   ForwardDifferenceOperator

    See:   BackwardDifferenceOperator
    {Core/Common/CreateDerivativeKernel,Create Derivative Kernel} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SetOrder = _swig_new_instance_method(_itkDerivativeOperatorPython.itkDerivativeOperatorF3_SetOrder)
    GetOrder = _swig_new_instance_method(_itkDerivativeOperatorPython.itkDerivativeOperatorF3_GetOrder)
    __swig_destroy__ = _itkDerivativeOperatorPython.delete_itkDerivativeOperatorF3

    def __init__(self, *args):
        r"""
        __init__(self) -> itkDerivativeOperatorF3
        __init__(self, arg0) -> itkDerivativeOperatorF3

        Parameters
        ----------
        arg0: itkDerivativeOperatorF3 const &



        A NeighborhoodOperator for taking an n-th order derivative at a pixel.

        DerivativeOperator's coefficients are a tightest-fitting convolution
        kernel for calculating the n-th order directional derivative at a
        pixel. DerivativeOperator is a directional NeighborhoodOperator that
        should be applied to a Neighborhood or NeighborhoodPointer using the
        inner product method.

        An example operator to compute X derivatives of a 2D image can be
        created with: and creates a kernel that looks like:

        DerivativeOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood

        See:   ForwardDifferenceOperator

        See:   BackwardDifferenceOperator
        {Core/Common/CreateDerivativeKernel,Create Derivative Kernel} 
        """
        _itkDerivativeOperatorPython.itkDerivativeOperatorF3_swiginit(self, _itkDerivativeOperatorPython.new_itkDerivativeOperatorF3(*args))

# Register itkDerivativeOperatorF3 in _itkDerivativeOperatorPython:
_itkDerivativeOperatorPython.itkDerivativeOperatorF3_swigregister(itkDerivativeOperatorF3)

class itkDerivativeOperatorF4(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF4):
    r"""


    A NeighborhoodOperator for taking an n-th order derivative at a pixel.

    DerivativeOperator's coefficients are a tightest-fitting convolution
    kernel for calculating the n-th order directional derivative at a
    pixel. DerivativeOperator is a directional NeighborhoodOperator that
    should be applied to a Neighborhood or NeighborhoodPointer using the
    inner product method.

    An example operator to compute X derivatives of a 2D image can be
    created with: and creates a kernel that looks like:

    DerivativeOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood

    See:   ForwardDifferenceOperator

    See:   BackwardDifferenceOperator
    {Core/Common/CreateDerivativeKernel,Create Derivative Kernel} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SetOrder = _swig_new_instance_method(_itkDerivativeOperatorPython.itkDerivativeOperatorF4_SetOrder)
    GetOrder = _swig_new_instance_method(_itkDerivativeOperatorPython.itkDerivativeOperatorF4_GetOrder)
    __swig_destroy__ = _itkDerivativeOperatorPython.delete_itkDerivativeOperatorF4

    def __init__(self, *args):
        r"""
        __init__(self) -> itkDerivativeOperatorF4
        __init__(self, arg0) -> itkDerivativeOperatorF4

        Parameters
        ----------
        arg0: itkDerivativeOperatorF4 const &



        A NeighborhoodOperator for taking an n-th order derivative at a pixel.

        DerivativeOperator's coefficients are a tightest-fitting convolution
        kernel for calculating the n-th order directional derivative at a
        pixel. DerivativeOperator is a directional NeighborhoodOperator that
        should be applied to a Neighborhood or NeighborhoodPointer using the
        inner product method.

        An example operator to compute X derivatives of a 2D image can be
        created with: and creates a kernel that looks like:

        DerivativeOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood

        See:   ForwardDifferenceOperator

        See:   BackwardDifferenceOperator
        {Core/Common/CreateDerivativeKernel,Create Derivative Kernel} 
        """
        _itkDerivativeOperatorPython.itkDerivativeOperatorF4_swiginit(self, _itkDerivativeOperatorPython.new_itkDerivativeOperatorF4(*args))

# Register itkDerivativeOperatorF4 in _itkDerivativeOperatorPython:
_itkDerivativeOperatorPython.itkDerivativeOperatorF4_swigregister(itkDerivativeOperatorF4)



