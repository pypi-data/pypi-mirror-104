# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKImageFusionPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkLabelMapToRGBImageFilterPython
else:
    import _itkLabelMapToRGBImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkLabelMapToRGBImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkLabelMapToRGBImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkLabelMapFilterPython
import itk.itkStatisticsLabelObjectPython
import itk.itkShapeLabelObjectPython
import itk.itkPointPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkLabelObjectPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkLabelObjectLinePython
import itk.itkIndexPython
import itk.ITKCommonBasePython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkAffineTransformPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkOptimizerParametersPython
import itk.itkArrayPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkTransformBasePython
import itk.itkArray2DPython
import itk.itkDiffusionTensor3DPython
import itk.itkVariableLengthVectorPython
import itk.itkImageRegionPython
import itk.itkHistogramPython
import itk.itkSamplePython
import itk.ITKLabelMapBasePython
import itk.itkImageSourceCommonPython
import itk.itkImageSourcePython
import itk.itkImagePython
import itk.itkRGBPixelPython
import itk.itkRGBAPixelPython
import itk.itkVectorImagePython
import itk.itkImageToImageFilterCommonPython

def itkLabelMapToRGBImageFilterLM2IRGBUC2_New():
    return itkLabelMapToRGBImageFilterLM2IRGBUC2.New()

class itkLabelMapToRGBImageFilterLM2IRGBUC2(itk.itkLabelMapFilterPython.itkLabelMapFilterLM2IRGBUC2):
    r"""


    Convert a LabelMap to a colored image.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   LabelToRGBImageFilter, LabelToRGBFunctor

    See:   LabelMapOverlayImageFilter, LabelMapToBinaryImageFilter,
    LabelMapMaskImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_Clone)
    SetFunctor = _swig_new_instance_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_SetFunctor)
    GetFunctor = _swig_new_instance_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_GetFunctor)
    __swig_destroy__ = _itkLabelMapToRGBImageFilterPython.delete_itkLabelMapToRGBImageFilterLM2IRGBUC2
    cast = _swig_new_static_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToRGBImageFilterLM2IRGBUC2

        Create a new object of the class itkLabelMapToRGBImageFilterLM2IRGBUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToRGBImageFilterLM2IRGBUC2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelMapToRGBImageFilterLM2IRGBUC2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelMapToRGBImageFilterLM2IRGBUC2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToRGBImageFilterLM2IRGBUC2 in _itkLabelMapToRGBImageFilterPython:
_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_swigregister(itkLabelMapToRGBImageFilterLM2IRGBUC2)
itkLabelMapToRGBImageFilterLM2IRGBUC2___New_orig__ = _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2___New_orig__
itkLabelMapToRGBImageFilterLM2IRGBUC2_cast = _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM2IRGBUC2_cast


def itkLabelMapToRGBImageFilterLM3IRGBUC3_New():
    return itkLabelMapToRGBImageFilterLM3IRGBUC3.New()

class itkLabelMapToRGBImageFilterLM3IRGBUC3(itk.itkLabelMapFilterPython.itkLabelMapFilterLM3IRGBUC3):
    r"""


    Convert a LabelMap to a colored image.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   LabelToRGBImageFilter, LabelToRGBFunctor

    See:   LabelMapOverlayImageFilter, LabelMapToBinaryImageFilter,
    LabelMapMaskImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_Clone)
    SetFunctor = _swig_new_instance_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_SetFunctor)
    GetFunctor = _swig_new_instance_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_GetFunctor)
    __swig_destroy__ = _itkLabelMapToRGBImageFilterPython.delete_itkLabelMapToRGBImageFilterLM3IRGBUC3
    cast = _swig_new_static_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToRGBImageFilterLM3IRGBUC3

        Create a new object of the class itkLabelMapToRGBImageFilterLM3IRGBUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToRGBImageFilterLM3IRGBUC3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelMapToRGBImageFilterLM3IRGBUC3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelMapToRGBImageFilterLM3IRGBUC3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToRGBImageFilterLM3IRGBUC3 in _itkLabelMapToRGBImageFilterPython:
_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_swigregister(itkLabelMapToRGBImageFilterLM3IRGBUC3)
itkLabelMapToRGBImageFilterLM3IRGBUC3___New_orig__ = _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3___New_orig__
itkLabelMapToRGBImageFilterLM3IRGBUC3_cast = _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM3IRGBUC3_cast


def itkLabelMapToRGBImageFilterLM4IRGBUC4_New():
    return itkLabelMapToRGBImageFilterLM4IRGBUC4.New()

class itkLabelMapToRGBImageFilterLM4IRGBUC4(itk.itkLabelMapFilterPython.itkLabelMapFilterLM4IRGBUC4):
    r"""


    Convert a LabelMap to a colored image.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   LabelToRGBImageFilter, LabelToRGBFunctor

    See:   LabelMapOverlayImageFilter, LabelMapToBinaryImageFilter,
    LabelMapMaskImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM4IRGBUC4___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM4IRGBUC4_Clone)
    SetFunctor = _swig_new_instance_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM4IRGBUC4_SetFunctor)
    GetFunctor = _swig_new_instance_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM4IRGBUC4_GetFunctor)
    __swig_destroy__ = _itkLabelMapToRGBImageFilterPython.delete_itkLabelMapToRGBImageFilterLM4IRGBUC4
    cast = _swig_new_static_method(_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM4IRGBUC4_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToRGBImageFilterLM4IRGBUC4

        Create a new object of the class itkLabelMapToRGBImageFilterLM4IRGBUC4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToRGBImageFilterLM4IRGBUC4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelMapToRGBImageFilterLM4IRGBUC4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelMapToRGBImageFilterLM4IRGBUC4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToRGBImageFilterLM4IRGBUC4 in _itkLabelMapToRGBImageFilterPython:
_itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM4IRGBUC4_swigregister(itkLabelMapToRGBImageFilterLM4IRGBUC4)
itkLabelMapToRGBImageFilterLM4IRGBUC4___New_orig__ = _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM4IRGBUC4___New_orig__
itkLabelMapToRGBImageFilterLM4IRGBUC4_cast = _itkLabelMapToRGBImageFilterPython.itkLabelMapToRGBImageFilterLM4IRGBUC4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def label_map_to_rgb_image_filter(*args: itkt.ImageLike,  functor=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for LabelMapToRGBImageFilter"""
    import itk

    kwarg_typehints = { 'functor':functor }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.LabelMapToRGBImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def label_map_to_rgb_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKImageFusion.LabelMapToRGBImageFilter
    label_map_to_rgb_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    label_map_to_rgb_image_filter.__doc__ = filter_object.__doc__




