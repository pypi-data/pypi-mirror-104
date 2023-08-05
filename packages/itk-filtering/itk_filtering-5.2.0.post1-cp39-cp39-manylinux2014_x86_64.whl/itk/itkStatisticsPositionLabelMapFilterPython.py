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
    from . import _itkStatisticsPositionLabelMapFilterPython
else:
    import _itkStatisticsPositionLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkStatisticsPositionLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkStatisticsPositionLabelMapFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkShapePositionLabelMapFilterPython
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

def itkStatisticsPositionLabelMapFilterLM2_New():
    return itkStatisticsPositionLabelMapFilterLM2.New()

class itkStatisticsPositionLabelMapFilterLM2(itk.itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM2):
    r"""


    Mark a single pixel in the label object which correspond to a position
    given by an attribute.

    This code was contributed in the Insight Journal paper: "Label object
    representation and manipulation with ITK" by Lehmann
    G.https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   StatisticsLabelObject, BinaryStatisticsOpeningImageFilter,
    LabelStatisticsOpeningImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM2_Clone)
    __swig_destroy__ = _itkStatisticsPositionLabelMapFilterPython.delete_itkStatisticsPositionLabelMapFilterLM2
    cast = _swig_new_static_method(_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkStatisticsPositionLabelMapFilterLM2

        Create a new object of the class itkStatisticsPositionLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsPositionLabelMapFilterLM2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkStatisticsPositionLabelMapFilterLM2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkStatisticsPositionLabelMapFilterLM2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStatisticsPositionLabelMapFilterLM2 in _itkStatisticsPositionLabelMapFilterPython:
_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM2_swigregister(itkStatisticsPositionLabelMapFilterLM2)
itkStatisticsPositionLabelMapFilterLM2___New_orig__ = _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM2___New_orig__
itkStatisticsPositionLabelMapFilterLM2_cast = _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM2_cast


def itkStatisticsPositionLabelMapFilterLM3_New():
    return itkStatisticsPositionLabelMapFilterLM3.New()

class itkStatisticsPositionLabelMapFilterLM3(itk.itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM3):
    r"""


    Mark a single pixel in the label object which correspond to a position
    given by an attribute.

    This code was contributed in the Insight Journal paper: "Label object
    representation and manipulation with ITK" by Lehmann
    G.https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   StatisticsLabelObject, BinaryStatisticsOpeningImageFilter,
    LabelStatisticsOpeningImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM3_Clone)
    __swig_destroy__ = _itkStatisticsPositionLabelMapFilterPython.delete_itkStatisticsPositionLabelMapFilterLM3
    cast = _swig_new_static_method(_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkStatisticsPositionLabelMapFilterLM3

        Create a new object of the class itkStatisticsPositionLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsPositionLabelMapFilterLM3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkStatisticsPositionLabelMapFilterLM3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkStatisticsPositionLabelMapFilterLM3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStatisticsPositionLabelMapFilterLM3 in _itkStatisticsPositionLabelMapFilterPython:
_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM3_swigregister(itkStatisticsPositionLabelMapFilterLM3)
itkStatisticsPositionLabelMapFilterLM3___New_orig__ = _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM3___New_orig__
itkStatisticsPositionLabelMapFilterLM3_cast = _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM3_cast


def itkStatisticsPositionLabelMapFilterLM4_New():
    return itkStatisticsPositionLabelMapFilterLM4.New()

class itkStatisticsPositionLabelMapFilterLM4(itk.itkShapePositionLabelMapFilterPython.itkShapePositionLabelMapFilterLM4):
    r"""


    Mark a single pixel in the label object which correspond to a position
    given by an attribute.

    This code was contributed in the Insight Journal paper: "Label object
    representation and manipulation with ITK" by Lehmann
    G.https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   StatisticsLabelObject, BinaryStatisticsOpeningImageFilter,
    LabelStatisticsOpeningImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM4___New_orig__)
    Clone = _swig_new_instance_method(_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM4_Clone)
    __swig_destroy__ = _itkStatisticsPositionLabelMapFilterPython.delete_itkStatisticsPositionLabelMapFilterLM4
    cast = _swig_new_static_method(_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM4_cast)

    def New(*args, **kargs):
        """New() -> itkStatisticsPositionLabelMapFilterLM4

        Create a new object of the class itkStatisticsPositionLabelMapFilterLM4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsPositionLabelMapFilterLM4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkStatisticsPositionLabelMapFilterLM4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkStatisticsPositionLabelMapFilterLM4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStatisticsPositionLabelMapFilterLM4 in _itkStatisticsPositionLabelMapFilterPython:
_itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM4_swigregister(itkStatisticsPositionLabelMapFilterLM4)
itkStatisticsPositionLabelMapFilterLM4___New_orig__ = _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM4___New_orig__
itkStatisticsPositionLabelMapFilterLM4_cast = _itkStatisticsPositionLabelMapFilterPython.itkStatisticsPositionLabelMapFilterLM4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def statistics_position_label_map_filter(*args: itkt.ImageLike,  attribute: Union[int, str]=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for StatisticsPositionLabelMapFilter"""
    import itk

    kwarg_typehints = { 'attribute':attribute }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.StatisticsPositionLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def statistics_position_label_map_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelMap.StatisticsPositionLabelMapFilter
    statistics_position_label_map_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    statistics_position_label_map_filter.__doc__ = filter_object.__doc__




