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
    from . import _itkBinaryOpeningByReconstructionImageFilterPython
else:
    import _itkBinaryOpeningByReconstructionImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBinaryOpeningByReconstructionImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBinaryOpeningByReconstructionImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkFlatStructuringElementPython
import itk.itkNeighborhoodPython
import itk.itkRGBPixelPython
import itk.itkFixedArrayPython
import itk.pyBasePython
import itk.ITKCommonBasePython
import itk.itkSizePython
import itk.itkOffsetPython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkVectorPython
import itk.itkImagePython
import itk.itkMatrixPython
import itk.itkPointPython
import itk.vnl_matrix_fixedPython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkRGBAPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkBoxImageFilterPython
import itk.itkImageToImageFilterAPython
import itk.itkImageSourcePython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterCommonPython

def itkBinaryOpeningByReconstructionImageFilterIUC2SE2_New():
    return itkBinaryOpeningByReconstructionImageFilterIUC2SE2.New()

class itkBinaryOpeningByReconstructionImageFilterIUC2SE2(itk.itkFlatStructuringElementPython.itkKernelImageFilterIUC2IUC2SE2):
    r"""


    binary morphological closing of an image.

    This filter removes small (i.e., smaller than the structuring element)
    objects in the image. It is defined as: Opening(f) =
    ReconstructionByDilatation(Erosion(f)).

    The structuring element is assumed to be composed of binary values
    (zero or one). Only elements of the structuring element having values
    > 0 are candidates for affecting the center pixel.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:  MorphologyImageFilter, OpeningByReconstructionImageFilter,
    BinaryClosingByReconstructionImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_Clone)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_GetForegroundValue)
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_GetBackgroundValue)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_FullyConnectedOff)
    __swig_destroy__ = _itkBinaryOpeningByReconstructionImageFilterPython.delete_itkBinaryOpeningByReconstructionImageFilterIUC2SE2
    cast = _swig_new_static_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryOpeningByReconstructionImageFilterIUC2SE2

        Create a new object of the class itkBinaryOpeningByReconstructionImageFilterIUC2SE2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryOpeningByReconstructionImageFilterIUC2SE2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBinaryOpeningByReconstructionImageFilterIUC2SE2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBinaryOpeningByReconstructionImageFilterIUC2SE2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryOpeningByReconstructionImageFilterIUC2SE2 in _itkBinaryOpeningByReconstructionImageFilterPython:
_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_swigregister(itkBinaryOpeningByReconstructionImageFilterIUC2SE2)
itkBinaryOpeningByReconstructionImageFilterIUC2SE2___New_orig__ = _itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2___New_orig__
itkBinaryOpeningByReconstructionImageFilterIUC2SE2_cast = _itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC2SE2_cast


def itkBinaryOpeningByReconstructionImageFilterIUC3SE3_New():
    return itkBinaryOpeningByReconstructionImageFilterIUC3SE3.New()

class itkBinaryOpeningByReconstructionImageFilterIUC3SE3(itk.itkFlatStructuringElementPython.itkKernelImageFilterIUC3IUC3SE3):
    r"""


    binary morphological closing of an image.

    This filter removes small (i.e., smaller than the structuring element)
    objects in the image. It is defined as: Opening(f) =
    ReconstructionByDilatation(Erosion(f)).

    The structuring element is assumed to be composed of binary values
    (zero or one). Only elements of the structuring element having values
    > 0 are candidates for affecting the center pixel.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:  MorphologyImageFilter, OpeningByReconstructionImageFilter,
    BinaryClosingByReconstructionImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_Clone)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_GetForegroundValue)
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_GetBackgroundValue)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_FullyConnectedOff)
    __swig_destroy__ = _itkBinaryOpeningByReconstructionImageFilterPython.delete_itkBinaryOpeningByReconstructionImageFilterIUC3SE3
    cast = _swig_new_static_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryOpeningByReconstructionImageFilterIUC3SE3

        Create a new object of the class itkBinaryOpeningByReconstructionImageFilterIUC3SE3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryOpeningByReconstructionImageFilterIUC3SE3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBinaryOpeningByReconstructionImageFilterIUC3SE3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBinaryOpeningByReconstructionImageFilterIUC3SE3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryOpeningByReconstructionImageFilterIUC3SE3 in _itkBinaryOpeningByReconstructionImageFilterPython:
_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_swigregister(itkBinaryOpeningByReconstructionImageFilterIUC3SE3)
itkBinaryOpeningByReconstructionImageFilterIUC3SE3___New_orig__ = _itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3___New_orig__
itkBinaryOpeningByReconstructionImageFilterIUC3SE3_cast = _itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC3SE3_cast


def itkBinaryOpeningByReconstructionImageFilterIUC4SE4_New():
    return itkBinaryOpeningByReconstructionImageFilterIUC4SE4.New()

class itkBinaryOpeningByReconstructionImageFilterIUC4SE4(itk.itkFlatStructuringElementPython.itkKernelImageFilterIUC4IUC4SE4):
    r"""


    binary morphological closing of an image.

    This filter removes small (i.e., smaller than the structuring element)
    objects in the image. It is defined as: Opening(f) =
    ReconstructionByDilatation(Erosion(f)).

    The structuring element is assumed to be composed of binary values
    (zero or one). Only elements of the structuring element having values
    > 0 are candidates for affecting the center pixel.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:  MorphologyImageFilter, OpeningByReconstructionImageFilter,
    BinaryClosingByReconstructionImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC4SE4___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC4SE4_Clone)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC4SE4_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC4SE4_GetForegroundValue)
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC4SE4_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC4SE4_GetBackgroundValue)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC4SE4_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC4SE4_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC4SE4_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC4SE4_FullyConnectedOff)
    __swig_destroy__ = _itkBinaryOpeningByReconstructionImageFilterPython.delete_itkBinaryOpeningByReconstructionImageFilterIUC4SE4
    cast = _swig_new_static_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC4SE4_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryOpeningByReconstructionImageFilterIUC4SE4

        Create a new object of the class itkBinaryOpeningByReconstructionImageFilterIUC4SE4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryOpeningByReconstructionImageFilterIUC4SE4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBinaryOpeningByReconstructionImageFilterIUC4SE4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBinaryOpeningByReconstructionImageFilterIUC4SE4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryOpeningByReconstructionImageFilterIUC4SE4 in _itkBinaryOpeningByReconstructionImageFilterPython:
_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC4SE4_swigregister(itkBinaryOpeningByReconstructionImageFilterIUC4SE4)
itkBinaryOpeningByReconstructionImageFilterIUC4SE4___New_orig__ = _itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC4SE4___New_orig__
itkBinaryOpeningByReconstructionImageFilterIUC4SE4_cast = _itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUC4SE4_cast


def itkBinaryOpeningByReconstructionImageFilterIUS2SE2_New():
    return itkBinaryOpeningByReconstructionImageFilterIUS2SE2.New()

class itkBinaryOpeningByReconstructionImageFilterIUS2SE2(itk.itkFlatStructuringElementPython.itkKernelImageFilterIUS2IUS2SE2):
    r"""


    binary morphological closing of an image.

    This filter removes small (i.e., smaller than the structuring element)
    objects in the image. It is defined as: Opening(f) =
    ReconstructionByDilatation(Erosion(f)).

    The structuring element is assumed to be composed of binary values
    (zero or one). Only elements of the structuring element having values
    > 0 are candidates for affecting the center pixel.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:  MorphologyImageFilter, OpeningByReconstructionImageFilter,
    BinaryClosingByReconstructionImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_Clone)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_GetForegroundValue)
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_GetBackgroundValue)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_FullyConnectedOff)
    __swig_destroy__ = _itkBinaryOpeningByReconstructionImageFilterPython.delete_itkBinaryOpeningByReconstructionImageFilterIUS2SE2
    cast = _swig_new_static_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryOpeningByReconstructionImageFilterIUS2SE2

        Create a new object of the class itkBinaryOpeningByReconstructionImageFilterIUS2SE2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryOpeningByReconstructionImageFilterIUS2SE2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBinaryOpeningByReconstructionImageFilterIUS2SE2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBinaryOpeningByReconstructionImageFilterIUS2SE2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryOpeningByReconstructionImageFilterIUS2SE2 in _itkBinaryOpeningByReconstructionImageFilterPython:
_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_swigregister(itkBinaryOpeningByReconstructionImageFilterIUS2SE2)
itkBinaryOpeningByReconstructionImageFilterIUS2SE2___New_orig__ = _itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2___New_orig__
itkBinaryOpeningByReconstructionImageFilterIUS2SE2_cast = _itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS2SE2_cast


def itkBinaryOpeningByReconstructionImageFilterIUS3SE3_New():
    return itkBinaryOpeningByReconstructionImageFilterIUS3SE3.New()

class itkBinaryOpeningByReconstructionImageFilterIUS3SE3(itk.itkFlatStructuringElementPython.itkKernelImageFilterIUS3IUS3SE3):
    r"""


    binary morphological closing of an image.

    This filter removes small (i.e., smaller than the structuring element)
    objects in the image. It is defined as: Opening(f) =
    ReconstructionByDilatation(Erosion(f)).

    The structuring element is assumed to be composed of binary values
    (zero or one). Only elements of the structuring element having values
    > 0 are candidates for affecting the center pixel.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:  MorphologyImageFilter, OpeningByReconstructionImageFilter,
    BinaryClosingByReconstructionImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_Clone)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_GetForegroundValue)
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_GetBackgroundValue)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_FullyConnectedOff)
    __swig_destroy__ = _itkBinaryOpeningByReconstructionImageFilterPython.delete_itkBinaryOpeningByReconstructionImageFilterIUS3SE3
    cast = _swig_new_static_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryOpeningByReconstructionImageFilterIUS3SE3

        Create a new object of the class itkBinaryOpeningByReconstructionImageFilterIUS3SE3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryOpeningByReconstructionImageFilterIUS3SE3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBinaryOpeningByReconstructionImageFilterIUS3SE3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBinaryOpeningByReconstructionImageFilterIUS3SE3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryOpeningByReconstructionImageFilterIUS3SE3 in _itkBinaryOpeningByReconstructionImageFilterPython:
_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_swigregister(itkBinaryOpeningByReconstructionImageFilterIUS3SE3)
itkBinaryOpeningByReconstructionImageFilterIUS3SE3___New_orig__ = _itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3___New_orig__
itkBinaryOpeningByReconstructionImageFilterIUS3SE3_cast = _itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS3SE3_cast


def itkBinaryOpeningByReconstructionImageFilterIUS4SE4_New():
    return itkBinaryOpeningByReconstructionImageFilterIUS4SE4.New()

class itkBinaryOpeningByReconstructionImageFilterIUS4SE4(itk.itkFlatStructuringElementPython.itkKernelImageFilterIUS4IUS4SE4):
    r"""


    binary morphological closing of an image.

    This filter removes small (i.e., smaller than the structuring element)
    objects in the image. It is defined as: Opening(f) =
    ReconstructionByDilatation(Erosion(f)).

    The structuring element is assumed to be composed of binary values
    (zero or one). Only elements of the structuring element having values
    > 0 are candidates for affecting the center pixel.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:  MorphologyImageFilter, OpeningByReconstructionImageFilter,
    BinaryClosingByReconstructionImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS4SE4___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS4SE4_Clone)
    SetForegroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS4SE4_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS4SE4_GetForegroundValue)
    SetBackgroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS4SE4_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS4SE4_GetBackgroundValue)
    SetFullyConnected = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS4SE4_SetFullyConnected)
    GetFullyConnected = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS4SE4_GetFullyConnected)
    FullyConnectedOn = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS4SE4_FullyConnectedOn)
    FullyConnectedOff = _swig_new_instance_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS4SE4_FullyConnectedOff)
    __swig_destroy__ = _itkBinaryOpeningByReconstructionImageFilterPython.delete_itkBinaryOpeningByReconstructionImageFilterIUS4SE4
    cast = _swig_new_static_method(_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS4SE4_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryOpeningByReconstructionImageFilterIUS4SE4

        Create a new object of the class itkBinaryOpeningByReconstructionImageFilterIUS4SE4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryOpeningByReconstructionImageFilterIUS4SE4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBinaryOpeningByReconstructionImageFilterIUS4SE4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBinaryOpeningByReconstructionImageFilterIUS4SE4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryOpeningByReconstructionImageFilterIUS4SE4 in _itkBinaryOpeningByReconstructionImageFilterPython:
_itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS4SE4_swigregister(itkBinaryOpeningByReconstructionImageFilterIUS4SE4)
itkBinaryOpeningByReconstructionImageFilterIUS4SE4___New_orig__ = _itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS4SE4___New_orig__
itkBinaryOpeningByReconstructionImageFilterIUS4SE4_cast = _itkBinaryOpeningByReconstructionImageFilterPython.itkBinaryOpeningByReconstructionImageFilterIUS4SE4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def binary_opening_by_reconstruction_image_filter(*args: itkt.ImageLike,  foreground_value: int=..., background_value: int=..., fully_connected: bool=..., kernel: itkt.FlatStructuringElement=..., radius: Union[int, Sequence[int], int, Sequence[int]]=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for BinaryOpeningByReconstructionImageFilter"""
    import itk

    kwarg_typehints = { 'foreground_value':foreground_value,'background_value':background_value,'fully_connected':fully_connected,'kernel':kernel,'radius':radius }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.BinaryOpeningByReconstructionImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def binary_opening_by_reconstruction_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKBinaryMathematicalMorphology.BinaryOpeningByReconstructionImageFilter
    binary_opening_by_reconstruction_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    binary_opening_by_reconstruction_image_filter.__doc__ = filter_object.__doc__




