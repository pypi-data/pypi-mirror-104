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
    from . import _itkCosImageFilterPython
else:
    import _itkCosImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkCosImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkCosImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkImageRegionPython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkInPlaceImageFilterBPython
import itk.itkImageToImageFilterBPython
import itk.itkImageSourcePython
import itk.itkImagePython
import itk.itkRGBPixelPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.vnl_vector_refPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkCovariantVectorPython
import itk.itkRGBAPixelPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterCommonPython
import itk.itkInPlaceImageFilterAPython
import itk.itkImageToImageFilterAPython

def itkCosImageFilterID2ID2_New():
    return itkCosImageFilterID2ID2.New()

class itkCosImageFilterID2ID2(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID2ID2):
    r"""


    Computes the cosine of each pixel.

    This filter is templated over the pixel type of the input image and
    the pixel type of the output image.

    The filter walks over all of the pixels in the input image, and for
    each pixel does the following:

    cast the pixel value to double,

    apply the std::cos() function to the double value,

    cast the double value resulting from std::cos() to the pixel type of
    the output image,

    store the cast value into the output image.  The filter expects both
    images to have the same dimension (e.g. both 2D, or both 3D, or both
    ND) 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCosImageFilterPython.itkCosImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkCosImageFilterPython.itkCosImageFilterID2ID2_Clone)
    InputConvertibleToDoubleCheck = _itkCosImageFilterPython.itkCosImageFilterID2ID2_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkCosImageFilterPython.itkCosImageFilterID2ID2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkCosImageFilterPython.delete_itkCosImageFilterID2ID2
    cast = _swig_new_static_method(_itkCosImageFilterPython.itkCosImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkCosImageFilterID2ID2

        Create a new object of the class itkCosImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCosImageFilterID2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCosImageFilterID2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCosImageFilterID2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCosImageFilterID2ID2 in _itkCosImageFilterPython:
_itkCosImageFilterPython.itkCosImageFilterID2ID2_swigregister(itkCosImageFilterID2ID2)
itkCosImageFilterID2ID2___New_orig__ = _itkCosImageFilterPython.itkCosImageFilterID2ID2___New_orig__
itkCosImageFilterID2ID2_cast = _itkCosImageFilterPython.itkCosImageFilterID2ID2_cast


def itkCosImageFilterID3ID3_New():
    return itkCosImageFilterID3ID3.New()

class itkCosImageFilterID3ID3(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID3ID3):
    r"""


    Computes the cosine of each pixel.

    This filter is templated over the pixel type of the input image and
    the pixel type of the output image.

    The filter walks over all of the pixels in the input image, and for
    each pixel does the following:

    cast the pixel value to double,

    apply the std::cos() function to the double value,

    cast the double value resulting from std::cos() to the pixel type of
    the output image,

    store the cast value into the output image.  The filter expects both
    images to have the same dimension (e.g. both 2D, or both 3D, or both
    ND) 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCosImageFilterPython.itkCosImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkCosImageFilterPython.itkCosImageFilterID3ID3_Clone)
    InputConvertibleToDoubleCheck = _itkCosImageFilterPython.itkCosImageFilterID3ID3_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkCosImageFilterPython.itkCosImageFilterID3ID3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkCosImageFilterPython.delete_itkCosImageFilterID3ID3
    cast = _swig_new_static_method(_itkCosImageFilterPython.itkCosImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkCosImageFilterID3ID3

        Create a new object of the class itkCosImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCosImageFilterID3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCosImageFilterID3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCosImageFilterID3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCosImageFilterID3ID3 in _itkCosImageFilterPython:
_itkCosImageFilterPython.itkCosImageFilterID3ID3_swigregister(itkCosImageFilterID3ID3)
itkCosImageFilterID3ID3___New_orig__ = _itkCosImageFilterPython.itkCosImageFilterID3ID3___New_orig__
itkCosImageFilterID3ID3_cast = _itkCosImageFilterPython.itkCosImageFilterID3ID3_cast


def itkCosImageFilterID4ID4_New():
    return itkCosImageFilterID4ID4.New()

class itkCosImageFilterID4ID4(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID4ID4):
    r"""


    Computes the cosine of each pixel.

    This filter is templated over the pixel type of the input image and
    the pixel type of the output image.

    The filter walks over all of the pixels in the input image, and for
    each pixel does the following:

    cast the pixel value to double,

    apply the std::cos() function to the double value,

    cast the double value resulting from std::cos() to the pixel type of
    the output image,

    store the cast value into the output image.  The filter expects both
    images to have the same dimension (e.g. both 2D, or both 3D, or both
    ND) 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCosImageFilterPython.itkCosImageFilterID4ID4___New_orig__)
    Clone = _swig_new_instance_method(_itkCosImageFilterPython.itkCosImageFilterID4ID4_Clone)
    InputConvertibleToDoubleCheck = _itkCosImageFilterPython.itkCosImageFilterID4ID4_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkCosImageFilterPython.itkCosImageFilterID4ID4_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkCosImageFilterPython.delete_itkCosImageFilterID4ID4
    cast = _swig_new_static_method(_itkCosImageFilterPython.itkCosImageFilterID4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkCosImageFilterID4ID4

        Create a new object of the class itkCosImageFilterID4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCosImageFilterID4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCosImageFilterID4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCosImageFilterID4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCosImageFilterID4ID4 in _itkCosImageFilterPython:
_itkCosImageFilterPython.itkCosImageFilterID4ID4_swigregister(itkCosImageFilterID4ID4)
itkCosImageFilterID4ID4___New_orig__ = _itkCosImageFilterPython.itkCosImageFilterID4ID4___New_orig__
itkCosImageFilterID4ID4_cast = _itkCosImageFilterPython.itkCosImageFilterID4ID4_cast


def itkCosImageFilterIF2IF2_New():
    return itkCosImageFilterIF2IF2.New()

class itkCosImageFilterIF2IF2(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF2IF2):
    r"""


    Computes the cosine of each pixel.

    This filter is templated over the pixel type of the input image and
    the pixel type of the output image.

    The filter walks over all of the pixels in the input image, and for
    each pixel does the following:

    cast the pixel value to double,

    apply the std::cos() function to the double value,

    cast the double value resulting from std::cos() to the pixel type of
    the output image,

    store the cast value into the output image.  The filter expects both
    images to have the same dimension (e.g. both 2D, or both 3D, or both
    ND) 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCosImageFilterPython.itkCosImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkCosImageFilterPython.itkCosImageFilterIF2IF2_Clone)
    InputConvertibleToDoubleCheck = _itkCosImageFilterPython.itkCosImageFilterIF2IF2_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkCosImageFilterPython.itkCosImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkCosImageFilterPython.delete_itkCosImageFilterIF2IF2
    cast = _swig_new_static_method(_itkCosImageFilterPython.itkCosImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkCosImageFilterIF2IF2

        Create a new object of the class itkCosImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCosImageFilterIF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCosImageFilterIF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCosImageFilterIF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCosImageFilterIF2IF2 in _itkCosImageFilterPython:
_itkCosImageFilterPython.itkCosImageFilterIF2IF2_swigregister(itkCosImageFilterIF2IF2)
itkCosImageFilterIF2IF2___New_orig__ = _itkCosImageFilterPython.itkCosImageFilterIF2IF2___New_orig__
itkCosImageFilterIF2IF2_cast = _itkCosImageFilterPython.itkCosImageFilterIF2IF2_cast


def itkCosImageFilterIF3IF3_New():
    return itkCosImageFilterIF3IF3.New()

class itkCosImageFilterIF3IF3(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF3IF3):
    r"""


    Computes the cosine of each pixel.

    This filter is templated over the pixel type of the input image and
    the pixel type of the output image.

    The filter walks over all of the pixels in the input image, and for
    each pixel does the following:

    cast the pixel value to double,

    apply the std::cos() function to the double value,

    cast the double value resulting from std::cos() to the pixel type of
    the output image,

    store the cast value into the output image.  The filter expects both
    images to have the same dimension (e.g. both 2D, or both 3D, or both
    ND) 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCosImageFilterPython.itkCosImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkCosImageFilterPython.itkCosImageFilterIF3IF3_Clone)
    InputConvertibleToDoubleCheck = _itkCosImageFilterPython.itkCosImageFilterIF3IF3_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkCosImageFilterPython.itkCosImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkCosImageFilterPython.delete_itkCosImageFilterIF3IF3
    cast = _swig_new_static_method(_itkCosImageFilterPython.itkCosImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkCosImageFilterIF3IF3

        Create a new object of the class itkCosImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCosImageFilterIF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCosImageFilterIF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCosImageFilterIF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCosImageFilterIF3IF3 in _itkCosImageFilterPython:
_itkCosImageFilterPython.itkCosImageFilterIF3IF3_swigregister(itkCosImageFilterIF3IF3)
itkCosImageFilterIF3IF3___New_orig__ = _itkCosImageFilterPython.itkCosImageFilterIF3IF3___New_orig__
itkCosImageFilterIF3IF3_cast = _itkCosImageFilterPython.itkCosImageFilterIF3IF3_cast


def itkCosImageFilterIF4IF4_New():
    return itkCosImageFilterIF4IF4.New()

class itkCosImageFilterIF4IF4(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF4IF4):
    r"""


    Computes the cosine of each pixel.

    This filter is templated over the pixel type of the input image and
    the pixel type of the output image.

    The filter walks over all of the pixels in the input image, and for
    each pixel does the following:

    cast the pixel value to double,

    apply the std::cos() function to the double value,

    cast the double value resulting from std::cos() to the pixel type of
    the output image,

    store the cast value into the output image.  The filter expects both
    images to have the same dimension (e.g. both 2D, or both 3D, or both
    ND) 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCosImageFilterPython.itkCosImageFilterIF4IF4___New_orig__)
    Clone = _swig_new_instance_method(_itkCosImageFilterPython.itkCosImageFilterIF4IF4_Clone)
    InputConvertibleToDoubleCheck = _itkCosImageFilterPython.itkCosImageFilterIF4IF4_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkCosImageFilterPython.itkCosImageFilterIF4IF4_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkCosImageFilterPython.delete_itkCosImageFilterIF4IF4
    cast = _swig_new_static_method(_itkCosImageFilterPython.itkCosImageFilterIF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkCosImageFilterIF4IF4

        Create a new object of the class itkCosImageFilterIF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCosImageFilterIF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCosImageFilterIF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCosImageFilterIF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCosImageFilterIF4IF4 in _itkCosImageFilterPython:
_itkCosImageFilterPython.itkCosImageFilterIF4IF4_swigregister(itkCosImageFilterIF4IF4)
itkCosImageFilterIF4IF4___New_orig__ = _itkCosImageFilterPython.itkCosImageFilterIF4IF4___New_orig__
itkCosImageFilterIF4IF4_cast = _itkCosImageFilterPython.itkCosImageFilterIF4IF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def cos_image_filter(*args: itkt.ImageLike, **kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for CosImageFilter"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.CosImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def cos_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKImageIntensity.CosImageFilter
    cos_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    cos_image_filter.__doc__ = filter_object.__doc__




