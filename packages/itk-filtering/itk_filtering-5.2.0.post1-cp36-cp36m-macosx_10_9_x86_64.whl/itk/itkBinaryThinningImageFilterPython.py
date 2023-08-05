# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKBinaryMathematicalMorphologyPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkBinaryThinningImageFilterPython
else:
    import _itkBinaryThinningImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBinaryThinningImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBinaryThinningImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkImageToImageFilterAPython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkImageRegionPython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkOffsetPython
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

def itkBinaryThinningImageFilterISS2ISS2_New():
    return itkBinaryThinningImageFilterISS2ISS2.New()

class itkBinaryThinningImageFilterISS2ISS2(itk.itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    r"""


    This filter computes one-pixel-wide edges of the input image.

    This class is parameterized over the type of the input image and the
    type of the output image.

    The input is assumed to be a binary image. If the foreground pixels of
    the input image do not have a value of 1, they are rescaled to 1
    internally to simplify the computation.

    The filter will produce a skeleton of the object. The output
    background values are 0, and the foreground values are 1.

    This filter is a sequential thinning algorithm and known to be
    computational time dependable on the image size. The algorithm
    corresponds with the 2D implementation described in:

    Rafael C. Gonzales and Richard E. Woods. Digital Image Processing.
    Addison Wesley, 491-494, (1993).

    To do: Make this filter ND.

    See:  MorphologyImageFilter
    example{Filtering/BinaryMathematicalMorphology/ThinImage,Thin Image}

    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_Clone)
    GetThinning = _swig_new_instance_method(_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_GetThinning)
    SameDimensionCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_SameDimensionCheck
    
    InputAdditiveOperatorsCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_InputAdditiveOperatorsCheck
    
    InputConvertibleToIntCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_InputConvertibleToIntCheck
    
    IntConvertibleToInputCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_IntConvertibleToInputCheck
    
    SameTypeCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_SameTypeCheck
    
    __swig_destroy__ = _itkBinaryThinningImageFilterPython.delete_itkBinaryThinningImageFilterISS2ISS2
    cast = _swig_new_static_method(_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryThinningImageFilterISS2ISS2

        Create a new object of the class itkBinaryThinningImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryThinningImageFilterISS2ISS2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBinaryThinningImageFilterISS2ISS2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBinaryThinningImageFilterISS2ISS2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryThinningImageFilterISS2ISS2 in _itkBinaryThinningImageFilterPython:
_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_swigregister(itkBinaryThinningImageFilterISS2ISS2)
itkBinaryThinningImageFilterISS2ISS2___New_orig__ = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2___New_orig__
itkBinaryThinningImageFilterISS2ISS2_cast = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterISS2ISS2_cast


def itkBinaryThinningImageFilterIUC2IUC2_New():
    return itkBinaryThinningImageFilterIUC2IUC2.New()

class itkBinaryThinningImageFilterIUC2IUC2(itk.itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    r"""


    This filter computes one-pixel-wide edges of the input image.

    This class is parameterized over the type of the input image and the
    type of the output image.

    The input is assumed to be a binary image. If the foreground pixels of
    the input image do not have a value of 1, they are rescaled to 1
    internally to simplify the computation.

    The filter will produce a skeleton of the object. The output
    background values are 0, and the foreground values are 1.

    This filter is a sequential thinning algorithm and known to be
    computational time dependable on the image size. The algorithm
    corresponds with the 2D implementation described in:

    Rafael C. Gonzales and Richard E. Woods. Digital Image Processing.
    Addison Wesley, 491-494, (1993).

    To do: Make this filter ND.

    See:  MorphologyImageFilter
    example{Filtering/BinaryMathematicalMorphology/ThinImage,Thin Image}

    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_Clone)
    GetThinning = _swig_new_instance_method(_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_GetThinning)
    SameDimensionCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_SameDimensionCheck
    
    InputAdditiveOperatorsCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_InputAdditiveOperatorsCheck
    
    InputConvertibleToIntCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_InputConvertibleToIntCheck
    
    IntConvertibleToInputCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_IntConvertibleToInputCheck
    
    SameTypeCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_SameTypeCheck
    
    __swig_destroy__ = _itkBinaryThinningImageFilterPython.delete_itkBinaryThinningImageFilterIUC2IUC2
    cast = _swig_new_static_method(_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryThinningImageFilterIUC2IUC2

        Create a new object of the class itkBinaryThinningImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryThinningImageFilterIUC2IUC2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBinaryThinningImageFilterIUC2IUC2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBinaryThinningImageFilterIUC2IUC2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryThinningImageFilterIUC2IUC2 in _itkBinaryThinningImageFilterPython:
_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_swigregister(itkBinaryThinningImageFilterIUC2IUC2)
itkBinaryThinningImageFilterIUC2IUC2___New_orig__ = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2___New_orig__
itkBinaryThinningImageFilterIUC2IUC2_cast = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUC2IUC2_cast


def itkBinaryThinningImageFilterIUS2IUS2_New():
    return itkBinaryThinningImageFilterIUS2IUS2.New()

class itkBinaryThinningImageFilterIUS2IUS2(itk.itkImageToImageFilterAPython.itkImageToImageFilterIUS2IUS2):
    r"""


    This filter computes one-pixel-wide edges of the input image.

    This class is parameterized over the type of the input image and the
    type of the output image.

    The input is assumed to be a binary image. If the foreground pixels of
    the input image do not have a value of 1, they are rescaled to 1
    internally to simplify the computation.

    The filter will produce a skeleton of the object. The output
    background values are 0, and the foreground values are 1.

    This filter is a sequential thinning algorithm and known to be
    computational time dependable on the image size. The algorithm
    corresponds with the 2D implementation described in:

    Rafael C. Gonzales and Richard E. Woods. Digital Image Processing.
    Addison Wesley, 491-494, (1993).

    To do: Make this filter ND.

    See:  MorphologyImageFilter
    example{Filtering/BinaryMathematicalMorphology/ThinImage,Thin Image}

    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_Clone)
    GetThinning = _swig_new_instance_method(_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_GetThinning)
    SameDimensionCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_SameDimensionCheck
    
    InputAdditiveOperatorsCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_InputAdditiveOperatorsCheck
    
    InputConvertibleToIntCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_InputConvertibleToIntCheck
    
    IntConvertibleToInputCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_IntConvertibleToInputCheck
    
    SameTypeCheck = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_SameTypeCheck
    
    __swig_destroy__ = _itkBinaryThinningImageFilterPython.delete_itkBinaryThinningImageFilterIUS2IUS2
    cast = _swig_new_static_method(_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryThinningImageFilterIUS2IUS2

        Create a new object of the class itkBinaryThinningImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryThinningImageFilterIUS2IUS2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBinaryThinningImageFilterIUS2IUS2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBinaryThinningImageFilterIUS2IUS2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryThinningImageFilterIUS2IUS2 in _itkBinaryThinningImageFilterPython:
_itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_swigregister(itkBinaryThinningImageFilterIUS2IUS2)
itkBinaryThinningImageFilterIUS2IUS2___New_orig__ = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2___New_orig__
itkBinaryThinningImageFilterIUS2IUS2_cast = _itkBinaryThinningImageFilterPython.itkBinaryThinningImageFilterIUS2IUS2_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def binary_thinning_image_filter(*args: itkt.ImageLike, **kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for BinaryThinningImageFilter"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.BinaryThinningImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def binary_thinning_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKBinaryMathematicalMorphology.BinaryThinningImageFilter
    binary_thinning_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    binary_thinning_image_filter.__doc__ = filter_object.__doc__




