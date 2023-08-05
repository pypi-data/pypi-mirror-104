# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKPathPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkPathBasePython
else:
    import _itkPathBasePython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkPathBasePython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkPathBasePython.SWIG_PyStaticMethod_New

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
import itk.itkContinuousIndexPython
import itk.itkPointPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkIndexPython
import itk.itkSizePython
import itk.itkOffsetPython
class itkPathDCID22(itk.ITKCommonBasePython.itkDataObject):
    r"""


    Represent a path through ND Space.

    This base class is intended to represent a path through an image. As a
    path, it maps a 1D parameter (such as time or arc length, etc) to an
    index (or possibly an offset or a point) in ND space. This mapping is
    done via the abstract Evaluate() method, which must be overridden in
    all instantiable subclasses. The only geometric requirement for a
    gerneral path is that it be continuous. A path may be open or closed,
    and may cross itself several times. A classic application of this
    class is the representation of contours in 2D images using chaincodes
    or freeman codes. Another use of a path is to guide the movement of an
    iterator through an image.

    Parameters:
    -----------

    TInput:  Type of the 1D parameter of the path, e.g. unsigned int or
    double.

    TOutput:  Type of the path location at the given input, e.g.
    itk::Offset< VDimension > or itk::ContinuousIndex< VDimension >

    VDimension:  Dimension of the path.

    See:  Index

    See:  Point

    See:  ContinuousIndex 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    StartOfInput = _swig_new_instance_method(_itkPathBasePython.itkPathDCID22_StartOfInput)
    EndOfInput = _swig_new_instance_method(_itkPathBasePython.itkPathDCID22_EndOfInput)
    Evaluate = _swig_new_instance_method(_itkPathBasePython.itkPathDCID22_Evaluate)
    EvaluateToIndex = _swig_new_instance_method(_itkPathBasePython.itkPathDCID22_EvaluateToIndex)
    IncrementInput = _swig_new_instance_method(_itkPathBasePython.itkPathDCID22_IncrementInput)
    __swig_destroy__ = _itkPathBasePython.delete_itkPathDCID22
    cast = _swig_new_static_method(_itkPathBasePython.itkPathDCID22_cast)

# Register itkPathDCID22 in _itkPathBasePython:
_itkPathBasePython.itkPathDCID22_swigregister(itkPathDCID22)
itkPathDCID22_cast = _itkPathBasePython.itkPathDCID22_cast

class itkPathDCID33(itk.ITKCommonBasePython.itkDataObject):
    r"""


    Represent a path through ND Space.

    This base class is intended to represent a path through an image. As a
    path, it maps a 1D parameter (such as time or arc length, etc) to an
    index (or possibly an offset or a point) in ND space. This mapping is
    done via the abstract Evaluate() method, which must be overridden in
    all instantiable subclasses. The only geometric requirement for a
    gerneral path is that it be continuous. A path may be open or closed,
    and may cross itself several times. A classic application of this
    class is the representation of contours in 2D images using chaincodes
    or freeman codes. Another use of a path is to guide the movement of an
    iterator through an image.

    Parameters:
    -----------

    TInput:  Type of the 1D parameter of the path, e.g. unsigned int or
    double.

    TOutput:  Type of the path location at the given input, e.g.
    itk::Offset< VDimension > or itk::ContinuousIndex< VDimension >

    VDimension:  Dimension of the path.

    See:  Index

    See:  Point

    See:  ContinuousIndex 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    StartOfInput = _swig_new_instance_method(_itkPathBasePython.itkPathDCID33_StartOfInput)
    EndOfInput = _swig_new_instance_method(_itkPathBasePython.itkPathDCID33_EndOfInput)
    Evaluate = _swig_new_instance_method(_itkPathBasePython.itkPathDCID33_Evaluate)
    EvaluateToIndex = _swig_new_instance_method(_itkPathBasePython.itkPathDCID33_EvaluateToIndex)
    IncrementInput = _swig_new_instance_method(_itkPathBasePython.itkPathDCID33_IncrementInput)
    __swig_destroy__ = _itkPathBasePython.delete_itkPathDCID33
    cast = _swig_new_static_method(_itkPathBasePython.itkPathDCID33_cast)

# Register itkPathDCID33 in _itkPathBasePython:
_itkPathBasePython.itkPathDCID33_swigregister(itkPathDCID33)
itkPathDCID33_cast = _itkPathBasePython.itkPathDCID33_cast

class itkPathDCID44(itk.ITKCommonBasePython.itkDataObject):
    r"""


    Represent a path through ND Space.

    This base class is intended to represent a path through an image. As a
    path, it maps a 1D parameter (such as time or arc length, etc) to an
    index (or possibly an offset or a point) in ND space. This mapping is
    done via the abstract Evaluate() method, which must be overridden in
    all instantiable subclasses. The only geometric requirement for a
    gerneral path is that it be continuous. A path may be open or closed,
    and may cross itself several times. A classic application of this
    class is the representation of contours in 2D images using chaincodes
    or freeman codes. Another use of a path is to guide the movement of an
    iterator through an image.

    Parameters:
    -----------

    TInput:  Type of the 1D parameter of the path, e.g. unsigned int or
    double.

    TOutput:  Type of the path location at the given input, e.g.
    itk::Offset< VDimension > or itk::ContinuousIndex< VDimension >

    VDimension:  Dimension of the path.

    See:  Index

    See:  Point

    See:  ContinuousIndex 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    StartOfInput = _swig_new_instance_method(_itkPathBasePython.itkPathDCID44_StartOfInput)
    EndOfInput = _swig_new_instance_method(_itkPathBasePython.itkPathDCID44_EndOfInput)
    Evaluate = _swig_new_instance_method(_itkPathBasePython.itkPathDCID44_Evaluate)
    EvaluateToIndex = _swig_new_instance_method(_itkPathBasePython.itkPathDCID44_EvaluateToIndex)
    IncrementInput = _swig_new_instance_method(_itkPathBasePython.itkPathDCID44_IncrementInput)
    __swig_destroy__ = _itkPathBasePython.delete_itkPathDCID44
    cast = _swig_new_static_method(_itkPathBasePython.itkPathDCID44_cast)

# Register itkPathDCID44 in _itkPathBasePython:
_itkPathBasePython.itkPathDCID44_swigregister(itkPathDCID44)
itkPathDCID44_cast = _itkPathBasePython.itkPathDCID44_cast



