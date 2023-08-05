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
    from . import _itkPathSourcePython
else:
    import _itkPathSourcePython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkPathSourcePython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkPathSourcePython.SWIG_PyStaticMethod_New

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
import itk.itkPolyLineParametricPathPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkFixedArrayPython
import itk.itkParametricPathPython
import itk.itkPathBasePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkContinuousIndexPython
import itk.itkPointPython
import itk.itkVectorContainerPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython

def itkPathSourcePLPP2_New():
    return itkPathSourcePLPP2.New()

class itkPathSourcePLPP2(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    Base class for all process objects that output path data.

    PathSource is the base class for all process objects that output path
    data. Specifically, this class defines the GetOutput() method that
    returns a pointer to the output path. The class also defines some
    internal private data members that are used to manage streaming of
    data. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPathSourcePython.itkPathSourcePLPP2___New_orig__)
    Clone = _swig_new_instance_method(_itkPathSourcePython.itkPathSourcePLPP2_Clone)
    GetOutput = _swig_new_instance_method(_itkPathSourcePython.itkPathSourcePLPP2_GetOutput)
    GraftOutput = _swig_new_instance_method(_itkPathSourcePython.itkPathSourcePLPP2_GraftOutput)
    GraftNthOutput = _swig_new_instance_method(_itkPathSourcePython.itkPathSourcePLPP2_GraftNthOutput)
    __swig_destroy__ = _itkPathSourcePython.delete_itkPathSourcePLPP2
    cast = _swig_new_static_method(_itkPathSourcePython.itkPathSourcePLPP2_cast)

    def New(*args, **kargs):
        """New() -> itkPathSourcePLPP2

        Create a new object of the class itkPathSourcePLPP2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPathSourcePLPP2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPathSourcePLPP2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPathSourcePLPP2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPathSourcePLPP2 in _itkPathSourcePython:
_itkPathSourcePython.itkPathSourcePLPP2_swigregister(itkPathSourcePLPP2)
itkPathSourcePLPP2___New_orig__ = _itkPathSourcePython.itkPathSourcePLPP2___New_orig__
itkPathSourcePLPP2_cast = _itkPathSourcePython.itkPathSourcePLPP2_cast


def itkPathSourcePLPP3_New():
    return itkPathSourcePLPP3.New()

class itkPathSourcePLPP3(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    Base class for all process objects that output path data.

    PathSource is the base class for all process objects that output path
    data. Specifically, this class defines the GetOutput() method that
    returns a pointer to the output path. The class also defines some
    internal private data members that are used to manage streaming of
    data. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPathSourcePython.itkPathSourcePLPP3___New_orig__)
    Clone = _swig_new_instance_method(_itkPathSourcePython.itkPathSourcePLPP3_Clone)
    GetOutput = _swig_new_instance_method(_itkPathSourcePython.itkPathSourcePLPP3_GetOutput)
    GraftOutput = _swig_new_instance_method(_itkPathSourcePython.itkPathSourcePLPP3_GraftOutput)
    GraftNthOutput = _swig_new_instance_method(_itkPathSourcePython.itkPathSourcePLPP3_GraftNthOutput)
    __swig_destroy__ = _itkPathSourcePython.delete_itkPathSourcePLPP3
    cast = _swig_new_static_method(_itkPathSourcePython.itkPathSourcePLPP3_cast)

    def New(*args, **kargs):
        """New() -> itkPathSourcePLPP3

        Create a new object of the class itkPathSourcePLPP3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPathSourcePLPP3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPathSourcePLPP3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPathSourcePLPP3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPathSourcePLPP3 in _itkPathSourcePython:
_itkPathSourcePython.itkPathSourcePLPP3_swigregister(itkPathSourcePLPP3)
itkPathSourcePLPP3___New_orig__ = _itkPathSourcePython.itkPathSourcePLPP3___New_orig__
itkPathSourcePLPP3_cast = _itkPathSourcePython.itkPathSourcePLPP3_cast


def itkPathSourcePLPP4_New():
    return itkPathSourcePLPP4.New()

class itkPathSourcePLPP4(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    Base class for all process objects that output path data.

    PathSource is the base class for all process objects that output path
    data. Specifically, this class defines the GetOutput() method that
    returns a pointer to the output path. The class also defines some
    internal private data members that are used to manage streaming of
    data. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPathSourcePython.itkPathSourcePLPP4___New_orig__)
    Clone = _swig_new_instance_method(_itkPathSourcePython.itkPathSourcePLPP4_Clone)
    GetOutput = _swig_new_instance_method(_itkPathSourcePython.itkPathSourcePLPP4_GetOutput)
    GraftOutput = _swig_new_instance_method(_itkPathSourcePython.itkPathSourcePLPP4_GraftOutput)
    GraftNthOutput = _swig_new_instance_method(_itkPathSourcePython.itkPathSourcePLPP4_GraftNthOutput)
    __swig_destroy__ = _itkPathSourcePython.delete_itkPathSourcePLPP4
    cast = _swig_new_static_method(_itkPathSourcePython.itkPathSourcePLPP4_cast)

    def New(*args, **kargs):
        """New() -> itkPathSourcePLPP4

        Create a new object of the class itkPathSourcePLPP4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPathSourcePLPP4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPathSourcePLPP4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPathSourcePLPP4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPathSourcePLPP4 in _itkPathSourcePython:
_itkPathSourcePython.itkPathSourcePLPP4_swigregister(itkPathSourcePLPP4)
itkPathSourcePLPP4___New_orig__ = _itkPathSourcePython.itkPathSourcePLPP4___New_orig__
itkPathSourcePLPP4_cast = _itkPathSourcePython.itkPathSourcePLPP4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def path_source(*args, **kwargs):
    """Functional interface for PathSource"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.PathSource.New(*args, **kwargs)
    return instance.__internal_call__()

def path_source_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKPath.PathSource
    path_source.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    path_source.__doc__ = filter_object.__doc__




