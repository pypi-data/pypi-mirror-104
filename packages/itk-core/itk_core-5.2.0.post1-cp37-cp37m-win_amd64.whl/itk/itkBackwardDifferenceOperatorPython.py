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
    from . import _itkBackwardDifferenceOperatorPython
else:
    import _itkBackwardDifferenceOperatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBackwardDifferenceOperatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBackwardDifferenceOperatorPython.SWIG_PyStaticMethod_New

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
import itk.itkFixedArrayPython
import itk.pyBasePython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.itkRGBPixelPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.ITKCommonBasePython
class itkBackwardDifferenceOperatorD2(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2):
    r"""


    Operator whose inner product with a neighborhood returns a "half"
    derivative at the center of the neighborhood.

    BackwardDifferenceOperator uses backward differences i.e. $ F(x) -
    F(x-1) $ to calculate a "half" derivative useful, among other
    things, in solving differential equations. It is a directional
    NeighborhoodOperator that should be applied to a Neighborhood using
    the inner product.

    BackwardDifferenceOperator does not have any user-declared "special
    member function", following the C++ Rule of Zero: the compiler will
    generate them if necessary.
    {Core/Common/CreateABackwardDifferenceOperator,Create A Backward
    Difference Operator} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkBackwardDifferenceOperatorPython.delete_itkBackwardDifferenceOperatorD2

    def __init__(self, *args):
        r"""
        __init__(self) -> itkBackwardDifferenceOperatorD2
        __init__(self, arg0) -> itkBackwardDifferenceOperatorD2

        Parameters
        ----------
        arg0: itkBackwardDifferenceOperatorD2 const &



        Operator whose inner product with a neighborhood returns a "half"
        derivative at the center of the neighborhood.

        BackwardDifferenceOperator uses backward differences i.e. $ F(x) -
        F(x-1) $ to calculate a "half" derivative useful, among other
        things, in solving differential equations. It is a directional
        NeighborhoodOperator that should be applied to a Neighborhood using
        the inner product.

        BackwardDifferenceOperator does not have any user-declared "special
        member function", following the C++ Rule of Zero: the compiler will
        generate them if necessary.
        {Core/Common/CreateABackwardDifferenceOperator,Create A Backward
        Difference Operator} 
        """
        _itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorD2_swiginit(self, _itkBackwardDifferenceOperatorPython.new_itkBackwardDifferenceOperatorD2(*args))

# Register itkBackwardDifferenceOperatorD2 in _itkBackwardDifferenceOperatorPython:
_itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorD2_swigregister(itkBackwardDifferenceOperatorD2)

class itkBackwardDifferenceOperatorD3(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3):
    r"""


    Operator whose inner product with a neighborhood returns a "half"
    derivative at the center of the neighborhood.

    BackwardDifferenceOperator uses backward differences i.e. $ F(x) -
    F(x-1) $ to calculate a "half" derivative useful, among other
    things, in solving differential equations. It is a directional
    NeighborhoodOperator that should be applied to a Neighborhood using
    the inner product.

    BackwardDifferenceOperator does not have any user-declared "special
    member function", following the C++ Rule of Zero: the compiler will
    generate them if necessary.
    {Core/Common/CreateABackwardDifferenceOperator,Create A Backward
    Difference Operator} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkBackwardDifferenceOperatorPython.delete_itkBackwardDifferenceOperatorD3

    def __init__(self, *args):
        r"""
        __init__(self) -> itkBackwardDifferenceOperatorD3
        __init__(self, arg0) -> itkBackwardDifferenceOperatorD3

        Parameters
        ----------
        arg0: itkBackwardDifferenceOperatorD3 const &



        Operator whose inner product with a neighborhood returns a "half"
        derivative at the center of the neighborhood.

        BackwardDifferenceOperator uses backward differences i.e. $ F(x) -
        F(x-1) $ to calculate a "half" derivative useful, among other
        things, in solving differential equations. It is a directional
        NeighborhoodOperator that should be applied to a Neighborhood using
        the inner product.

        BackwardDifferenceOperator does not have any user-declared "special
        member function", following the C++ Rule of Zero: the compiler will
        generate them if necessary.
        {Core/Common/CreateABackwardDifferenceOperator,Create A Backward
        Difference Operator} 
        """
        _itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorD3_swiginit(self, _itkBackwardDifferenceOperatorPython.new_itkBackwardDifferenceOperatorD3(*args))

# Register itkBackwardDifferenceOperatorD3 in _itkBackwardDifferenceOperatorPython:
_itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorD3_swigregister(itkBackwardDifferenceOperatorD3)

class itkBackwardDifferenceOperatorD4(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD4):
    r"""


    Operator whose inner product with a neighborhood returns a "half"
    derivative at the center of the neighborhood.

    BackwardDifferenceOperator uses backward differences i.e. $ F(x) -
    F(x-1) $ to calculate a "half" derivative useful, among other
    things, in solving differential equations. It is a directional
    NeighborhoodOperator that should be applied to a Neighborhood using
    the inner product.

    BackwardDifferenceOperator does not have any user-declared "special
    member function", following the C++ Rule of Zero: the compiler will
    generate them if necessary.
    {Core/Common/CreateABackwardDifferenceOperator,Create A Backward
    Difference Operator} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkBackwardDifferenceOperatorPython.delete_itkBackwardDifferenceOperatorD4

    def __init__(self, *args):
        r"""
        __init__(self) -> itkBackwardDifferenceOperatorD4
        __init__(self, arg0) -> itkBackwardDifferenceOperatorD4

        Parameters
        ----------
        arg0: itkBackwardDifferenceOperatorD4 const &



        Operator whose inner product with a neighborhood returns a "half"
        derivative at the center of the neighborhood.

        BackwardDifferenceOperator uses backward differences i.e. $ F(x) -
        F(x-1) $ to calculate a "half" derivative useful, among other
        things, in solving differential equations. It is a directional
        NeighborhoodOperator that should be applied to a Neighborhood using
        the inner product.

        BackwardDifferenceOperator does not have any user-declared "special
        member function", following the C++ Rule of Zero: the compiler will
        generate them if necessary.
        {Core/Common/CreateABackwardDifferenceOperator,Create A Backward
        Difference Operator} 
        """
        _itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorD4_swiginit(self, _itkBackwardDifferenceOperatorPython.new_itkBackwardDifferenceOperatorD4(*args))

# Register itkBackwardDifferenceOperatorD4 in _itkBackwardDifferenceOperatorPython:
_itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorD4_swigregister(itkBackwardDifferenceOperatorD4)

class itkBackwardDifferenceOperatorF2(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2):
    r"""


    Operator whose inner product with a neighborhood returns a "half"
    derivative at the center of the neighborhood.

    BackwardDifferenceOperator uses backward differences i.e. $ F(x) -
    F(x-1) $ to calculate a "half" derivative useful, among other
    things, in solving differential equations. It is a directional
    NeighborhoodOperator that should be applied to a Neighborhood using
    the inner product.

    BackwardDifferenceOperator does not have any user-declared "special
    member function", following the C++ Rule of Zero: the compiler will
    generate them if necessary.
    {Core/Common/CreateABackwardDifferenceOperator,Create A Backward
    Difference Operator} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkBackwardDifferenceOperatorPython.delete_itkBackwardDifferenceOperatorF2

    def __init__(self, *args):
        r"""
        __init__(self) -> itkBackwardDifferenceOperatorF2
        __init__(self, arg0) -> itkBackwardDifferenceOperatorF2

        Parameters
        ----------
        arg0: itkBackwardDifferenceOperatorF2 const &



        Operator whose inner product with a neighborhood returns a "half"
        derivative at the center of the neighborhood.

        BackwardDifferenceOperator uses backward differences i.e. $ F(x) -
        F(x-1) $ to calculate a "half" derivative useful, among other
        things, in solving differential equations. It is a directional
        NeighborhoodOperator that should be applied to a Neighborhood using
        the inner product.

        BackwardDifferenceOperator does not have any user-declared "special
        member function", following the C++ Rule of Zero: the compiler will
        generate them if necessary.
        {Core/Common/CreateABackwardDifferenceOperator,Create A Backward
        Difference Operator} 
        """
        _itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorF2_swiginit(self, _itkBackwardDifferenceOperatorPython.new_itkBackwardDifferenceOperatorF2(*args))

# Register itkBackwardDifferenceOperatorF2 in _itkBackwardDifferenceOperatorPython:
_itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorF2_swigregister(itkBackwardDifferenceOperatorF2)

class itkBackwardDifferenceOperatorF3(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3):
    r"""


    Operator whose inner product with a neighborhood returns a "half"
    derivative at the center of the neighborhood.

    BackwardDifferenceOperator uses backward differences i.e. $ F(x) -
    F(x-1) $ to calculate a "half" derivative useful, among other
    things, in solving differential equations. It is a directional
    NeighborhoodOperator that should be applied to a Neighborhood using
    the inner product.

    BackwardDifferenceOperator does not have any user-declared "special
    member function", following the C++ Rule of Zero: the compiler will
    generate them if necessary.
    {Core/Common/CreateABackwardDifferenceOperator,Create A Backward
    Difference Operator} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkBackwardDifferenceOperatorPython.delete_itkBackwardDifferenceOperatorF3

    def __init__(self, *args):
        r"""
        __init__(self) -> itkBackwardDifferenceOperatorF3
        __init__(self, arg0) -> itkBackwardDifferenceOperatorF3

        Parameters
        ----------
        arg0: itkBackwardDifferenceOperatorF3 const &



        Operator whose inner product with a neighborhood returns a "half"
        derivative at the center of the neighborhood.

        BackwardDifferenceOperator uses backward differences i.e. $ F(x) -
        F(x-1) $ to calculate a "half" derivative useful, among other
        things, in solving differential equations. It is a directional
        NeighborhoodOperator that should be applied to a Neighborhood using
        the inner product.

        BackwardDifferenceOperator does not have any user-declared "special
        member function", following the C++ Rule of Zero: the compiler will
        generate them if necessary.
        {Core/Common/CreateABackwardDifferenceOperator,Create A Backward
        Difference Operator} 
        """
        _itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorF3_swiginit(self, _itkBackwardDifferenceOperatorPython.new_itkBackwardDifferenceOperatorF3(*args))

# Register itkBackwardDifferenceOperatorF3 in _itkBackwardDifferenceOperatorPython:
_itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorF3_swigregister(itkBackwardDifferenceOperatorF3)

class itkBackwardDifferenceOperatorF4(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF4):
    r"""


    Operator whose inner product with a neighborhood returns a "half"
    derivative at the center of the neighborhood.

    BackwardDifferenceOperator uses backward differences i.e. $ F(x) -
    F(x-1) $ to calculate a "half" derivative useful, among other
    things, in solving differential equations. It is a directional
    NeighborhoodOperator that should be applied to a Neighborhood using
    the inner product.

    BackwardDifferenceOperator does not have any user-declared "special
    member function", following the C++ Rule of Zero: the compiler will
    generate them if necessary.
    {Core/Common/CreateABackwardDifferenceOperator,Create A Backward
    Difference Operator} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkBackwardDifferenceOperatorPython.delete_itkBackwardDifferenceOperatorF4

    def __init__(self, *args):
        r"""
        __init__(self) -> itkBackwardDifferenceOperatorF4
        __init__(self, arg0) -> itkBackwardDifferenceOperatorF4

        Parameters
        ----------
        arg0: itkBackwardDifferenceOperatorF4 const &



        Operator whose inner product with a neighborhood returns a "half"
        derivative at the center of the neighborhood.

        BackwardDifferenceOperator uses backward differences i.e. $ F(x) -
        F(x-1) $ to calculate a "half" derivative useful, among other
        things, in solving differential equations. It is a directional
        NeighborhoodOperator that should be applied to a Neighborhood using
        the inner product.

        BackwardDifferenceOperator does not have any user-declared "special
        member function", following the C++ Rule of Zero: the compiler will
        generate them if necessary.
        {Core/Common/CreateABackwardDifferenceOperator,Create A Backward
        Difference Operator} 
        """
        _itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorF4_swiginit(self, _itkBackwardDifferenceOperatorPython.new_itkBackwardDifferenceOperatorF4(*args))

# Register itkBackwardDifferenceOperatorF4 in _itkBackwardDifferenceOperatorPython:
_itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorF4_swigregister(itkBackwardDifferenceOperatorF4)



