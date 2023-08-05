# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKDisplacementFieldPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython
else:
    import _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.SWIG_PyStaticMethod_New

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
import itk.itkFixedArrayPython
import itk.pyBasePython
import itk.ITKCommonBasePython
import itk.itkArrayPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkDisplacementFieldTransformPython
import itk.itkCovariantVectorPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkDiffusionTensor3DPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkTransformBasePython
import itk.itkVariableLengthVectorPython
import itk.itkArray2DPython
import itk.itkOptimizerParametersPython
import itk.itkIndexPython
import itk.itkSizePython
import itk.itkOffsetPython
import itk.itkImagePython
import itk.itkRGBAPixelPython
import itk.itkImageRegionPython
import itk.itkRGBPixelPython

def itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_New():
    return itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.New()

class itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2(itk.itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD2):
    r"""


    Representation of a smooth deformation field with B-splines.

    Although there already exists a B-spline transform in ITK which can be
    used for processes such as image registration, if these processes
    involve a dense sampling of an image a significant computational
    speed-up can be achieved by densely sampling the B-spline transform
    prior to invoking transformations.

    This class takes as input a displacement field, smooths it on demand
    using the specified B-spline parameters. This represents an
    alternative approach to B-spline (FFD) registration and is explained
    more in detail in the reference given below.

    Nicholas J. Tustison REFERENCE NJ Tustison, BB Avants, JC Gee,
    "Directly Manipulated Free-Form Deformation Image Registration",
    IEEE Transactions on Image Processing, 18(3):624-635, 2009. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_Clone)
    UpdateTransformParameters = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_UpdateTransformParameters)
    SetSplineOrder = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_SetSplineOrder)
    GetSplineOrder = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_GetSplineOrder)
    SetNumberOfControlPointsForTheUpdateField = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_SetNumberOfControlPointsForTheUpdateField)
    GetNumberOfControlPointsForTheUpdateField = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_GetNumberOfControlPointsForTheUpdateField)
    SetMeshSizeForTheUpdateField = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_SetMeshSizeForTheUpdateField)
    SetNumberOfControlPointsForTheTotalField = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_SetNumberOfControlPointsForTheTotalField)
    GetNumberOfControlPointsForTheTotalField = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_GetNumberOfControlPointsForTheTotalField)
    SetMeshSizeForTheTotalField = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_SetMeshSizeForTheTotalField)
    EnforceStationaryBoundaryOn = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_EnforceStationaryBoundaryOn)
    EnforceStationaryBoundaryOff = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_EnforceStationaryBoundaryOff)
    SetEnforceStationaryBoundary = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_SetEnforceStationaryBoundary)
    GetEnforceStationaryBoundary = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_GetEnforceStationaryBoundary)
    __swig_destroy__ = _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.delete_itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2
    cast = _swig_new_static_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2

        Create a new object of the class itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2 in _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython:
_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_swigregister(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2___New_orig__ = _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2___New_orig__
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_cast = _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD2_cast


def itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_New():
    return itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.New()

class itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3(itk.itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD3):
    r"""


    Representation of a smooth deformation field with B-splines.

    Although there already exists a B-spline transform in ITK which can be
    used for processes such as image registration, if these processes
    involve a dense sampling of an image a significant computational
    speed-up can be achieved by densely sampling the B-spline transform
    prior to invoking transformations.

    This class takes as input a displacement field, smooths it on demand
    using the specified B-spline parameters. This represents an
    alternative approach to B-spline (FFD) registration and is explained
    more in detail in the reference given below.

    Nicholas J. Tustison REFERENCE NJ Tustison, BB Avants, JC Gee,
    "Directly Manipulated Free-Form Deformation Image Registration",
    IEEE Transactions on Image Processing, 18(3):624-635, 2009. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_Clone)
    UpdateTransformParameters = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_UpdateTransformParameters)
    SetSplineOrder = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_SetSplineOrder)
    GetSplineOrder = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_GetSplineOrder)
    SetNumberOfControlPointsForTheUpdateField = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_SetNumberOfControlPointsForTheUpdateField)
    GetNumberOfControlPointsForTheUpdateField = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_GetNumberOfControlPointsForTheUpdateField)
    SetMeshSizeForTheUpdateField = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_SetMeshSizeForTheUpdateField)
    SetNumberOfControlPointsForTheTotalField = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_SetNumberOfControlPointsForTheTotalField)
    GetNumberOfControlPointsForTheTotalField = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_GetNumberOfControlPointsForTheTotalField)
    SetMeshSizeForTheTotalField = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_SetMeshSizeForTheTotalField)
    EnforceStationaryBoundaryOn = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_EnforceStationaryBoundaryOn)
    EnforceStationaryBoundaryOff = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_EnforceStationaryBoundaryOff)
    SetEnforceStationaryBoundary = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_SetEnforceStationaryBoundary)
    GetEnforceStationaryBoundary = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_GetEnforceStationaryBoundary)
    __swig_destroy__ = _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.delete_itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3
    cast = _swig_new_static_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3

        Create a new object of the class itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3 in _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython:
_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_swigregister(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3___New_orig__ = _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3___New_orig__
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_cast = _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD3_cast


def itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4_New():
    return itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4.New()

class itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4(itk.itkDisplacementFieldTransformPython.itkDisplacementFieldTransformD4):
    r"""


    Representation of a smooth deformation field with B-splines.

    Although there already exists a B-spline transform in ITK which can be
    used for processes such as image registration, if these processes
    involve a dense sampling of an image a significant computational
    speed-up can be achieved by densely sampling the B-spline transform
    prior to invoking transformations.

    This class takes as input a displacement field, smooths it on demand
    using the specified B-spline parameters. This represents an
    alternative approach to B-spline (FFD) registration and is explained
    more in detail in the reference given below.

    Nicholas J. Tustison REFERENCE NJ Tustison, BB Avants, JC Gee,
    "Directly Manipulated Free-Form Deformation Image Registration",
    IEEE Transactions on Image Processing, 18(3):624-635, 2009. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4_Clone)
    UpdateTransformParameters = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4_UpdateTransformParameters)
    SetSplineOrder = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4_SetSplineOrder)
    GetSplineOrder = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4_GetSplineOrder)
    SetNumberOfControlPointsForTheUpdateField = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4_SetNumberOfControlPointsForTheUpdateField)
    GetNumberOfControlPointsForTheUpdateField = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4_GetNumberOfControlPointsForTheUpdateField)
    SetMeshSizeForTheUpdateField = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4_SetMeshSizeForTheUpdateField)
    SetNumberOfControlPointsForTheTotalField = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4_SetNumberOfControlPointsForTheTotalField)
    GetNumberOfControlPointsForTheTotalField = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4_GetNumberOfControlPointsForTheTotalField)
    SetMeshSizeForTheTotalField = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4_SetMeshSizeForTheTotalField)
    EnforceStationaryBoundaryOn = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4_EnforceStationaryBoundaryOn)
    EnforceStationaryBoundaryOff = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4_EnforceStationaryBoundaryOff)
    SetEnforceStationaryBoundary = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4_SetEnforceStationaryBoundary)
    GetEnforceStationaryBoundary = _swig_new_instance_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4_GetEnforceStationaryBoundary)
    __swig_destroy__ = _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.delete_itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4
    cast = _swig_new_static_method(_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4

        Create a new object of the class itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4 in _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython:
_itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4_swigregister(itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4)
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4___New_orig__ = _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4___New_orig__
itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4_cast = _itkBSplineSmoothingOnUpdateDisplacementFieldTransformPython.itkBSplineSmoothingOnUpdateDisplacementFieldTransformD4_cast



