# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKMeshPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkMeshToMeshFilterPython
else:
    import _itkMeshToMeshFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMeshToMeshFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMeshToMeshFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkMeshBasePython
import itk.itkArrayPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_matrixPython
import itk.itkBoundingBoxPython
import itk.itkMapContainerPython
import itk.itkPointPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.ITKCommonBasePython
import itk.itkVectorContainerPython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkSizePython
import itk.itkOffsetPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkPointSetPython
import itk.itkMeshSourcePython

def itkMeshToMeshFilterMD2MD2_New():
    return itkMeshToMeshFilterMD2MD2.New()

class itkMeshToMeshFilterMD2MD2(itk.itkMeshSourcePython.itkMeshSourceMD2):
    r"""


    MeshToMeshFilter is the base class for all process objects that output
    mesh data, and require mesh data as input. Specifically, this class
    defines the SetInput() method for defining the input to a filter. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2___New_orig__)
    Clone = _swig_new_instance_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2_Clone)
    SetInput = _swig_new_instance_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2_SetInput)
    GetInput = _swig_new_instance_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2_GetInput)
    __swig_destroy__ = _itkMeshToMeshFilterPython.delete_itkMeshToMeshFilterMD2MD2
    cast = _swig_new_static_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2_cast)

    def New(*args, **kargs):
        """New() -> itkMeshToMeshFilterMD2MD2

        Create a new object of the class itkMeshToMeshFilterMD2MD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshToMeshFilterMD2MD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMeshToMeshFilterMD2MD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMeshToMeshFilterMD2MD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeshToMeshFilterMD2MD2 in _itkMeshToMeshFilterPython:
_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2_swigregister(itkMeshToMeshFilterMD2MD2)
itkMeshToMeshFilterMD2MD2___New_orig__ = _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2___New_orig__
itkMeshToMeshFilterMD2MD2_cast = _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2_cast


def itkMeshToMeshFilterMD3MD3_New():
    return itkMeshToMeshFilterMD3MD3.New()

class itkMeshToMeshFilterMD3MD3(itk.itkMeshSourcePython.itkMeshSourceMD3):
    r"""


    MeshToMeshFilter is the base class for all process objects that output
    mesh data, and require mesh data as input. Specifically, this class
    defines the SetInput() method for defining the input to a filter. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3___New_orig__)
    Clone = _swig_new_instance_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3_Clone)
    SetInput = _swig_new_instance_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3_SetInput)
    GetInput = _swig_new_instance_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3_GetInput)
    __swig_destroy__ = _itkMeshToMeshFilterPython.delete_itkMeshToMeshFilterMD3MD3
    cast = _swig_new_static_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3_cast)

    def New(*args, **kargs):
        """New() -> itkMeshToMeshFilterMD3MD3

        Create a new object of the class itkMeshToMeshFilterMD3MD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshToMeshFilterMD3MD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMeshToMeshFilterMD3MD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMeshToMeshFilterMD3MD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeshToMeshFilterMD3MD3 in _itkMeshToMeshFilterPython:
_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3_swigregister(itkMeshToMeshFilterMD3MD3)
itkMeshToMeshFilterMD3MD3___New_orig__ = _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3___New_orig__
itkMeshToMeshFilterMD3MD3_cast = _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3_cast


def itkMeshToMeshFilterMD4MD4_New():
    return itkMeshToMeshFilterMD4MD4.New()

class itkMeshToMeshFilterMD4MD4(itk.itkMeshSourcePython.itkMeshSourceMD4):
    r"""


    MeshToMeshFilter is the base class for all process objects that output
    mesh data, and require mesh data as input. Specifically, this class
    defines the SetInput() method for defining the input to a filter. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD4MD4___New_orig__)
    Clone = _swig_new_instance_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD4MD4_Clone)
    SetInput = _swig_new_instance_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD4MD4_SetInput)
    GetInput = _swig_new_instance_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD4MD4_GetInput)
    __swig_destroy__ = _itkMeshToMeshFilterPython.delete_itkMeshToMeshFilterMD4MD4
    cast = _swig_new_static_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD4MD4_cast)

    def New(*args, **kargs):
        """New() -> itkMeshToMeshFilterMD4MD4

        Create a new object of the class itkMeshToMeshFilterMD4MD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshToMeshFilterMD4MD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMeshToMeshFilterMD4MD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMeshToMeshFilterMD4MD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeshToMeshFilterMD4MD4 in _itkMeshToMeshFilterPython:
_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD4MD4_swigregister(itkMeshToMeshFilterMD4MD4)
itkMeshToMeshFilterMD4MD4___New_orig__ = _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD4MD4___New_orig__
itkMeshToMeshFilterMD4MD4_cast = _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD4MD4_cast


def itkMeshToMeshFilterMF2MF2_New():
    return itkMeshToMeshFilterMF2MF2.New()

class itkMeshToMeshFilterMF2MF2(itk.itkMeshSourcePython.itkMeshSourceMF2):
    r"""


    MeshToMeshFilter is the base class for all process objects that output
    mesh data, and require mesh data as input. Specifically, this class
    defines the SetInput() method for defining the input to a filter. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2___New_orig__)
    Clone = _swig_new_instance_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2_Clone)
    SetInput = _swig_new_instance_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2_SetInput)
    GetInput = _swig_new_instance_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2_GetInput)
    __swig_destroy__ = _itkMeshToMeshFilterPython.delete_itkMeshToMeshFilterMF2MF2
    cast = _swig_new_static_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2_cast)

    def New(*args, **kargs):
        """New() -> itkMeshToMeshFilterMF2MF2

        Create a new object of the class itkMeshToMeshFilterMF2MF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshToMeshFilterMF2MF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMeshToMeshFilterMF2MF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMeshToMeshFilterMF2MF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeshToMeshFilterMF2MF2 in _itkMeshToMeshFilterPython:
_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2_swigregister(itkMeshToMeshFilterMF2MF2)
itkMeshToMeshFilterMF2MF2___New_orig__ = _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2___New_orig__
itkMeshToMeshFilterMF2MF2_cast = _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2_cast


def itkMeshToMeshFilterMF3MF3_New():
    return itkMeshToMeshFilterMF3MF3.New()

class itkMeshToMeshFilterMF3MF3(itk.itkMeshSourcePython.itkMeshSourceMF3):
    r"""


    MeshToMeshFilter is the base class for all process objects that output
    mesh data, and require mesh data as input. Specifically, this class
    defines the SetInput() method for defining the input to a filter. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3___New_orig__)
    Clone = _swig_new_instance_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3_Clone)
    SetInput = _swig_new_instance_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3_SetInput)
    GetInput = _swig_new_instance_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3_GetInput)
    __swig_destroy__ = _itkMeshToMeshFilterPython.delete_itkMeshToMeshFilterMF3MF3
    cast = _swig_new_static_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3_cast)

    def New(*args, **kargs):
        """New() -> itkMeshToMeshFilterMF3MF3

        Create a new object of the class itkMeshToMeshFilterMF3MF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshToMeshFilterMF3MF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMeshToMeshFilterMF3MF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMeshToMeshFilterMF3MF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeshToMeshFilterMF3MF3 in _itkMeshToMeshFilterPython:
_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3_swigregister(itkMeshToMeshFilterMF3MF3)
itkMeshToMeshFilterMF3MF3___New_orig__ = _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3___New_orig__
itkMeshToMeshFilterMF3MF3_cast = _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3_cast


def itkMeshToMeshFilterMF4MF4_New():
    return itkMeshToMeshFilterMF4MF4.New()

class itkMeshToMeshFilterMF4MF4(itk.itkMeshSourcePython.itkMeshSourceMF4):
    r"""


    MeshToMeshFilter is the base class for all process objects that output
    mesh data, and require mesh data as input. Specifically, this class
    defines the SetInput() method for defining the input to a filter. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF4MF4___New_orig__)
    Clone = _swig_new_instance_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF4MF4_Clone)
    SetInput = _swig_new_instance_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF4MF4_SetInput)
    GetInput = _swig_new_instance_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF4MF4_GetInput)
    __swig_destroy__ = _itkMeshToMeshFilterPython.delete_itkMeshToMeshFilterMF4MF4
    cast = _swig_new_static_method(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF4MF4_cast)

    def New(*args, **kargs):
        """New() -> itkMeshToMeshFilterMF4MF4

        Create a new object of the class itkMeshToMeshFilterMF4MF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshToMeshFilterMF4MF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMeshToMeshFilterMF4MF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMeshToMeshFilterMF4MF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeshToMeshFilterMF4MF4 in _itkMeshToMeshFilterPython:
_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF4MF4_swigregister(itkMeshToMeshFilterMF4MF4)
itkMeshToMeshFilterMF4MF4___New_orig__ = _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF4MF4___New_orig__
itkMeshToMeshFilterMF4MF4_cast = _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF4MF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def mesh_to_mesh_filter(*args,  output: itkt.Mesh=...,**kwargs)-> itkt.MeshSourceReturn:
    """Functional interface for MeshToMeshFilter"""
    import itk

    kwarg_typehints = { 'output':output }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.MeshToMeshFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def mesh_to_mesh_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKMesh.MeshToMeshFilter
    mesh_to_mesh_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    mesh_to_mesh_filter.__doc__ = filter_object.__doc__




