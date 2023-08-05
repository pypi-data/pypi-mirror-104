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
    from . import _itkObjectByObjectLabelMapFilterPython
else:
    import _itkObjectByObjectLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkObjectByObjectLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkObjectByObjectLabelMapFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkImageRegionPython
import itk.itkSizePython
import itk.pyBasePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.ITKCommonBasePython
import itk.itkImageToImageFilterCommonPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.stdcomplexPython
import itk.itkImagePython
import itk.itkCovariantVectorPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkPointPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkRGBPixelPython
import itk.itkRGBAPixelPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkLabelMapFilterPython
import itk.itkStatisticsLabelObjectPython
import itk.itkHistogramPython
import itk.itkSamplePython
import itk.itkArrayPython
import itk.itkAffineTransformPython
import itk.itkTransformBasePython
import itk.itkArray2DPython
import itk.itkDiffusionTensor3DPython
import itk.itkOptimizerParametersPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkShapeLabelObjectPython
import itk.itkLabelObjectPython
import itk.itkLabelObjectLinePython
import itk.ITKLabelMapBasePython

def itkObjectByObjectLabelMapFilterLM2_New():
    return itkObjectByObjectLabelMapFilterLM2.New()

class itkObjectByObjectLabelMapFilterLM2(itk.itkLabelMapFilterPython.itkLabelMapFilterLM2LM2):
    r"""


    ObjectByObjectLabelMapFilter applies an image pipeline to all the
    objects of a label map and produce a new label map.

    The image pipeline can simply produce a modified object or produce
    several objects from the single input object. Several options are
    provided to handle the different cases.

    KeepLabel, which defaults to true, makes the filter try to keep as
    much as possible the labels of the original objects. If an image
    pipeline produce several objects the label of the input object is
    assigned to the first output object. The other output objects get
    another label not present in the input image. When KeepLabel is set to
    false, all the objects are relabeled in the order of apparition during
    the filter process.

    BinaryInternalOutput can be set to true if the image pipeline produce
    binary output image. In that case, the objects produced are identified
    with a connected component algorithm before being reinserted in the
    output label map. InternalForegroundValue can be set to a specific
    value which represent the foreground value in the binary image.

    PadSize and ConstrainPaddingToImage can be used to extend the size of
    the image to process passed to the image pipeline. This is useful if
    the image pipeline is known to be able to enlarge the object. The
    padding can be constrained to the input label map region by setting
    ConstrainPaddingToImage to true - this parameter can make a difference
    for the algorithm with a different behavior on the border of the
    image. By default, the image is padded by 1 pixel and constrained to
    the image region.

    : When applying a single filter, input and output filters are the
    same; while applying a pipeline, input and output filters are
    different, may not even be of the same type. It is the responsibility
    of the user to connect the pipeline properly outside of this filter.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    {Filtering/LabelMap/ApplyMorphologicalClosingOnAllLabelObjects,Apply
    Morphological Closing On All Label Objects} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_Clone)
    SetFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetFilter)
    GetFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetFilter)
    SetInputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetInputFilter)
    GetModifiableInputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetModifiableInputFilter)
    GetInputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetInputFilter)
    SetOutputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetOutputFilter)
    GetModifiableOutputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetModifiableOutputFilter)
    GetOutputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetOutputFilter)
    SetKeepLabels = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetKeepLabels)
    GetKeepLabels = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetKeepLabels)
    KeepLabelsOn = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_KeepLabelsOn)
    KeepLabelsOff = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_KeepLabelsOff)
    SetPadSize = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetPadSize)
    GetPadSize = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetPadSize)
    SetConstrainPaddingToImage = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetConstrainPaddingToImage)
    GetConstrainPaddingToImage = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetConstrainPaddingToImage)
    ConstrainPaddingToImageOn = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_ConstrainPaddingToImageOn)
    ConstrainPaddingToImageOff = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_ConstrainPaddingToImageOff)
    SetBinaryInternalOutput = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetBinaryInternalOutput)
    GetBinaryInternalOutput = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetBinaryInternalOutput)
    BinaryInternalOutputOn = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_BinaryInternalOutputOn)
    BinaryInternalOutputOff = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_BinaryInternalOutputOff)
    SetInternalForegroundValue = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_SetInternalForegroundValue)
    GetInternalForegroundValue = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetInternalForegroundValue)
    GetLabel = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_GetLabel)
    __swig_destroy__ = _itkObjectByObjectLabelMapFilterPython.delete_itkObjectByObjectLabelMapFilterLM2
    cast = _swig_new_static_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkObjectByObjectLabelMapFilterLM2

        Create a new object of the class itkObjectByObjectLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkObjectByObjectLabelMapFilterLM2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkObjectByObjectLabelMapFilterLM2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkObjectByObjectLabelMapFilterLM2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkObjectByObjectLabelMapFilterLM2 in _itkObjectByObjectLabelMapFilterPython:
_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_swigregister(itkObjectByObjectLabelMapFilterLM2)
itkObjectByObjectLabelMapFilterLM2___New_orig__ = _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2___New_orig__
itkObjectByObjectLabelMapFilterLM2_cast = _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM2_cast


def itkObjectByObjectLabelMapFilterLM3_New():
    return itkObjectByObjectLabelMapFilterLM3.New()

class itkObjectByObjectLabelMapFilterLM3(itk.itkLabelMapFilterPython.itkLabelMapFilterLM3LM3):
    r"""


    ObjectByObjectLabelMapFilter applies an image pipeline to all the
    objects of a label map and produce a new label map.

    The image pipeline can simply produce a modified object or produce
    several objects from the single input object. Several options are
    provided to handle the different cases.

    KeepLabel, which defaults to true, makes the filter try to keep as
    much as possible the labels of the original objects. If an image
    pipeline produce several objects the label of the input object is
    assigned to the first output object. The other output objects get
    another label not present in the input image. When KeepLabel is set to
    false, all the objects are relabeled in the order of apparition during
    the filter process.

    BinaryInternalOutput can be set to true if the image pipeline produce
    binary output image. In that case, the objects produced are identified
    with a connected component algorithm before being reinserted in the
    output label map. InternalForegroundValue can be set to a specific
    value which represent the foreground value in the binary image.

    PadSize and ConstrainPaddingToImage can be used to extend the size of
    the image to process passed to the image pipeline. This is useful if
    the image pipeline is known to be able to enlarge the object. The
    padding can be constrained to the input label map region by setting
    ConstrainPaddingToImage to true - this parameter can make a difference
    for the algorithm with a different behavior on the border of the
    image. By default, the image is padded by 1 pixel and constrained to
    the image region.

    : When applying a single filter, input and output filters are the
    same; while applying a pipeline, input and output filters are
    different, may not even be of the same type. It is the responsibility
    of the user to connect the pipeline properly outside of this filter.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    {Filtering/LabelMap/ApplyMorphologicalClosingOnAllLabelObjects,Apply
    Morphological Closing On All Label Objects} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_Clone)
    SetFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetFilter)
    GetFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetFilter)
    SetInputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetInputFilter)
    GetModifiableInputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetModifiableInputFilter)
    GetInputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetInputFilter)
    SetOutputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetOutputFilter)
    GetModifiableOutputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetModifiableOutputFilter)
    GetOutputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetOutputFilter)
    SetKeepLabels = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetKeepLabels)
    GetKeepLabels = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetKeepLabels)
    KeepLabelsOn = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_KeepLabelsOn)
    KeepLabelsOff = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_KeepLabelsOff)
    SetPadSize = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetPadSize)
    GetPadSize = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetPadSize)
    SetConstrainPaddingToImage = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetConstrainPaddingToImage)
    GetConstrainPaddingToImage = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetConstrainPaddingToImage)
    ConstrainPaddingToImageOn = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_ConstrainPaddingToImageOn)
    ConstrainPaddingToImageOff = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_ConstrainPaddingToImageOff)
    SetBinaryInternalOutput = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetBinaryInternalOutput)
    GetBinaryInternalOutput = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetBinaryInternalOutput)
    BinaryInternalOutputOn = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_BinaryInternalOutputOn)
    BinaryInternalOutputOff = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_BinaryInternalOutputOff)
    SetInternalForegroundValue = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_SetInternalForegroundValue)
    GetInternalForegroundValue = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetInternalForegroundValue)
    GetLabel = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_GetLabel)
    __swig_destroy__ = _itkObjectByObjectLabelMapFilterPython.delete_itkObjectByObjectLabelMapFilterLM3
    cast = _swig_new_static_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkObjectByObjectLabelMapFilterLM3

        Create a new object of the class itkObjectByObjectLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkObjectByObjectLabelMapFilterLM3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkObjectByObjectLabelMapFilterLM3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkObjectByObjectLabelMapFilterLM3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkObjectByObjectLabelMapFilterLM3 in _itkObjectByObjectLabelMapFilterPython:
_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_swigregister(itkObjectByObjectLabelMapFilterLM3)
itkObjectByObjectLabelMapFilterLM3___New_orig__ = _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3___New_orig__
itkObjectByObjectLabelMapFilterLM3_cast = _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM3_cast


def itkObjectByObjectLabelMapFilterLM4_New():
    return itkObjectByObjectLabelMapFilterLM4.New()

class itkObjectByObjectLabelMapFilterLM4(itk.itkLabelMapFilterPython.itkLabelMapFilterLM4LM4):
    r"""


    ObjectByObjectLabelMapFilter applies an image pipeline to all the
    objects of a label map and produce a new label map.

    The image pipeline can simply produce a modified object or produce
    several objects from the single input object. Several options are
    provided to handle the different cases.

    KeepLabel, which defaults to true, makes the filter try to keep as
    much as possible the labels of the original objects. If an image
    pipeline produce several objects the label of the input object is
    assigned to the first output object. The other output objects get
    another label not present in the input image. When KeepLabel is set to
    false, all the objects are relabeled in the order of apparition during
    the filter process.

    BinaryInternalOutput can be set to true if the image pipeline produce
    binary output image. In that case, the objects produced are identified
    with a connected component algorithm before being reinserted in the
    output label map. InternalForegroundValue can be set to a specific
    value which represent the foreground value in the binary image.

    PadSize and ConstrainPaddingToImage can be used to extend the size of
    the image to process passed to the image pipeline. This is useful if
    the image pipeline is known to be able to enlarge the object. The
    padding can be constrained to the input label map region by setting
    ConstrainPaddingToImage to true - this parameter can make a difference
    for the algorithm with a different behavior on the border of the
    image. By default, the image is padded by 1 pixel and constrained to
    the image region.

    : When applying a single filter, input and output filters are the
    same; while applying a pipeline, input and output filters are
    different, may not even be of the same type. It is the responsibility
    of the user to connect the pipeline properly outside of this filter.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    {Filtering/LabelMap/ApplyMorphologicalClosingOnAllLabelObjects,Apply
    Morphological Closing On All Label Objects} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4___New_orig__)
    Clone = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_Clone)
    SetFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_SetFilter)
    GetFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_GetFilter)
    SetInputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_SetInputFilter)
    GetModifiableInputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_GetModifiableInputFilter)
    GetInputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_GetInputFilter)
    SetOutputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_SetOutputFilter)
    GetModifiableOutputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_GetModifiableOutputFilter)
    GetOutputFilter = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_GetOutputFilter)
    SetKeepLabels = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_SetKeepLabels)
    GetKeepLabels = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_GetKeepLabels)
    KeepLabelsOn = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_KeepLabelsOn)
    KeepLabelsOff = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_KeepLabelsOff)
    SetPadSize = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_SetPadSize)
    GetPadSize = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_GetPadSize)
    SetConstrainPaddingToImage = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_SetConstrainPaddingToImage)
    GetConstrainPaddingToImage = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_GetConstrainPaddingToImage)
    ConstrainPaddingToImageOn = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_ConstrainPaddingToImageOn)
    ConstrainPaddingToImageOff = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_ConstrainPaddingToImageOff)
    SetBinaryInternalOutput = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_SetBinaryInternalOutput)
    GetBinaryInternalOutput = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_GetBinaryInternalOutput)
    BinaryInternalOutputOn = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_BinaryInternalOutputOn)
    BinaryInternalOutputOff = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_BinaryInternalOutputOff)
    SetInternalForegroundValue = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_SetInternalForegroundValue)
    GetInternalForegroundValue = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_GetInternalForegroundValue)
    GetLabel = _swig_new_instance_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_GetLabel)
    __swig_destroy__ = _itkObjectByObjectLabelMapFilterPython.delete_itkObjectByObjectLabelMapFilterLM4
    cast = _swig_new_static_method(_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_cast)

    def New(*args, **kargs):
        """New() -> itkObjectByObjectLabelMapFilterLM4

        Create a new object of the class itkObjectByObjectLabelMapFilterLM4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkObjectByObjectLabelMapFilterLM4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkObjectByObjectLabelMapFilterLM4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkObjectByObjectLabelMapFilterLM4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkObjectByObjectLabelMapFilterLM4 in _itkObjectByObjectLabelMapFilterPython:
_itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_swigregister(itkObjectByObjectLabelMapFilterLM4)
itkObjectByObjectLabelMapFilterLM4___New_orig__ = _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4___New_orig__
itkObjectByObjectLabelMapFilterLM4_cast = _itkObjectByObjectLabelMapFilterPython.itkObjectByObjectLabelMapFilterLM4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def object_by_object_label_map_filter(*args: itkt.ImageLike,  filter=..., input_filter=..., output_filter=..., keep_labels: bool=..., pad_size: Sequence[int]=..., constrain_padding_to_image: bool=..., binary_internal_output: bool=..., internal_foreground_value: int=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for ObjectByObjectLabelMapFilter"""
    import itk

    kwarg_typehints = { 'filter':filter,'input_filter':input_filter,'output_filter':output_filter,'keep_labels':keep_labels,'pad_size':pad_size,'constrain_padding_to_image':constrain_padding_to_image,'binary_internal_output':binary_internal_output,'internal_foreground_value':internal_foreground_value }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.ObjectByObjectLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def object_by_object_label_map_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelMap.ObjectByObjectLabelMapFilter
    object_by_object_label_map_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    object_by_object_label_map_filter.__doc__ = filter_object.__doc__




