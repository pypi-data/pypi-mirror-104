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
    from . import _itkBSplineExponentialDiffeomorphicTransformPython
else:
    import _itkBSplineExponentialDiffeomorphicTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBSplineExponentialDiffeomorphicTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBSplineExponentialDiffeomorphicTransformPython.SWIG_PyStaticMethod_New

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
import itk.itkImagePython
import itk.itkMatrixPython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkRGBPixelPython
import itk.itkRGBAPixelPython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.ITKCommonBasePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkConstantVelocityFieldTransformPython
import itk.itkDisplacementFieldTransformPython
import itk.itkArray2DPython
import itk.itkVariableLengthVectorPython
import itk.itkArrayPython
import itk.itkDiffusionTensor3DPython
import itk.itkTransformBasePython
import itk.itkOptimizerParametersPython

def itkBSplineExponentialDiffeomorphicTransformD2_New():
    return itkBSplineExponentialDiffeomorphicTransformD2.New()

class itkBSplineExponentialDiffeomorphicTransformD2(itk.itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2):
    r"""


    Exponential transform using B-splines as the smoothing kernel.

    Exponential transform inspired by the work of J. Ashburner (see
    reference below). Assuming a constant velocity field, the transform
    takes as input the update field at time point t = 1, $u$ and smooths
    it using a B-spline smoothing (i.e. fitting) operation, $S_{update}$
    defined by SplineOrder and NumberOfControlPointsForTheUpdateField. We
    add that the current estimate of the velocity field and then perform a
    second smoothing step such that the new velocity field is

    \\begin{eqnarray*} v_{new} = S_{velocity}( v_{old} + S_{update}( u )
    ). \\end{eqnarray*}

    We then exponentiate $v_{new}$ using the class
    ExponentialDisplacementImageFilter to yield both the forward and
    inverse displacement fields.

    J. Ashburner. A Fast Diffeomorphic Image Registration Algorithm.
    NeuroImage, 38(1):95-113, 2007.

    Nick Tustison

    Brian Avants 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_Clone)
    UpdateTransformParameters = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_UpdateTransformParameters)
    BSplineSmoothConstantVelocityField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_BSplineSmoothConstantVelocityField)
    SetSplineOrder = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_SetSplineOrder)
    GetSplineOrder = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_GetSplineOrder)
    SetNumberOfControlPointsForTheConstantVelocityField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_SetNumberOfControlPointsForTheConstantVelocityField)
    GetNumberOfControlPointsForTheConstantVelocityField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_GetNumberOfControlPointsForTheConstantVelocityField)
    SetNumberOfControlPointsForTheUpdateField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_SetNumberOfControlPointsForTheUpdateField)
    GetNumberOfControlPointsForTheUpdateField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_GetNumberOfControlPointsForTheUpdateField)
    SetMeshSizeForTheConstantVelocityField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_SetMeshSizeForTheConstantVelocityField)
    SetMeshSizeForTheUpdateField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_SetMeshSizeForTheUpdateField)
    __swig_destroy__ = _itkBSplineExponentialDiffeomorphicTransformPython.delete_itkBSplineExponentialDiffeomorphicTransformD2
    cast = _swig_new_static_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineExponentialDiffeomorphicTransformD2

        Create a new object of the class itkBSplineExponentialDiffeomorphicTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineExponentialDiffeomorphicTransformD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBSplineExponentialDiffeomorphicTransformD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBSplineExponentialDiffeomorphicTransformD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineExponentialDiffeomorphicTransformD2 in _itkBSplineExponentialDiffeomorphicTransformPython:
_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_swigregister(itkBSplineExponentialDiffeomorphicTransformD2)
itkBSplineExponentialDiffeomorphicTransformD2___New_orig__ = _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2___New_orig__
itkBSplineExponentialDiffeomorphicTransformD2_cast = _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD2_cast


def itkBSplineExponentialDiffeomorphicTransformD3_New():
    return itkBSplineExponentialDiffeomorphicTransformD3.New()

class itkBSplineExponentialDiffeomorphicTransformD3(itk.itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3):
    r"""


    Exponential transform using B-splines as the smoothing kernel.

    Exponential transform inspired by the work of J. Ashburner (see
    reference below). Assuming a constant velocity field, the transform
    takes as input the update field at time point t = 1, $u$ and smooths
    it using a B-spline smoothing (i.e. fitting) operation, $S_{update}$
    defined by SplineOrder and NumberOfControlPointsForTheUpdateField. We
    add that the current estimate of the velocity field and then perform a
    second smoothing step such that the new velocity field is

    \\begin{eqnarray*} v_{new} = S_{velocity}( v_{old} + S_{update}( u )
    ). \\end{eqnarray*}

    We then exponentiate $v_{new}$ using the class
    ExponentialDisplacementImageFilter to yield both the forward and
    inverse displacement fields.

    J. Ashburner. A Fast Diffeomorphic Image Registration Algorithm.
    NeuroImage, 38(1):95-113, 2007.

    Nick Tustison

    Brian Avants 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_Clone)
    UpdateTransformParameters = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_UpdateTransformParameters)
    BSplineSmoothConstantVelocityField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_BSplineSmoothConstantVelocityField)
    SetSplineOrder = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_SetSplineOrder)
    GetSplineOrder = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_GetSplineOrder)
    SetNumberOfControlPointsForTheConstantVelocityField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_SetNumberOfControlPointsForTheConstantVelocityField)
    GetNumberOfControlPointsForTheConstantVelocityField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_GetNumberOfControlPointsForTheConstantVelocityField)
    SetNumberOfControlPointsForTheUpdateField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_SetNumberOfControlPointsForTheUpdateField)
    GetNumberOfControlPointsForTheUpdateField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_GetNumberOfControlPointsForTheUpdateField)
    SetMeshSizeForTheConstantVelocityField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_SetMeshSizeForTheConstantVelocityField)
    SetMeshSizeForTheUpdateField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_SetMeshSizeForTheUpdateField)
    __swig_destroy__ = _itkBSplineExponentialDiffeomorphicTransformPython.delete_itkBSplineExponentialDiffeomorphicTransformD3
    cast = _swig_new_static_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineExponentialDiffeomorphicTransformD3

        Create a new object of the class itkBSplineExponentialDiffeomorphicTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineExponentialDiffeomorphicTransformD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBSplineExponentialDiffeomorphicTransformD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBSplineExponentialDiffeomorphicTransformD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineExponentialDiffeomorphicTransformD3 in _itkBSplineExponentialDiffeomorphicTransformPython:
_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_swigregister(itkBSplineExponentialDiffeomorphicTransformD3)
itkBSplineExponentialDiffeomorphicTransformD3___New_orig__ = _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3___New_orig__
itkBSplineExponentialDiffeomorphicTransformD3_cast = _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD3_cast


def itkBSplineExponentialDiffeomorphicTransformD4_New():
    return itkBSplineExponentialDiffeomorphicTransformD4.New()

class itkBSplineExponentialDiffeomorphicTransformD4(itk.itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD4):
    r"""


    Exponential transform using B-splines as the smoothing kernel.

    Exponential transform inspired by the work of J. Ashburner (see
    reference below). Assuming a constant velocity field, the transform
    takes as input the update field at time point t = 1, $u$ and smooths
    it using a B-spline smoothing (i.e. fitting) operation, $S_{update}$
    defined by SplineOrder and NumberOfControlPointsForTheUpdateField. We
    add that the current estimate of the velocity field and then perform a
    second smoothing step such that the new velocity field is

    \\begin{eqnarray*} v_{new} = S_{velocity}( v_{old} + S_{update}( u )
    ). \\end{eqnarray*}

    We then exponentiate $v_{new}$ using the class
    ExponentialDisplacementImageFilter to yield both the forward and
    inverse displacement fields.

    J. Ashburner. A Fast Diffeomorphic Image Registration Algorithm.
    NeuroImage, 38(1):95-113, 2007.

    Nick Tustison

    Brian Avants 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD4___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD4_Clone)
    UpdateTransformParameters = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD4_UpdateTransformParameters)
    BSplineSmoothConstantVelocityField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD4_BSplineSmoothConstantVelocityField)
    SetSplineOrder = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD4_SetSplineOrder)
    GetSplineOrder = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD4_GetSplineOrder)
    SetNumberOfControlPointsForTheConstantVelocityField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD4_SetNumberOfControlPointsForTheConstantVelocityField)
    GetNumberOfControlPointsForTheConstantVelocityField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD4_GetNumberOfControlPointsForTheConstantVelocityField)
    SetNumberOfControlPointsForTheUpdateField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD4_SetNumberOfControlPointsForTheUpdateField)
    GetNumberOfControlPointsForTheUpdateField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD4_GetNumberOfControlPointsForTheUpdateField)
    SetMeshSizeForTheConstantVelocityField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD4_SetMeshSizeForTheConstantVelocityField)
    SetMeshSizeForTheUpdateField = _swig_new_instance_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD4_SetMeshSizeForTheUpdateField)
    __swig_destroy__ = _itkBSplineExponentialDiffeomorphicTransformPython.delete_itkBSplineExponentialDiffeomorphicTransformD4
    cast = _swig_new_static_method(_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD4_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineExponentialDiffeomorphicTransformD4

        Create a new object of the class itkBSplineExponentialDiffeomorphicTransformD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineExponentialDiffeomorphicTransformD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBSplineExponentialDiffeomorphicTransformD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBSplineExponentialDiffeomorphicTransformD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineExponentialDiffeomorphicTransformD4 in _itkBSplineExponentialDiffeomorphicTransformPython:
_itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD4_swigregister(itkBSplineExponentialDiffeomorphicTransformD4)
itkBSplineExponentialDiffeomorphicTransformD4___New_orig__ = _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD4___New_orig__
itkBSplineExponentialDiffeomorphicTransformD4_cast = _itkBSplineExponentialDiffeomorphicTransformPython.itkBSplineExponentialDiffeomorphicTransformD4_cast



