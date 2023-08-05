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
    from . import _itkChangeLabelLabelMapFilterPython
else:
    import _itkChangeLabelLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkChangeLabelLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkChangeLabelLabelMapFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkInPlaceLabelMapFilterPython
import itk.ITKLabelMapBasePython
import itk.itkImagePython
import itk.itkFixedArrayPython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.itkImageRegionPython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkMatrixPython
import itk.itkPointPython
import itk.vnl_matrix_fixedPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython
import itk.itkImageSourcePython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterCommonPython
import itk.itkStatisticsLabelObjectPython
import itk.itkAffineTransformPython
import itk.itkTransformBasePython
import itk.itkOptimizerParametersPython
import itk.itkArrayPython
import itk.itkArray2DPython
import itk.itkDiffusionTensor3DPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkShapeLabelObjectPython
import itk.itkLabelObjectPython
import itk.itkLabelObjectLinePython
import itk.itkHistogramPython
import itk.itkSamplePython
import itk.itkLabelMapFilterPython

def itkChangeLabelLabelMapFilterLM2_New():
    return itkChangeLabelLabelMapFilterLM2.New()

class itkChangeLabelLabelMapFilterLM2(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    r"""


    Replace the label Ids of selected LabelObjects with new label Ids.

    This filter takes as input a label map and a list of pairs of Label
    Ids, to produce as output a new label map where the label Ids have
    been replaced according to the pairs in the list.

    Labels that are relabeled to the same label Id are automatically
    merged and optimized into a single LabelObject. The background label
    can also be changed. Any object relabeled to the output background
    will automatically be removed.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, RelabelComponentImageFilter,
    ChangeLabelImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_Clone)
    SetChangeMap = _swig_new_instance_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_SetChangeMap)
    GetChangeMap = _swig_new_instance_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_GetChangeMap)
    SetChange = _swig_new_instance_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_SetChange)
    ClearChangeMap = _swig_new_instance_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_ClearChangeMap)
    __swig_destroy__ = _itkChangeLabelLabelMapFilterPython.delete_itkChangeLabelLabelMapFilterLM2
    cast = _swig_new_static_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkChangeLabelLabelMapFilterLM2

        Create a new object of the class itkChangeLabelLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkChangeLabelLabelMapFilterLM2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkChangeLabelLabelMapFilterLM2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkChangeLabelLabelMapFilterLM2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkChangeLabelLabelMapFilterLM2 in _itkChangeLabelLabelMapFilterPython:
_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_swigregister(itkChangeLabelLabelMapFilterLM2)
itkChangeLabelLabelMapFilterLM2___New_orig__ = _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2___New_orig__
itkChangeLabelLabelMapFilterLM2_cast = _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM2_cast


def itkChangeLabelLabelMapFilterLM3_New():
    return itkChangeLabelLabelMapFilterLM3.New()

class itkChangeLabelLabelMapFilterLM3(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    r"""


    Replace the label Ids of selected LabelObjects with new label Ids.

    This filter takes as input a label map and a list of pairs of Label
    Ids, to produce as output a new label map where the label Ids have
    been replaced according to the pairs in the list.

    Labels that are relabeled to the same label Id are automatically
    merged and optimized into a single LabelObject. The background label
    can also be changed. Any object relabeled to the output background
    will automatically be removed.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, RelabelComponentImageFilter,
    ChangeLabelImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_Clone)
    SetChangeMap = _swig_new_instance_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_SetChangeMap)
    GetChangeMap = _swig_new_instance_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_GetChangeMap)
    SetChange = _swig_new_instance_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_SetChange)
    ClearChangeMap = _swig_new_instance_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_ClearChangeMap)
    __swig_destroy__ = _itkChangeLabelLabelMapFilterPython.delete_itkChangeLabelLabelMapFilterLM3
    cast = _swig_new_static_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkChangeLabelLabelMapFilterLM3

        Create a new object of the class itkChangeLabelLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkChangeLabelLabelMapFilterLM3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkChangeLabelLabelMapFilterLM3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkChangeLabelLabelMapFilterLM3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkChangeLabelLabelMapFilterLM3 in _itkChangeLabelLabelMapFilterPython:
_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_swigregister(itkChangeLabelLabelMapFilterLM3)
itkChangeLabelLabelMapFilterLM3___New_orig__ = _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3___New_orig__
itkChangeLabelLabelMapFilterLM3_cast = _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM3_cast


def itkChangeLabelLabelMapFilterLM4_New():
    return itkChangeLabelLabelMapFilterLM4.New()

class itkChangeLabelLabelMapFilterLM4(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM4):
    r"""


    Replace the label Ids of selected LabelObjects with new label Ids.

    This filter takes as input a label map and a list of pairs of Label
    Ids, to produce as output a new label map where the label Ids have
    been replaced according to the pairs in the list.

    Labels that are relabeled to the same label Id are automatically
    merged and optimized into a single LabelObject. The background label
    can also be changed. Any object relabeled to the output background
    will automatically be removed.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, RelabelComponentImageFilter,
    ChangeLabelImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM4___New_orig__)
    Clone = _swig_new_instance_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM4_Clone)
    SetChangeMap = _swig_new_instance_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM4_SetChangeMap)
    GetChangeMap = _swig_new_instance_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM4_GetChangeMap)
    SetChange = _swig_new_instance_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM4_SetChange)
    ClearChangeMap = _swig_new_instance_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM4_ClearChangeMap)
    __swig_destroy__ = _itkChangeLabelLabelMapFilterPython.delete_itkChangeLabelLabelMapFilterLM4
    cast = _swig_new_static_method(_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM4_cast)

    def New(*args, **kargs):
        """New() -> itkChangeLabelLabelMapFilterLM4

        Create a new object of the class itkChangeLabelLabelMapFilterLM4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkChangeLabelLabelMapFilterLM4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkChangeLabelLabelMapFilterLM4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkChangeLabelLabelMapFilterLM4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkChangeLabelLabelMapFilterLM4 in _itkChangeLabelLabelMapFilterPython:
_itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM4_swigregister(itkChangeLabelLabelMapFilterLM4)
itkChangeLabelLabelMapFilterLM4___New_orig__ = _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM4___New_orig__
itkChangeLabelLabelMapFilterLM4_cast = _itkChangeLabelLabelMapFilterPython.itkChangeLabelLabelMapFilterLM4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def change_label_label_map_filter(*args: itkt.ImageLike,  change_map=..., change: int=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for ChangeLabelLabelMapFilter"""
    import itk

    kwarg_typehints = { 'change_map':change_map,'change':change }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.ChangeLabelLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def change_label_label_map_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelMap.ChangeLabelLabelMapFilter
    change_label_label_map_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    change_label_label_map_filter.__doc__ = filter_object.__doc__




