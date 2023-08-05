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
    from . import _itkVnlHalfHermitianToRealInverseFFTImageFilterPython
else:
    import _itkVnlHalfHermitianToRealInverseFFTImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkHalfHermitianToRealInverseFFTImageFilterPython
import itk.itkImageToImageFilterBPython
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
import itk.itkSimpleDataObjectDecoratorPython
import itk.itkArrayPython

def itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2_New():
    return itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2.New()

class itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2(itk.itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD2ID2):
    r"""


    VNL-based reverse Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   HalfHermitianToRealInverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2_Clone)
    PixelUnsignedIntDivisionOperatorsCheck = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2_PixelUnsignedIntDivisionOperatorsCheck
    
    ImageDimensionsMatchCheck = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2_ImageDimensionsMatchCheck
    
    __swig_destroy__ = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.delete_itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2
    cast = _swig_new_static_method(_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2

        Create a new object of the class itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2 in _itkVnlHalfHermitianToRealInverseFFTImageFilterPython:
_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2_swigregister(itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2)
itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2___New_orig__ = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2___New_orig__
itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2_cast = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD2ID2_cast


def itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3_New():
    return itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3.New()

class itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3(itk.itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD3ID3):
    r"""


    VNL-based reverse Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   HalfHermitianToRealInverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3_Clone)
    PixelUnsignedIntDivisionOperatorsCheck = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3_PixelUnsignedIntDivisionOperatorsCheck
    
    ImageDimensionsMatchCheck = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3_ImageDimensionsMatchCheck
    
    __swig_destroy__ = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.delete_itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3
    cast = _swig_new_static_method(_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3

        Create a new object of the class itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3 in _itkVnlHalfHermitianToRealInverseFFTImageFilterPython:
_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3_swigregister(itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3)
itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3___New_orig__ = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3___New_orig__
itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3_cast = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD3ID3_cast


def itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4_New():
    return itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4.New()

class itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4(itk.itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICD4ID4):
    r"""


    VNL-based reverse Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   HalfHermitianToRealInverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4_Clone)
    PixelUnsignedIntDivisionOperatorsCheck = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4_PixelUnsignedIntDivisionOperatorsCheck
    
    ImageDimensionsMatchCheck = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4_ImageDimensionsMatchCheck
    
    __swig_destroy__ = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.delete_itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4
    cast = _swig_new_static_method(_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4

        Create a new object of the class itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4 in _itkVnlHalfHermitianToRealInverseFFTImageFilterPython:
_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4_swigregister(itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4)
itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4___New_orig__ = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4___New_orig__
itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4_cast = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICD4ID4_cast


def itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2_New():
    return itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2.New()

class itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2(itk.itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF2IF2):
    r"""


    VNL-based reverse Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   HalfHermitianToRealInverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2_Clone)
    PixelUnsignedIntDivisionOperatorsCheck = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2_PixelUnsignedIntDivisionOperatorsCheck
    
    ImageDimensionsMatchCheck = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2_ImageDimensionsMatchCheck
    
    __swig_destroy__ = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.delete_itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2
    cast = _swig_new_static_method(_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2

        Create a new object of the class itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2 in _itkVnlHalfHermitianToRealInverseFFTImageFilterPython:
_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2_swigregister(itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2)
itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2___New_orig__ = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2___New_orig__
itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2_cast = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF2IF2_cast


def itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3_New():
    return itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3.New()

class itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3(itk.itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF3IF3):
    r"""


    VNL-based reverse Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   HalfHermitianToRealInverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3_Clone)
    PixelUnsignedIntDivisionOperatorsCheck = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3_PixelUnsignedIntDivisionOperatorsCheck
    
    ImageDimensionsMatchCheck = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3_ImageDimensionsMatchCheck
    
    __swig_destroy__ = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.delete_itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3
    cast = _swig_new_static_method(_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3

        Create a new object of the class itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3 in _itkVnlHalfHermitianToRealInverseFFTImageFilterPython:
_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3_swigregister(itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3)
itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3___New_orig__ = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3___New_orig__
itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3_cast = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF3IF3_cast


def itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4_New():
    return itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4.New()

class itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4(itk.itkHalfHermitianToRealInverseFFTImageFilterPython.itkHalfHermitianToRealInverseFFTImageFilterICF4IF4):
    r"""


    VNL-based reverse Fast Fourier Transform.

    The input image size must be a multiple of combinations of 2s, 3s,
    and/or 5s in all dimensions (2, 3, and 5 should be the only prime
    factors of the image size along each dimension).

    See:   HalfHermitianToRealInverseFFTImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4___New_orig__)
    Clone = _swig_new_instance_method(_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4_Clone)
    PixelUnsignedIntDivisionOperatorsCheck = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4_PixelUnsignedIntDivisionOperatorsCheck
    
    ImageDimensionsMatchCheck = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4_ImageDimensionsMatchCheck
    
    __swig_destroy__ = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.delete_itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4
    cast = _swig_new_static_method(_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4

        Create a new object of the class itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4 in _itkVnlHalfHermitianToRealInverseFFTImageFilterPython:
_itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4_swigregister(itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4)
itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4___New_orig__ = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4___New_orig__
itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4_cast = _itkVnlHalfHermitianToRealInverseFFTImageFilterPython.itkVnlHalfHermitianToRealInverseFFTImageFilterICF4IF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def vnl_half_hermitian_to_real_inverse_fft_image_filter(*args: itkt.ImageLike,  actual_x_dimension_is_odd_input=..., actual_x_dimension_is_odd: bool=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for VnlHalfHermitianToRealInverseFFTImageFilter"""
    import itk

    kwarg_typehints = { 'actual_x_dimension_is_odd_input':actual_x_dimension_is_odd_input,'actual_x_dimension_is_odd':actual_x_dimension_is_odd }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.VnlHalfHermitianToRealInverseFFTImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def vnl_half_hermitian_to_real_inverse_fft_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKFFT.VnlHalfHermitianToRealInverseFFTImageFilter
    vnl_half_hermitian_to_real_inverse_fft_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    vnl_half_hermitian_to_real_inverse_fft_image_filter.__doc__ = filter_object.__doc__




