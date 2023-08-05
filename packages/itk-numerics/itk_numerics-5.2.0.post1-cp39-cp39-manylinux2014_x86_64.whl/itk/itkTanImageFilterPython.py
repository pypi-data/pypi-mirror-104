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
    from . import _itkTanImageFilterPython
else:
    import _itkTanImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkTanImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkTanImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkUnaryGeneratorImageFilterPython
import itk.itkInPlaceImageFilterBPython
import itk.itkImageToImageFilterBPython
import itk.itkImageRegionPython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkImageSourcePython
import itk.itkImagePython
import itk.itkMatrixPython
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkRGBPixelPython
import itk.itkRGBAPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterCommonPython
import itk.itkInPlaceImageFilterAPython
import itk.itkImageToImageFilterAPython

def itkTanImageFilterID2ID2_New():
    return itkTanImageFilterID2ID2.New()

class itkTanImageFilterID2ID2(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID2ID2):
    r"""


    Computes the tangent of each input pixel.

    The computations are performed using std::tan(x). 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTanImageFilterPython.itkTanImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkTanImageFilterPython.itkTanImageFilterID2ID2_Clone)
    InputConvertibleToDoubleCheck = _itkTanImageFilterPython.itkTanImageFilterID2ID2_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkTanImageFilterPython.itkTanImageFilterID2ID2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkTanImageFilterPython.delete_itkTanImageFilterID2ID2
    cast = _swig_new_static_method(_itkTanImageFilterPython.itkTanImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkTanImageFilterID2ID2

        Create a new object of the class itkTanImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTanImageFilterID2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTanImageFilterID2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTanImageFilterID2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTanImageFilterID2ID2 in _itkTanImageFilterPython:
_itkTanImageFilterPython.itkTanImageFilterID2ID2_swigregister(itkTanImageFilterID2ID2)
itkTanImageFilterID2ID2___New_orig__ = _itkTanImageFilterPython.itkTanImageFilterID2ID2___New_orig__
itkTanImageFilterID2ID2_cast = _itkTanImageFilterPython.itkTanImageFilterID2ID2_cast


def itkTanImageFilterID3ID3_New():
    return itkTanImageFilterID3ID3.New()

class itkTanImageFilterID3ID3(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID3ID3):
    r"""


    Computes the tangent of each input pixel.

    The computations are performed using std::tan(x). 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTanImageFilterPython.itkTanImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkTanImageFilterPython.itkTanImageFilterID3ID3_Clone)
    InputConvertibleToDoubleCheck = _itkTanImageFilterPython.itkTanImageFilterID3ID3_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkTanImageFilterPython.itkTanImageFilterID3ID3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkTanImageFilterPython.delete_itkTanImageFilterID3ID3
    cast = _swig_new_static_method(_itkTanImageFilterPython.itkTanImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkTanImageFilterID3ID3

        Create a new object of the class itkTanImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTanImageFilterID3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTanImageFilterID3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTanImageFilterID3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTanImageFilterID3ID3 in _itkTanImageFilterPython:
_itkTanImageFilterPython.itkTanImageFilterID3ID3_swigregister(itkTanImageFilterID3ID3)
itkTanImageFilterID3ID3___New_orig__ = _itkTanImageFilterPython.itkTanImageFilterID3ID3___New_orig__
itkTanImageFilterID3ID3_cast = _itkTanImageFilterPython.itkTanImageFilterID3ID3_cast


def itkTanImageFilterID4ID4_New():
    return itkTanImageFilterID4ID4.New()

class itkTanImageFilterID4ID4(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID4ID4):
    r"""


    Computes the tangent of each input pixel.

    The computations are performed using std::tan(x). 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTanImageFilterPython.itkTanImageFilterID4ID4___New_orig__)
    Clone = _swig_new_instance_method(_itkTanImageFilterPython.itkTanImageFilterID4ID4_Clone)
    InputConvertibleToDoubleCheck = _itkTanImageFilterPython.itkTanImageFilterID4ID4_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkTanImageFilterPython.itkTanImageFilterID4ID4_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkTanImageFilterPython.delete_itkTanImageFilterID4ID4
    cast = _swig_new_static_method(_itkTanImageFilterPython.itkTanImageFilterID4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkTanImageFilterID4ID4

        Create a new object of the class itkTanImageFilterID4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTanImageFilterID4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTanImageFilterID4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTanImageFilterID4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTanImageFilterID4ID4 in _itkTanImageFilterPython:
_itkTanImageFilterPython.itkTanImageFilterID4ID4_swigregister(itkTanImageFilterID4ID4)
itkTanImageFilterID4ID4___New_orig__ = _itkTanImageFilterPython.itkTanImageFilterID4ID4___New_orig__
itkTanImageFilterID4ID4_cast = _itkTanImageFilterPython.itkTanImageFilterID4ID4_cast


def itkTanImageFilterIF2IF2_New():
    return itkTanImageFilterIF2IF2.New()

class itkTanImageFilterIF2IF2(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF2IF2):
    r"""


    Computes the tangent of each input pixel.

    The computations are performed using std::tan(x). 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTanImageFilterPython.itkTanImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkTanImageFilterPython.itkTanImageFilterIF2IF2_Clone)
    InputConvertibleToDoubleCheck = _itkTanImageFilterPython.itkTanImageFilterIF2IF2_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkTanImageFilterPython.itkTanImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkTanImageFilterPython.delete_itkTanImageFilterIF2IF2
    cast = _swig_new_static_method(_itkTanImageFilterPython.itkTanImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkTanImageFilterIF2IF2

        Create a new object of the class itkTanImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTanImageFilterIF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTanImageFilterIF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTanImageFilterIF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTanImageFilterIF2IF2 in _itkTanImageFilterPython:
_itkTanImageFilterPython.itkTanImageFilterIF2IF2_swigregister(itkTanImageFilterIF2IF2)
itkTanImageFilterIF2IF2___New_orig__ = _itkTanImageFilterPython.itkTanImageFilterIF2IF2___New_orig__
itkTanImageFilterIF2IF2_cast = _itkTanImageFilterPython.itkTanImageFilterIF2IF2_cast


def itkTanImageFilterIF3IF3_New():
    return itkTanImageFilterIF3IF3.New()

class itkTanImageFilterIF3IF3(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF3IF3):
    r"""


    Computes the tangent of each input pixel.

    The computations are performed using std::tan(x). 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTanImageFilterPython.itkTanImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkTanImageFilterPython.itkTanImageFilterIF3IF3_Clone)
    InputConvertibleToDoubleCheck = _itkTanImageFilterPython.itkTanImageFilterIF3IF3_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkTanImageFilterPython.itkTanImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkTanImageFilterPython.delete_itkTanImageFilterIF3IF3
    cast = _swig_new_static_method(_itkTanImageFilterPython.itkTanImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkTanImageFilterIF3IF3

        Create a new object of the class itkTanImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTanImageFilterIF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTanImageFilterIF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTanImageFilterIF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTanImageFilterIF3IF3 in _itkTanImageFilterPython:
_itkTanImageFilterPython.itkTanImageFilterIF3IF3_swigregister(itkTanImageFilterIF3IF3)
itkTanImageFilterIF3IF3___New_orig__ = _itkTanImageFilterPython.itkTanImageFilterIF3IF3___New_orig__
itkTanImageFilterIF3IF3_cast = _itkTanImageFilterPython.itkTanImageFilterIF3IF3_cast


def itkTanImageFilterIF4IF4_New():
    return itkTanImageFilterIF4IF4.New()

class itkTanImageFilterIF4IF4(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF4IF4):
    r"""


    Computes the tangent of each input pixel.

    The computations are performed using std::tan(x). 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTanImageFilterPython.itkTanImageFilterIF4IF4___New_orig__)
    Clone = _swig_new_instance_method(_itkTanImageFilterPython.itkTanImageFilterIF4IF4_Clone)
    InputConvertibleToDoubleCheck = _itkTanImageFilterPython.itkTanImageFilterIF4IF4_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkTanImageFilterPython.itkTanImageFilterIF4IF4_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkTanImageFilterPython.delete_itkTanImageFilterIF4IF4
    cast = _swig_new_static_method(_itkTanImageFilterPython.itkTanImageFilterIF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkTanImageFilterIF4IF4

        Create a new object of the class itkTanImageFilterIF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTanImageFilterIF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTanImageFilterIF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTanImageFilterIF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTanImageFilterIF4IF4 in _itkTanImageFilterPython:
_itkTanImageFilterPython.itkTanImageFilterIF4IF4_swigregister(itkTanImageFilterIF4IF4)
itkTanImageFilterIF4IF4___New_orig__ = _itkTanImageFilterPython.itkTanImageFilterIF4IF4___New_orig__
itkTanImageFilterIF4IF4_cast = _itkTanImageFilterPython.itkTanImageFilterIF4IF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def tan_image_filter(*args: itkt.ImageLike, **kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for TanImageFilter"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.TanImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def tan_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKImageIntensity.TanImageFilter
    tan_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    tan_image_filter.__doc__ = filter_object.__doc__




