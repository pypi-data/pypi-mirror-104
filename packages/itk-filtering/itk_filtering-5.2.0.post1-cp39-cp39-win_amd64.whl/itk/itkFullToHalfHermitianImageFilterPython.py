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
    from . import _itkFullToHalfHermitianImageFilterPython
else:
    import _itkFullToHalfHermitianImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkFullToHalfHermitianImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkFullToHalfHermitianImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkImageToImageFilterBPython
import itk.itkImageRegionPython
import itk.itkSizePython
import itk.pyBasePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.ITKCommonBasePython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.stdcomplexPython
import itk.itkImagePython
import itk.itkVectorPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkPointPython
import itk.itkRGBPixelPython
import itk.itkRGBAPixelPython
import itk.itkSimpleDataObjectDecoratorPython
import itk.itkArrayPython

def itkFullToHalfHermitianImageFilterICD2_New():
    return itkFullToHalfHermitianImageFilterICD2.New()

class itkFullToHalfHermitianImageFilterICD2(itk.itkImageToImageFilterBPython.itkImageToImageFilterICD2ICD2):
    r"""


    Reduces the size of a full complex image produced from a forward
    discrete Fourier transform of a real image to only the non-redundant
    half of the image.

    In particular, this filter reduces the size of the image in the first
    dimension to $\\lfloor N/2 \\rfloor + 1 $.

    See:   HalfToFullHermitianImageFilter

    See:   ForwardFFTImageFilter

    See:   InverseFFTImageFilter

    See:   RealToHalfHermitianForwardFFTImageFilter

    See:   HalfHermitianToRealInverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD2___New_orig__)
    Clone = _swig_new_instance_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD2_Clone)
    GetActualXDimensionIsOddOutput = _swig_new_instance_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD2_GetActualXDimensionIsOddOutput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD2_GetActualXDimensionIsOdd)
    __swig_destroy__ = _itkFullToHalfHermitianImageFilterPython.delete_itkFullToHalfHermitianImageFilterICD2
    cast = _swig_new_static_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD2_cast)

    def New(*args, **kargs):
        """New() -> itkFullToHalfHermitianImageFilterICD2

        Create a new object of the class itkFullToHalfHermitianImageFilterICD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFullToHalfHermitianImageFilterICD2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFullToHalfHermitianImageFilterICD2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFullToHalfHermitianImageFilterICD2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFullToHalfHermitianImageFilterICD2 in _itkFullToHalfHermitianImageFilterPython:
_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD2_swigregister(itkFullToHalfHermitianImageFilterICD2)
itkFullToHalfHermitianImageFilterICD2___New_orig__ = _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD2___New_orig__
itkFullToHalfHermitianImageFilterICD2_cast = _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD2_cast


def itkFullToHalfHermitianImageFilterICD3_New():
    return itkFullToHalfHermitianImageFilterICD3.New()

class itkFullToHalfHermitianImageFilterICD3(itk.itkImageToImageFilterBPython.itkImageToImageFilterICD3ICD3):
    r"""


    Reduces the size of a full complex image produced from a forward
    discrete Fourier transform of a real image to only the non-redundant
    half of the image.

    In particular, this filter reduces the size of the image in the first
    dimension to $\\lfloor N/2 \\rfloor + 1 $.

    See:   HalfToFullHermitianImageFilter

    See:   ForwardFFTImageFilter

    See:   InverseFFTImageFilter

    See:   RealToHalfHermitianForwardFFTImageFilter

    See:   HalfHermitianToRealInverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD3___New_orig__)
    Clone = _swig_new_instance_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD3_Clone)
    GetActualXDimensionIsOddOutput = _swig_new_instance_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD3_GetActualXDimensionIsOddOutput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD3_GetActualXDimensionIsOdd)
    __swig_destroy__ = _itkFullToHalfHermitianImageFilterPython.delete_itkFullToHalfHermitianImageFilterICD3
    cast = _swig_new_static_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD3_cast)

    def New(*args, **kargs):
        """New() -> itkFullToHalfHermitianImageFilterICD3

        Create a new object of the class itkFullToHalfHermitianImageFilterICD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFullToHalfHermitianImageFilterICD3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFullToHalfHermitianImageFilterICD3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFullToHalfHermitianImageFilterICD3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFullToHalfHermitianImageFilterICD3 in _itkFullToHalfHermitianImageFilterPython:
_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD3_swigregister(itkFullToHalfHermitianImageFilterICD3)
itkFullToHalfHermitianImageFilterICD3___New_orig__ = _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD3___New_orig__
itkFullToHalfHermitianImageFilterICD3_cast = _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD3_cast


def itkFullToHalfHermitianImageFilterICD4_New():
    return itkFullToHalfHermitianImageFilterICD4.New()

class itkFullToHalfHermitianImageFilterICD4(itk.itkImageToImageFilterBPython.itkImageToImageFilterICD4ICD4):
    r"""


    Reduces the size of a full complex image produced from a forward
    discrete Fourier transform of a real image to only the non-redundant
    half of the image.

    In particular, this filter reduces the size of the image in the first
    dimension to $\\lfloor N/2 \\rfloor + 1 $.

    See:   HalfToFullHermitianImageFilter

    See:   ForwardFFTImageFilter

    See:   InverseFFTImageFilter

    See:   RealToHalfHermitianForwardFFTImageFilter

    See:   HalfHermitianToRealInverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD4___New_orig__)
    Clone = _swig_new_instance_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD4_Clone)
    GetActualXDimensionIsOddOutput = _swig_new_instance_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD4_GetActualXDimensionIsOddOutput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD4_GetActualXDimensionIsOdd)
    __swig_destroy__ = _itkFullToHalfHermitianImageFilterPython.delete_itkFullToHalfHermitianImageFilterICD4
    cast = _swig_new_static_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD4_cast)

    def New(*args, **kargs):
        """New() -> itkFullToHalfHermitianImageFilterICD4

        Create a new object of the class itkFullToHalfHermitianImageFilterICD4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFullToHalfHermitianImageFilterICD4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFullToHalfHermitianImageFilterICD4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFullToHalfHermitianImageFilterICD4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFullToHalfHermitianImageFilterICD4 in _itkFullToHalfHermitianImageFilterPython:
_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD4_swigregister(itkFullToHalfHermitianImageFilterICD4)
itkFullToHalfHermitianImageFilterICD4___New_orig__ = _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD4___New_orig__
itkFullToHalfHermitianImageFilterICD4_cast = _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICD4_cast


def itkFullToHalfHermitianImageFilterICF2_New():
    return itkFullToHalfHermitianImageFilterICF2.New()

class itkFullToHalfHermitianImageFilterICF2(itk.itkImageToImageFilterBPython.itkImageToImageFilterICF2ICF2):
    r"""


    Reduces the size of a full complex image produced from a forward
    discrete Fourier transform of a real image to only the non-redundant
    half of the image.

    In particular, this filter reduces the size of the image in the first
    dimension to $\\lfloor N/2 \\rfloor + 1 $.

    See:   HalfToFullHermitianImageFilter

    See:   ForwardFFTImageFilter

    See:   InverseFFTImageFilter

    See:   RealToHalfHermitianForwardFFTImageFilter

    See:   HalfHermitianToRealInverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2___New_orig__)
    Clone = _swig_new_instance_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2_Clone)
    GetActualXDimensionIsOddOutput = _swig_new_instance_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2_GetActualXDimensionIsOddOutput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2_GetActualXDimensionIsOdd)
    __swig_destroy__ = _itkFullToHalfHermitianImageFilterPython.delete_itkFullToHalfHermitianImageFilterICF2
    cast = _swig_new_static_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2_cast)

    def New(*args, **kargs):
        """New() -> itkFullToHalfHermitianImageFilterICF2

        Create a new object of the class itkFullToHalfHermitianImageFilterICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFullToHalfHermitianImageFilterICF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFullToHalfHermitianImageFilterICF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFullToHalfHermitianImageFilterICF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFullToHalfHermitianImageFilterICF2 in _itkFullToHalfHermitianImageFilterPython:
_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2_swigregister(itkFullToHalfHermitianImageFilterICF2)
itkFullToHalfHermitianImageFilterICF2___New_orig__ = _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2___New_orig__
itkFullToHalfHermitianImageFilterICF2_cast = _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF2_cast


def itkFullToHalfHermitianImageFilterICF3_New():
    return itkFullToHalfHermitianImageFilterICF3.New()

class itkFullToHalfHermitianImageFilterICF3(itk.itkImageToImageFilterBPython.itkImageToImageFilterICF3ICF3):
    r"""


    Reduces the size of a full complex image produced from a forward
    discrete Fourier transform of a real image to only the non-redundant
    half of the image.

    In particular, this filter reduces the size of the image in the first
    dimension to $\\lfloor N/2 \\rfloor + 1 $.

    See:   HalfToFullHermitianImageFilter

    See:   ForwardFFTImageFilter

    See:   InverseFFTImageFilter

    See:   RealToHalfHermitianForwardFFTImageFilter

    See:   HalfHermitianToRealInverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3___New_orig__)
    Clone = _swig_new_instance_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3_Clone)
    GetActualXDimensionIsOddOutput = _swig_new_instance_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3_GetActualXDimensionIsOddOutput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3_GetActualXDimensionIsOdd)
    __swig_destroy__ = _itkFullToHalfHermitianImageFilterPython.delete_itkFullToHalfHermitianImageFilterICF3
    cast = _swig_new_static_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3_cast)

    def New(*args, **kargs):
        """New() -> itkFullToHalfHermitianImageFilterICF3

        Create a new object of the class itkFullToHalfHermitianImageFilterICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFullToHalfHermitianImageFilterICF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFullToHalfHermitianImageFilterICF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFullToHalfHermitianImageFilterICF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFullToHalfHermitianImageFilterICF3 in _itkFullToHalfHermitianImageFilterPython:
_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3_swigregister(itkFullToHalfHermitianImageFilterICF3)
itkFullToHalfHermitianImageFilterICF3___New_orig__ = _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3___New_orig__
itkFullToHalfHermitianImageFilterICF3_cast = _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF3_cast


def itkFullToHalfHermitianImageFilterICF4_New():
    return itkFullToHalfHermitianImageFilterICF4.New()

class itkFullToHalfHermitianImageFilterICF4(itk.itkImageToImageFilterBPython.itkImageToImageFilterICF4ICF4):
    r"""


    Reduces the size of a full complex image produced from a forward
    discrete Fourier transform of a real image to only the non-redundant
    half of the image.

    In particular, this filter reduces the size of the image in the first
    dimension to $\\lfloor N/2 \\rfloor + 1 $.

    See:   HalfToFullHermitianImageFilter

    See:   ForwardFFTImageFilter

    See:   InverseFFTImageFilter

    See:   RealToHalfHermitianForwardFFTImageFilter

    See:   HalfHermitianToRealInverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF4___New_orig__)
    Clone = _swig_new_instance_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF4_Clone)
    GetActualXDimensionIsOddOutput = _swig_new_instance_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF4_GetActualXDimensionIsOddOutput)
    GetActualXDimensionIsOdd = _swig_new_instance_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF4_GetActualXDimensionIsOdd)
    __swig_destroy__ = _itkFullToHalfHermitianImageFilterPython.delete_itkFullToHalfHermitianImageFilterICF4
    cast = _swig_new_static_method(_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF4_cast)

    def New(*args, **kargs):
        """New() -> itkFullToHalfHermitianImageFilterICF4

        Create a new object of the class itkFullToHalfHermitianImageFilterICF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFullToHalfHermitianImageFilterICF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFullToHalfHermitianImageFilterICF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFullToHalfHermitianImageFilterICF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFullToHalfHermitianImageFilterICF4 in _itkFullToHalfHermitianImageFilterPython:
_itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF4_swigregister(itkFullToHalfHermitianImageFilterICF4)
itkFullToHalfHermitianImageFilterICF4___New_orig__ = _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF4___New_orig__
itkFullToHalfHermitianImageFilterICF4_cast = _itkFullToHalfHermitianImageFilterPython.itkFullToHalfHermitianImageFilterICF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def full_to_half_hermitian_image_filter(*args: itkt.ImageLike, **kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for FullToHalfHermitianImageFilter"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.FullToHalfHermitianImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def full_to_half_hermitian_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKFFT.FullToHalfHermitianImageFilter
    full_to_half_hermitian_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    full_to_half_hermitian_image_filter.__doc__ = filter_object.__doc__




