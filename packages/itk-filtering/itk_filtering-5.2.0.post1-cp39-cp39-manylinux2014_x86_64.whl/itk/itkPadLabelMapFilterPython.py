# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKLabelMapPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkPadLabelMapFilterPython
else:
    import _itkPadLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkPadLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkPadLabelMapFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkChangeRegionLabelMapFilterPython
import itk.itkStatisticsLabelObjectPython
import itk.itkIndexPython
import itk.itkSizePython
import itk.pyBasePython
import itk.itkOffsetPython
import itk.itkHistogramPython
import itk.itkSamplePython
import itk.itkFixedArrayPython
import itk.ITKCommonBasePython
import itk.itkArrayPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkAffineTransformPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkOptimizerParametersPython
import itk.itkPointPython
import itk.itkArray2DPython
import itk.itkCovariantVectorPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkTransformBasePython
import itk.itkDiffusionTensor3DPython
import itk.itkVariableLengthVectorPython
import itk.itkShapeLabelObjectPython
import itk.itkLabelObjectPython
import itk.itkLabelObjectLinePython
import itk.itkImageRegionPython
import itk.itkInPlaceLabelMapFilterPython
import itk.ITKLabelMapBasePython
import itk.itkImageSourcePython
import itk.itkImagePython
import itk.itkRGBPixelPython
import itk.itkRGBAPixelPython
import itk.itkVectorImagePython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterCommonPython
import itk.itkLabelMapFilterPython

def itkPadLabelMapFilterLM2_New():
    return itkPadLabelMapFilterLM2.New()

class itkPadLabelMapFilterLM2(itk.itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM2):
    r"""


    Pad a LabelMap image.

    This filter pads a label map.

    The SetPadSize() method can be used to set the pad size of the lower
    and the upper boundaries in a single call. By default, the filter
    doesn't pad anything.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   CropLabelMapFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_Clone)
    SetUpperBoundaryPadSize = _swig_new_instance_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_SetUpperBoundaryPadSize)
    GetUpperBoundaryPadSize = _swig_new_instance_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_GetUpperBoundaryPadSize)
    SetLowerBoundaryPadSize = _swig_new_instance_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_SetLowerBoundaryPadSize)
    GetLowerBoundaryPadSize = _swig_new_instance_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_GetLowerBoundaryPadSize)
    SetPadSize = _swig_new_instance_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_SetPadSize)
    __swig_destroy__ = _itkPadLabelMapFilterPython.delete_itkPadLabelMapFilterLM2
    cast = _swig_new_static_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkPadLabelMapFilterLM2

        Create a new object of the class itkPadLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPadLabelMapFilterLM2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPadLabelMapFilterLM2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPadLabelMapFilterLM2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPadLabelMapFilterLM2 in _itkPadLabelMapFilterPython:
_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_swigregister(itkPadLabelMapFilterLM2)
itkPadLabelMapFilterLM2___New_orig__ = _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2___New_orig__
itkPadLabelMapFilterLM2_cast = _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM2_cast


def itkPadLabelMapFilterLM3_New():
    return itkPadLabelMapFilterLM3.New()

class itkPadLabelMapFilterLM3(itk.itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM3):
    r"""


    Pad a LabelMap image.

    This filter pads a label map.

    The SetPadSize() method can be used to set the pad size of the lower
    and the upper boundaries in a single call. By default, the filter
    doesn't pad anything.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   CropLabelMapFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_Clone)
    SetUpperBoundaryPadSize = _swig_new_instance_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_SetUpperBoundaryPadSize)
    GetUpperBoundaryPadSize = _swig_new_instance_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_GetUpperBoundaryPadSize)
    SetLowerBoundaryPadSize = _swig_new_instance_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_SetLowerBoundaryPadSize)
    GetLowerBoundaryPadSize = _swig_new_instance_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_GetLowerBoundaryPadSize)
    SetPadSize = _swig_new_instance_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_SetPadSize)
    __swig_destroy__ = _itkPadLabelMapFilterPython.delete_itkPadLabelMapFilterLM3
    cast = _swig_new_static_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkPadLabelMapFilterLM3

        Create a new object of the class itkPadLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPadLabelMapFilterLM3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPadLabelMapFilterLM3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPadLabelMapFilterLM3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPadLabelMapFilterLM3 in _itkPadLabelMapFilterPython:
_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_swigregister(itkPadLabelMapFilterLM3)
itkPadLabelMapFilterLM3___New_orig__ = _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3___New_orig__
itkPadLabelMapFilterLM3_cast = _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM3_cast


def itkPadLabelMapFilterLM4_New():
    return itkPadLabelMapFilterLM4.New()

class itkPadLabelMapFilterLM4(itk.itkChangeRegionLabelMapFilterPython.itkChangeRegionLabelMapFilterLM4):
    r"""


    Pad a LabelMap image.

    This filter pads a label map.

    The SetPadSize() method can be used to set the pad size of the lower
    and the upper boundaries in a single call. By default, the filter
    doesn't pad anything.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   CropLabelMapFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM4___New_orig__)
    Clone = _swig_new_instance_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM4_Clone)
    SetUpperBoundaryPadSize = _swig_new_instance_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM4_SetUpperBoundaryPadSize)
    GetUpperBoundaryPadSize = _swig_new_instance_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM4_GetUpperBoundaryPadSize)
    SetLowerBoundaryPadSize = _swig_new_instance_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM4_SetLowerBoundaryPadSize)
    GetLowerBoundaryPadSize = _swig_new_instance_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM4_GetLowerBoundaryPadSize)
    SetPadSize = _swig_new_instance_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM4_SetPadSize)
    __swig_destroy__ = _itkPadLabelMapFilterPython.delete_itkPadLabelMapFilterLM4
    cast = _swig_new_static_method(_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM4_cast)

    def New(*args, **kargs):
        """New() -> itkPadLabelMapFilterLM4

        Create a new object of the class itkPadLabelMapFilterLM4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPadLabelMapFilterLM4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkPadLabelMapFilterLM4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkPadLabelMapFilterLM4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPadLabelMapFilterLM4 in _itkPadLabelMapFilterPython:
_itkPadLabelMapFilterPython.itkPadLabelMapFilterLM4_swigregister(itkPadLabelMapFilterLM4)
itkPadLabelMapFilterLM4___New_orig__ = _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM4___New_orig__
itkPadLabelMapFilterLM4_cast = _itkPadLabelMapFilterPython.itkPadLabelMapFilterLM4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def pad_label_map_filter(*args: itkt.ImageLike,  upper_boundary_pad_size: Sequence[int]=..., lower_boundary_pad_size: Sequence[int]=..., pad_size: Sequence[int]=..., region: itkt.ImageRegion=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for PadLabelMapFilter"""
    import itk

    kwarg_typehints = { 'upper_boundary_pad_size':upper_boundary_pad_size,'lower_boundary_pad_size':lower_boundary_pad_size,'pad_size':pad_size,'region':region }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.PadLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def pad_label_map_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelMap.PadLabelMapFilter
    pad_label_map_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    pad_label_map_filter.__doc__ = filter_object.__doc__




