# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKFFTPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkInverseFFTImageFilterPython
else:
    import _itkInverseFFTImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkInverseFFTImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkInverseFFTImageFilterPython.SWIG_PyStaticMethod_New

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

def itkInverseFFTImageFilterICD2ID2_New():
    return itkInverseFFTImageFilterICD2ID2.New()

class itkInverseFFTImageFilterICD2ID2(itk.itkImageToImageFilterBPython.itkImageToImageFilterICD2ID2):
    r"""


    Base class for inverse Fast Fourier Transform.

    This is a base class for the "inverse" or "reverse" Discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child available on the system
    when the object is created via the object factory system.

    This class transforms a full complex image with Hermitian symmetry
    into its real spatial domain representation. If the input does not
    have Hermitian symmetry, the imaginary component is discarded.

    See:   ForwardFFTImageFilter, InverseFFTImageFilter
    example{Filtering/FFT/ComputeInverseFFTOfImage,Compute Inverse FFT Of
    Image} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD2ID2___New_orig__)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD2ID2_GetSizeGreatestPrimeFactor)
    __swig_destroy__ = _itkInverseFFTImageFilterPython.delete_itkInverseFFTImageFilterICD2ID2
    cast = _swig_new_static_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkInverseFFTImageFilterICD2ID2

        Create a new object of the class itkInverseFFTImageFilterICD2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInverseFFTImageFilterICD2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkInverseFFTImageFilterICD2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkInverseFFTImageFilterICD2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkInverseFFTImageFilterICD2ID2 in _itkInverseFFTImageFilterPython:
_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD2ID2_swigregister(itkInverseFFTImageFilterICD2ID2)
itkInverseFFTImageFilterICD2ID2___New_orig__ = _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD2ID2___New_orig__
itkInverseFFTImageFilterICD2ID2_cast = _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD2ID2_cast


def itkInverseFFTImageFilterICD3ID3_New():
    return itkInverseFFTImageFilterICD3ID3.New()

class itkInverseFFTImageFilterICD3ID3(itk.itkImageToImageFilterBPython.itkImageToImageFilterICD3ID3):
    r"""


    Base class for inverse Fast Fourier Transform.

    This is a base class for the "inverse" or "reverse" Discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child available on the system
    when the object is created via the object factory system.

    This class transforms a full complex image with Hermitian symmetry
    into its real spatial domain representation. If the input does not
    have Hermitian symmetry, the imaginary component is discarded.

    See:   ForwardFFTImageFilter, InverseFFTImageFilter
    example{Filtering/FFT/ComputeInverseFFTOfImage,Compute Inverse FFT Of
    Image} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD3ID3___New_orig__)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD3ID3_GetSizeGreatestPrimeFactor)
    __swig_destroy__ = _itkInverseFFTImageFilterPython.delete_itkInverseFFTImageFilterICD3ID3
    cast = _swig_new_static_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkInverseFFTImageFilterICD3ID3

        Create a new object of the class itkInverseFFTImageFilterICD3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInverseFFTImageFilterICD3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkInverseFFTImageFilterICD3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkInverseFFTImageFilterICD3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkInverseFFTImageFilterICD3ID3 in _itkInverseFFTImageFilterPython:
_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD3ID3_swigregister(itkInverseFFTImageFilterICD3ID3)
itkInverseFFTImageFilterICD3ID3___New_orig__ = _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD3ID3___New_orig__
itkInverseFFTImageFilterICD3ID3_cast = _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD3ID3_cast


def itkInverseFFTImageFilterICD4ID4_New():
    return itkInverseFFTImageFilterICD4ID4.New()

class itkInverseFFTImageFilterICD4ID4(itk.itkImageToImageFilterBPython.itkImageToImageFilterICD4ID4):
    r"""


    Base class for inverse Fast Fourier Transform.

    This is a base class for the "inverse" or "reverse" Discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child available on the system
    when the object is created via the object factory system.

    This class transforms a full complex image with Hermitian symmetry
    into its real spatial domain representation. If the input does not
    have Hermitian symmetry, the imaginary component is discarded.

    See:   ForwardFFTImageFilter, InverseFFTImageFilter
    example{Filtering/FFT/ComputeInverseFFTOfImage,Compute Inverse FFT Of
    Image} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD4ID4___New_orig__)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD4ID4_GetSizeGreatestPrimeFactor)
    __swig_destroy__ = _itkInverseFFTImageFilterPython.delete_itkInverseFFTImageFilterICD4ID4
    cast = _swig_new_static_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkInverseFFTImageFilterICD4ID4

        Create a new object of the class itkInverseFFTImageFilterICD4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInverseFFTImageFilterICD4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkInverseFFTImageFilterICD4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkInverseFFTImageFilterICD4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkInverseFFTImageFilterICD4ID4 in _itkInverseFFTImageFilterPython:
_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD4ID4_swigregister(itkInverseFFTImageFilterICD4ID4)
itkInverseFFTImageFilterICD4ID4___New_orig__ = _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD4ID4___New_orig__
itkInverseFFTImageFilterICD4ID4_cast = _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICD4ID4_cast


def itkInverseFFTImageFilterICF2IF2_New():
    return itkInverseFFTImageFilterICF2IF2.New()

class itkInverseFFTImageFilterICF2IF2(itk.itkImageToImageFilterBPython.itkImageToImageFilterICF2IF2):
    r"""


    Base class for inverse Fast Fourier Transform.

    This is a base class for the "inverse" or "reverse" Discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child available on the system
    when the object is created via the object factory system.

    This class transforms a full complex image with Hermitian symmetry
    into its real spatial domain representation. If the input does not
    have Hermitian symmetry, the imaginary component is discarded.

    See:   ForwardFFTImageFilter, InverseFFTImageFilter
    example{Filtering/FFT/ComputeInverseFFTOfImage,Compute Inverse FFT Of
    Image} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2___New_orig__)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2_GetSizeGreatestPrimeFactor)
    __swig_destroy__ = _itkInverseFFTImageFilterPython.delete_itkInverseFFTImageFilterICF2IF2
    cast = _swig_new_static_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkInverseFFTImageFilterICF2IF2

        Create a new object of the class itkInverseFFTImageFilterICF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInverseFFTImageFilterICF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkInverseFFTImageFilterICF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkInverseFFTImageFilterICF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkInverseFFTImageFilterICF2IF2 in _itkInverseFFTImageFilterPython:
_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2_swigregister(itkInverseFFTImageFilterICF2IF2)
itkInverseFFTImageFilterICF2IF2___New_orig__ = _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2___New_orig__
itkInverseFFTImageFilterICF2IF2_cast = _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF2IF2_cast


def itkInverseFFTImageFilterICF3IF3_New():
    return itkInverseFFTImageFilterICF3IF3.New()

class itkInverseFFTImageFilterICF3IF3(itk.itkImageToImageFilterBPython.itkImageToImageFilterICF3IF3):
    r"""


    Base class for inverse Fast Fourier Transform.

    This is a base class for the "inverse" or "reverse" Discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child available on the system
    when the object is created via the object factory system.

    This class transforms a full complex image with Hermitian symmetry
    into its real spatial domain representation. If the input does not
    have Hermitian symmetry, the imaginary component is discarded.

    See:   ForwardFFTImageFilter, InverseFFTImageFilter
    example{Filtering/FFT/ComputeInverseFFTOfImage,Compute Inverse FFT Of
    Image} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3___New_orig__)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3_GetSizeGreatestPrimeFactor)
    __swig_destroy__ = _itkInverseFFTImageFilterPython.delete_itkInverseFFTImageFilterICF3IF3
    cast = _swig_new_static_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkInverseFFTImageFilterICF3IF3

        Create a new object of the class itkInverseFFTImageFilterICF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInverseFFTImageFilterICF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkInverseFFTImageFilterICF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkInverseFFTImageFilterICF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkInverseFFTImageFilterICF3IF3 in _itkInverseFFTImageFilterPython:
_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3_swigregister(itkInverseFFTImageFilterICF3IF3)
itkInverseFFTImageFilterICF3IF3___New_orig__ = _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3___New_orig__
itkInverseFFTImageFilterICF3IF3_cast = _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF3IF3_cast


def itkInverseFFTImageFilterICF4IF4_New():
    return itkInverseFFTImageFilterICF4IF4.New()

class itkInverseFFTImageFilterICF4IF4(itk.itkImageToImageFilterBPython.itkImageToImageFilterICF4IF4):
    r"""


    Base class for inverse Fast Fourier Transform.

    This is a base class for the "inverse" or "reverse" Discrete
    Fourier Transform. This is an abstract base class: the actual
    implementation is provided by the best child available on the system
    when the object is created via the object factory system.

    This class transforms a full complex image with Hermitian symmetry
    into its real spatial domain representation. If the input does not
    have Hermitian symmetry, the imaginary component is discarded.

    See:   ForwardFFTImageFilter, InverseFFTImageFilter
    example{Filtering/FFT/ComputeInverseFFTOfImage,Compute Inverse FFT Of
    Image} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF4IF4___New_orig__)
    GetSizeGreatestPrimeFactor = _swig_new_instance_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF4IF4_GetSizeGreatestPrimeFactor)
    __swig_destroy__ = _itkInverseFFTImageFilterPython.delete_itkInverseFFTImageFilterICF4IF4
    cast = _swig_new_static_method(_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkInverseFFTImageFilterICF4IF4

        Create a new object of the class itkInverseFFTImageFilterICF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInverseFFTImageFilterICF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkInverseFFTImageFilterICF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkInverseFFTImageFilterICF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkInverseFFTImageFilterICF4IF4 in _itkInverseFFTImageFilterPython:
_itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF4IF4_swigregister(itkInverseFFTImageFilterICF4IF4)
itkInverseFFTImageFilterICF4IF4___New_orig__ = _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF4IF4___New_orig__
itkInverseFFTImageFilterICF4IF4_cast = _itkInverseFFTImageFilterPython.itkInverseFFTImageFilterICF4IF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def inverse_fft_image_filter(*args: itkt.ImageLike, **kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for InverseFFTImageFilter"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.InverseFFTImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def inverse_fft_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKFFT.InverseFFTImageFilter
    inverse_fft_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    inverse_fft_image_filter.__doc__ = filter_object.__doc__




