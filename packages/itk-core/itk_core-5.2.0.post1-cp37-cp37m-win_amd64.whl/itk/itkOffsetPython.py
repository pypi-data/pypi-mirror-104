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
    from . import _itkOffsetPython
else:
    import _itkOffsetPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkOffsetPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkOffsetPython.SWIG_PyStaticMethod_New

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
import itk.itkSizePython
import itk.pyBasePython
class itkOffset1(object):
    r"""Proxy of C++ itkOffset1 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    GetOffsetDimension = _swig_new_static_method(_itkOffsetPython.itkOffset1_GetOffsetDimension)
    __add__ = _swig_new_instance_method(_itkOffsetPython.itkOffset1___add__)
    __sub__ = _swig_new_instance_method(_itkOffsetPython.itkOffset1___sub__)
    __iadd__ = _swig_new_instance_method(_itkOffsetPython.itkOffset1___iadd__)
    __isub__ = _swig_new_instance_method(_itkOffsetPython.itkOffset1___isub__)
    GetOffset = _swig_new_instance_method(_itkOffsetPython.itkOffset1_GetOffset)
    SetOffset = _swig_new_instance_method(_itkOffsetPython.itkOffset1_SetOffset)
    SetElement = _swig_new_instance_method(_itkOffsetPython.itkOffset1_SetElement)
    GetElement = _swig_new_instance_method(_itkOffsetPython.itkOffset1_GetElement)
    Fill = _swig_new_instance_method(_itkOffsetPython.itkOffset1_Fill)
    GetBasisOffset = _swig_new_static_method(_itkOffsetPython.itkOffset1_GetBasisOffset)
    assign = _swig_new_instance_method(_itkOffsetPython.itkOffset1_assign)
    swap = _swig_new_instance_method(_itkOffsetPython.itkOffset1_swap)
    begin = _swig_new_instance_method(_itkOffsetPython.itkOffset1_begin)
    end = _swig_new_instance_method(_itkOffsetPython.itkOffset1_end)
    rbegin = _swig_new_instance_method(_itkOffsetPython.itkOffset1_rbegin)
    rend = _swig_new_instance_method(_itkOffsetPython.itkOffset1_rend)
    size = _swig_new_instance_method(_itkOffsetPython.itkOffset1_size)
    max_size = _swig_new_instance_method(_itkOffsetPython.itkOffset1_max_size)
    empty = _swig_new_instance_method(_itkOffsetPython.itkOffset1_empty)
    at = _swig_new_instance_method(_itkOffsetPython.itkOffset1_at)
    front = _swig_new_instance_method(_itkOffsetPython.itkOffset1_front)
    back = _swig_new_instance_method(_itkOffsetPython.itkOffset1_back)
    data = _swig_new_instance_method(_itkOffsetPython.itkOffset1_data)

    def __init__(self, *args):
        r"""
        __init__(self) -> itkOffset1
        __init__(self, arg0) -> itkOffset1

        Parameters
        ----------
        arg0: itkOffset1 const &

        """
        _itkOffsetPython.itkOffset1_swiginit(self, _itkOffsetPython.new_itkOffset1(*args))
    __swig_destroy__ = _itkOffsetPython.delete_itkOffset1
    __getitem__ = _swig_new_instance_method(_itkOffsetPython.itkOffset1___getitem__)
    __setitem__ = _swig_new_instance_method(_itkOffsetPython.itkOffset1___setitem__)
    __len__ = _swig_new_static_method(_itkOffsetPython.itkOffset1___len__)
    __repr__ = _swig_new_instance_method(_itkOffsetPython.itkOffset1___repr__)

    def __eq__(self, other):
        return tuple(self) == tuple(other)


# Register itkOffset1 in _itkOffsetPython:
_itkOffsetPython.itkOffset1_swigregister(itkOffset1)
itkOffset1_GetOffsetDimension = _itkOffsetPython.itkOffset1_GetOffsetDimension
itkOffset1_GetBasisOffset = _itkOffsetPython.itkOffset1_GetBasisOffset
itkOffset1___len__ = _itkOffsetPython.itkOffset1___len__

class itkOffset2(object):
    r"""Proxy of C++ itkOffset2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    GetOffsetDimension = _swig_new_static_method(_itkOffsetPython.itkOffset2_GetOffsetDimension)
    __add__ = _swig_new_instance_method(_itkOffsetPython.itkOffset2___add__)
    __sub__ = _swig_new_instance_method(_itkOffsetPython.itkOffset2___sub__)
    __iadd__ = _swig_new_instance_method(_itkOffsetPython.itkOffset2___iadd__)
    __isub__ = _swig_new_instance_method(_itkOffsetPython.itkOffset2___isub__)
    GetOffset = _swig_new_instance_method(_itkOffsetPython.itkOffset2_GetOffset)
    SetOffset = _swig_new_instance_method(_itkOffsetPython.itkOffset2_SetOffset)
    SetElement = _swig_new_instance_method(_itkOffsetPython.itkOffset2_SetElement)
    GetElement = _swig_new_instance_method(_itkOffsetPython.itkOffset2_GetElement)
    Fill = _swig_new_instance_method(_itkOffsetPython.itkOffset2_Fill)
    GetBasisOffset = _swig_new_static_method(_itkOffsetPython.itkOffset2_GetBasisOffset)
    assign = _swig_new_instance_method(_itkOffsetPython.itkOffset2_assign)
    swap = _swig_new_instance_method(_itkOffsetPython.itkOffset2_swap)
    begin = _swig_new_instance_method(_itkOffsetPython.itkOffset2_begin)
    end = _swig_new_instance_method(_itkOffsetPython.itkOffset2_end)
    rbegin = _swig_new_instance_method(_itkOffsetPython.itkOffset2_rbegin)
    rend = _swig_new_instance_method(_itkOffsetPython.itkOffset2_rend)
    size = _swig_new_instance_method(_itkOffsetPython.itkOffset2_size)
    max_size = _swig_new_instance_method(_itkOffsetPython.itkOffset2_max_size)
    empty = _swig_new_instance_method(_itkOffsetPython.itkOffset2_empty)
    at = _swig_new_instance_method(_itkOffsetPython.itkOffset2_at)
    front = _swig_new_instance_method(_itkOffsetPython.itkOffset2_front)
    back = _swig_new_instance_method(_itkOffsetPython.itkOffset2_back)
    data = _swig_new_instance_method(_itkOffsetPython.itkOffset2_data)

    def __init__(self, *args):
        r"""
        __init__(self) -> itkOffset2
        __init__(self, arg0) -> itkOffset2

        Parameters
        ----------
        arg0: itkOffset2 const &

        """
        _itkOffsetPython.itkOffset2_swiginit(self, _itkOffsetPython.new_itkOffset2(*args))
    __swig_destroy__ = _itkOffsetPython.delete_itkOffset2
    __getitem__ = _swig_new_instance_method(_itkOffsetPython.itkOffset2___getitem__)
    __setitem__ = _swig_new_instance_method(_itkOffsetPython.itkOffset2___setitem__)
    __len__ = _swig_new_static_method(_itkOffsetPython.itkOffset2___len__)
    __repr__ = _swig_new_instance_method(_itkOffsetPython.itkOffset2___repr__)

    def __eq__(self, other):
        return tuple(self) == tuple(other)


# Register itkOffset2 in _itkOffsetPython:
_itkOffsetPython.itkOffset2_swigregister(itkOffset2)
itkOffset2_GetOffsetDimension = _itkOffsetPython.itkOffset2_GetOffsetDimension
itkOffset2_GetBasisOffset = _itkOffsetPython.itkOffset2_GetBasisOffset
itkOffset2___len__ = _itkOffsetPython.itkOffset2___len__

class itkOffset3(object):
    r"""Proxy of C++ itkOffset3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    GetOffsetDimension = _swig_new_static_method(_itkOffsetPython.itkOffset3_GetOffsetDimension)
    __add__ = _swig_new_instance_method(_itkOffsetPython.itkOffset3___add__)
    __sub__ = _swig_new_instance_method(_itkOffsetPython.itkOffset3___sub__)
    __iadd__ = _swig_new_instance_method(_itkOffsetPython.itkOffset3___iadd__)
    __isub__ = _swig_new_instance_method(_itkOffsetPython.itkOffset3___isub__)
    GetOffset = _swig_new_instance_method(_itkOffsetPython.itkOffset3_GetOffset)
    SetOffset = _swig_new_instance_method(_itkOffsetPython.itkOffset3_SetOffset)
    SetElement = _swig_new_instance_method(_itkOffsetPython.itkOffset3_SetElement)
    GetElement = _swig_new_instance_method(_itkOffsetPython.itkOffset3_GetElement)
    Fill = _swig_new_instance_method(_itkOffsetPython.itkOffset3_Fill)
    GetBasisOffset = _swig_new_static_method(_itkOffsetPython.itkOffset3_GetBasisOffset)
    assign = _swig_new_instance_method(_itkOffsetPython.itkOffset3_assign)
    swap = _swig_new_instance_method(_itkOffsetPython.itkOffset3_swap)
    begin = _swig_new_instance_method(_itkOffsetPython.itkOffset3_begin)
    end = _swig_new_instance_method(_itkOffsetPython.itkOffset3_end)
    rbegin = _swig_new_instance_method(_itkOffsetPython.itkOffset3_rbegin)
    rend = _swig_new_instance_method(_itkOffsetPython.itkOffset3_rend)
    size = _swig_new_instance_method(_itkOffsetPython.itkOffset3_size)
    max_size = _swig_new_instance_method(_itkOffsetPython.itkOffset3_max_size)
    empty = _swig_new_instance_method(_itkOffsetPython.itkOffset3_empty)
    at = _swig_new_instance_method(_itkOffsetPython.itkOffset3_at)
    front = _swig_new_instance_method(_itkOffsetPython.itkOffset3_front)
    back = _swig_new_instance_method(_itkOffsetPython.itkOffset3_back)
    data = _swig_new_instance_method(_itkOffsetPython.itkOffset3_data)

    def __init__(self, *args):
        r"""
        __init__(self) -> itkOffset3
        __init__(self, arg0) -> itkOffset3

        Parameters
        ----------
        arg0: itkOffset3 const &

        """
        _itkOffsetPython.itkOffset3_swiginit(self, _itkOffsetPython.new_itkOffset3(*args))
    __swig_destroy__ = _itkOffsetPython.delete_itkOffset3
    __getitem__ = _swig_new_instance_method(_itkOffsetPython.itkOffset3___getitem__)
    __setitem__ = _swig_new_instance_method(_itkOffsetPython.itkOffset3___setitem__)
    __len__ = _swig_new_static_method(_itkOffsetPython.itkOffset3___len__)
    __repr__ = _swig_new_instance_method(_itkOffsetPython.itkOffset3___repr__)

    def __eq__(self, other):
        return tuple(self) == tuple(other)


# Register itkOffset3 in _itkOffsetPython:
_itkOffsetPython.itkOffset3_swigregister(itkOffset3)
itkOffset3_GetOffsetDimension = _itkOffsetPython.itkOffset3_GetOffsetDimension
itkOffset3_GetBasisOffset = _itkOffsetPython.itkOffset3_GetBasisOffset
itkOffset3___len__ = _itkOffsetPython.itkOffset3___len__

class itkOffset4(object):
    r"""Proxy of C++ itkOffset4 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    GetOffsetDimension = _swig_new_static_method(_itkOffsetPython.itkOffset4_GetOffsetDimension)
    __add__ = _swig_new_instance_method(_itkOffsetPython.itkOffset4___add__)
    __sub__ = _swig_new_instance_method(_itkOffsetPython.itkOffset4___sub__)
    __iadd__ = _swig_new_instance_method(_itkOffsetPython.itkOffset4___iadd__)
    __isub__ = _swig_new_instance_method(_itkOffsetPython.itkOffset4___isub__)
    GetOffset = _swig_new_instance_method(_itkOffsetPython.itkOffset4_GetOffset)
    SetOffset = _swig_new_instance_method(_itkOffsetPython.itkOffset4_SetOffset)
    SetElement = _swig_new_instance_method(_itkOffsetPython.itkOffset4_SetElement)
    GetElement = _swig_new_instance_method(_itkOffsetPython.itkOffset4_GetElement)
    Fill = _swig_new_instance_method(_itkOffsetPython.itkOffset4_Fill)
    GetBasisOffset = _swig_new_static_method(_itkOffsetPython.itkOffset4_GetBasisOffset)
    assign = _swig_new_instance_method(_itkOffsetPython.itkOffset4_assign)
    swap = _swig_new_instance_method(_itkOffsetPython.itkOffset4_swap)
    begin = _swig_new_instance_method(_itkOffsetPython.itkOffset4_begin)
    end = _swig_new_instance_method(_itkOffsetPython.itkOffset4_end)
    rbegin = _swig_new_instance_method(_itkOffsetPython.itkOffset4_rbegin)
    rend = _swig_new_instance_method(_itkOffsetPython.itkOffset4_rend)
    size = _swig_new_instance_method(_itkOffsetPython.itkOffset4_size)
    max_size = _swig_new_instance_method(_itkOffsetPython.itkOffset4_max_size)
    empty = _swig_new_instance_method(_itkOffsetPython.itkOffset4_empty)
    at = _swig_new_instance_method(_itkOffsetPython.itkOffset4_at)
    front = _swig_new_instance_method(_itkOffsetPython.itkOffset4_front)
    back = _swig_new_instance_method(_itkOffsetPython.itkOffset4_back)
    data = _swig_new_instance_method(_itkOffsetPython.itkOffset4_data)

    def __init__(self, *args):
        r"""
        __init__(self) -> itkOffset4
        __init__(self, arg0) -> itkOffset4

        Parameters
        ----------
        arg0: itkOffset4 const &

        """
        _itkOffsetPython.itkOffset4_swiginit(self, _itkOffsetPython.new_itkOffset4(*args))
    __swig_destroy__ = _itkOffsetPython.delete_itkOffset4
    __getitem__ = _swig_new_instance_method(_itkOffsetPython.itkOffset4___getitem__)
    __setitem__ = _swig_new_instance_method(_itkOffsetPython.itkOffset4___setitem__)
    __len__ = _swig_new_static_method(_itkOffsetPython.itkOffset4___len__)
    __repr__ = _swig_new_instance_method(_itkOffsetPython.itkOffset4___repr__)

    def __eq__(self, other):
        return tuple(self) == tuple(other)


# Register itkOffset4 in _itkOffsetPython:
_itkOffsetPython.itkOffset4_swigregister(itkOffset4)
itkOffset4_GetOffsetDimension = _itkOffsetPython.itkOffset4_GetOffsetDimension
itkOffset4_GetBasisOffset = _itkOffsetPython.itkOffset4_GetBasisOffset
itkOffset4___len__ = _itkOffsetPython.itkOffset4___len__

class itkOffset5(object):
    r"""Proxy of C++ itkOffset5 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    GetOffsetDimension = _swig_new_static_method(_itkOffsetPython.itkOffset5_GetOffsetDimension)
    __add__ = _swig_new_instance_method(_itkOffsetPython.itkOffset5___add__)
    __sub__ = _swig_new_instance_method(_itkOffsetPython.itkOffset5___sub__)
    __iadd__ = _swig_new_instance_method(_itkOffsetPython.itkOffset5___iadd__)
    __isub__ = _swig_new_instance_method(_itkOffsetPython.itkOffset5___isub__)
    GetOffset = _swig_new_instance_method(_itkOffsetPython.itkOffset5_GetOffset)
    SetOffset = _swig_new_instance_method(_itkOffsetPython.itkOffset5_SetOffset)
    SetElement = _swig_new_instance_method(_itkOffsetPython.itkOffset5_SetElement)
    GetElement = _swig_new_instance_method(_itkOffsetPython.itkOffset5_GetElement)
    Fill = _swig_new_instance_method(_itkOffsetPython.itkOffset5_Fill)
    GetBasisOffset = _swig_new_static_method(_itkOffsetPython.itkOffset5_GetBasisOffset)
    assign = _swig_new_instance_method(_itkOffsetPython.itkOffset5_assign)
    swap = _swig_new_instance_method(_itkOffsetPython.itkOffset5_swap)
    begin = _swig_new_instance_method(_itkOffsetPython.itkOffset5_begin)
    end = _swig_new_instance_method(_itkOffsetPython.itkOffset5_end)
    rbegin = _swig_new_instance_method(_itkOffsetPython.itkOffset5_rbegin)
    rend = _swig_new_instance_method(_itkOffsetPython.itkOffset5_rend)
    size = _swig_new_instance_method(_itkOffsetPython.itkOffset5_size)
    max_size = _swig_new_instance_method(_itkOffsetPython.itkOffset5_max_size)
    empty = _swig_new_instance_method(_itkOffsetPython.itkOffset5_empty)
    at = _swig_new_instance_method(_itkOffsetPython.itkOffset5_at)
    front = _swig_new_instance_method(_itkOffsetPython.itkOffset5_front)
    back = _swig_new_instance_method(_itkOffsetPython.itkOffset5_back)
    data = _swig_new_instance_method(_itkOffsetPython.itkOffset5_data)

    def __init__(self, *args):
        r"""
        __init__(self) -> itkOffset5
        __init__(self, arg0) -> itkOffset5

        Parameters
        ----------
        arg0: itkOffset5 const &

        """
        _itkOffsetPython.itkOffset5_swiginit(self, _itkOffsetPython.new_itkOffset5(*args))
    __swig_destroy__ = _itkOffsetPython.delete_itkOffset5
    __getitem__ = _swig_new_instance_method(_itkOffsetPython.itkOffset5___getitem__)
    __setitem__ = _swig_new_instance_method(_itkOffsetPython.itkOffset5___setitem__)
    __len__ = _swig_new_static_method(_itkOffsetPython.itkOffset5___len__)
    __repr__ = _swig_new_instance_method(_itkOffsetPython.itkOffset5___repr__)

    def __eq__(self, other):
        return tuple(self) == tuple(other)


# Register itkOffset5 in _itkOffsetPython:
_itkOffsetPython.itkOffset5_swigregister(itkOffset5)
itkOffset5_GetOffsetDimension = _itkOffsetPython.itkOffset5_GetOffsetDimension
itkOffset5_GetBasisOffset = _itkOffsetPython.itkOffset5_GetBasisOffset
itkOffset5___len__ = _itkOffsetPython.itkOffset5___len__



