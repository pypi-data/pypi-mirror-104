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
    from . import _itkLabelObjectPython
else:
    import _itkLabelObjectPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkLabelObjectPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkLabelObjectPython.SWIG_PyStaticMethod_New

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
import itk.itkOffsetPython
import itk.itkSizePython
import itk.pyBasePython
import itk.itkLabelObjectLinePython
import itk.itkIndexPython
import itk.ITKCommonBasePython

def itkLabelObjectUL2_New():
    return itkLabelObjectUL2.New()

class itkLabelObjectUL2(itk.ITKCommonBasePython.itkLightObject):
    r"""


    The base class for the representation of an labeled binary object in
    an image.

    LabelObject is the base class to represent a labeled object in an
    image. It should be used associated with the LabelMap.

    LabelObject store mainly 2 things: the label of the object, and a set
    of lines which are part of the object. No attribute is available in
    that class, so this class can be used as a base class to implement a
    label object with attribute, or when no attribute is needed (see the
    reconstruction filters for an example. If a simple attribute is
    needed, AttributeLabelObject can be used directly.

    All the subclasses of LabelObject have to reimplement the
    CopyAttributesFrom() and CopyAllFrom() method. No need to reimplement
    CopyLinesFrom() since all derived class share the same type line data
    members.

    The pixels locations belonging to the LabelObject can be obtained
    using:

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:http://www.insight-
    journal.org/browse/publication/176

    See:   LabelMapFilter, AttributeLabelObject 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelObjectPython.itkLabelObjectUL2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_Clone)
    GetAttributeFromName = _swig_new_static_method(_itkLabelObjectPython.itkLabelObjectUL2_GetAttributeFromName)
    GetNameFromAttribute = _swig_new_static_method(_itkLabelObjectPython.itkLabelObjectUL2_GetNameFromAttribute)
    GetLabel = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_GetLabel)
    SetLabel = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_SetLabel)
    HasIndex = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_HasIndex)
    AddIndex = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_AddIndex)
    RemoveIndex = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_RemoveIndex)
    AddLine = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_AddLine)
    GetNumberOfLines = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_GetNumberOfLines)
    GetLine = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_GetLine)
    Size = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_Size)
    Empty = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_Empty)
    Clear = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_Clear)
    GetIndex = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_GetIndex)
    Optimize = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_Optimize)
    Shift = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL2_Shift)
    __swig_destroy__ = _itkLabelObjectPython.delete_itkLabelObjectUL2
    cast = _swig_new_static_method(_itkLabelObjectPython.itkLabelObjectUL2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelObjectUL2

        Create a new object of the class itkLabelObjectUL2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelObjectUL2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelObjectUL2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelObjectUL2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelObjectUL2 in _itkLabelObjectPython:
_itkLabelObjectPython.itkLabelObjectUL2_swigregister(itkLabelObjectUL2)
itkLabelObjectUL2___New_orig__ = _itkLabelObjectPython.itkLabelObjectUL2___New_orig__
itkLabelObjectUL2_GetAttributeFromName = _itkLabelObjectPython.itkLabelObjectUL2_GetAttributeFromName
itkLabelObjectUL2_GetNameFromAttribute = _itkLabelObjectPython.itkLabelObjectUL2_GetNameFromAttribute
itkLabelObjectUL2_cast = _itkLabelObjectPython.itkLabelObjectUL2_cast


def itkLabelObjectUL3_New():
    return itkLabelObjectUL3.New()

class itkLabelObjectUL3(itk.ITKCommonBasePython.itkLightObject):
    r"""


    The base class for the representation of an labeled binary object in
    an image.

    LabelObject is the base class to represent a labeled object in an
    image. It should be used associated with the LabelMap.

    LabelObject store mainly 2 things: the label of the object, and a set
    of lines which are part of the object. No attribute is available in
    that class, so this class can be used as a base class to implement a
    label object with attribute, or when no attribute is needed (see the
    reconstruction filters for an example. If a simple attribute is
    needed, AttributeLabelObject can be used directly.

    All the subclasses of LabelObject have to reimplement the
    CopyAttributesFrom() and CopyAllFrom() method. No need to reimplement
    CopyLinesFrom() since all derived class share the same type line data
    members.

    The pixels locations belonging to the LabelObject can be obtained
    using:

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:http://www.insight-
    journal.org/browse/publication/176

    See:   LabelMapFilter, AttributeLabelObject 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelObjectPython.itkLabelObjectUL3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_Clone)
    GetAttributeFromName = _swig_new_static_method(_itkLabelObjectPython.itkLabelObjectUL3_GetAttributeFromName)
    GetNameFromAttribute = _swig_new_static_method(_itkLabelObjectPython.itkLabelObjectUL3_GetNameFromAttribute)
    GetLabel = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_GetLabel)
    SetLabel = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_SetLabel)
    HasIndex = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_HasIndex)
    AddIndex = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_AddIndex)
    RemoveIndex = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_RemoveIndex)
    AddLine = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_AddLine)
    GetNumberOfLines = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_GetNumberOfLines)
    GetLine = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_GetLine)
    Size = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_Size)
    Empty = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_Empty)
    Clear = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_Clear)
    GetIndex = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_GetIndex)
    Optimize = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_Optimize)
    Shift = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL3_Shift)
    __swig_destroy__ = _itkLabelObjectPython.delete_itkLabelObjectUL3
    cast = _swig_new_static_method(_itkLabelObjectPython.itkLabelObjectUL3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelObjectUL3

        Create a new object of the class itkLabelObjectUL3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelObjectUL3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelObjectUL3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelObjectUL3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelObjectUL3 in _itkLabelObjectPython:
_itkLabelObjectPython.itkLabelObjectUL3_swigregister(itkLabelObjectUL3)
itkLabelObjectUL3___New_orig__ = _itkLabelObjectPython.itkLabelObjectUL3___New_orig__
itkLabelObjectUL3_GetAttributeFromName = _itkLabelObjectPython.itkLabelObjectUL3_GetAttributeFromName
itkLabelObjectUL3_GetNameFromAttribute = _itkLabelObjectPython.itkLabelObjectUL3_GetNameFromAttribute
itkLabelObjectUL3_cast = _itkLabelObjectPython.itkLabelObjectUL3_cast


def itkLabelObjectUL4_New():
    return itkLabelObjectUL4.New()

class itkLabelObjectUL4(itk.ITKCommonBasePython.itkLightObject):
    r"""


    The base class for the representation of an labeled binary object in
    an image.

    LabelObject is the base class to represent a labeled object in an
    image. It should be used associated with the LabelMap.

    LabelObject store mainly 2 things: the label of the object, and a set
    of lines which are part of the object. No attribute is available in
    that class, so this class can be used as a base class to implement a
    label object with attribute, or when no attribute is needed (see the
    reconstruction filters for an example. If a simple attribute is
    needed, AttributeLabelObject can be used directly.

    All the subclasses of LabelObject have to reimplement the
    CopyAttributesFrom() and CopyAllFrom() method. No need to reimplement
    CopyLinesFrom() since all derived class share the same type line data
    members.

    The pixels locations belonging to the LabelObject can be obtained
    using:

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:http://www.insight-
    journal.org/browse/publication/176

    See:   LabelMapFilter, AttributeLabelObject 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelObjectPython.itkLabelObjectUL4___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL4_Clone)
    GetAttributeFromName = _swig_new_static_method(_itkLabelObjectPython.itkLabelObjectUL4_GetAttributeFromName)
    GetNameFromAttribute = _swig_new_static_method(_itkLabelObjectPython.itkLabelObjectUL4_GetNameFromAttribute)
    GetLabel = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL4_GetLabel)
    SetLabel = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL4_SetLabel)
    HasIndex = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL4_HasIndex)
    AddIndex = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL4_AddIndex)
    RemoveIndex = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL4_RemoveIndex)
    AddLine = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL4_AddLine)
    GetNumberOfLines = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL4_GetNumberOfLines)
    GetLine = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL4_GetLine)
    Size = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL4_Size)
    Empty = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL4_Empty)
    Clear = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL4_Clear)
    GetIndex = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL4_GetIndex)
    Optimize = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL4_Optimize)
    Shift = _swig_new_instance_method(_itkLabelObjectPython.itkLabelObjectUL4_Shift)
    __swig_destroy__ = _itkLabelObjectPython.delete_itkLabelObjectUL4
    cast = _swig_new_static_method(_itkLabelObjectPython.itkLabelObjectUL4_cast)

    def New(*args, **kargs):
        """New() -> itkLabelObjectUL4

        Create a new object of the class itkLabelObjectUL4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelObjectUL4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelObjectUL4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelObjectUL4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelObjectUL4 in _itkLabelObjectPython:
_itkLabelObjectPython.itkLabelObjectUL4_swigregister(itkLabelObjectUL4)
itkLabelObjectUL4___New_orig__ = _itkLabelObjectPython.itkLabelObjectUL4___New_orig__
itkLabelObjectUL4_GetAttributeFromName = _itkLabelObjectPython.itkLabelObjectUL4_GetAttributeFromName
itkLabelObjectUL4_GetNameFromAttribute = _itkLabelObjectPython.itkLabelObjectUL4_GetNameFromAttribute
itkLabelObjectUL4_cast = _itkLabelObjectPython.itkLabelObjectUL4_cast



