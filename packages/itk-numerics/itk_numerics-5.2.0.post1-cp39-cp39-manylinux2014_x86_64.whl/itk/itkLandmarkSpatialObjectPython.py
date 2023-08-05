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
    from . import _itkLandmarkSpatialObjectPython
else:
    import _itkLandmarkSpatialObjectPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkLandmarkSpatialObjectPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkLandmarkSpatialObjectPython.SWIG_PyStaticMethod_New

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
import itk.itkPointBasedSpatialObjectPython
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.ITKCommonBasePython
import itk.itkSpatialObjectBasePython
import itk.itkSpatialObjectPropertyPython
import itk.itkRGBAPixelPython
import itk.itkAffineTransformPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkOptimizerParametersPython
import itk.itkArrayPython
import itk.itkArray2DPython
import itk.itkCovariantVectorPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkTransformBasePython
import itk.itkDiffusionTensor3DPython
import itk.itkVariableLengthVectorPython
import itk.itkBoundingBoxPython
import itk.itkMapContainerPython
import itk.itkVectorContainerPython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkSizePython
import itk.itkOffsetPython
import itk.itkImageRegionPython
import itk.itkSpatialObjectPointPython
class listitkLandmarkSpatialObject2_Pointer(collections.abc.MutableSequence):
    r"""Proxy of C++ std::list< itkLandmarkSpatialObject2_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_pop)
    append = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_append)
    empty = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_empty)
    size = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_size)
    swap = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_swap)
    begin = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_begin)
    end = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_end)
    rbegin = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_rend)
    clear = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> listitkLandmarkSpatialObject2_Pointer
        __init__(self, other) -> listitkLandmarkSpatialObject2_Pointer

        Parameters
        ----------
        other: std::list< itkLandmarkSpatialObject2_Pointer > const &

        __init__(self, size) -> listitkLandmarkSpatialObject2_Pointer

        Parameters
        ----------
        size: std::list< itkLandmarkSpatialObject2_Pointer >::size_type

        __init__(self, size, value) -> listitkLandmarkSpatialObject2_Pointer

        Parameters
        ----------
        size: std::list< itkLandmarkSpatialObject2_Pointer >::size_type
        value: std::list< itkLandmarkSpatialObject2_Pointer >::value_type const &

        """
        _itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_swiginit(self, _itkLandmarkSpatialObjectPython.new_listitkLandmarkSpatialObject2_Pointer(*args))
    push_back = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_push_back)
    front = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_front)
    back = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_back)
    assign = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_assign)
    resize = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_resize)
    insert = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_reverse)
    __swig_destroy__ = _itkLandmarkSpatialObjectPython.delete_listitkLandmarkSpatialObject2_Pointer

# Register listitkLandmarkSpatialObject2_Pointer in _itkLandmarkSpatialObjectPython:
_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_swigregister(listitkLandmarkSpatialObject2_Pointer)

class listitkLandmarkSpatialObject3_Pointer(collections.abc.MutableSequence):
    r"""Proxy of C++ std::list< itkLandmarkSpatialObject3_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_pop)
    append = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_append)
    empty = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_empty)
    size = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_size)
    swap = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_swap)
    begin = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_begin)
    end = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_end)
    rbegin = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_rend)
    clear = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> listitkLandmarkSpatialObject3_Pointer
        __init__(self, other) -> listitkLandmarkSpatialObject3_Pointer

        Parameters
        ----------
        other: std::list< itkLandmarkSpatialObject3_Pointer > const &

        __init__(self, size) -> listitkLandmarkSpatialObject3_Pointer

        Parameters
        ----------
        size: std::list< itkLandmarkSpatialObject3_Pointer >::size_type

        __init__(self, size, value) -> listitkLandmarkSpatialObject3_Pointer

        Parameters
        ----------
        size: std::list< itkLandmarkSpatialObject3_Pointer >::size_type
        value: std::list< itkLandmarkSpatialObject3_Pointer >::value_type const &

        """
        _itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_swiginit(self, _itkLandmarkSpatialObjectPython.new_listitkLandmarkSpatialObject3_Pointer(*args))
    push_back = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_push_back)
    front = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_front)
    back = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_back)
    assign = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_assign)
    resize = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_resize)
    insert = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_reverse)
    __swig_destroy__ = _itkLandmarkSpatialObjectPython.delete_listitkLandmarkSpatialObject3_Pointer

# Register listitkLandmarkSpatialObject3_Pointer in _itkLandmarkSpatialObjectPython:
_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_swigregister(listitkLandmarkSpatialObject3_Pointer)

class listitkLandmarkSpatialObject4_Pointer(collections.abc.MutableSequence):
    r"""Proxy of C++ std::list< itkLandmarkSpatialObject4_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_pop)
    append = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_append)
    empty = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_empty)
    size = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_size)
    swap = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_swap)
    begin = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_begin)
    end = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_end)
    rbegin = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_rend)
    clear = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(self) -> listitkLandmarkSpatialObject4_Pointer
        __init__(self, other) -> listitkLandmarkSpatialObject4_Pointer

        Parameters
        ----------
        other: std::list< itkLandmarkSpatialObject4_Pointer > const &

        __init__(self, size) -> listitkLandmarkSpatialObject4_Pointer

        Parameters
        ----------
        size: std::list< itkLandmarkSpatialObject4_Pointer >::size_type

        __init__(self, size, value) -> listitkLandmarkSpatialObject4_Pointer

        Parameters
        ----------
        size: std::list< itkLandmarkSpatialObject4_Pointer >::size_type
        value: std::list< itkLandmarkSpatialObject4_Pointer >::value_type const &

        """
        _itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_swiginit(self, _itkLandmarkSpatialObjectPython.new_listitkLandmarkSpatialObject4_Pointer(*args))
    push_back = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_push_back)
    front = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_front)
    back = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_back)
    assign = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_assign)
    resize = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_resize)
    insert = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_reverse)
    __swig_destroy__ = _itkLandmarkSpatialObjectPython.delete_listitkLandmarkSpatialObject4_Pointer

# Register listitkLandmarkSpatialObject4_Pointer in _itkLandmarkSpatialObjectPython:
_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject4_Pointer_swigregister(listitkLandmarkSpatialObject4_Pointer)


def itkLandmarkSpatialObject2_New():
    return itkLandmarkSpatialObject2.New()

class itkLandmarkSpatialObject2(itk.itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject2):
    r"""


    Representation of a Landmark based on the spatial object classes.

    The Landmark is basically defined by a set of points with spatial
    locations.

    See:   SpatialObjectPoint 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2___New_orig__)
    Clone = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_Clone)
    __swig_destroy__ = _itkLandmarkSpatialObjectPython.delete_itkLandmarkSpatialObject2
    cast = _swig_new_static_method(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_cast)

    def New(*args, **kargs):
        """New() -> itkLandmarkSpatialObject2

        Create a new object of the class itkLandmarkSpatialObject2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLandmarkSpatialObject2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLandmarkSpatialObject2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLandmarkSpatialObject2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLandmarkSpatialObject2 in _itkLandmarkSpatialObjectPython:
_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_swigregister(itkLandmarkSpatialObject2)
itkLandmarkSpatialObject2___New_orig__ = _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2___New_orig__
itkLandmarkSpatialObject2_cast = _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_cast


def itkLandmarkSpatialObject3_New():
    return itkLandmarkSpatialObject3.New()

class itkLandmarkSpatialObject3(itk.itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3):
    r"""


    Representation of a Landmark based on the spatial object classes.

    The Landmark is basically defined by a set of points with spatial
    locations.

    See:   SpatialObjectPoint 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3___New_orig__)
    Clone = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_Clone)
    __swig_destroy__ = _itkLandmarkSpatialObjectPython.delete_itkLandmarkSpatialObject3
    cast = _swig_new_static_method(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_cast)

    def New(*args, **kargs):
        """New() -> itkLandmarkSpatialObject3

        Create a new object of the class itkLandmarkSpatialObject3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLandmarkSpatialObject3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLandmarkSpatialObject3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLandmarkSpatialObject3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLandmarkSpatialObject3 in _itkLandmarkSpatialObjectPython:
_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_swigregister(itkLandmarkSpatialObject3)
itkLandmarkSpatialObject3___New_orig__ = _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3___New_orig__
itkLandmarkSpatialObject3_cast = _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_cast


def itkLandmarkSpatialObject4_New():
    return itkLandmarkSpatialObject4.New()

class itkLandmarkSpatialObject4(itk.itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject4):
    r"""


    Representation of a Landmark based on the spatial object classes.

    The Landmark is basically defined by a set of points with spatial
    locations.

    See:   SpatialObjectPoint 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject4___New_orig__)
    Clone = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject4_Clone)
    __swig_destroy__ = _itkLandmarkSpatialObjectPython.delete_itkLandmarkSpatialObject4
    cast = _swig_new_static_method(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject4_cast)

    def New(*args, **kargs):
        """New() -> itkLandmarkSpatialObject4

        Create a new object of the class itkLandmarkSpatialObject4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLandmarkSpatialObject4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLandmarkSpatialObject4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLandmarkSpatialObject4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLandmarkSpatialObject4 in _itkLandmarkSpatialObjectPython:
_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject4_swigregister(itkLandmarkSpatialObject4)
itkLandmarkSpatialObject4___New_orig__ = _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject4___New_orig__
itkLandmarkSpatialObject4_cast = _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject4_cast



