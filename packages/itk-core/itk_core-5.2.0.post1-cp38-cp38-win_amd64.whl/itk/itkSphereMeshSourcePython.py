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
    from . import _itkSphereMeshSourcePython
else:
    import _itkSphereMeshSourcePython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkSphereMeshSourcePython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkSphereMeshSourcePython.SWIG_PyStaticMethod_New

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
import itk.itkPointPython
import itk.itkFixedArrayPython
import itk.pyBasePython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.ITKCommonBasePython
import itk.itkMeshSourcePython
import itk.itkPointSetPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkVectorContainerPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkMeshBasePython
import itk.itkMapContainerPython
import itk.itkArrayPython
import itk.itkBoundingBoxPython

def itkSphereMeshSourceMD2_New():
    return itkSphereMeshSourceMD2.New()

class itkSphereMeshSourceMD2(itk.itkMeshSourcePython.itkMeshSourceMD2):
    r"""


    Input the center and resolutions in 2 directions(verizon and horizon)
    to create a sphere-like deformable model. The cell on the surface is
    in the shape of triangular. More parameters are added to make the
    sphere mesh have global and local deform ability. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD2___New_orig__)
    Clone = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD2_Clone)
    SetResolutionX = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD2_SetResolutionX)
    SetResolutionY = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD2_SetResolutionY)
    SetCenter = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD2_SetCenter)
    SetScale = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD2_SetScale)
    SetSquareness1 = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD2_SetSquareness1)
    SetSquareness2 = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD2_SetSquareness2)
    __swig_destroy__ = _itkSphereMeshSourcePython.delete_itkSphereMeshSourceMD2
    cast = _swig_new_static_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD2_cast)

    def New(*args, **kargs):
        """New() -> itkSphereMeshSourceMD2

        Create a new object of the class itkSphereMeshSourceMD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSphereMeshSourceMD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkSphereMeshSourceMD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkSphereMeshSourceMD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSphereMeshSourceMD2 in _itkSphereMeshSourcePython:
_itkSphereMeshSourcePython.itkSphereMeshSourceMD2_swigregister(itkSphereMeshSourceMD2)
itkSphereMeshSourceMD2___New_orig__ = _itkSphereMeshSourcePython.itkSphereMeshSourceMD2___New_orig__
itkSphereMeshSourceMD2_cast = _itkSphereMeshSourcePython.itkSphereMeshSourceMD2_cast


def itkSphereMeshSourceMD3_New():
    return itkSphereMeshSourceMD3.New()

class itkSphereMeshSourceMD3(itk.itkMeshSourcePython.itkMeshSourceMD3):
    r"""


    Input the center and resolutions in 2 directions(verizon and horizon)
    to create a sphere-like deformable model. The cell on the surface is
    in the shape of triangular. More parameters are added to make the
    sphere mesh have global and local deform ability. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD3___New_orig__)
    Clone = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD3_Clone)
    SetResolutionX = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD3_SetResolutionX)
    SetResolutionY = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD3_SetResolutionY)
    SetCenter = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD3_SetCenter)
    SetScale = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD3_SetScale)
    SetSquareness1 = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD3_SetSquareness1)
    SetSquareness2 = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD3_SetSquareness2)
    __swig_destroy__ = _itkSphereMeshSourcePython.delete_itkSphereMeshSourceMD3
    cast = _swig_new_static_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD3_cast)

    def New(*args, **kargs):
        """New() -> itkSphereMeshSourceMD3

        Create a new object of the class itkSphereMeshSourceMD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSphereMeshSourceMD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkSphereMeshSourceMD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkSphereMeshSourceMD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSphereMeshSourceMD3 in _itkSphereMeshSourcePython:
_itkSphereMeshSourcePython.itkSphereMeshSourceMD3_swigregister(itkSphereMeshSourceMD3)
itkSphereMeshSourceMD3___New_orig__ = _itkSphereMeshSourcePython.itkSphereMeshSourceMD3___New_orig__
itkSphereMeshSourceMD3_cast = _itkSphereMeshSourcePython.itkSphereMeshSourceMD3_cast


def itkSphereMeshSourceMD4_New():
    return itkSphereMeshSourceMD4.New()

class itkSphereMeshSourceMD4(itk.itkMeshSourcePython.itkMeshSourceMD4):
    r"""


    Input the center and resolutions in 2 directions(verizon and horizon)
    to create a sphere-like deformable model. The cell on the surface is
    in the shape of triangular. More parameters are added to make the
    sphere mesh have global and local deform ability. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD4___New_orig__)
    Clone = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD4_Clone)
    SetResolutionX = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD4_SetResolutionX)
    SetResolutionY = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD4_SetResolutionY)
    SetCenter = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD4_SetCenter)
    SetScale = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD4_SetScale)
    SetSquareness1 = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD4_SetSquareness1)
    SetSquareness2 = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD4_SetSquareness2)
    __swig_destroy__ = _itkSphereMeshSourcePython.delete_itkSphereMeshSourceMD4
    cast = _swig_new_static_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMD4_cast)

    def New(*args, **kargs):
        """New() -> itkSphereMeshSourceMD4

        Create a new object of the class itkSphereMeshSourceMD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSphereMeshSourceMD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkSphereMeshSourceMD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkSphereMeshSourceMD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSphereMeshSourceMD4 in _itkSphereMeshSourcePython:
_itkSphereMeshSourcePython.itkSphereMeshSourceMD4_swigregister(itkSphereMeshSourceMD4)
itkSphereMeshSourceMD4___New_orig__ = _itkSphereMeshSourcePython.itkSphereMeshSourceMD4___New_orig__
itkSphereMeshSourceMD4_cast = _itkSphereMeshSourcePython.itkSphereMeshSourceMD4_cast


def itkSphereMeshSourceMF2_New():
    return itkSphereMeshSourceMF2.New()

class itkSphereMeshSourceMF2(itk.itkMeshSourcePython.itkMeshSourceMF2):
    r"""


    Input the center and resolutions in 2 directions(verizon and horizon)
    to create a sphere-like deformable model. The cell on the surface is
    in the shape of triangular. More parameters are added to make the
    sphere mesh have global and local deform ability. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF2___New_orig__)
    Clone = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF2_Clone)
    SetResolutionX = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF2_SetResolutionX)
    SetResolutionY = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF2_SetResolutionY)
    SetCenter = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF2_SetCenter)
    SetScale = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF2_SetScale)
    SetSquareness1 = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF2_SetSquareness1)
    SetSquareness2 = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF2_SetSquareness2)
    __swig_destroy__ = _itkSphereMeshSourcePython.delete_itkSphereMeshSourceMF2
    cast = _swig_new_static_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF2_cast)

    def New(*args, **kargs):
        """New() -> itkSphereMeshSourceMF2

        Create a new object of the class itkSphereMeshSourceMF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSphereMeshSourceMF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkSphereMeshSourceMF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkSphereMeshSourceMF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSphereMeshSourceMF2 in _itkSphereMeshSourcePython:
_itkSphereMeshSourcePython.itkSphereMeshSourceMF2_swigregister(itkSphereMeshSourceMF2)
itkSphereMeshSourceMF2___New_orig__ = _itkSphereMeshSourcePython.itkSphereMeshSourceMF2___New_orig__
itkSphereMeshSourceMF2_cast = _itkSphereMeshSourcePython.itkSphereMeshSourceMF2_cast


def itkSphereMeshSourceMF3_New():
    return itkSphereMeshSourceMF3.New()

class itkSphereMeshSourceMF3(itk.itkMeshSourcePython.itkMeshSourceMF3):
    r"""


    Input the center and resolutions in 2 directions(verizon and horizon)
    to create a sphere-like deformable model. The cell on the surface is
    in the shape of triangular. More parameters are added to make the
    sphere mesh have global and local deform ability. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF3___New_orig__)
    Clone = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF3_Clone)
    SetResolutionX = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF3_SetResolutionX)
    SetResolutionY = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF3_SetResolutionY)
    SetCenter = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF3_SetCenter)
    SetScale = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF3_SetScale)
    SetSquareness1 = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF3_SetSquareness1)
    SetSquareness2 = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF3_SetSquareness2)
    __swig_destroy__ = _itkSphereMeshSourcePython.delete_itkSphereMeshSourceMF3
    cast = _swig_new_static_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF3_cast)

    def New(*args, **kargs):
        """New() -> itkSphereMeshSourceMF3

        Create a new object of the class itkSphereMeshSourceMF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSphereMeshSourceMF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkSphereMeshSourceMF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkSphereMeshSourceMF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSphereMeshSourceMF3 in _itkSphereMeshSourcePython:
_itkSphereMeshSourcePython.itkSphereMeshSourceMF3_swigregister(itkSphereMeshSourceMF3)
itkSphereMeshSourceMF3___New_orig__ = _itkSphereMeshSourcePython.itkSphereMeshSourceMF3___New_orig__
itkSphereMeshSourceMF3_cast = _itkSphereMeshSourcePython.itkSphereMeshSourceMF3_cast


def itkSphereMeshSourceMF4_New():
    return itkSphereMeshSourceMF4.New()

class itkSphereMeshSourceMF4(itk.itkMeshSourcePython.itkMeshSourceMF4):
    r"""


    Input the center and resolutions in 2 directions(verizon and horizon)
    to create a sphere-like deformable model. The cell on the surface is
    in the shape of triangular. More parameters are added to make the
    sphere mesh have global and local deform ability. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF4___New_orig__)
    Clone = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF4_Clone)
    SetResolutionX = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF4_SetResolutionX)
    SetResolutionY = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF4_SetResolutionY)
    SetCenter = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF4_SetCenter)
    SetScale = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF4_SetScale)
    SetSquareness1 = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF4_SetSquareness1)
    SetSquareness2 = _swig_new_instance_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF4_SetSquareness2)
    __swig_destroy__ = _itkSphereMeshSourcePython.delete_itkSphereMeshSourceMF4
    cast = _swig_new_static_method(_itkSphereMeshSourcePython.itkSphereMeshSourceMF4_cast)

    def New(*args, **kargs):
        """New() -> itkSphereMeshSourceMF4

        Create a new object of the class itkSphereMeshSourceMF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSphereMeshSourceMF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkSphereMeshSourceMF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkSphereMeshSourceMF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSphereMeshSourceMF4 in _itkSphereMeshSourcePython:
_itkSphereMeshSourcePython.itkSphereMeshSourceMF4_swigregister(itkSphereMeshSourceMF4)
itkSphereMeshSourceMF4___New_orig__ = _itkSphereMeshSourcePython.itkSphereMeshSourceMF4___New_orig__
itkSphereMeshSourceMF4_cast = _itkSphereMeshSourcePython.itkSphereMeshSourceMF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def sphere_mesh_source(*args,  resolution_x: int=..., resolution_y: int=..., center: Sequence[float]=..., scale: Sequence[float]=..., squareness1: float=..., squareness2: float=..., output: itkt.Mesh=...,**kwargs)-> itkt.MeshSourceReturn:
    """Functional interface for SphereMeshSource"""
    import itk

    kwarg_typehints = { 'resolution_x':resolution_x,'resolution_y':resolution_y,'center':center,'scale':scale,'squareness1':squareness1,'squareness2':squareness2,'output':output }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.SphereMeshSource.New(*args, **kwargs)
    return instance.__internal_call__()

def sphere_mesh_source_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKMesh.SphereMeshSource
    sphere_mesh_source.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    sphere_mesh_source.__doc__ = filter_object.__doc__




