# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKSignedDistanceFunctionPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkShapeSignedDistanceFunctionPython
else:
    import _itkShapeSignedDistanceFunctionPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkShapeSignedDistanceFunctionPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkShapeSignedDistanceFunctionPython.SWIG_PyStaticMethod_New

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
import itk.itkSpatialFunctionPython
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.itkFunctionBasePython
import itk.itkRGBPixelPython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkSizePython
import itk.itkOffsetPython
import itk.ITKCommonBasePython
import itk.itkImagePython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkImageRegionPython
import itk.itkRGBAPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkArrayPython
import itk.itkOptimizerParametersPython
class itkShapeSignedDistanceFunctionD2(itk.itkSpatialFunctionPython.itkSpatialFunctionD2PD2):
    r"""


    Base class for functions which evaluates the signed distance from a
    shape.

    ShapeSignedDistanceFunction is the base class for functions which
    returns the signed distance from a shape at an arbitrary point. A
    shape assumed to be defined by a set of shape and pose parameters.

    Note that Initialize() must be called before use. This allows the
    class an opportunity to validate any inputs.

    This class is templated over the coordinate representation type (e.g.
    float or double) and the space dimension.

    ShapeSignedDistanceFunction is used to encapsulate the shape prior in
    ShapePriorSegmentationLevelSetFunctions.

    See:  SpatialFunction

    See:  ShapePriorSegmentationLevelSetFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetParameters = _swig_new_instance_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD2_SetParameters)
    GetParameters = _swig_new_instance_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD2_GetParameters)
    GetNumberOfShapeParameters = _swig_new_instance_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD2_GetNumberOfShapeParameters)
    GetNumberOfPoseParameters = _swig_new_instance_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD2_GetNumberOfPoseParameters)
    GetNumberOfParameters = _swig_new_instance_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD2_GetNumberOfParameters)
    Initialize = _swig_new_instance_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD2_Initialize)
    __swig_destroy__ = _itkShapeSignedDistanceFunctionPython.delete_itkShapeSignedDistanceFunctionD2
    cast = _swig_new_static_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD2_cast)

# Register itkShapeSignedDistanceFunctionD2 in _itkShapeSignedDistanceFunctionPython:
_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD2_swigregister(itkShapeSignedDistanceFunctionD2)
itkShapeSignedDistanceFunctionD2_cast = _itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD2_cast

class itkShapeSignedDistanceFunctionD3(itk.itkSpatialFunctionPython.itkSpatialFunctionD3PD3):
    r"""


    Base class for functions which evaluates the signed distance from a
    shape.

    ShapeSignedDistanceFunction is the base class for functions which
    returns the signed distance from a shape at an arbitrary point. A
    shape assumed to be defined by a set of shape and pose parameters.

    Note that Initialize() must be called before use. This allows the
    class an opportunity to validate any inputs.

    This class is templated over the coordinate representation type (e.g.
    float or double) and the space dimension.

    ShapeSignedDistanceFunction is used to encapsulate the shape prior in
    ShapePriorSegmentationLevelSetFunctions.

    See:  SpatialFunction

    See:  ShapePriorSegmentationLevelSetFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetParameters = _swig_new_instance_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD3_SetParameters)
    GetParameters = _swig_new_instance_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD3_GetParameters)
    GetNumberOfShapeParameters = _swig_new_instance_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD3_GetNumberOfShapeParameters)
    GetNumberOfPoseParameters = _swig_new_instance_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD3_GetNumberOfPoseParameters)
    GetNumberOfParameters = _swig_new_instance_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD3_GetNumberOfParameters)
    Initialize = _swig_new_instance_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD3_Initialize)
    __swig_destroy__ = _itkShapeSignedDistanceFunctionPython.delete_itkShapeSignedDistanceFunctionD3
    cast = _swig_new_static_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD3_cast)

# Register itkShapeSignedDistanceFunctionD3 in _itkShapeSignedDistanceFunctionPython:
_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD3_swigregister(itkShapeSignedDistanceFunctionD3)
itkShapeSignedDistanceFunctionD3_cast = _itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD3_cast

class itkShapeSignedDistanceFunctionD4(itk.itkSpatialFunctionPython.itkSpatialFunctionD4PD4):
    r"""


    Base class for functions which evaluates the signed distance from a
    shape.

    ShapeSignedDistanceFunction is the base class for functions which
    returns the signed distance from a shape at an arbitrary point. A
    shape assumed to be defined by a set of shape and pose parameters.

    Note that Initialize() must be called before use. This allows the
    class an opportunity to validate any inputs.

    This class is templated over the coordinate representation type (e.g.
    float or double) and the space dimension.

    ShapeSignedDistanceFunction is used to encapsulate the shape prior in
    ShapePriorSegmentationLevelSetFunctions.

    See:  SpatialFunction

    See:  ShapePriorSegmentationLevelSetFunction 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetParameters = _swig_new_instance_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD4_SetParameters)
    GetParameters = _swig_new_instance_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD4_GetParameters)
    GetNumberOfShapeParameters = _swig_new_instance_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD4_GetNumberOfShapeParameters)
    GetNumberOfPoseParameters = _swig_new_instance_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD4_GetNumberOfPoseParameters)
    GetNumberOfParameters = _swig_new_instance_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD4_GetNumberOfParameters)
    Initialize = _swig_new_instance_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD4_Initialize)
    __swig_destroy__ = _itkShapeSignedDistanceFunctionPython.delete_itkShapeSignedDistanceFunctionD4
    cast = _swig_new_static_method(_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD4_cast)

# Register itkShapeSignedDistanceFunctionD4 in _itkShapeSignedDistanceFunctionPython:
_itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD4_swigregister(itkShapeSignedDistanceFunctionD4)
itkShapeSignedDistanceFunctionD4_cast = _itkShapeSignedDistanceFunctionPython.itkShapeSignedDistanceFunctionD4_cast



