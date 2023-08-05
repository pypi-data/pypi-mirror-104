# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKTransformPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkComposeScaleSkewVersor3DTransformPython
else:
    import _itkComposeScaleSkewVersor3DTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkComposeScaleSkewVersor3DTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkComposeScaleSkewVersor3DTransformPython.SWIG_PyStaticMethod_New

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
import itk.itkArray2DPython
import itk.vnl_matrixPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.itkMatrixPython
import itk.itkCovariantVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.itkVectorPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkOptimizerParametersPython
import itk.itkArrayPython
import itk.ITKCommonBasePython
import itk.itkVersorRigid3DTransformPython
import itk.itkVersorTransformPython
import itk.itkVersorPython
import itk.itkRigid3DTransformPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkDiffusionTensor3DPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkVariableLengthVectorPython
import itk.itkTransformBasePython

def itkComposeScaleSkewVersor3DTransformD_New():
    return itkComposeScaleSkewVersor3DTransformD.New()

class itkComposeScaleSkewVersor3DTransformD(itk.itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD):
    r"""


    ComposeScaleSkewVersor3DTransform of a vector space (space coords)

    This transform applies a versor rotation and translation & scale/skew
    to the space

    The parameters for this transform can be set either using individual
    Set methods or in serialized form using SetParameters() and
    SetFixedParameters().

    The serialization of the optimizable parameters is an array of 12
    elements. The first 3 elements are the components of the versor
    representation of 3D rotation. The next 3 parameters defines the
    translation in each dimension. The next 3 parameters defines scaling
    in each dimension. The last 3 parameters defines the skew.

    The serialization of the fixed parameters is an array of 3 elements
    defining the center of rotation.

    The transform can be described as: $ (\\textbf{R}_v * \\textbf{S}
    * \\textbf{K})\\textbf{x} $ where $\\textbf{R}_v$ is the
    rotation matrix given the versor, where $\\textbf{S}$ is the
    diagonal scale matrix. where $\\textbf{K}$ is the upper triangle
    skew (shear) matrix. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkComposeScaleSkewVersor3DTransformPython.itkComposeScaleSkewVersor3DTransformD___New_orig__)
    Clone = _swig_new_instance_method(_itkComposeScaleSkewVersor3DTransformPython.itkComposeScaleSkewVersor3DTransformD_Clone)
    SetMatrix = _swig_new_instance_method(_itkComposeScaleSkewVersor3DTransformPython.itkComposeScaleSkewVersor3DTransformD_SetMatrix)
    SetScale = _swig_new_instance_method(_itkComposeScaleSkewVersor3DTransformPython.itkComposeScaleSkewVersor3DTransformD_SetScale)
    GetScale = _swig_new_instance_method(_itkComposeScaleSkewVersor3DTransformPython.itkComposeScaleSkewVersor3DTransformD_GetScale)
    SetSkew = _swig_new_instance_method(_itkComposeScaleSkewVersor3DTransformPython.itkComposeScaleSkewVersor3DTransformD_SetSkew)
    GetSkew = _swig_new_instance_method(_itkComposeScaleSkewVersor3DTransformPython.itkComposeScaleSkewVersor3DTransformD_GetSkew)
    __swig_destroy__ = _itkComposeScaleSkewVersor3DTransformPython.delete_itkComposeScaleSkewVersor3DTransformD
    cast = _swig_new_static_method(_itkComposeScaleSkewVersor3DTransformPython.itkComposeScaleSkewVersor3DTransformD_cast)

    def New(*args, **kargs):
        """New() -> itkComposeScaleSkewVersor3DTransformD

        Create a new object of the class itkComposeScaleSkewVersor3DTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkComposeScaleSkewVersor3DTransformD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkComposeScaleSkewVersor3DTransformD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkComposeScaleSkewVersor3DTransformD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkComposeScaleSkewVersor3DTransformD in _itkComposeScaleSkewVersor3DTransformPython:
_itkComposeScaleSkewVersor3DTransformPython.itkComposeScaleSkewVersor3DTransformD_swigregister(itkComposeScaleSkewVersor3DTransformD)
itkComposeScaleSkewVersor3DTransformD___New_orig__ = _itkComposeScaleSkewVersor3DTransformPython.itkComposeScaleSkewVersor3DTransformD___New_orig__
itkComposeScaleSkewVersor3DTransformD_cast = _itkComposeScaleSkewVersor3DTransformPython.itkComposeScaleSkewVersor3DTransformD_cast



