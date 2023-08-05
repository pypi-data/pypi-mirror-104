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
    from . import _itkSimilarity2DTransformPython
else:
    import _itkSimilarity2DTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkSimilarity2DTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkSimilarity2DTransformPython.SWIG_PyStaticMethod_New

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
import itk.itkArray2DPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.itkPointPython
import itk.itkTransformBasePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkVariableLengthVectorPython
import itk.itkDiffusionTensor3DPython
import itk.itkArrayPython
import itk.itkOptimizerParametersPython
import itk.itkRigid2DTransformPython
import itk.itkMatrixOffsetTransformBasePython

def itkSimilarity2DTransformD_New():
    return itkSimilarity2DTransformD.New()

class itkSimilarity2DTransformD(itk.itkRigid2DTransformPython.itkRigid2DTransformD):
    r"""


    Similarity2DTransform of a vector space (e.g. space coordinates)

    This transform applies a homogeneous scale and rigid transform in 2D
    space. The transform is specified as a scale and rotation around a
    arbitrary center and is followed by a translation. given one angle for
    rotation, a homogeneous scale and a 2D offset for translation.

    The parameters for this transform can be set either using individual
    Set methods or in serialized form using SetParameters() and
    SetFixedParameters().

    The serialization of the optimizable parameters is an array of 3
    elements ordered as follows: p[0] = scale p[1] = angle p[2] = x
    component of the translation p[3] = y component of the translation

    The serialization of the fixed parameters is an array of 2 elements
    ordered as follows: p[0] = x coordinate of the center p[1] = y
    coordinate of the center

    Access methods for the center, translation and underlying matrix
    offset vectors are documented in the superclass
    MatrixOffsetTransformBase.

    Access methods for the angle are documented in superclass
    Rigid2DTransform.

    See:   Transform

    See:   MatrixOffsetTransformBase

    See:   Rigid2DTransform 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSimilarity2DTransformPython.itkSimilarity2DTransformD___New_orig__)
    Clone = _swig_new_instance_method(_itkSimilarity2DTransformPython.itkSimilarity2DTransformD_Clone)
    SetScale = _swig_new_instance_method(_itkSimilarity2DTransformPython.itkSimilarity2DTransformD_SetScale)
    GetScale = _swig_new_instance_method(_itkSimilarity2DTransformPython.itkSimilarity2DTransformD_GetScale)
    CloneInverseTo = _swig_new_instance_method(_itkSimilarity2DTransformPython.itkSimilarity2DTransformD_CloneInverseTo)
    GetInverse = _swig_new_instance_method(_itkSimilarity2DTransformPython.itkSimilarity2DTransformD_GetInverse)
    CloneTo = _swig_new_instance_method(_itkSimilarity2DTransformPython.itkSimilarity2DTransformD_CloneTo)
    SetMatrix = _swig_new_instance_method(_itkSimilarity2DTransformPython.itkSimilarity2DTransformD_SetMatrix)
    __swig_destroy__ = _itkSimilarity2DTransformPython.delete_itkSimilarity2DTransformD
    cast = _swig_new_static_method(_itkSimilarity2DTransformPython.itkSimilarity2DTransformD_cast)

    def New(*args, **kargs):
        """New() -> itkSimilarity2DTransformD

        Create a new object of the class itkSimilarity2DTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSimilarity2DTransformD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkSimilarity2DTransformD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkSimilarity2DTransformD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSimilarity2DTransformD in _itkSimilarity2DTransformPython:
_itkSimilarity2DTransformPython.itkSimilarity2DTransformD_swigregister(itkSimilarity2DTransformD)
itkSimilarity2DTransformD___New_orig__ = _itkSimilarity2DTransformPython.itkSimilarity2DTransformD___New_orig__
itkSimilarity2DTransformD_cast = _itkSimilarity2DTransformPython.itkSimilarity2DTransformD_cast



