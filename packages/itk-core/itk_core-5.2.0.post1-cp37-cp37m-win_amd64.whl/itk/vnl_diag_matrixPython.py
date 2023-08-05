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
    from . import _vnl_diag_matrixPython
else:
    import _vnl_diag_matrixPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _vnl_diag_matrixPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _vnl_diag_matrixPython.SWIG_PyStaticMethod_New

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
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_matrixPython
class vnl_diag_matrixCD(object):
    r"""Proxy of C++ vnl_diag_matrixCD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _vnl_diag_matrixPython.delete_vnl_diag_matrixCD

    def __init__(self, *args):
        r"""
        __init__(self) -> vnl_diag_matrixCD
        __init__(self, arg0) -> vnl_diag_matrixCD

        Parameters
        ----------
        arg0: vnl_diag_matrixCD const &

        __init__(self, nn) -> vnl_diag_matrixCD

        Parameters
        ----------
        nn: unsigned int

        __init__(self, nn, value) -> vnl_diag_matrixCD

        Parameters
        ----------
        nn: unsigned int
        value: stdcomplexD const &

        __init__(self, that) -> vnl_diag_matrixCD

        Parameters
        ----------
        that: vnl_vectorCD

        """
        _vnl_diag_matrixPython.vnl_diag_matrixCD_swiginit(self, _vnl_diag_matrixPython.new_vnl_diag_matrixCD(*args))
    __imul__ = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD___imul__)

    def __itruediv__(self, *args):
        return _vnl_diag_matrixPython.vnl_diag_matrixCD___itruediv__(self, *args)
    __idiv__ = __itruediv__


    invert_in_place = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_invert_in_place)
    determinant = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_determinant)
    solve = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_solve)
    __call__ = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD___call__)
    get_diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_get_diagonal)
    diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_diagonal)
    fill_diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_fill_diagonal)
    set_diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_set_diagonal)
    begin = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_begin)
    end = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_end)
    size = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_size)
    rows = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_rows)
    cols = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_cols)
    columns = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_columns)
    put = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_put)
    get = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_get)
    as_matrix = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_as_matrix)
    set_size = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_set_size)
    clear = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_clear)
    fill = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_fill)
    data_block = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_data_block)
    set = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCD_set)

# Register vnl_diag_matrixCD in _vnl_diag_matrixPython:
_vnl_diag_matrixPython.vnl_diag_matrixCD_swigregister(vnl_diag_matrixCD)

class vnl_diag_matrixCF(object):
    r"""Proxy of C++ vnl_diag_matrixCF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _vnl_diag_matrixPython.delete_vnl_diag_matrixCF

    def __init__(self, *args):
        r"""
        __init__(self) -> vnl_diag_matrixCF
        __init__(self, arg0) -> vnl_diag_matrixCF

        Parameters
        ----------
        arg0: vnl_diag_matrixCF const &

        __init__(self, nn) -> vnl_diag_matrixCF

        Parameters
        ----------
        nn: unsigned int

        __init__(self, nn, value) -> vnl_diag_matrixCF

        Parameters
        ----------
        nn: unsigned int
        value: stdcomplexF const &

        __init__(self, that) -> vnl_diag_matrixCF

        Parameters
        ----------
        that: vnl_vectorCF

        """
        _vnl_diag_matrixPython.vnl_diag_matrixCF_swiginit(self, _vnl_diag_matrixPython.new_vnl_diag_matrixCF(*args))
    __imul__ = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF___imul__)

    def __itruediv__(self, *args):
        return _vnl_diag_matrixPython.vnl_diag_matrixCF___itruediv__(self, *args)
    __idiv__ = __itruediv__


    invert_in_place = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_invert_in_place)
    determinant = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_determinant)
    solve = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_solve)
    __call__ = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF___call__)
    get_diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_get_diagonal)
    diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_diagonal)
    fill_diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_fill_diagonal)
    set_diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_set_diagonal)
    begin = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_begin)
    end = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_end)
    size = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_size)
    rows = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_rows)
    cols = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_cols)
    columns = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_columns)
    put = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_put)
    get = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_get)
    as_matrix = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_as_matrix)
    set_size = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_set_size)
    clear = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_clear)
    fill = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_fill)
    data_block = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_data_block)
    set = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixCF_set)

# Register vnl_diag_matrixCF in _vnl_diag_matrixPython:
_vnl_diag_matrixPython.vnl_diag_matrixCF_swigregister(vnl_diag_matrixCF)

class vnl_diag_matrixD(object):
    r"""Proxy of C++ vnl_diag_matrixD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _vnl_diag_matrixPython.delete_vnl_diag_matrixD

    def __init__(self, *args):
        r"""
        __init__(self) -> vnl_diag_matrixD
        __init__(self, arg0) -> vnl_diag_matrixD

        Parameters
        ----------
        arg0: vnl_diag_matrixD const &

        __init__(self, nn) -> vnl_diag_matrixD

        Parameters
        ----------
        nn: unsigned int

        __init__(self, nn, value) -> vnl_diag_matrixD

        Parameters
        ----------
        nn: unsigned int
        value: double const &

        __init__(self, that) -> vnl_diag_matrixD

        Parameters
        ----------
        that: vnl_vectorD

        """
        _vnl_diag_matrixPython.vnl_diag_matrixD_swiginit(self, _vnl_diag_matrixPython.new_vnl_diag_matrixD(*args))
    __imul__ = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD___imul__)

    def __itruediv__(self, *args):
        return _vnl_diag_matrixPython.vnl_diag_matrixD___itruediv__(self, *args)
    __idiv__ = __itruediv__


    invert_in_place = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_invert_in_place)
    determinant = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_determinant)
    solve = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_solve)
    __call__ = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD___call__)
    get_diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_get_diagonal)
    diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_diagonal)
    fill_diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_fill_diagonal)
    set_diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_set_diagonal)
    begin = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_begin)
    end = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_end)
    size = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_size)
    rows = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_rows)
    cols = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_cols)
    columns = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_columns)
    put = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_put)
    get = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_get)
    as_matrix = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_as_matrix)
    set_size = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_set_size)
    clear = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_clear)
    fill = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_fill)
    data_block = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_data_block)
    set = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixD_set)

# Register vnl_diag_matrixD in _vnl_diag_matrixPython:
_vnl_diag_matrixPython.vnl_diag_matrixD_swigregister(vnl_diag_matrixD)

class vnl_diag_matrixF(object):
    r"""Proxy of C++ vnl_diag_matrixF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _vnl_diag_matrixPython.delete_vnl_diag_matrixF

    def __init__(self, *args):
        r"""
        __init__(self) -> vnl_diag_matrixF
        __init__(self, arg0) -> vnl_diag_matrixF

        Parameters
        ----------
        arg0: vnl_diag_matrixF const &

        __init__(self, nn) -> vnl_diag_matrixF

        Parameters
        ----------
        nn: unsigned int

        __init__(self, nn, value) -> vnl_diag_matrixF

        Parameters
        ----------
        nn: unsigned int
        value: float const &

        __init__(self, that) -> vnl_diag_matrixF

        Parameters
        ----------
        that: vnl_vectorF

        """
        _vnl_diag_matrixPython.vnl_diag_matrixF_swiginit(self, _vnl_diag_matrixPython.new_vnl_diag_matrixF(*args))
    __imul__ = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF___imul__)

    def __itruediv__(self, *args):
        return _vnl_diag_matrixPython.vnl_diag_matrixF___itruediv__(self, *args)
    __idiv__ = __itruediv__


    invert_in_place = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_invert_in_place)
    determinant = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_determinant)
    solve = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_solve)
    __call__ = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF___call__)
    get_diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_get_diagonal)
    diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_diagonal)
    fill_diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_fill_diagonal)
    set_diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_set_diagonal)
    begin = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_begin)
    end = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_end)
    size = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_size)
    rows = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_rows)
    cols = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_cols)
    columns = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_columns)
    put = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_put)
    get = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_get)
    as_matrix = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_as_matrix)
    set_size = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_set_size)
    clear = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_clear)
    fill = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_fill)
    data_block = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_data_block)
    set = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixF_set)

# Register vnl_diag_matrixF in _vnl_diag_matrixPython:
_vnl_diag_matrixPython.vnl_diag_matrixF_swigregister(vnl_diag_matrixF)

class vnl_diag_matrixLD(object):
    r"""Proxy of C++ vnl_diag_matrixLD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _vnl_diag_matrixPython.delete_vnl_diag_matrixLD

    def __init__(self, *args):
        r"""
        __init__(self) -> vnl_diag_matrixLD
        __init__(self, arg0) -> vnl_diag_matrixLD

        Parameters
        ----------
        arg0: vnl_diag_matrixLD const &

        __init__(self, nn) -> vnl_diag_matrixLD

        Parameters
        ----------
        nn: unsigned int

        __init__(self, nn, value) -> vnl_diag_matrixLD

        Parameters
        ----------
        nn: unsigned int
        value: long double const &

        __init__(self, that) -> vnl_diag_matrixLD

        Parameters
        ----------
        that: vnl_vectorLD

        """
        _vnl_diag_matrixPython.vnl_diag_matrixLD_swiginit(self, _vnl_diag_matrixPython.new_vnl_diag_matrixLD(*args))
    __imul__ = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD___imul__)

    def __itruediv__(self, *args):
        return _vnl_diag_matrixPython.vnl_diag_matrixLD___itruediv__(self, *args)
    __idiv__ = __itruediv__


    invert_in_place = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_invert_in_place)
    determinant = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_determinant)
    solve = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_solve)
    __call__ = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD___call__)
    get_diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_get_diagonal)
    diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_diagonal)
    fill_diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_fill_diagonal)
    set_diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_set_diagonal)
    begin = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_begin)
    end = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_end)
    size = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_size)
    rows = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_rows)
    cols = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_cols)
    columns = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_columns)
    put = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_put)
    get = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_get)
    as_matrix = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_as_matrix)
    set_size = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_set_size)
    clear = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_clear)
    fill = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_fill)
    data_block = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_data_block)
    set = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixLD_set)

# Register vnl_diag_matrixLD in _vnl_diag_matrixPython:
_vnl_diag_matrixPython.vnl_diag_matrixLD_swigregister(vnl_diag_matrixLD)

class vnl_diag_matrixSI(object):
    r"""Proxy of C++ vnl_diag_matrixSI class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _vnl_diag_matrixPython.delete_vnl_diag_matrixSI

    def __init__(self, *args):
        r"""
        __init__(self) -> vnl_diag_matrixSI
        __init__(self, arg0) -> vnl_diag_matrixSI

        Parameters
        ----------
        arg0: vnl_diag_matrixSI const &

        __init__(self, nn) -> vnl_diag_matrixSI

        Parameters
        ----------
        nn: unsigned int

        __init__(self, nn, value) -> vnl_diag_matrixSI

        Parameters
        ----------
        nn: unsigned int
        value: int const &

        __init__(self, that) -> vnl_diag_matrixSI

        Parameters
        ----------
        that: vnl_vectorSI

        """
        _vnl_diag_matrixPython.vnl_diag_matrixSI_swiginit(self, _vnl_diag_matrixPython.new_vnl_diag_matrixSI(*args))
    __imul__ = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI___imul__)

    def __itruediv__(self, *args):
        return _vnl_diag_matrixPython.vnl_diag_matrixSI___itruediv__(self, *args)
    __idiv__ = __itruediv__


    invert_in_place = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_invert_in_place)
    determinant = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_determinant)
    solve = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_solve)
    __call__ = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI___call__)
    get_diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_get_diagonal)
    diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_diagonal)
    fill_diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_fill_diagonal)
    set_diagonal = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_set_diagonal)
    begin = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_begin)
    end = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_end)
    size = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_size)
    rows = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_rows)
    cols = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_cols)
    columns = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_columns)
    put = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_put)
    get = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_get)
    as_matrix = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_as_matrix)
    set_size = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_set_size)
    clear = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_clear)
    fill = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_fill)
    data_block = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_data_block)
    set = _swig_new_instance_method(_vnl_diag_matrixPython.vnl_diag_matrixSI_set)

# Register vnl_diag_matrixSI in _vnl_diag_matrixPython:
_vnl_diag_matrixPython.vnl_diag_matrixSI_swigregister(vnl_diag_matrixSI)



