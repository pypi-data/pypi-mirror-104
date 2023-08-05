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
    from . import _itkAndImageFilterPython
else:
    import _itkAndImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkAndImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkAndImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkBinaryGeneratorImageFilterPython
import itk.itkSimpleDataObjectDecoratorPython
import itk.itkRGBPixelPython
import itk.itkFixedArrayPython
import itk.pyBasePython
import itk.stdcomplexPython
import itk.ITKCommonBasePython
import itk.itkArrayPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkRGBAPixelPython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.itkVectorPython
import itk.itkImagePython
import itk.itkMatrixPython
import itk.itkPointPython
import itk.vnl_matrix_fixedPython
import itk.itkImageRegionPython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkInPlaceImageFilterBPython
import itk.itkImageToImageFilterBPython
import itk.itkImageSourcePython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterCommonPython
import itk.itkInPlaceImageFilterAPython
import itk.itkImageToImageFilterAPython

def itkAndImageFilterISS2ISS2ISS2_New():
    return itkAndImageFilterISS2ISS2ISS2.New()

class itkAndImageFilterISS2ISS2ISS2(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS2ISS2ISS2):
    r"""


    Implements the AND bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise AND operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be Where "&" is the bitwise
    AND operator in C++. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAndImageFilterPython.itkAndImageFilterISS2ISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkAndImageFilterPython.itkAndImageFilterISS2ISS2ISS2_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkAndImageFilterPython.itkAndImageFilterISS2ISS2ISS2_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkAndImageFilterPython.delete_itkAndImageFilterISS2ISS2ISS2
    cast = _swig_new_static_method(_itkAndImageFilterPython.itkAndImageFilterISS2ISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkAndImageFilterISS2ISS2ISS2

        Create a new object of the class itkAndImageFilterISS2ISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAndImageFilterISS2ISS2ISS2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkAndImageFilterISS2ISS2ISS2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkAndImageFilterISS2ISS2ISS2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAndImageFilterISS2ISS2ISS2 in _itkAndImageFilterPython:
_itkAndImageFilterPython.itkAndImageFilterISS2ISS2ISS2_swigregister(itkAndImageFilterISS2ISS2ISS2)
itkAndImageFilterISS2ISS2ISS2___New_orig__ = _itkAndImageFilterPython.itkAndImageFilterISS2ISS2ISS2___New_orig__
itkAndImageFilterISS2ISS2ISS2_cast = _itkAndImageFilterPython.itkAndImageFilterISS2ISS2ISS2_cast


def itkAndImageFilterISS3ISS3ISS3_New():
    return itkAndImageFilterISS3ISS3ISS3.New()

class itkAndImageFilterISS3ISS3ISS3(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS3ISS3ISS3):
    r"""


    Implements the AND bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise AND operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be Where "&" is the bitwise
    AND operator in C++. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAndImageFilterPython.itkAndImageFilterISS3ISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkAndImageFilterPython.itkAndImageFilterISS3ISS3ISS3_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkAndImageFilterPython.itkAndImageFilterISS3ISS3ISS3_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkAndImageFilterPython.delete_itkAndImageFilterISS3ISS3ISS3
    cast = _swig_new_static_method(_itkAndImageFilterPython.itkAndImageFilterISS3ISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkAndImageFilterISS3ISS3ISS3

        Create a new object of the class itkAndImageFilterISS3ISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAndImageFilterISS3ISS3ISS3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkAndImageFilterISS3ISS3ISS3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkAndImageFilterISS3ISS3ISS3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAndImageFilterISS3ISS3ISS3 in _itkAndImageFilterPython:
_itkAndImageFilterPython.itkAndImageFilterISS3ISS3ISS3_swigregister(itkAndImageFilterISS3ISS3ISS3)
itkAndImageFilterISS3ISS3ISS3___New_orig__ = _itkAndImageFilterPython.itkAndImageFilterISS3ISS3ISS3___New_orig__
itkAndImageFilterISS3ISS3ISS3_cast = _itkAndImageFilterPython.itkAndImageFilterISS3ISS3ISS3_cast


def itkAndImageFilterISS4ISS4ISS4_New():
    return itkAndImageFilterISS4ISS4ISS4.New()

class itkAndImageFilterISS4ISS4ISS4(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS4ISS4ISS4):
    r"""


    Implements the AND bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise AND operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be Where "&" is the bitwise
    AND operator in C++. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAndImageFilterPython.itkAndImageFilterISS4ISS4ISS4___New_orig__)
    Clone = _swig_new_instance_method(_itkAndImageFilterPython.itkAndImageFilterISS4ISS4ISS4_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkAndImageFilterPython.itkAndImageFilterISS4ISS4ISS4_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkAndImageFilterPython.delete_itkAndImageFilterISS4ISS4ISS4
    cast = _swig_new_static_method(_itkAndImageFilterPython.itkAndImageFilterISS4ISS4ISS4_cast)

    def New(*args, **kargs):
        """New() -> itkAndImageFilterISS4ISS4ISS4

        Create a new object of the class itkAndImageFilterISS4ISS4ISS4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAndImageFilterISS4ISS4ISS4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkAndImageFilterISS4ISS4ISS4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkAndImageFilterISS4ISS4ISS4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAndImageFilterISS4ISS4ISS4 in _itkAndImageFilterPython:
_itkAndImageFilterPython.itkAndImageFilterISS4ISS4ISS4_swigregister(itkAndImageFilterISS4ISS4ISS4)
itkAndImageFilterISS4ISS4ISS4___New_orig__ = _itkAndImageFilterPython.itkAndImageFilterISS4ISS4ISS4___New_orig__
itkAndImageFilterISS4ISS4ISS4_cast = _itkAndImageFilterPython.itkAndImageFilterISS4ISS4ISS4_cast


def itkAndImageFilterIUC2IUC2IUC2_New():
    return itkAndImageFilterIUC2IUC2IUC2.New()

class itkAndImageFilterIUC2IUC2IUC2(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC2IUC2IUC2):
    r"""


    Implements the AND bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise AND operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be Where "&" is the bitwise
    AND operator in C++. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAndImageFilterPython.itkAndImageFilterIUC2IUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkAndImageFilterPython.itkAndImageFilterIUC2IUC2IUC2_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkAndImageFilterPython.itkAndImageFilterIUC2IUC2IUC2_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkAndImageFilterPython.delete_itkAndImageFilterIUC2IUC2IUC2
    cast = _swig_new_static_method(_itkAndImageFilterPython.itkAndImageFilterIUC2IUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkAndImageFilterIUC2IUC2IUC2

        Create a new object of the class itkAndImageFilterIUC2IUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAndImageFilterIUC2IUC2IUC2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkAndImageFilterIUC2IUC2IUC2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkAndImageFilterIUC2IUC2IUC2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAndImageFilterIUC2IUC2IUC2 in _itkAndImageFilterPython:
_itkAndImageFilterPython.itkAndImageFilterIUC2IUC2IUC2_swigregister(itkAndImageFilterIUC2IUC2IUC2)
itkAndImageFilterIUC2IUC2IUC2___New_orig__ = _itkAndImageFilterPython.itkAndImageFilterIUC2IUC2IUC2___New_orig__
itkAndImageFilterIUC2IUC2IUC2_cast = _itkAndImageFilterPython.itkAndImageFilterIUC2IUC2IUC2_cast


def itkAndImageFilterIUC3IUC3IUC3_New():
    return itkAndImageFilterIUC3IUC3IUC3.New()

class itkAndImageFilterIUC3IUC3IUC3(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC3IUC3IUC3):
    r"""


    Implements the AND bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise AND operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be Where "&" is the bitwise
    AND operator in C++. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAndImageFilterPython.itkAndImageFilterIUC3IUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkAndImageFilterPython.itkAndImageFilterIUC3IUC3IUC3_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkAndImageFilterPython.itkAndImageFilterIUC3IUC3IUC3_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkAndImageFilterPython.delete_itkAndImageFilterIUC3IUC3IUC3
    cast = _swig_new_static_method(_itkAndImageFilterPython.itkAndImageFilterIUC3IUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkAndImageFilterIUC3IUC3IUC3

        Create a new object of the class itkAndImageFilterIUC3IUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAndImageFilterIUC3IUC3IUC3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkAndImageFilterIUC3IUC3IUC3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkAndImageFilterIUC3IUC3IUC3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAndImageFilterIUC3IUC3IUC3 in _itkAndImageFilterPython:
_itkAndImageFilterPython.itkAndImageFilterIUC3IUC3IUC3_swigregister(itkAndImageFilterIUC3IUC3IUC3)
itkAndImageFilterIUC3IUC3IUC3___New_orig__ = _itkAndImageFilterPython.itkAndImageFilterIUC3IUC3IUC3___New_orig__
itkAndImageFilterIUC3IUC3IUC3_cast = _itkAndImageFilterPython.itkAndImageFilterIUC3IUC3IUC3_cast


def itkAndImageFilterIUC4IUC4IUC4_New():
    return itkAndImageFilterIUC4IUC4IUC4.New()

class itkAndImageFilterIUC4IUC4IUC4(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC4IUC4IUC4):
    r"""


    Implements the AND bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise AND operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be Where "&" is the bitwise
    AND operator in C++. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAndImageFilterPython.itkAndImageFilterIUC4IUC4IUC4___New_orig__)
    Clone = _swig_new_instance_method(_itkAndImageFilterPython.itkAndImageFilterIUC4IUC4IUC4_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkAndImageFilterPython.itkAndImageFilterIUC4IUC4IUC4_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkAndImageFilterPython.delete_itkAndImageFilterIUC4IUC4IUC4
    cast = _swig_new_static_method(_itkAndImageFilterPython.itkAndImageFilterIUC4IUC4IUC4_cast)

    def New(*args, **kargs):
        """New() -> itkAndImageFilterIUC4IUC4IUC4

        Create a new object of the class itkAndImageFilterIUC4IUC4IUC4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAndImageFilterIUC4IUC4IUC4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkAndImageFilterIUC4IUC4IUC4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkAndImageFilterIUC4IUC4IUC4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAndImageFilterIUC4IUC4IUC4 in _itkAndImageFilterPython:
_itkAndImageFilterPython.itkAndImageFilterIUC4IUC4IUC4_swigregister(itkAndImageFilterIUC4IUC4IUC4)
itkAndImageFilterIUC4IUC4IUC4___New_orig__ = _itkAndImageFilterPython.itkAndImageFilterIUC4IUC4IUC4___New_orig__
itkAndImageFilterIUC4IUC4IUC4_cast = _itkAndImageFilterPython.itkAndImageFilterIUC4IUC4IUC4_cast


def itkAndImageFilterIUS2IUS2IUS2_New():
    return itkAndImageFilterIUS2IUS2IUS2.New()

class itkAndImageFilterIUS2IUS2IUS2(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS2IUS2IUS2):
    r"""


    Implements the AND bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise AND operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be Where "&" is the bitwise
    AND operator in C++. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAndImageFilterPython.itkAndImageFilterIUS2IUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkAndImageFilterPython.itkAndImageFilterIUS2IUS2IUS2_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkAndImageFilterPython.itkAndImageFilterIUS2IUS2IUS2_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkAndImageFilterPython.delete_itkAndImageFilterIUS2IUS2IUS2
    cast = _swig_new_static_method(_itkAndImageFilterPython.itkAndImageFilterIUS2IUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkAndImageFilterIUS2IUS2IUS2

        Create a new object of the class itkAndImageFilterIUS2IUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAndImageFilterIUS2IUS2IUS2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkAndImageFilterIUS2IUS2IUS2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkAndImageFilterIUS2IUS2IUS2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAndImageFilterIUS2IUS2IUS2 in _itkAndImageFilterPython:
_itkAndImageFilterPython.itkAndImageFilterIUS2IUS2IUS2_swigregister(itkAndImageFilterIUS2IUS2IUS2)
itkAndImageFilterIUS2IUS2IUS2___New_orig__ = _itkAndImageFilterPython.itkAndImageFilterIUS2IUS2IUS2___New_orig__
itkAndImageFilterIUS2IUS2IUS2_cast = _itkAndImageFilterPython.itkAndImageFilterIUS2IUS2IUS2_cast


def itkAndImageFilterIUS3IUS3IUS3_New():
    return itkAndImageFilterIUS3IUS3IUS3.New()

class itkAndImageFilterIUS3IUS3IUS3(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS3IUS3IUS3):
    r"""


    Implements the AND bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise AND operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be Where "&" is the bitwise
    AND operator in C++. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAndImageFilterPython.itkAndImageFilterIUS3IUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkAndImageFilterPython.itkAndImageFilterIUS3IUS3IUS3_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkAndImageFilterPython.itkAndImageFilterIUS3IUS3IUS3_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkAndImageFilterPython.delete_itkAndImageFilterIUS3IUS3IUS3
    cast = _swig_new_static_method(_itkAndImageFilterPython.itkAndImageFilterIUS3IUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkAndImageFilterIUS3IUS3IUS3

        Create a new object of the class itkAndImageFilterIUS3IUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAndImageFilterIUS3IUS3IUS3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkAndImageFilterIUS3IUS3IUS3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkAndImageFilterIUS3IUS3IUS3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAndImageFilterIUS3IUS3IUS3 in _itkAndImageFilterPython:
_itkAndImageFilterPython.itkAndImageFilterIUS3IUS3IUS3_swigregister(itkAndImageFilterIUS3IUS3IUS3)
itkAndImageFilterIUS3IUS3IUS3___New_orig__ = _itkAndImageFilterPython.itkAndImageFilterIUS3IUS3IUS3___New_orig__
itkAndImageFilterIUS3IUS3IUS3_cast = _itkAndImageFilterPython.itkAndImageFilterIUS3IUS3IUS3_cast


def itkAndImageFilterIUS4IUS4IUS4_New():
    return itkAndImageFilterIUS4IUS4IUS4.New()

class itkAndImageFilterIUS4IUS4IUS4(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS4IUS4IUS4):
    r"""


    Implements the AND bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise AND operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be Where "&" is the bitwise
    AND operator in C++. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAndImageFilterPython.itkAndImageFilterIUS4IUS4IUS4___New_orig__)
    Clone = _swig_new_instance_method(_itkAndImageFilterPython.itkAndImageFilterIUS4IUS4IUS4_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkAndImageFilterPython.itkAndImageFilterIUS4IUS4IUS4_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkAndImageFilterPython.delete_itkAndImageFilterIUS4IUS4IUS4
    cast = _swig_new_static_method(_itkAndImageFilterPython.itkAndImageFilterIUS4IUS4IUS4_cast)

    def New(*args, **kargs):
        """New() -> itkAndImageFilterIUS4IUS4IUS4

        Create a new object of the class itkAndImageFilterIUS4IUS4IUS4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAndImageFilterIUS4IUS4IUS4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkAndImageFilterIUS4IUS4IUS4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkAndImageFilterIUS4IUS4IUS4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAndImageFilterIUS4IUS4IUS4 in _itkAndImageFilterPython:
_itkAndImageFilterPython.itkAndImageFilterIUS4IUS4IUS4_swigregister(itkAndImageFilterIUS4IUS4IUS4)
itkAndImageFilterIUS4IUS4IUS4___New_orig__ = _itkAndImageFilterPython.itkAndImageFilterIUS4IUS4IUS4___New_orig__
itkAndImageFilterIUS4IUS4IUS4_cast = _itkAndImageFilterPython.itkAndImageFilterIUS4IUS4IUS4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def and_image_filter(*args: itkt.ImageLike,  constant1: int=..., constant2: int=..., constant: int=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for AndImageFilter"""
    import itk

    kwarg_typehints = { 'constant1':constant1,'constant2':constant2,'constant':constant }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.AndImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def and_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKImageIntensity.AndImageFilter
    and_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    and_image_filter.__doc__ = filter_object.__doc__




