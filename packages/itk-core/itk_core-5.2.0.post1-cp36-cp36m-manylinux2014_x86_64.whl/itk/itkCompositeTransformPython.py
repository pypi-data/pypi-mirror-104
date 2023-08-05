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
    from . import _itkCompositeTransformPython
else:
    import _itkCompositeTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkCompositeTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkCompositeTransformPython.SWIG_PyStaticMethod_New

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
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_vectorPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.itkPointPython
import itk.ITKCommonBasePython
import itk.itkVariableLengthVectorPython
import itk.itkArray2DPython
import itk.itkTransformBasePython
import itk.itkDiffusionTensor3DPython
import itk.itkArrayPython
import itk.itkOptimizerParametersPython
import itk.itkMultiTransformPython

def itkCompositeTransformD2_New():
    return itkCompositeTransformD2.New()

class itkCompositeTransformD2(itk.itkMultiTransformPython.itkMultiTransformD22):
    r"""


    This class contains a list of transforms and concatenates them by
    composition.

    This class concatenates transforms in reverse queue order by means of
    composition: $ T_0 o T_1 = T_0(T_1(x)) $ Transforms are stored in a
    container (queue), in the following order: $ T_0, T_1, ... , T_N-1 $
    Transforms are added via a single method, AddTransform(). This adds
    the transforms to the back of the queue. A single method for adding
    transforms is meant to simplify the interface and prevent errors. One
    use of the class is to optimize only a subset of included transforms.

    The sub transforms are the same dimensionality as this class.

    Example: A user wants to optimize two Affine transforms together, then
    add a Deformation Field (DF) transform, and optimize it separately. He
    first adds the two Affines, then runs the optimization and both
    Affines transforms are optimized. Next, he adds the DF transform and
    calls SetOnlyMostRecentTransformToOptimizeOn, which clears the
    optimization flags for both of the affine transforms, and leaves the
    flag set only for the DF transform, since it was the last transform
    added. Now he runs the optimization and only the DF transform is
    optimized, but the affines are included in the transformation during
    the optimization.

    Optimization Flags: The m_TransformsToOptimize flags hold one flag for
    each transform in the queue, designating if each transform is to be
    used for optimization. Note that all transforms in the queue are
    applied in TransformPoint, regardless of these flags states'. The
    methods GetParameters, SetParameters,
    ComputeJacobianWithRespectToParameters, GetTransformCategory,
    GetFixedParameters, and SetFixedParameters all query these flags and
    include only those transforms whose corresponding flag is set. Their
    input or output is a concatenated array of all transforms set for use
    in optimization. The goal is to be able to optimize multiple
    transforms at

    Setting Optimization Flags: A transform's optimization flag is set
    when it is added to the queue, and remains set as other transforms are
    added. The methods SetNthTransformToOptimize* and
    SetAllTransformToOptimize* are used to set and clear flags
    arbitrarily. SetOnlyMostRecentTransformToOptimizeOn is a convenience
    method for setting only the most recently added transform for
    optimization, with the idea that this will be a common practice.

    Indexing: The index values used in GetNthTransform and
    SetNthTransformToOptimize* and SetAllTransformToOptimize* follow the
    order in which transforms were added. Thus, the first transform added
    is at index 0, the next at index 1, etc.

    Inverse: The inverse transform is created by retrieving the inverse
    from each sub transform and adding them to a composite transform in
    reverse order. The m_TransformsToOptimizeFlags is copied in reverse
    for the inverse. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCompositeTransformPython.itkCompositeTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_Clone)
    SetNthTransformToOptimize = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_SetNthTransformToOptimize)
    SetNthTransformToOptimizeOn = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_SetNthTransformToOptimizeOn)
    SetNthTransformToOptimizeOff = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_SetNthTransformToOptimizeOff)
    SetAllTransformsToOptimize = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_SetAllTransformsToOptimize)
    SetAllTransformsToOptimizeOn = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_SetAllTransformsToOptimizeOn)
    SetAllTransformsToOptimizeOff = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_SetAllTransformsToOptimizeOff)
    SetOnlyMostRecentTransformToOptimizeOn = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_SetOnlyMostRecentTransformToOptimizeOn)
    GetNthTransformToOptimize = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_GetNthTransformToOptimize)
    GetTransformsToOptimizeFlags = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_GetTransformsToOptimizeFlags)
    GetInverse = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_GetInverse)
    TransformVector = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_TransformVector)
    TransformCovariantVector = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_TransformCovariantVector)
    TransformDiffusionTensor3D = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_TransformDiffusionTensor3D)
    TransformSymmetricSecondRankTensor = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_TransformSymmetricSecondRankTensor)
    UpdateTransformParameters = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_UpdateTransformParameters)
    FlattenTransformQueue = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_FlattenTransformQueue)
    __swig_destroy__ = _itkCompositeTransformPython.delete_itkCompositeTransformD2
    cast = _swig_new_static_method(_itkCompositeTransformPython.itkCompositeTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkCompositeTransformD2

        Create a new object of the class itkCompositeTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCompositeTransformD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCompositeTransformD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCompositeTransformD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCompositeTransformD2 in _itkCompositeTransformPython:
_itkCompositeTransformPython.itkCompositeTransformD2_swigregister(itkCompositeTransformD2)
itkCompositeTransformD2___New_orig__ = _itkCompositeTransformPython.itkCompositeTransformD2___New_orig__
itkCompositeTransformD2_cast = _itkCompositeTransformPython.itkCompositeTransformD2_cast


def itkCompositeTransformD3_New():
    return itkCompositeTransformD3.New()

class itkCompositeTransformD3(itk.itkMultiTransformPython.itkMultiTransformD33):
    r"""


    This class contains a list of transforms and concatenates them by
    composition.

    This class concatenates transforms in reverse queue order by means of
    composition: $ T_0 o T_1 = T_0(T_1(x)) $ Transforms are stored in a
    container (queue), in the following order: $ T_0, T_1, ... , T_N-1 $
    Transforms are added via a single method, AddTransform(). This adds
    the transforms to the back of the queue. A single method for adding
    transforms is meant to simplify the interface and prevent errors. One
    use of the class is to optimize only a subset of included transforms.

    The sub transforms are the same dimensionality as this class.

    Example: A user wants to optimize two Affine transforms together, then
    add a Deformation Field (DF) transform, and optimize it separately. He
    first adds the two Affines, then runs the optimization and both
    Affines transforms are optimized. Next, he adds the DF transform and
    calls SetOnlyMostRecentTransformToOptimizeOn, which clears the
    optimization flags for both of the affine transforms, and leaves the
    flag set only for the DF transform, since it was the last transform
    added. Now he runs the optimization and only the DF transform is
    optimized, but the affines are included in the transformation during
    the optimization.

    Optimization Flags: The m_TransformsToOptimize flags hold one flag for
    each transform in the queue, designating if each transform is to be
    used for optimization. Note that all transforms in the queue are
    applied in TransformPoint, regardless of these flags states'. The
    methods GetParameters, SetParameters,
    ComputeJacobianWithRespectToParameters, GetTransformCategory,
    GetFixedParameters, and SetFixedParameters all query these flags and
    include only those transforms whose corresponding flag is set. Their
    input or output is a concatenated array of all transforms set for use
    in optimization. The goal is to be able to optimize multiple
    transforms at

    Setting Optimization Flags: A transform's optimization flag is set
    when it is added to the queue, and remains set as other transforms are
    added. The methods SetNthTransformToOptimize* and
    SetAllTransformToOptimize* are used to set and clear flags
    arbitrarily. SetOnlyMostRecentTransformToOptimizeOn is a convenience
    method for setting only the most recently added transform for
    optimization, with the idea that this will be a common practice.

    Indexing: The index values used in GetNthTransform and
    SetNthTransformToOptimize* and SetAllTransformToOptimize* follow the
    order in which transforms were added. Thus, the first transform added
    is at index 0, the next at index 1, etc.

    Inverse: The inverse transform is created by retrieving the inverse
    from each sub transform and adding them to a composite transform in
    reverse order. The m_TransformsToOptimizeFlags is copied in reverse
    for the inverse. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCompositeTransformPython.itkCompositeTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_Clone)
    SetNthTransformToOptimize = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_SetNthTransformToOptimize)
    SetNthTransformToOptimizeOn = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_SetNthTransformToOptimizeOn)
    SetNthTransformToOptimizeOff = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_SetNthTransformToOptimizeOff)
    SetAllTransformsToOptimize = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_SetAllTransformsToOptimize)
    SetAllTransformsToOptimizeOn = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_SetAllTransformsToOptimizeOn)
    SetAllTransformsToOptimizeOff = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_SetAllTransformsToOptimizeOff)
    SetOnlyMostRecentTransformToOptimizeOn = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_SetOnlyMostRecentTransformToOptimizeOn)
    GetNthTransformToOptimize = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_GetNthTransformToOptimize)
    GetTransformsToOptimizeFlags = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_GetTransformsToOptimizeFlags)
    GetInverse = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_GetInverse)
    TransformVector = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_TransformVector)
    TransformCovariantVector = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_TransformCovariantVector)
    TransformDiffusionTensor3D = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_TransformDiffusionTensor3D)
    TransformSymmetricSecondRankTensor = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_TransformSymmetricSecondRankTensor)
    UpdateTransformParameters = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_UpdateTransformParameters)
    FlattenTransformQueue = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_FlattenTransformQueue)
    __swig_destroy__ = _itkCompositeTransformPython.delete_itkCompositeTransformD3
    cast = _swig_new_static_method(_itkCompositeTransformPython.itkCompositeTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkCompositeTransformD3

        Create a new object of the class itkCompositeTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCompositeTransformD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCompositeTransformD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCompositeTransformD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCompositeTransformD3 in _itkCompositeTransformPython:
_itkCompositeTransformPython.itkCompositeTransformD3_swigregister(itkCompositeTransformD3)
itkCompositeTransformD3___New_orig__ = _itkCompositeTransformPython.itkCompositeTransformD3___New_orig__
itkCompositeTransformD3_cast = _itkCompositeTransformPython.itkCompositeTransformD3_cast


def itkCompositeTransformD4_New():
    return itkCompositeTransformD4.New()

class itkCompositeTransformD4(itk.itkMultiTransformPython.itkMultiTransformD44):
    r"""


    This class contains a list of transforms and concatenates them by
    composition.

    This class concatenates transforms in reverse queue order by means of
    composition: $ T_0 o T_1 = T_0(T_1(x)) $ Transforms are stored in a
    container (queue), in the following order: $ T_0, T_1, ... , T_N-1 $
    Transforms are added via a single method, AddTransform(). This adds
    the transforms to the back of the queue. A single method for adding
    transforms is meant to simplify the interface and prevent errors. One
    use of the class is to optimize only a subset of included transforms.

    The sub transforms are the same dimensionality as this class.

    Example: A user wants to optimize two Affine transforms together, then
    add a Deformation Field (DF) transform, and optimize it separately. He
    first adds the two Affines, then runs the optimization and both
    Affines transforms are optimized. Next, he adds the DF transform and
    calls SetOnlyMostRecentTransformToOptimizeOn, which clears the
    optimization flags for both of the affine transforms, and leaves the
    flag set only for the DF transform, since it was the last transform
    added. Now he runs the optimization and only the DF transform is
    optimized, but the affines are included in the transformation during
    the optimization.

    Optimization Flags: The m_TransformsToOptimize flags hold one flag for
    each transform in the queue, designating if each transform is to be
    used for optimization. Note that all transforms in the queue are
    applied in TransformPoint, regardless of these flags states'. The
    methods GetParameters, SetParameters,
    ComputeJacobianWithRespectToParameters, GetTransformCategory,
    GetFixedParameters, and SetFixedParameters all query these flags and
    include only those transforms whose corresponding flag is set. Their
    input or output is a concatenated array of all transforms set for use
    in optimization. The goal is to be able to optimize multiple
    transforms at

    Setting Optimization Flags: A transform's optimization flag is set
    when it is added to the queue, and remains set as other transforms are
    added. The methods SetNthTransformToOptimize* and
    SetAllTransformToOptimize* are used to set and clear flags
    arbitrarily. SetOnlyMostRecentTransformToOptimizeOn is a convenience
    method for setting only the most recently added transform for
    optimization, with the idea that this will be a common practice.

    Indexing: The index values used in GetNthTransform and
    SetNthTransformToOptimize* and SetAllTransformToOptimize* follow the
    order in which transforms were added. Thus, the first transform added
    is at index 0, the next at index 1, etc.

    Inverse: The inverse transform is created by retrieving the inverse
    from each sub transform and adding them to a composite transform in
    reverse order. The m_TransformsToOptimizeFlags is copied in reverse
    for the inverse. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCompositeTransformPython.itkCompositeTransformD4___New_orig__)
    Clone = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD4_Clone)
    SetNthTransformToOptimize = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD4_SetNthTransformToOptimize)
    SetNthTransformToOptimizeOn = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD4_SetNthTransformToOptimizeOn)
    SetNthTransformToOptimizeOff = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD4_SetNthTransformToOptimizeOff)
    SetAllTransformsToOptimize = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD4_SetAllTransformsToOptimize)
    SetAllTransformsToOptimizeOn = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD4_SetAllTransformsToOptimizeOn)
    SetAllTransformsToOptimizeOff = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD4_SetAllTransformsToOptimizeOff)
    SetOnlyMostRecentTransformToOptimizeOn = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD4_SetOnlyMostRecentTransformToOptimizeOn)
    GetNthTransformToOptimize = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD4_GetNthTransformToOptimize)
    GetTransformsToOptimizeFlags = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD4_GetTransformsToOptimizeFlags)
    GetInverse = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD4_GetInverse)
    TransformVector = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD4_TransformVector)
    TransformCovariantVector = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD4_TransformCovariantVector)
    TransformDiffusionTensor3D = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD4_TransformDiffusionTensor3D)
    TransformSymmetricSecondRankTensor = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD4_TransformSymmetricSecondRankTensor)
    UpdateTransformParameters = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD4_UpdateTransformParameters)
    FlattenTransformQueue = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD4_FlattenTransformQueue)
    __swig_destroy__ = _itkCompositeTransformPython.delete_itkCompositeTransformD4
    cast = _swig_new_static_method(_itkCompositeTransformPython.itkCompositeTransformD4_cast)

    def New(*args, **kargs):
        """New() -> itkCompositeTransformD4

        Create a new object of the class itkCompositeTransformD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCompositeTransformD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCompositeTransformD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCompositeTransformD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCompositeTransformD4 in _itkCompositeTransformPython:
_itkCompositeTransformPython.itkCompositeTransformD4_swigregister(itkCompositeTransformD4)
itkCompositeTransformD4___New_orig__ = _itkCompositeTransformPython.itkCompositeTransformD4___New_orig__
itkCompositeTransformD4_cast = _itkCompositeTransformPython.itkCompositeTransformD4_cast



