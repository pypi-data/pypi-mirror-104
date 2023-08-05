# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKLabelVotingPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkVotingBinaryHoleFillingImageFilterPython
else:
    import _itkVotingBinaryHoleFillingImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkVotingBinaryHoleFillingImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkVotingBinaryHoleFillingImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkVotingBinaryImageFilterPython
import itk.itkImageToImageFilterAPython
import itk.itkImageToImageFilterCommonPython
import itk.pyBasePython
import itk.itkVectorImagePython
import itk.itkImagePython
import itk.itkPointPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkFixedArrayPython
import itk.itkRGBPixelPython
import itk.ITKCommonBasePython
import itk.itkCovariantVectorPython
import itk.itkRGBAPixelPython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython

def itkVotingBinaryHoleFillingImageFilterISS2ISS2_New():
    return itkVotingBinaryHoleFillingImageFilterISS2ISS2.New()

class itkVotingBinaryHoleFillingImageFilterISS2ISS2(itk.itkVotingBinaryImageFilterPython.itkVotingBinaryImageFilterISS2ISS2):
    r"""


    Fills in holes and cavities by applying a voting operation on each
    pixel.

    See:  Image

    See:   VotingBinaryImageFilter

    See:   VotingBinaryIterativeHoleFillingImageFilter

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_Clone)
    GetMajorityThreshold = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_GetMajorityThreshold)
    SetMajorityThreshold = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_SetMajorityThreshold)
    GetNumberOfPixelsChanged = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_GetNumberOfPixelsChanged)
    IntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_IntConvertibleToInputCheck
    
    UnsignedIntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_UnsignedIntConvertibleToInputCheck
    
    __swig_destroy__ = _itkVotingBinaryHoleFillingImageFilterPython.delete_itkVotingBinaryHoleFillingImageFilterISS2ISS2
    cast = _swig_new_static_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkVotingBinaryHoleFillingImageFilterISS2ISS2

        Create a new object of the class itkVotingBinaryHoleFillingImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVotingBinaryHoleFillingImageFilterISS2ISS2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVotingBinaryHoleFillingImageFilterISS2ISS2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVotingBinaryHoleFillingImageFilterISS2ISS2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVotingBinaryHoleFillingImageFilterISS2ISS2 in _itkVotingBinaryHoleFillingImageFilterPython:
_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_swigregister(itkVotingBinaryHoleFillingImageFilterISS2ISS2)
itkVotingBinaryHoleFillingImageFilterISS2ISS2___New_orig__ = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2___New_orig__
itkVotingBinaryHoleFillingImageFilterISS2ISS2_cast = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS2ISS2_cast


def itkVotingBinaryHoleFillingImageFilterISS3ISS3_New():
    return itkVotingBinaryHoleFillingImageFilterISS3ISS3.New()

class itkVotingBinaryHoleFillingImageFilterISS3ISS3(itk.itkVotingBinaryImageFilterPython.itkVotingBinaryImageFilterISS3ISS3):
    r"""


    Fills in holes and cavities by applying a voting operation on each
    pixel.

    See:  Image

    See:   VotingBinaryImageFilter

    See:   VotingBinaryIterativeHoleFillingImageFilter

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_Clone)
    GetMajorityThreshold = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_GetMajorityThreshold)
    SetMajorityThreshold = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_SetMajorityThreshold)
    GetNumberOfPixelsChanged = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_GetNumberOfPixelsChanged)
    IntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_IntConvertibleToInputCheck
    
    UnsignedIntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_UnsignedIntConvertibleToInputCheck
    
    __swig_destroy__ = _itkVotingBinaryHoleFillingImageFilterPython.delete_itkVotingBinaryHoleFillingImageFilterISS3ISS3
    cast = _swig_new_static_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkVotingBinaryHoleFillingImageFilterISS3ISS3

        Create a new object of the class itkVotingBinaryHoleFillingImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVotingBinaryHoleFillingImageFilterISS3ISS3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVotingBinaryHoleFillingImageFilterISS3ISS3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVotingBinaryHoleFillingImageFilterISS3ISS3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVotingBinaryHoleFillingImageFilterISS3ISS3 in _itkVotingBinaryHoleFillingImageFilterPython:
_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_swigregister(itkVotingBinaryHoleFillingImageFilterISS3ISS3)
itkVotingBinaryHoleFillingImageFilterISS3ISS3___New_orig__ = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3___New_orig__
itkVotingBinaryHoleFillingImageFilterISS3ISS3_cast = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS3ISS3_cast


def itkVotingBinaryHoleFillingImageFilterISS4ISS4_New():
    return itkVotingBinaryHoleFillingImageFilterISS4ISS4.New()

class itkVotingBinaryHoleFillingImageFilterISS4ISS4(itk.itkVotingBinaryImageFilterPython.itkVotingBinaryImageFilterISS4ISS4):
    r"""


    Fills in holes and cavities by applying a voting operation on each
    pixel.

    See:  Image

    See:   VotingBinaryImageFilter

    See:   VotingBinaryIterativeHoleFillingImageFilter

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS4ISS4___New_orig__)
    Clone = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS4ISS4_Clone)
    GetMajorityThreshold = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS4ISS4_GetMajorityThreshold)
    SetMajorityThreshold = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS4ISS4_SetMajorityThreshold)
    GetNumberOfPixelsChanged = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS4ISS4_GetNumberOfPixelsChanged)
    IntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS4ISS4_IntConvertibleToInputCheck
    
    UnsignedIntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS4ISS4_UnsignedIntConvertibleToInputCheck
    
    __swig_destroy__ = _itkVotingBinaryHoleFillingImageFilterPython.delete_itkVotingBinaryHoleFillingImageFilterISS4ISS4
    cast = _swig_new_static_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS4ISS4_cast)

    def New(*args, **kargs):
        """New() -> itkVotingBinaryHoleFillingImageFilterISS4ISS4

        Create a new object of the class itkVotingBinaryHoleFillingImageFilterISS4ISS4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVotingBinaryHoleFillingImageFilterISS4ISS4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVotingBinaryHoleFillingImageFilterISS4ISS4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVotingBinaryHoleFillingImageFilterISS4ISS4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVotingBinaryHoleFillingImageFilterISS4ISS4 in _itkVotingBinaryHoleFillingImageFilterPython:
_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS4ISS4_swigregister(itkVotingBinaryHoleFillingImageFilterISS4ISS4)
itkVotingBinaryHoleFillingImageFilterISS4ISS4___New_orig__ = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS4ISS4___New_orig__
itkVotingBinaryHoleFillingImageFilterISS4ISS4_cast = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterISS4ISS4_cast


def itkVotingBinaryHoleFillingImageFilterIUC2IUC2_New():
    return itkVotingBinaryHoleFillingImageFilterIUC2IUC2.New()

class itkVotingBinaryHoleFillingImageFilterIUC2IUC2(itk.itkVotingBinaryImageFilterPython.itkVotingBinaryImageFilterIUC2IUC2):
    r"""


    Fills in holes and cavities by applying a voting operation on each
    pixel.

    See:  Image

    See:   VotingBinaryImageFilter

    See:   VotingBinaryIterativeHoleFillingImageFilter

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_Clone)
    GetMajorityThreshold = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_GetMajorityThreshold)
    SetMajorityThreshold = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_SetMajorityThreshold)
    GetNumberOfPixelsChanged = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_GetNumberOfPixelsChanged)
    IntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_IntConvertibleToInputCheck
    
    UnsignedIntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_UnsignedIntConvertibleToInputCheck
    
    __swig_destroy__ = _itkVotingBinaryHoleFillingImageFilterPython.delete_itkVotingBinaryHoleFillingImageFilterIUC2IUC2
    cast = _swig_new_static_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkVotingBinaryHoleFillingImageFilterIUC2IUC2

        Create a new object of the class itkVotingBinaryHoleFillingImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVotingBinaryHoleFillingImageFilterIUC2IUC2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVotingBinaryHoleFillingImageFilterIUC2IUC2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVotingBinaryHoleFillingImageFilterIUC2IUC2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVotingBinaryHoleFillingImageFilterIUC2IUC2 in _itkVotingBinaryHoleFillingImageFilterPython:
_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_swigregister(itkVotingBinaryHoleFillingImageFilterIUC2IUC2)
itkVotingBinaryHoleFillingImageFilterIUC2IUC2___New_orig__ = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2___New_orig__
itkVotingBinaryHoleFillingImageFilterIUC2IUC2_cast = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC2IUC2_cast


def itkVotingBinaryHoleFillingImageFilterIUC3IUC3_New():
    return itkVotingBinaryHoleFillingImageFilterIUC3IUC3.New()

class itkVotingBinaryHoleFillingImageFilterIUC3IUC3(itk.itkVotingBinaryImageFilterPython.itkVotingBinaryImageFilterIUC3IUC3):
    r"""


    Fills in holes and cavities by applying a voting operation on each
    pixel.

    See:  Image

    See:   VotingBinaryImageFilter

    See:   VotingBinaryIterativeHoleFillingImageFilter

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_Clone)
    GetMajorityThreshold = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_GetMajorityThreshold)
    SetMajorityThreshold = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_SetMajorityThreshold)
    GetNumberOfPixelsChanged = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_GetNumberOfPixelsChanged)
    IntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_IntConvertibleToInputCheck
    
    UnsignedIntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_UnsignedIntConvertibleToInputCheck
    
    __swig_destroy__ = _itkVotingBinaryHoleFillingImageFilterPython.delete_itkVotingBinaryHoleFillingImageFilterIUC3IUC3
    cast = _swig_new_static_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkVotingBinaryHoleFillingImageFilterIUC3IUC3

        Create a new object of the class itkVotingBinaryHoleFillingImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVotingBinaryHoleFillingImageFilterIUC3IUC3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVotingBinaryHoleFillingImageFilterIUC3IUC3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVotingBinaryHoleFillingImageFilterIUC3IUC3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVotingBinaryHoleFillingImageFilterIUC3IUC3 in _itkVotingBinaryHoleFillingImageFilterPython:
_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_swigregister(itkVotingBinaryHoleFillingImageFilterIUC3IUC3)
itkVotingBinaryHoleFillingImageFilterIUC3IUC3___New_orig__ = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3___New_orig__
itkVotingBinaryHoleFillingImageFilterIUC3IUC3_cast = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC3IUC3_cast


def itkVotingBinaryHoleFillingImageFilterIUC4IUC4_New():
    return itkVotingBinaryHoleFillingImageFilterIUC4IUC4.New()

class itkVotingBinaryHoleFillingImageFilterIUC4IUC4(itk.itkVotingBinaryImageFilterPython.itkVotingBinaryImageFilterIUC4IUC4):
    r"""


    Fills in holes and cavities by applying a voting operation on each
    pixel.

    See:  Image

    See:   VotingBinaryImageFilter

    See:   VotingBinaryIterativeHoleFillingImageFilter

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC4IUC4___New_orig__)
    Clone = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC4IUC4_Clone)
    GetMajorityThreshold = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC4IUC4_GetMajorityThreshold)
    SetMajorityThreshold = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC4IUC4_SetMajorityThreshold)
    GetNumberOfPixelsChanged = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC4IUC4_GetNumberOfPixelsChanged)
    IntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC4IUC4_IntConvertibleToInputCheck
    
    UnsignedIntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC4IUC4_UnsignedIntConvertibleToInputCheck
    
    __swig_destroy__ = _itkVotingBinaryHoleFillingImageFilterPython.delete_itkVotingBinaryHoleFillingImageFilterIUC4IUC4
    cast = _swig_new_static_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC4IUC4_cast)

    def New(*args, **kargs):
        """New() -> itkVotingBinaryHoleFillingImageFilterIUC4IUC4

        Create a new object of the class itkVotingBinaryHoleFillingImageFilterIUC4IUC4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVotingBinaryHoleFillingImageFilterIUC4IUC4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVotingBinaryHoleFillingImageFilterIUC4IUC4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVotingBinaryHoleFillingImageFilterIUC4IUC4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVotingBinaryHoleFillingImageFilterIUC4IUC4 in _itkVotingBinaryHoleFillingImageFilterPython:
_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC4IUC4_swigregister(itkVotingBinaryHoleFillingImageFilterIUC4IUC4)
itkVotingBinaryHoleFillingImageFilterIUC4IUC4___New_orig__ = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC4IUC4___New_orig__
itkVotingBinaryHoleFillingImageFilterIUC4IUC4_cast = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUC4IUC4_cast


def itkVotingBinaryHoleFillingImageFilterIUS2IUS2_New():
    return itkVotingBinaryHoleFillingImageFilterIUS2IUS2.New()

class itkVotingBinaryHoleFillingImageFilterIUS2IUS2(itk.itkVotingBinaryImageFilterPython.itkVotingBinaryImageFilterIUS2IUS2):
    r"""


    Fills in holes and cavities by applying a voting operation on each
    pixel.

    See:  Image

    See:   VotingBinaryImageFilter

    See:   VotingBinaryIterativeHoleFillingImageFilter

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS2IUS2_Clone)
    GetMajorityThreshold = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS2IUS2_GetMajorityThreshold)
    SetMajorityThreshold = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS2IUS2_SetMajorityThreshold)
    GetNumberOfPixelsChanged = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS2IUS2_GetNumberOfPixelsChanged)
    IntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS2IUS2_IntConvertibleToInputCheck
    
    UnsignedIntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS2IUS2_UnsignedIntConvertibleToInputCheck
    
    __swig_destroy__ = _itkVotingBinaryHoleFillingImageFilterPython.delete_itkVotingBinaryHoleFillingImageFilterIUS2IUS2
    cast = _swig_new_static_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkVotingBinaryHoleFillingImageFilterIUS2IUS2

        Create a new object of the class itkVotingBinaryHoleFillingImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVotingBinaryHoleFillingImageFilterIUS2IUS2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVotingBinaryHoleFillingImageFilterIUS2IUS2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVotingBinaryHoleFillingImageFilterIUS2IUS2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVotingBinaryHoleFillingImageFilterIUS2IUS2 in _itkVotingBinaryHoleFillingImageFilterPython:
_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS2IUS2_swigregister(itkVotingBinaryHoleFillingImageFilterIUS2IUS2)
itkVotingBinaryHoleFillingImageFilterIUS2IUS2___New_orig__ = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS2IUS2___New_orig__
itkVotingBinaryHoleFillingImageFilterIUS2IUS2_cast = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS2IUS2_cast


def itkVotingBinaryHoleFillingImageFilterIUS3IUS3_New():
    return itkVotingBinaryHoleFillingImageFilterIUS3IUS3.New()

class itkVotingBinaryHoleFillingImageFilterIUS3IUS3(itk.itkVotingBinaryImageFilterPython.itkVotingBinaryImageFilterIUS3IUS3):
    r"""


    Fills in holes and cavities by applying a voting operation on each
    pixel.

    See:  Image

    See:   VotingBinaryImageFilter

    See:   VotingBinaryIterativeHoleFillingImageFilter

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS3IUS3_Clone)
    GetMajorityThreshold = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS3IUS3_GetMajorityThreshold)
    SetMajorityThreshold = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS3IUS3_SetMajorityThreshold)
    GetNumberOfPixelsChanged = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS3IUS3_GetNumberOfPixelsChanged)
    IntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS3IUS3_IntConvertibleToInputCheck
    
    UnsignedIntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS3IUS3_UnsignedIntConvertibleToInputCheck
    
    __swig_destroy__ = _itkVotingBinaryHoleFillingImageFilterPython.delete_itkVotingBinaryHoleFillingImageFilterIUS3IUS3
    cast = _swig_new_static_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkVotingBinaryHoleFillingImageFilterIUS3IUS3

        Create a new object of the class itkVotingBinaryHoleFillingImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVotingBinaryHoleFillingImageFilterIUS3IUS3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVotingBinaryHoleFillingImageFilterIUS3IUS3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVotingBinaryHoleFillingImageFilterIUS3IUS3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVotingBinaryHoleFillingImageFilterIUS3IUS3 in _itkVotingBinaryHoleFillingImageFilterPython:
_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS3IUS3_swigregister(itkVotingBinaryHoleFillingImageFilterIUS3IUS3)
itkVotingBinaryHoleFillingImageFilterIUS3IUS3___New_orig__ = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS3IUS3___New_orig__
itkVotingBinaryHoleFillingImageFilterIUS3IUS3_cast = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS3IUS3_cast


def itkVotingBinaryHoleFillingImageFilterIUS4IUS4_New():
    return itkVotingBinaryHoleFillingImageFilterIUS4IUS4.New()

class itkVotingBinaryHoleFillingImageFilterIUS4IUS4(itk.itkVotingBinaryImageFilterPython.itkVotingBinaryImageFilterIUS4IUS4):
    r"""


    Fills in holes and cavities by applying a voting operation on each
    pixel.

    See:  Image

    See:   VotingBinaryImageFilter

    See:   VotingBinaryIterativeHoleFillingImageFilter

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS4IUS4___New_orig__)
    Clone = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS4IUS4_Clone)
    GetMajorityThreshold = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS4IUS4_GetMajorityThreshold)
    SetMajorityThreshold = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS4IUS4_SetMajorityThreshold)
    GetNumberOfPixelsChanged = _swig_new_instance_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS4IUS4_GetNumberOfPixelsChanged)
    IntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS4IUS4_IntConvertibleToInputCheck
    
    UnsignedIntConvertibleToInputCheck = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS4IUS4_UnsignedIntConvertibleToInputCheck
    
    __swig_destroy__ = _itkVotingBinaryHoleFillingImageFilterPython.delete_itkVotingBinaryHoleFillingImageFilterIUS4IUS4
    cast = _swig_new_static_method(_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS4IUS4_cast)

    def New(*args, **kargs):
        """New() -> itkVotingBinaryHoleFillingImageFilterIUS4IUS4

        Create a new object of the class itkVotingBinaryHoleFillingImageFilterIUS4IUS4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVotingBinaryHoleFillingImageFilterIUS4IUS4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVotingBinaryHoleFillingImageFilterIUS4IUS4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVotingBinaryHoleFillingImageFilterIUS4IUS4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVotingBinaryHoleFillingImageFilterIUS4IUS4 in _itkVotingBinaryHoleFillingImageFilterPython:
_itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS4IUS4_swigregister(itkVotingBinaryHoleFillingImageFilterIUS4IUS4)
itkVotingBinaryHoleFillingImageFilterIUS4IUS4___New_orig__ = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS4IUS4___New_orig__
itkVotingBinaryHoleFillingImageFilterIUS4IUS4_cast = _itkVotingBinaryHoleFillingImageFilterPython.itkVotingBinaryHoleFillingImageFilterIUS4IUS4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def voting_binary_hole_filling_image_filter(*args: itkt.ImageLike,  majority_threshold: int=..., birth_threshold: int=..., survival_threshold: int=..., radius: Sequence[int]=..., background_value: int=..., foreground_value: int=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for VotingBinaryHoleFillingImageFilter"""
    import itk

    kwarg_typehints = { 'majority_threshold':majority_threshold,'birth_threshold':birth_threshold,'survival_threshold':survival_threshold,'radius':radius,'background_value':background_value,'foreground_value':foreground_value }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] != ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.VotingBinaryHoleFillingImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def voting_binary_hole_filling_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelVoting.VotingBinaryHoleFillingImageFilter
    voting_binary_hole_filling_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    voting_binary_hole_filling_image_filter.__doc__ = filter_object.__doc__




