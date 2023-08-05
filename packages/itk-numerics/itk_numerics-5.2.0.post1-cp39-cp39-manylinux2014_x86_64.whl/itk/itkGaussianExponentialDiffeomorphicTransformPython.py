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
    from . import _itkGaussianExponentialDiffeomorphicTransformPython
else:
    import _itkGaussianExponentialDiffeomorphicTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkGaussianExponentialDiffeomorphicTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkGaussianExponentialDiffeomorphicTransformPython.SWIG_PyStaticMethod_New

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
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkRGBPixelPython
import itk.itkImageRegionPython
import itk.ITKCommonBasePython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkRGBAPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkConstantVelocityFieldTransformPython
import itk.itkOptimizerParametersPython
import itk.itkArrayPython
import itk.itkTransformBasePython
import itk.itkArray2DPython
import itk.itkDiffusionTensor3DPython
import itk.itkVariableLengthVectorPython
import itk.itkDisplacementFieldTransformPython

def itkGaussianExponentialDiffeomorphicTransformD2_New():
    return itkGaussianExponentialDiffeomorphicTransformD2.New()

class itkGaussianExponentialDiffeomorphicTransformD2(itk.itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD2):
    r"""


    Exponential transform using a Gaussian smoothing kernel.

    Exponential transform inspired by the work of J. Ashburner (see
    reference below). Assuming a constant velocity field, the transform
    takes as input the update field at time point t = 1, $u$ and smooths
    it using Gaussian smoothing, $S_{update}$ defined by
    GaussianSmoothingVarianceForTheUpdateField We add that the current
    estimate of the velocity field and then perform a second smoothing
    step such that the new velocity field is

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
    __New_orig__ = _swig_new_static_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_Clone)
    UpdateTransformParameters = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_UpdateTransformParameters)
    GaussianSmoothConstantVelocityField = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_GaussianSmoothConstantVelocityField)
    SetGaussianSmoothingVarianceForTheConstantVelocityField = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_SetGaussianSmoothingVarianceForTheConstantVelocityField)
    GetGaussianSmoothingVarianceForTheConstantVelocityField = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_GetGaussianSmoothingVarianceForTheConstantVelocityField)
    SetGaussianSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_SetGaussianSmoothingVarianceForTheUpdateField)
    GetGaussianSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_GetGaussianSmoothingVarianceForTheUpdateField)
    __swig_destroy__ = _itkGaussianExponentialDiffeomorphicTransformPython.delete_itkGaussianExponentialDiffeomorphicTransformD2
    cast = _swig_new_static_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkGaussianExponentialDiffeomorphicTransformD2

        Create a new object of the class itkGaussianExponentialDiffeomorphicTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGaussianExponentialDiffeomorphicTransformD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGaussianExponentialDiffeomorphicTransformD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGaussianExponentialDiffeomorphicTransformD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGaussianExponentialDiffeomorphicTransformD2 in _itkGaussianExponentialDiffeomorphicTransformPython:
_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_swigregister(itkGaussianExponentialDiffeomorphicTransformD2)
itkGaussianExponentialDiffeomorphicTransformD2___New_orig__ = _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2___New_orig__
itkGaussianExponentialDiffeomorphicTransformD2_cast = _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD2_cast


def itkGaussianExponentialDiffeomorphicTransformD3_New():
    return itkGaussianExponentialDiffeomorphicTransformD3.New()

class itkGaussianExponentialDiffeomorphicTransformD3(itk.itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD3):
    r"""


    Exponential transform using a Gaussian smoothing kernel.

    Exponential transform inspired by the work of J. Ashburner (see
    reference below). Assuming a constant velocity field, the transform
    takes as input the update field at time point t = 1, $u$ and smooths
    it using Gaussian smoothing, $S_{update}$ defined by
    GaussianSmoothingVarianceForTheUpdateField We add that the current
    estimate of the velocity field and then perform a second smoothing
    step such that the new velocity field is

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
    __New_orig__ = _swig_new_static_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_Clone)
    UpdateTransformParameters = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_UpdateTransformParameters)
    GaussianSmoothConstantVelocityField = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_GaussianSmoothConstantVelocityField)
    SetGaussianSmoothingVarianceForTheConstantVelocityField = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_SetGaussianSmoothingVarianceForTheConstantVelocityField)
    GetGaussianSmoothingVarianceForTheConstantVelocityField = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_GetGaussianSmoothingVarianceForTheConstantVelocityField)
    SetGaussianSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_SetGaussianSmoothingVarianceForTheUpdateField)
    GetGaussianSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_GetGaussianSmoothingVarianceForTheUpdateField)
    __swig_destroy__ = _itkGaussianExponentialDiffeomorphicTransformPython.delete_itkGaussianExponentialDiffeomorphicTransformD3
    cast = _swig_new_static_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkGaussianExponentialDiffeomorphicTransformD3

        Create a new object of the class itkGaussianExponentialDiffeomorphicTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGaussianExponentialDiffeomorphicTransformD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGaussianExponentialDiffeomorphicTransformD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGaussianExponentialDiffeomorphicTransformD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGaussianExponentialDiffeomorphicTransformD3 in _itkGaussianExponentialDiffeomorphicTransformPython:
_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_swigregister(itkGaussianExponentialDiffeomorphicTransformD3)
itkGaussianExponentialDiffeomorphicTransformD3___New_orig__ = _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3___New_orig__
itkGaussianExponentialDiffeomorphicTransformD3_cast = _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD3_cast


def itkGaussianExponentialDiffeomorphicTransformD4_New():
    return itkGaussianExponentialDiffeomorphicTransformD4.New()

class itkGaussianExponentialDiffeomorphicTransformD4(itk.itkConstantVelocityFieldTransformPython.itkConstantVelocityFieldTransformD4):
    r"""


    Exponential transform using a Gaussian smoothing kernel.

    Exponential transform inspired by the work of J. Ashburner (see
    reference below). Assuming a constant velocity field, the transform
    takes as input the update field at time point t = 1, $u$ and smooths
    it using Gaussian smoothing, $S_{update}$ defined by
    GaussianSmoothingVarianceForTheUpdateField We add that the current
    estimate of the velocity field and then perform a second smoothing
    step such that the new velocity field is

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
    __New_orig__ = _swig_new_static_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD4___New_orig__)
    Clone = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD4_Clone)
    UpdateTransformParameters = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD4_UpdateTransformParameters)
    GaussianSmoothConstantVelocityField = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD4_GaussianSmoothConstantVelocityField)
    SetGaussianSmoothingVarianceForTheConstantVelocityField = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD4_SetGaussianSmoothingVarianceForTheConstantVelocityField)
    GetGaussianSmoothingVarianceForTheConstantVelocityField = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD4_GetGaussianSmoothingVarianceForTheConstantVelocityField)
    SetGaussianSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD4_SetGaussianSmoothingVarianceForTheUpdateField)
    GetGaussianSmoothingVarianceForTheUpdateField = _swig_new_instance_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD4_GetGaussianSmoothingVarianceForTheUpdateField)
    __swig_destroy__ = _itkGaussianExponentialDiffeomorphicTransformPython.delete_itkGaussianExponentialDiffeomorphicTransformD4
    cast = _swig_new_static_method(_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD4_cast)

    def New(*args, **kargs):
        """New() -> itkGaussianExponentialDiffeomorphicTransformD4

        Create a new object of the class itkGaussianExponentialDiffeomorphicTransformD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGaussianExponentialDiffeomorphicTransformD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGaussianExponentialDiffeomorphicTransformD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGaussianExponentialDiffeomorphicTransformD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGaussianExponentialDiffeomorphicTransformD4 in _itkGaussianExponentialDiffeomorphicTransformPython:
_itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD4_swigregister(itkGaussianExponentialDiffeomorphicTransformD4)
itkGaussianExponentialDiffeomorphicTransformD4___New_orig__ = _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD4___New_orig__
itkGaussianExponentialDiffeomorphicTransformD4_cast = _itkGaussianExponentialDiffeomorphicTransformPython.itkGaussianExponentialDiffeomorphicTransformD4_cast



