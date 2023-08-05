# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKIOTransformBasePython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkTransformFileReaderPython
else:
    import _itkTransformFileReaderPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkTransformFileReaderPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkTransformFileReaderPython.SWIG_PyStaticMethod_New

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
import itk.itkTransformIOBaseTemplatePython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkTransformBasePython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkVariableLengthVectorPython
import itk.itkOptimizerParametersPython
import itk.itkArrayPython
import itk.itkPointPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.itkCovariantVectorPython
import itk.vnl_matrix_fixedPython
import itk.itkArray2DPython
import itk.itkDiffusionTensor3DPython

def itkTransformFileReaderTemplateD_New():
    return itkTransformFileReaderTemplateD.New()

class itkTransformFileReaderTemplateD(itk.ITKCommonBasePython.itkLightProcessObject):
    r"""Proxy of C++ itkTransformFileReaderTemplateD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTransformFileReaderPython.itkTransformFileReaderTemplateD___New_orig__)
    Clone = _swig_new_instance_method(_itkTransformFileReaderPython.itkTransformFileReaderTemplateD_Clone)
    SetFileName = _swig_new_instance_method(_itkTransformFileReaderPython.itkTransformFileReaderTemplateD_SetFileName)
    GetFileName = _swig_new_instance_method(_itkTransformFileReaderPython.itkTransformFileReaderTemplateD_GetFileName)
    Update = _swig_new_instance_method(_itkTransformFileReaderPython.itkTransformFileReaderTemplateD_Update)
    GetTransformList = _swig_new_instance_method(_itkTransformFileReaderPython.itkTransformFileReaderTemplateD_GetTransformList)
    GetModifiableTransformList = _swig_new_instance_method(_itkTransformFileReaderPython.itkTransformFileReaderTemplateD_GetModifiableTransformList)
    SetTransformIO = _swig_new_instance_method(_itkTransformFileReaderPython.itkTransformFileReaderTemplateD_SetTransformIO)
    GetTransformIO = _swig_new_instance_method(_itkTransformFileReaderPython.itkTransformFileReaderTemplateD_GetTransformIO)
    __swig_destroy__ = _itkTransformFileReaderPython.delete_itkTransformFileReaderTemplateD
    cast = _swig_new_static_method(_itkTransformFileReaderPython.itkTransformFileReaderTemplateD_cast)

    def New(*args, **kargs):
        """New() -> itkTransformFileReaderTemplateD

        Create a new object of the class itkTransformFileReaderTemplateD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTransformFileReaderTemplateD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTransformFileReaderTemplateD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTransformFileReaderTemplateD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTransformFileReaderTemplateD in _itkTransformFileReaderPython:
_itkTransformFileReaderPython.itkTransformFileReaderTemplateD_swigregister(itkTransformFileReaderTemplateD)
itkTransformFileReaderTemplateD___New_orig__ = _itkTransformFileReaderPython.itkTransformFileReaderTemplateD___New_orig__
itkTransformFileReaderTemplateD_cast = _itkTransformFileReaderPython.itkTransformFileReaderTemplateD_cast


def itkTransformFileReaderTemplateF_New():
    return itkTransformFileReaderTemplateF.New()

class itkTransformFileReaderTemplateF(itk.ITKCommonBasePython.itkLightProcessObject):
    r"""Proxy of C++ itkTransformFileReaderTemplateF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTransformFileReaderPython.itkTransformFileReaderTemplateF___New_orig__)
    Clone = _swig_new_instance_method(_itkTransformFileReaderPython.itkTransformFileReaderTemplateF_Clone)
    SetFileName = _swig_new_instance_method(_itkTransformFileReaderPython.itkTransformFileReaderTemplateF_SetFileName)
    GetFileName = _swig_new_instance_method(_itkTransformFileReaderPython.itkTransformFileReaderTemplateF_GetFileName)
    Update = _swig_new_instance_method(_itkTransformFileReaderPython.itkTransformFileReaderTemplateF_Update)
    GetTransformList = _swig_new_instance_method(_itkTransformFileReaderPython.itkTransformFileReaderTemplateF_GetTransformList)
    GetModifiableTransformList = _swig_new_instance_method(_itkTransformFileReaderPython.itkTransformFileReaderTemplateF_GetModifiableTransformList)
    SetTransformIO = _swig_new_instance_method(_itkTransformFileReaderPython.itkTransformFileReaderTemplateF_SetTransformIO)
    GetTransformIO = _swig_new_instance_method(_itkTransformFileReaderPython.itkTransformFileReaderTemplateF_GetTransformIO)
    __swig_destroy__ = _itkTransformFileReaderPython.delete_itkTransformFileReaderTemplateF
    cast = _swig_new_static_method(_itkTransformFileReaderPython.itkTransformFileReaderTemplateF_cast)

    def New(*args, **kargs):
        """New() -> itkTransformFileReaderTemplateF

        Create a new object of the class itkTransformFileReaderTemplateF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTransformFileReaderTemplateF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTransformFileReaderTemplateF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTransformFileReaderTemplateF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTransformFileReaderTemplateF in _itkTransformFileReaderPython:
_itkTransformFileReaderPython.itkTransformFileReaderTemplateF_swigregister(itkTransformFileReaderTemplateF)
itkTransformFileReaderTemplateF___New_orig__ = _itkTransformFileReaderPython.itkTransformFileReaderTemplateF___New_orig__
itkTransformFileReaderTemplateF_cast = _itkTransformFileReaderPython.itkTransformFileReaderTemplateF_cast



