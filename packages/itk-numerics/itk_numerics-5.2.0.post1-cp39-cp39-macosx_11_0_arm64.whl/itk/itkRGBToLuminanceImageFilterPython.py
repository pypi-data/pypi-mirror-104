# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKImageIntensityPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkRGBToLuminanceImageFilterPython
else:
    import _itkRGBToLuminanceImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkRGBToLuminanceImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkRGBToLuminanceImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkUnaryGeneratorImageFilterPython
import itk.itkInPlaceImageFilterAPython
import itk.itkImageToImageFilterBPython
import itk.itkImageToImageFilterCommonPython
import itk.itkVectorImagePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.stdcomplexPython
import itk.itkVariableLengthVectorPython
import itk.itkImagePython
import itk.itkFixedArrayPython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.itkImageRegionPython
import itk.itkMatrixPython
import itk.itkPointPython
import itk.vnl_matrix_fixedPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterAPython
import itk.itkInPlaceImageFilterBPython

def itkRGBToLuminanceImageFilterIRGBAUC2IUC2_New():
    return itkRGBToLuminanceImageFilterIRGBAUC2IUC2.New()

class itkRGBToLuminanceImageFilterIRGBAUC2IUC2(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIRGBAUC2IUC2):
    r"""


    Converts an RGB image into a grayscale image.

    This filters converts an RGB image into a Luminance on by computing
    pixel-wise a linear combination on the Red, Green and Blue channels.
    The pixel type of the input image must have a GetLuminance() method.
    This is the case of the itk::RGBPixel class. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC2IUC2_Clone)
    InputHasNumericTraitsCheck = _itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC2IUC2_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkRGBToLuminanceImageFilterPython.delete_itkRGBToLuminanceImageFilterIRGBAUC2IUC2
    cast = _swig_new_static_method(_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkRGBToLuminanceImageFilterIRGBAUC2IUC2

        Create a new object of the class itkRGBToLuminanceImageFilterIRGBAUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRGBToLuminanceImageFilterIRGBAUC2IUC2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRGBToLuminanceImageFilterIRGBAUC2IUC2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRGBToLuminanceImageFilterIRGBAUC2IUC2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRGBToLuminanceImageFilterIRGBAUC2IUC2 in _itkRGBToLuminanceImageFilterPython:
_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC2IUC2_swigregister(itkRGBToLuminanceImageFilterIRGBAUC2IUC2)
itkRGBToLuminanceImageFilterIRGBAUC2IUC2___New_orig__ = _itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC2IUC2___New_orig__
itkRGBToLuminanceImageFilterIRGBAUC2IUC2_cast = _itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC2IUC2_cast


def itkRGBToLuminanceImageFilterIRGBAUC3IUC3_New():
    return itkRGBToLuminanceImageFilterIRGBAUC3IUC3.New()

class itkRGBToLuminanceImageFilterIRGBAUC3IUC3(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIRGBAUC3IUC3):
    r"""


    Converts an RGB image into a grayscale image.

    This filters converts an RGB image into a Luminance on by computing
    pixel-wise a linear combination on the Red, Green and Blue channels.
    The pixel type of the input image must have a GetLuminance() method.
    This is the case of the itk::RGBPixel class. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC3IUC3_Clone)
    InputHasNumericTraitsCheck = _itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC3IUC3_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkRGBToLuminanceImageFilterPython.delete_itkRGBToLuminanceImageFilterIRGBAUC3IUC3
    cast = _swig_new_static_method(_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkRGBToLuminanceImageFilterIRGBAUC3IUC3

        Create a new object of the class itkRGBToLuminanceImageFilterIRGBAUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRGBToLuminanceImageFilterIRGBAUC3IUC3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRGBToLuminanceImageFilterIRGBAUC3IUC3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRGBToLuminanceImageFilterIRGBAUC3IUC3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRGBToLuminanceImageFilterIRGBAUC3IUC3 in _itkRGBToLuminanceImageFilterPython:
_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC3IUC3_swigregister(itkRGBToLuminanceImageFilterIRGBAUC3IUC3)
itkRGBToLuminanceImageFilterIRGBAUC3IUC3___New_orig__ = _itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC3IUC3___New_orig__
itkRGBToLuminanceImageFilterIRGBAUC3IUC3_cast = _itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC3IUC3_cast


def itkRGBToLuminanceImageFilterIRGBAUC4IUC4_New():
    return itkRGBToLuminanceImageFilterIRGBAUC4IUC4.New()

class itkRGBToLuminanceImageFilterIRGBAUC4IUC4(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIRGBAUC4IUC4):
    r"""


    Converts an RGB image into a grayscale image.

    This filters converts an RGB image into a Luminance on by computing
    pixel-wise a linear combination on the Red, Green and Blue channels.
    The pixel type of the input image must have a GetLuminance() method.
    This is the case of the itk::RGBPixel class. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC4IUC4___New_orig__)
    Clone = _swig_new_instance_method(_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC4IUC4_Clone)
    InputHasNumericTraitsCheck = _itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC4IUC4_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkRGBToLuminanceImageFilterPython.delete_itkRGBToLuminanceImageFilterIRGBAUC4IUC4
    cast = _swig_new_static_method(_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC4IUC4_cast)

    def New(*args, **kargs):
        """New() -> itkRGBToLuminanceImageFilterIRGBAUC4IUC4

        Create a new object of the class itkRGBToLuminanceImageFilterIRGBAUC4IUC4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRGBToLuminanceImageFilterIRGBAUC4IUC4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRGBToLuminanceImageFilterIRGBAUC4IUC4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRGBToLuminanceImageFilterIRGBAUC4IUC4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRGBToLuminanceImageFilterIRGBAUC4IUC4 in _itkRGBToLuminanceImageFilterPython:
_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC4IUC4_swigregister(itkRGBToLuminanceImageFilterIRGBAUC4IUC4)
itkRGBToLuminanceImageFilterIRGBAUC4IUC4___New_orig__ = _itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC4IUC4___New_orig__
itkRGBToLuminanceImageFilterIRGBAUC4IUC4_cast = _itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBAUC4IUC4_cast


def itkRGBToLuminanceImageFilterIRGBUC2IUC2_New():
    return itkRGBToLuminanceImageFilterIRGBUC2IUC2.New()

class itkRGBToLuminanceImageFilterIRGBUC2IUC2(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIRGBUC2IUC2):
    r"""


    Converts an RGB image into a grayscale image.

    This filters converts an RGB image into a Luminance on by computing
    pixel-wise a linear combination on the Red, Green and Blue channels.
    The pixel type of the input image must have a GetLuminance() method.
    This is the case of the itk::RGBPixel class. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC2IUC2_Clone)
    InputHasNumericTraitsCheck = _itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC2IUC2_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkRGBToLuminanceImageFilterPython.delete_itkRGBToLuminanceImageFilterIRGBUC2IUC2
    cast = _swig_new_static_method(_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkRGBToLuminanceImageFilterIRGBUC2IUC2

        Create a new object of the class itkRGBToLuminanceImageFilterIRGBUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRGBToLuminanceImageFilterIRGBUC2IUC2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRGBToLuminanceImageFilterIRGBUC2IUC2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRGBToLuminanceImageFilterIRGBUC2IUC2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRGBToLuminanceImageFilterIRGBUC2IUC2 in _itkRGBToLuminanceImageFilterPython:
_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC2IUC2_swigregister(itkRGBToLuminanceImageFilterIRGBUC2IUC2)
itkRGBToLuminanceImageFilterIRGBUC2IUC2___New_orig__ = _itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC2IUC2___New_orig__
itkRGBToLuminanceImageFilterIRGBUC2IUC2_cast = _itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC2IUC2_cast


def itkRGBToLuminanceImageFilterIRGBUC3IUC3_New():
    return itkRGBToLuminanceImageFilterIRGBUC3IUC3.New()

class itkRGBToLuminanceImageFilterIRGBUC3IUC3(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIRGBUC3IUC3):
    r"""


    Converts an RGB image into a grayscale image.

    This filters converts an RGB image into a Luminance on by computing
    pixel-wise a linear combination on the Red, Green and Blue channels.
    The pixel type of the input image must have a GetLuminance() method.
    This is the case of the itk::RGBPixel class. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC3IUC3_Clone)
    InputHasNumericTraitsCheck = _itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC3IUC3_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkRGBToLuminanceImageFilterPython.delete_itkRGBToLuminanceImageFilterIRGBUC3IUC3
    cast = _swig_new_static_method(_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkRGBToLuminanceImageFilterIRGBUC3IUC3

        Create a new object of the class itkRGBToLuminanceImageFilterIRGBUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRGBToLuminanceImageFilterIRGBUC3IUC3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRGBToLuminanceImageFilterIRGBUC3IUC3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRGBToLuminanceImageFilterIRGBUC3IUC3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRGBToLuminanceImageFilterIRGBUC3IUC3 in _itkRGBToLuminanceImageFilterPython:
_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC3IUC3_swigregister(itkRGBToLuminanceImageFilterIRGBUC3IUC3)
itkRGBToLuminanceImageFilterIRGBUC3IUC3___New_orig__ = _itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC3IUC3___New_orig__
itkRGBToLuminanceImageFilterIRGBUC3IUC3_cast = _itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC3IUC3_cast


def itkRGBToLuminanceImageFilterIRGBUC4IUC4_New():
    return itkRGBToLuminanceImageFilterIRGBUC4IUC4.New()

class itkRGBToLuminanceImageFilterIRGBUC4IUC4(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIRGBUC4IUC4):
    r"""


    Converts an RGB image into a grayscale image.

    This filters converts an RGB image into a Luminance on by computing
    pixel-wise a linear combination on the Red, Green and Blue channels.
    The pixel type of the input image must have a GetLuminance() method.
    This is the case of the itk::RGBPixel class. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC4IUC4___New_orig__)
    Clone = _swig_new_instance_method(_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC4IUC4_Clone)
    InputHasNumericTraitsCheck = _itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC4IUC4_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkRGBToLuminanceImageFilterPython.delete_itkRGBToLuminanceImageFilterIRGBUC4IUC4
    cast = _swig_new_static_method(_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC4IUC4_cast)

    def New(*args, **kargs):
        """New() -> itkRGBToLuminanceImageFilterIRGBUC4IUC4

        Create a new object of the class itkRGBToLuminanceImageFilterIRGBUC4IUC4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRGBToLuminanceImageFilterIRGBUC4IUC4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRGBToLuminanceImageFilterIRGBUC4IUC4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRGBToLuminanceImageFilterIRGBUC4IUC4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRGBToLuminanceImageFilterIRGBUC4IUC4 in _itkRGBToLuminanceImageFilterPython:
_itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC4IUC4_swigregister(itkRGBToLuminanceImageFilterIRGBUC4IUC4)
itkRGBToLuminanceImageFilterIRGBUC4IUC4___New_orig__ = _itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC4IUC4___New_orig__
itkRGBToLuminanceImageFilterIRGBUC4IUC4_cast = _itkRGBToLuminanceImageFilterPython.itkRGBToLuminanceImageFilterIRGBUC4IUC4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def rgb_to_luminance_image_filter(*args: itkt.ImageLike, **kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for RGBToLuminanceImageFilter"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.RGBToLuminanceImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def rgb_to_luminance_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKImageIntensity.RGBToLuminanceImageFilter
    rgb_to_luminance_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    rgb_to_luminance_image_filter.__doc__ = filter_object.__doc__




