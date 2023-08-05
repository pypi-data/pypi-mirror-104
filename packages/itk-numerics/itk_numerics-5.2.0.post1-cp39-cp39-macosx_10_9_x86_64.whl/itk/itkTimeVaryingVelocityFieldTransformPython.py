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
    from . import _itkTimeVaryingVelocityFieldTransformPython
else:
    import _itkTimeVaryingVelocityFieldTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkTimeVaryingVelocityFieldTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkTimeVaryingVelocityFieldTransformPython.SWIG_PyStaticMethod_New

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
import itk.itkVelocityFieldTransformPython
import itk.itkDisplacementFieldTransformPython
import itk.itkArray2DPython
import itk.itkVariableLengthVectorPython
import itk.itkArrayPython
import itk.itkDiffusionTensor3DPython
import itk.itkTransformBasePython
import itk.itkOptimizerParametersPython

def itkTimeVaryingVelocityFieldTransformD2_New():
    return itkTimeVaryingVelocityFieldTransformD2.New()

class itkTimeVaryingVelocityFieldTransformD2(itk.itkVelocityFieldTransformPython.itkVelocityFieldTransformD2):
    r"""


    Transform objects based on integration of a time-varying velocity
    field.

    Diffeomorphisms are topology-preserving mappings that are useful for
    describing biologically plausible deformations. Mathematically, a
    diffeomorphism, $\\phi$, is generated from a time-varying velocity
    field, v, as described by the first-order differential equation:

    \\[ v(\\phi(x,t), t) = \\frac{d\\phi(x, t)}{dt}, \\phi(x, 0)
    = x \\]

    In this class, the input is the time-varying velocity field. The
    output diffeomorphism is produced using fourth order Runge-Kutta.

    WARNING:  The output deformation field needs to have dimensionality of
    1 less than the input time-varying velocity field. It is assumed that
    the last dimension of the time-varying velocity field corresponds to
    Time, and the other dimensions represent Space.

    Nick Tustison

    Brian Avants 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2_Clone)
    GetModifiableTimeVaryingVelocityField = _swig_new_instance_method(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2_GetModifiableTimeVaryingVelocityField)
    GetTimeVaryingVelocityField = _swig_new_instance_method(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2_GetTimeVaryingVelocityField)
    SetTimeVaryingVelocityField = _swig_new_instance_method(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2_SetTimeVaryingVelocityField)
    __swig_destroy__ = _itkTimeVaryingVelocityFieldTransformPython.delete_itkTimeVaryingVelocityFieldTransformD2
    cast = _swig_new_static_method(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkTimeVaryingVelocityFieldTransformD2

        Create a new object of the class itkTimeVaryingVelocityFieldTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTimeVaryingVelocityFieldTransformD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTimeVaryingVelocityFieldTransformD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTimeVaryingVelocityFieldTransformD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTimeVaryingVelocityFieldTransformD2 in _itkTimeVaryingVelocityFieldTransformPython:
_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2_swigregister(itkTimeVaryingVelocityFieldTransformD2)
itkTimeVaryingVelocityFieldTransformD2___New_orig__ = _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2___New_orig__
itkTimeVaryingVelocityFieldTransformD2_cast = _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD2_cast


def itkTimeVaryingVelocityFieldTransformD3_New():
    return itkTimeVaryingVelocityFieldTransformD3.New()

class itkTimeVaryingVelocityFieldTransformD3(itk.itkVelocityFieldTransformPython.itkVelocityFieldTransformD3):
    r"""


    Transform objects based on integration of a time-varying velocity
    field.

    Diffeomorphisms are topology-preserving mappings that are useful for
    describing biologically plausible deformations. Mathematically, a
    diffeomorphism, $\\phi$, is generated from a time-varying velocity
    field, v, as described by the first-order differential equation:

    \\[ v(\\phi(x,t), t) = \\frac{d\\phi(x, t)}{dt}, \\phi(x, 0)
    = x \\]

    In this class, the input is the time-varying velocity field. The
    output diffeomorphism is produced using fourth order Runge-Kutta.

    WARNING:  The output deformation field needs to have dimensionality of
    1 less than the input time-varying velocity field. It is assumed that
    the last dimension of the time-varying velocity field corresponds to
    Time, and the other dimensions represent Space.

    Nick Tustison

    Brian Avants 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3_Clone)
    GetModifiableTimeVaryingVelocityField = _swig_new_instance_method(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3_GetModifiableTimeVaryingVelocityField)
    GetTimeVaryingVelocityField = _swig_new_instance_method(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3_GetTimeVaryingVelocityField)
    SetTimeVaryingVelocityField = _swig_new_instance_method(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3_SetTimeVaryingVelocityField)
    __swig_destroy__ = _itkTimeVaryingVelocityFieldTransformPython.delete_itkTimeVaryingVelocityFieldTransformD3
    cast = _swig_new_static_method(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkTimeVaryingVelocityFieldTransformD3

        Create a new object of the class itkTimeVaryingVelocityFieldTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTimeVaryingVelocityFieldTransformD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTimeVaryingVelocityFieldTransformD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTimeVaryingVelocityFieldTransformD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTimeVaryingVelocityFieldTransformD3 in _itkTimeVaryingVelocityFieldTransformPython:
_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3_swigregister(itkTimeVaryingVelocityFieldTransformD3)
itkTimeVaryingVelocityFieldTransformD3___New_orig__ = _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3___New_orig__
itkTimeVaryingVelocityFieldTransformD3_cast = _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD3_cast


def itkTimeVaryingVelocityFieldTransformD4_New():
    return itkTimeVaryingVelocityFieldTransformD4.New()

class itkTimeVaryingVelocityFieldTransformD4(itk.itkVelocityFieldTransformPython.itkVelocityFieldTransformD4):
    r"""


    Transform objects based on integration of a time-varying velocity
    field.

    Diffeomorphisms are topology-preserving mappings that are useful for
    describing biologically plausible deformations. Mathematically, a
    diffeomorphism, $\\phi$, is generated from a time-varying velocity
    field, v, as described by the first-order differential equation:

    \\[ v(\\phi(x,t), t) = \\frac{d\\phi(x, t)}{dt}, \\phi(x, 0)
    = x \\]

    In this class, the input is the time-varying velocity field. The
    output diffeomorphism is produced using fourth order Runge-Kutta.

    WARNING:  The output deformation field needs to have dimensionality of
    1 less than the input time-varying velocity field. It is assumed that
    the last dimension of the time-varying velocity field corresponds to
    Time, and the other dimensions represent Space.

    Nick Tustison

    Brian Avants 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD4___New_orig__)
    Clone = _swig_new_instance_method(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD4_Clone)
    GetModifiableTimeVaryingVelocityField = _swig_new_instance_method(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD4_GetModifiableTimeVaryingVelocityField)
    GetTimeVaryingVelocityField = _swig_new_instance_method(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD4_GetTimeVaryingVelocityField)
    SetTimeVaryingVelocityField = _swig_new_instance_method(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD4_SetTimeVaryingVelocityField)
    __swig_destroy__ = _itkTimeVaryingVelocityFieldTransformPython.delete_itkTimeVaryingVelocityFieldTransformD4
    cast = _swig_new_static_method(_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD4_cast)

    def New(*args, **kargs):
        """New() -> itkTimeVaryingVelocityFieldTransformD4

        Create a new object of the class itkTimeVaryingVelocityFieldTransformD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTimeVaryingVelocityFieldTransformD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTimeVaryingVelocityFieldTransformD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTimeVaryingVelocityFieldTransformD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTimeVaryingVelocityFieldTransformD4 in _itkTimeVaryingVelocityFieldTransformPython:
_itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD4_swigregister(itkTimeVaryingVelocityFieldTransformD4)
itkTimeVaryingVelocityFieldTransformD4___New_orig__ = _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD4___New_orig__
itkTimeVaryingVelocityFieldTransformD4_cast = _itkTimeVaryingVelocityFieldTransformPython.itkTimeVaryingVelocityFieldTransformD4_cast



