# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKAnisotropicSmoothingPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkGradientAnisotropicDiffusionImageFilterPython
else:
    import _itkGradientAnisotropicDiffusionImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkGradientAnisotropicDiffusionImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkGradientAnisotropicDiffusionImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkAnisotropicDiffusionImageFilterPython
import itk.itkDenseFiniteDifferenceImageFilterPython
import itk.itkFiniteDifferenceImageFilterPython
import itk.itkInPlaceImageFilterAPython
import itk.itkImageToImageFilterAPython
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
import itk.itkImageToImageFilterBPython
import itk.itkFiniteDifferenceFunctionPython

def itkGradientAnisotropicDiffusionImageFilterID2ID2_New():
    return itkGradientAnisotropicDiffusionImageFilterID2ID2.New()

class itkGradientAnisotropicDiffusionImageFilterID2ID2(itk.itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterID2ID2):
    r"""


    This filter performs anisotropic diffusion on a scalar itk::Image
    using the classic Perona-Malik, gradient magnitude based equation.

    For detailed information on anisotropic diffusion, see
    itkAnisotropicDiffusionFunction and
    itkGradientNDAnisotropicDiffusionFunction.

    Inputs and Outputs The input to this filter should be a scalar
    itk::Image of any dimensionality. The output image will be a diffused
    copy of the input. Parameters Please see the description of parameters
    given in itkAnisotropicDiffusionImageFilter.

    See:   AnisotropicDiffusionImageFilter

    See:  AnisotropicDiffusionFunction

    See:  GradientAnisotropicDiffusionFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID2ID2_Clone)
    UpdateBufferHasNumericTraitsCheck = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID2ID2_UpdateBufferHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientAnisotropicDiffusionImageFilterPython.delete_itkGradientAnisotropicDiffusionImageFilterID2ID2
    cast = _swig_new_static_method(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkGradientAnisotropicDiffusionImageFilterID2ID2

        Create a new object of the class itkGradientAnisotropicDiffusionImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientAnisotropicDiffusionImageFilterID2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGradientAnisotropicDiffusionImageFilterID2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGradientAnisotropicDiffusionImageFilterID2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientAnisotropicDiffusionImageFilterID2ID2 in _itkGradientAnisotropicDiffusionImageFilterPython:
_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID2ID2_swigregister(itkGradientAnisotropicDiffusionImageFilterID2ID2)
itkGradientAnisotropicDiffusionImageFilterID2ID2___New_orig__ = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID2ID2___New_orig__
itkGradientAnisotropicDiffusionImageFilterID2ID2_cast = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID2ID2_cast


def itkGradientAnisotropicDiffusionImageFilterID3ID3_New():
    return itkGradientAnisotropicDiffusionImageFilterID3ID3.New()

class itkGradientAnisotropicDiffusionImageFilterID3ID3(itk.itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterID3ID3):
    r"""


    This filter performs anisotropic diffusion on a scalar itk::Image
    using the classic Perona-Malik, gradient magnitude based equation.

    For detailed information on anisotropic diffusion, see
    itkAnisotropicDiffusionFunction and
    itkGradientNDAnisotropicDiffusionFunction.

    Inputs and Outputs The input to this filter should be a scalar
    itk::Image of any dimensionality. The output image will be a diffused
    copy of the input. Parameters Please see the description of parameters
    given in itkAnisotropicDiffusionImageFilter.

    See:   AnisotropicDiffusionImageFilter

    See:  AnisotropicDiffusionFunction

    See:  GradientAnisotropicDiffusionFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID3ID3_Clone)
    UpdateBufferHasNumericTraitsCheck = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID3ID3_UpdateBufferHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientAnisotropicDiffusionImageFilterPython.delete_itkGradientAnisotropicDiffusionImageFilterID3ID3
    cast = _swig_new_static_method(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkGradientAnisotropicDiffusionImageFilterID3ID3

        Create a new object of the class itkGradientAnisotropicDiffusionImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientAnisotropicDiffusionImageFilterID3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGradientAnisotropicDiffusionImageFilterID3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGradientAnisotropicDiffusionImageFilterID3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientAnisotropicDiffusionImageFilterID3ID3 in _itkGradientAnisotropicDiffusionImageFilterPython:
_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID3ID3_swigregister(itkGradientAnisotropicDiffusionImageFilterID3ID3)
itkGradientAnisotropicDiffusionImageFilterID3ID3___New_orig__ = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID3ID3___New_orig__
itkGradientAnisotropicDiffusionImageFilterID3ID3_cast = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID3ID3_cast


def itkGradientAnisotropicDiffusionImageFilterID4ID4_New():
    return itkGradientAnisotropicDiffusionImageFilterID4ID4.New()

class itkGradientAnisotropicDiffusionImageFilterID4ID4(itk.itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterID4ID4):
    r"""


    This filter performs anisotropic diffusion on a scalar itk::Image
    using the classic Perona-Malik, gradient magnitude based equation.

    For detailed information on anisotropic diffusion, see
    itkAnisotropicDiffusionFunction and
    itkGradientNDAnisotropicDiffusionFunction.

    Inputs and Outputs The input to this filter should be a scalar
    itk::Image of any dimensionality. The output image will be a diffused
    copy of the input. Parameters Please see the description of parameters
    given in itkAnisotropicDiffusionImageFilter.

    See:   AnisotropicDiffusionImageFilter

    See:  AnisotropicDiffusionFunction

    See:  GradientAnisotropicDiffusionFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID4ID4___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID4ID4_Clone)
    UpdateBufferHasNumericTraitsCheck = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID4ID4_UpdateBufferHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientAnisotropicDiffusionImageFilterPython.delete_itkGradientAnisotropicDiffusionImageFilterID4ID4
    cast = _swig_new_static_method(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkGradientAnisotropicDiffusionImageFilterID4ID4

        Create a new object of the class itkGradientAnisotropicDiffusionImageFilterID4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientAnisotropicDiffusionImageFilterID4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGradientAnisotropicDiffusionImageFilterID4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGradientAnisotropicDiffusionImageFilterID4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientAnisotropicDiffusionImageFilterID4ID4 in _itkGradientAnisotropicDiffusionImageFilterPython:
_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID4ID4_swigregister(itkGradientAnisotropicDiffusionImageFilterID4ID4)
itkGradientAnisotropicDiffusionImageFilterID4ID4___New_orig__ = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID4ID4___New_orig__
itkGradientAnisotropicDiffusionImageFilterID4ID4_cast = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterID4ID4_cast


def itkGradientAnisotropicDiffusionImageFilterIF2IF2_New():
    return itkGradientAnisotropicDiffusionImageFilterIF2IF2.New()

class itkGradientAnisotropicDiffusionImageFilterIF2IF2(itk.itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterIF2IF2):
    r"""


    This filter performs anisotropic diffusion on a scalar itk::Image
    using the classic Perona-Malik, gradient magnitude based equation.

    For detailed information on anisotropic diffusion, see
    itkAnisotropicDiffusionFunction and
    itkGradientNDAnisotropicDiffusionFunction.

    Inputs and Outputs The input to this filter should be a scalar
    itk::Image of any dimensionality. The output image will be a diffused
    copy of the input. Parameters Please see the description of parameters
    given in itkAnisotropicDiffusionImageFilter.

    See:   AnisotropicDiffusionImageFilter

    See:  AnisotropicDiffusionFunction

    See:  GradientAnisotropicDiffusionFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2_Clone)
    UpdateBufferHasNumericTraitsCheck = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2_UpdateBufferHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientAnisotropicDiffusionImageFilterPython.delete_itkGradientAnisotropicDiffusionImageFilterIF2IF2
    cast = _swig_new_static_method(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkGradientAnisotropicDiffusionImageFilterIF2IF2

        Create a new object of the class itkGradientAnisotropicDiffusionImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientAnisotropicDiffusionImageFilterIF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGradientAnisotropicDiffusionImageFilterIF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGradientAnisotropicDiffusionImageFilterIF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientAnisotropicDiffusionImageFilterIF2IF2 in _itkGradientAnisotropicDiffusionImageFilterPython:
_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2_swigregister(itkGradientAnisotropicDiffusionImageFilterIF2IF2)
itkGradientAnisotropicDiffusionImageFilterIF2IF2___New_orig__ = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2___New_orig__
itkGradientAnisotropicDiffusionImageFilterIF2IF2_cast = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF2IF2_cast


def itkGradientAnisotropicDiffusionImageFilterIF3IF3_New():
    return itkGradientAnisotropicDiffusionImageFilterIF3IF3.New()

class itkGradientAnisotropicDiffusionImageFilterIF3IF3(itk.itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterIF3IF3):
    r"""


    This filter performs anisotropic diffusion on a scalar itk::Image
    using the classic Perona-Malik, gradient magnitude based equation.

    For detailed information on anisotropic diffusion, see
    itkAnisotropicDiffusionFunction and
    itkGradientNDAnisotropicDiffusionFunction.

    Inputs and Outputs The input to this filter should be a scalar
    itk::Image of any dimensionality. The output image will be a diffused
    copy of the input. Parameters Please see the description of parameters
    given in itkAnisotropicDiffusionImageFilter.

    See:   AnisotropicDiffusionImageFilter

    See:  AnisotropicDiffusionFunction

    See:  GradientAnisotropicDiffusionFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3_Clone)
    UpdateBufferHasNumericTraitsCheck = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3_UpdateBufferHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientAnisotropicDiffusionImageFilterPython.delete_itkGradientAnisotropicDiffusionImageFilterIF3IF3
    cast = _swig_new_static_method(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkGradientAnisotropicDiffusionImageFilterIF3IF3

        Create a new object of the class itkGradientAnisotropicDiffusionImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientAnisotropicDiffusionImageFilterIF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGradientAnisotropicDiffusionImageFilterIF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGradientAnisotropicDiffusionImageFilterIF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientAnisotropicDiffusionImageFilterIF3IF3 in _itkGradientAnisotropicDiffusionImageFilterPython:
_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3_swigregister(itkGradientAnisotropicDiffusionImageFilterIF3IF3)
itkGradientAnisotropicDiffusionImageFilterIF3IF3___New_orig__ = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3___New_orig__
itkGradientAnisotropicDiffusionImageFilterIF3IF3_cast = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF3IF3_cast


def itkGradientAnisotropicDiffusionImageFilterIF4IF4_New():
    return itkGradientAnisotropicDiffusionImageFilterIF4IF4.New()

class itkGradientAnisotropicDiffusionImageFilterIF4IF4(itk.itkAnisotropicDiffusionImageFilterPython.itkAnisotropicDiffusionImageFilterIF4IF4):
    r"""


    This filter performs anisotropic diffusion on a scalar itk::Image
    using the classic Perona-Malik, gradient magnitude based equation.

    For detailed information on anisotropic diffusion, see
    itkAnisotropicDiffusionFunction and
    itkGradientNDAnisotropicDiffusionFunction.

    Inputs and Outputs The input to this filter should be a scalar
    itk::Image of any dimensionality. The output image will be a diffused
    copy of the input. Parameters Please see the description of parameters
    given in itkAnisotropicDiffusionImageFilter.

    See:   AnisotropicDiffusionImageFilter

    See:  AnisotropicDiffusionFunction

    See:  GradientAnisotropicDiffusionFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF4IF4___New_orig__)
    Clone = _swig_new_instance_method(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF4IF4_Clone)
    UpdateBufferHasNumericTraitsCheck = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF4IF4_UpdateBufferHasNumericTraitsCheck
    
    __swig_destroy__ = _itkGradientAnisotropicDiffusionImageFilterPython.delete_itkGradientAnisotropicDiffusionImageFilterIF4IF4
    cast = _swig_new_static_method(_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkGradientAnisotropicDiffusionImageFilterIF4IF4

        Create a new object of the class itkGradientAnisotropicDiffusionImageFilterIF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGradientAnisotropicDiffusionImageFilterIF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGradientAnisotropicDiffusionImageFilterIF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGradientAnisotropicDiffusionImageFilterIF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGradientAnisotropicDiffusionImageFilterIF4IF4 in _itkGradientAnisotropicDiffusionImageFilterPython:
_itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF4IF4_swigregister(itkGradientAnisotropicDiffusionImageFilterIF4IF4)
itkGradientAnisotropicDiffusionImageFilterIF4IF4___New_orig__ = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF4IF4___New_orig__
itkGradientAnisotropicDiffusionImageFilterIF4IF4_cast = _itkGradientAnisotropicDiffusionImageFilterPython.itkGradientAnisotropicDiffusionImageFilterIF4IF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def gradient_anisotropic_diffusion_image_filter(*args: itkt.ImageLike,  time_step: float=..., conductance_parameter: float=..., conductance_scaling_update_interval: int=..., conductance_scaling_parameter: float=..., fixed_average_gradient_magnitude: float=..., difference_function=..., number_of_iterations: int=..., use_image_spacing: bool=..., maximum_rms_error: float=..., rms_change: float=..., manual_reinitialization: bool=..., is_initialized: bool=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for GradientAnisotropicDiffusionImageFilter"""
    import itk

    kwarg_typehints = { 'time_step':time_step,'conductance_parameter':conductance_parameter,'conductance_scaling_update_interval':conductance_scaling_update_interval,'conductance_scaling_parameter':conductance_scaling_parameter,'fixed_average_gradient_magnitude':fixed_average_gradient_magnitude,'difference_function':difference_function,'number_of_iterations':number_of_iterations,'use_image_spacing':use_image_spacing,'maximum_rms_error':maximum_rms_error,'rms_change':rms_change,'manual_reinitialization':manual_reinitialization,'is_initialized':is_initialized }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.GradientAnisotropicDiffusionImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def gradient_anisotropic_diffusion_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKAnisotropicSmoothing.GradientAnisotropicDiffusionImageFilter
    gradient_anisotropic_diffusion_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    gradient_anisotropic_diffusion_image_filter.__doc__ = filter_object.__doc__




