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
    from . import _itkTranslationTransformPython
else:
    import _itkTranslationTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkTranslationTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkTranslationTransformPython.SWIG_PyStaticMethod_New

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
import itk.itkOptimizerParametersPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.itkArrayPython
import itk.ITKCommonBasePython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.itkTransformBasePython
import itk.itkDiffusionTensor3DPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkVariableLengthVectorPython
import itk.itkArray2DPython

def itkTranslationTransformD2_New():
    return itkTranslationTransformD2.New()

class itkTranslationTransformD2(itk.itkTransformBasePython.itkTransformD22):
    r"""


    Translation transformation of a vector space (e.g. space coordinates)

    The same functionality could be obtained by using the Affine
    transform, but with a large difference in performance.

    example{Core/Transform/TranslateAVectorImage,Translate Vector Image}
    example{Registration/Common/GlobalRegistrationOfTwoImages,Global
    Registration Of Two Images}
    example{Registration/Common/MutualInformation,Mutual Information} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTranslationTransformPython.itkTranslationTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD2_Clone)
    GetOffset = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD2_GetOffset)
    SetOffset = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD2_SetOffset)
    Compose = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD2_Compose)
    Translate = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD2_Translate)
    TransformVector = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD2_TransformVector)
    BackTransform = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD2_BackTransform)
    GetInverse = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD2_GetInverse)
    SetIdentity = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD2_SetIdentity)
    __swig_destroy__ = _itkTranslationTransformPython.delete_itkTranslationTransformD2
    cast = _swig_new_static_method(_itkTranslationTransformPython.itkTranslationTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkTranslationTransformD2

        Create a new object of the class itkTranslationTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTranslationTransformD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTranslationTransformD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTranslationTransformD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTranslationTransformD2 in _itkTranslationTransformPython:
_itkTranslationTransformPython.itkTranslationTransformD2_swigregister(itkTranslationTransformD2)
itkTranslationTransformD2___New_orig__ = _itkTranslationTransformPython.itkTranslationTransformD2___New_orig__
itkTranslationTransformD2_cast = _itkTranslationTransformPython.itkTranslationTransformD2_cast


def itkTranslationTransformD3_New():
    return itkTranslationTransformD3.New()

class itkTranslationTransformD3(itk.itkTransformBasePython.itkTransformD33):
    r"""


    Translation transformation of a vector space (e.g. space coordinates)

    The same functionality could be obtained by using the Affine
    transform, but with a large difference in performance.

    example{Core/Transform/TranslateAVectorImage,Translate Vector Image}
    example{Registration/Common/GlobalRegistrationOfTwoImages,Global
    Registration Of Two Images}
    example{Registration/Common/MutualInformation,Mutual Information} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTranslationTransformPython.itkTranslationTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD3_Clone)
    GetOffset = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD3_GetOffset)
    SetOffset = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD3_SetOffset)
    Compose = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD3_Compose)
    Translate = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD3_Translate)
    TransformVector = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD3_TransformVector)
    BackTransform = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD3_BackTransform)
    GetInverse = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD3_GetInverse)
    SetIdentity = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD3_SetIdentity)
    __swig_destroy__ = _itkTranslationTransformPython.delete_itkTranslationTransformD3
    cast = _swig_new_static_method(_itkTranslationTransformPython.itkTranslationTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkTranslationTransformD3

        Create a new object of the class itkTranslationTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTranslationTransformD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTranslationTransformD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTranslationTransformD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTranslationTransformD3 in _itkTranslationTransformPython:
_itkTranslationTransformPython.itkTranslationTransformD3_swigregister(itkTranslationTransformD3)
itkTranslationTransformD3___New_orig__ = _itkTranslationTransformPython.itkTranslationTransformD3___New_orig__
itkTranslationTransformD3_cast = _itkTranslationTransformPython.itkTranslationTransformD3_cast


def itkTranslationTransformD4_New():
    return itkTranslationTransformD4.New()

class itkTranslationTransformD4(itk.itkTransformBasePython.itkTransformD44):
    r"""


    Translation transformation of a vector space (e.g. space coordinates)

    The same functionality could be obtained by using the Affine
    transform, but with a large difference in performance.

    example{Core/Transform/TranslateAVectorImage,Translate Vector Image}
    example{Registration/Common/GlobalRegistrationOfTwoImages,Global
    Registration Of Two Images}
    example{Registration/Common/MutualInformation,Mutual Information} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTranslationTransformPython.itkTranslationTransformD4___New_orig__)
    Clone = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD4_Clone)
    GetOffset = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD4_GetOffset)
    SetOffset = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD4_SetOffset)
    Compose = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD4_Compose)
    Translate = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD4_Translate)
    TransformVector = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD4_TransformVector)
    BackTransform = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD4_BackTransform)
    GetInverse = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD4_GetInverse)
    SetIdentity = _swig_new_instance_method(_itkTranslationTransformPython.itkTranslationTransformD4_SetIdentity)
    __swig_destroy__ = _itkTranslationTransformPython.delete_itkTranslationTransformD4
    cast = _swig_new_static_method(_itkTranslationTransformPython.itkTranslationTransformD4_cast)

    def New(*args, **kargs):
        """New() -> itkTranslationTransformD4

        Create a new object of the class itkTranslationTransformD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTranslationTransformD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTranslationTransformD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTranslationTransformD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTranslationTransformD4 in _itkTranslationTransformPython:
_itkTranslationTransformPython.itkTranslationTransformD4_swigregister(itkTranslationTransformD4)
itkTranslationTransformD4___New_orig__ = _itkTranslationTransformPython.itkTranslationTransformD4___New_orig__
itkTranslationTransformD4_cast = _itkTranslationTransformPython.itkTranslationTransformD4_cast



