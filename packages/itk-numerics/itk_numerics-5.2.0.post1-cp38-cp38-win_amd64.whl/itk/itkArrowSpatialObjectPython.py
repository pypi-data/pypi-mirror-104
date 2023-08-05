# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKSpatialObjectsPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkArrowSpatialObjectPython
else:
    import _itkArrowSpatialObjectPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkArrowSpatialObjectPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkArrowSpatialObjectPython.SWIG_PyStaticMethod_New

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
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.pyBasePython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.vnl_vector_refPython
import itk.itkSpatialObjectBasePython
import itk.ITKCommonBasePython
import itk.itkBoundingBoxPython
import itk.itkMapContainerPython
import itk.itkPointPython
import itk.itkVectorContainerPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkImageRegionPython
import itk.itkAffineTransformPython
import itk.itkTransformBasePython
import itk.itkVariableLengthVectorPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkDiffusionTensor3DPython
import itk.itkArray2DPython
import itk.itkArrayPython
import itk.itkOptimizerParametersPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkSpatialObjectPropertyPython
import itk.itkRGBAPixelPython

def itkArrowSpatialObject2_New():
    return itkArrowSpatialObject2.New()

class itkArrowSpatialObject2(itk.itkSpatialObjectBasePython.itkSpatialObject2):
    r"""


    Representation of a Arrow based on the spatial object classes.

    A ArrowSpatialObject represents a Arrow by serving as the parent of
    the elements of the Arrow. Since any itk::SpatialObject can have
    children (see SpatialObject::GetChildren()), this class needs no
    additional methods. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject2___New_orig__)
    Clone = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject2_Clone)
    SetPositionInObjectSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject2_SetPositionInObjectSpace)
    GetPositionInObjectSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject2_GetPositionInObjectSpace)
    SetDirectionInObjectSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject2_SetDirectionInObjectSpace)
    GetDirectionInObjectSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject2_GetDirectionInObjectSpace)
    SetLengthInObjectSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject2_SetLengthInObjectSpace)
    GetLengthInObjectSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject2_GetLengthInObjectSpace)
    GetPositionInWorldSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject2_GetPositionInWorldSpace)
    GetDirectionInWorldSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject2_GetDirectionInWorldSpace)
    GetLengthInWorldSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject2_GetLengthInWorldSpace)
    __swig_destroy__ = _itkArrowSpatialObjectPython.delete_itkArrowSpatialObject2
    cast = _swig_new_static_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject2_cast)

    def New(*args, **kargs):
        """New() -> itkArrowSpatialObject2

        Create a new object of the class itkArrowSpatialObject2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkArrowSpatialObject2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkArrowSpatialObject2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkArrowSpatialObject2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkArrowSpatialObject2 in _itkArrowSpatialObjectPython:
_itkArrowSpatialObjectPython.itkArrowSpatialObject2_swigregister(itkArrowSpatialObject2)
itkArrowSpatialObject2___New_orig__ = _itkArrowSpatialObjectPython.itkArrowSpatialObject2___New_orig__
itkArrowSpatialObject2_cast = _itkArrowSpatialObjectPython.itkArrowSpatialObject2_cast


def itkArrowSpatialObject3_New():
    return itkArrowSpatialObject3.New()

class itkArrowSpatialObject3(itk.itkSpatialObjectBasePython.itkSpatialObject3):
    r"""


    Representation of a Arrow based on the spatial object classes.

    A ArrowSpatialObject represents a Arrow by serving as the parent of
    the elements of the Arrow. Since any itk::SpatialObject can have
    children (see SpatialObject::GetChildren()), this class needs no
    additional methods. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject3___New_orig__)
    Clone = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject3_Clone)
    SetPositionInObjectSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject3_SetPositionInObjectSpace)
    GetPositionInObjectSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject3_GetPositionInObjectSpace)
    SetDirectionInObjectSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject3_SetDirectionInObjectSpace)
    GetDirectionInObjectSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject3_GetDirectionInObjectSpace)
    SetLengthInObjectSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject3_SetLengthInObjectSpace)
    GetLengthInObjectSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject3_GetLengthInObjectSpace)
    GetPositionInWorldSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject3_GetPositionInWorldSpace)
    GetDirectionInWorldSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject3_GetDirectionInWorldSpace)
    GetLengthInWorldSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject3_GetLengthInWorldSpace)
    __swig_destroy__ = _itkArrowSpatialObjectPython.delete_itkArrowSpatialObject3
    cast = _swig_new_static_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject3_cast)

    def New(*args, **kargs):
        """New() -> itkArrowSpatialObject3

        Create a new object of the class itkArrowSpatialObject3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkArrowSpatialObject3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkArrowSpatialObject3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkArrowSpatialObject3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkArrowSpatialObject3 in _itkArrowSpatialObjectPython:
_itkArrowSpatialObjectPython.itkArrowSpatialObject3_swigregister(itkArrowSpatialObject3)
itkArrowSpatialObject3___New_orig__ = _itkArrowSpatialObjectPython.itkArrowSpatialObject3___New_orig__
itkArrowSpatialObject3_cast = _itkArrowSpatialObjectPython.itkArrowSpatialObject3_cast


def itkArrowSpatialObject4_New():
    return itkArrowSpatialObject4.New()

class itkArrowSpatialObject4(itk.itkSpatialObjectBasePython.itkSpatialObject4):
    r"""


    Representation of a Arrow based on the spatial object classes.

    A ArrowSpatialObject represents a Arrow by serving as the parent of
    the elements of the Arrow. Since any itk::SpatialObject can have
    children (see SpatialObject::GetChildren()), this class needs no
    additional methods. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject4___New_orig__)
    Clone = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject4_Clone)
    SetPositionInObjectSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject4_SetPositionInObjectSpace)
    GetPositionInObjectSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject4_GetPositionInObjectSpace)
    SetDirectionInObjectSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject4_SetDirectionInObjectSpace)
    GetDirectionInObjectSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject4_GetDirectionInObjectSpace)
    SetLengthInObjectSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject4_SetLengthInObjectSpace)
    GetLengthInObjectSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject4_GetLengthInObjectSpace)
    GetPositionInWorldSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject4_GetPositionInWorldSpace)
    GetDirectionInWorldSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject4_GetDirectionInWorldSpace)
    GetLengthInWorldSpace = _swig_new_instance_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject4_GetLengthInWorldSpace)
    __swig_destroy__ = _itkArrowSpatialObjectPython.delete_itkArrowSpatialObject4
    cast = _swig_new_static_method(_itkArrowSpatialObjectPython.itkArrowSpatialObject4_cast)

    def New(*args, **kargs):
        """New() -> itkArrowSpatialObject4

        Create a new object of the class itkArrowSpatialObject4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkArrowSpatialObject4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkArrowSpatialObject4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkArrowSpatialObject4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkArrowSpatialObject4 in _itkArrowSpatialObjectPython:
_itkArrowSpatialObjectPython.itkArrowSpatialObject4_swigregister(itkArrowSpatialObject4)
itkArrowSpatialObject4___New_orig__ = _itkArrowSpatialObjectPython.itkArrowSpatialObject4___New_orig__
itkArrowSpatialObject4_cast = _itkArrowSpatialObjectPython.itkArrowSpatialObject4_cast



