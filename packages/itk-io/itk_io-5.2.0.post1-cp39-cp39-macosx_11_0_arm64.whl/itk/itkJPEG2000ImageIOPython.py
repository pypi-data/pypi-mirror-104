# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKIOJPEG2000Python



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkJPEG2000ImageIOPython
else:
    import _itkJPEG2000ImageIOPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkJPEG2000ImageIOPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkJPEG2000ImageIOPython.SWIG_PyStaticMethod_New

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
import itk.ITKIOImageBaseBasePython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython

def itkJPEG2000ImageIO_New():
    return itkJPEG2000ImageIO.New()

class itkJPEG2000ImageIO(itk.ITKIOImageBaseBasePython.itkStreamingImageIOBase):
    r"""


    Supports for the JPEG2000 file format based on openjpeg.

    JPEG2000 offers a large collection of interesting features including:
    compression (lossless and lossy), streaming, multi-channel images.

    This code was contributed in the Insight Journal paper: "Support for
    Streaming the JPEG2000 File Format" by Mosaliganti K., Ibanez L.,
    Megason Shttps://www.insight-journal.org/browse/publication/741 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkJPEG2000ImageIOPython.itkJPEG2000ImageIO___New_orig__)
    Clone = _swig_new_instance_method(_itkJPEG2000ImageIOPython.itkJPEG2000ImageIO_Clone)
    GetHeaderSize = _swig_new_instance_method(_itkJPEG2000ImageIOPython.itkJPEG2000ImageIO_GetHeaderSize)
    SetTileSize = _swig_new_instance_method(_itkJPEG2000ImageIOPython.itkJPEG2000ImageIO_SetTileSize)
    __swig_destroy__ = _itkJPEG2000ImageIOPython.delete_itkJPEG2000ImageIO
    cast = _swig_new_static_method(_itkJPEG2000ImageIOPython.itkJPEG2000ImageIO_cast)

    def New(*args, **kargs):
        """New() -> itkJPEG2000ImageIO

        Create a new object of the class itkJPEG2000ImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkJPEG2000ImageIO.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkJPEG2000ImageIO.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkJPEG2000ImageIO.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkJPEG2000ImageIO in _itkJPEG2000ImageIOPython:
_itkJPEG2000ImageIOPython.itkJPEG2000ImageIO_swigregister(itkJPEG2000ImageIO)
itkJPEG2000ImageIO___New_orig__ = _itkJPEG2000ImageIOPython.itkJPEG2000ImageIO___New_orig__
itkJPEG2000ImageIO_cast = _itkJPEG2000ImageIOPython.itkJPEG2000ImageIO_cast


def itkJPEG2000ImageIOFactory_New():
    return itkJPEG2000ImageIOFactory.New()

class itkJPEG2000ImageIOFactory(itk.ITKCommonBasePython.itkObjectFactoryBase):
    r"""


    Supports for the JPEG2000 file format based on openjpeg.

    This code was contributed in the Insight Journal paper: "Support for
    Streaming the JPEG2000 File Format" by Mosaliganti K., Ibanez L.,
    Megason Shttps://www.insight-journal.org/browse/publication/741

    JPEG2000 offers a large collection of interesting features including:
    compression (lossless and lossy), streaming, multi-channel images. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkJPEG2000ImageIOPython.itkJPEG2000ImageIOFactory___New_orig__)
    FactoryNew = _swig_new_static_method(_itkJPEG2000ImageIOPython.itkJPEG2000ImageIOFactory_FactoryNew)
    RegisterOneFactory = _swig_new_static_method(_itkJPEG2000ImageIOPython.itkJPEG2000ImageIOFactory_RegisterOneFactory)
    __swig_destroy__ = _itkJPEG2000ImageIOPython.delete_itkJPEG2000ImageIOFactory
    cast = _swig_new_static_method(_itkJPEG2000ImageIOPython.itkJPEG2000ImageIOFactory_cast)

    def New(*args, **kargs):
        """New() -> itkJPEG2000ImageIOFactory

        Create a new object of the class itkJPEG2000ImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkJPEG2000ImageIOFactory.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkJPEG2000ImageIOFactory.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkJPEG2000ImageIOFactory.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkJPEG2000ImageIOFactory in _itkJPEG2000ImageIOPython:
_itkJPEG2000ImageIOPython.itkJPEG2000ImageIOFactory_swigregister(itkJPEG2000ImageIOFactory)
itkJPEG2000ImageIOFactory___New_orig__ = _itkJPEG2000ImageIOPython.itkJPEG2000ImageIOFactory___New_orig__
itkJPEG2000ImageIOFactory_FactoryNew = _itkJPEG2000ImageIOPython.itkJPEG2000ImageIOFactory_FactoryNew
itkJPEG2000ImageIOFactory_RegisterOneFactory = _itkJPEG2000ImageIOPython.itkJPEG2000ImageIOFactory_RegisterOneFactory
itkJPEG2000ImageIOFactory_cast = _itkJPEG2000ImageIOPython.itkJPEG2000ImageIOFactory_cast

class itkJPEG2000ImageIOInternalEnums(object):
    r"""Proxy of C++ itkJPEG2000ImageIOInternalEnums class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    DecodingFormat_J2K_CFMT = _itkJPEG2000ImageIOPython.itkJPEG2000ImageIOInternalEnums_DecodingFormat_J2K_CFMT
    
    DecodingFormat_JP2_CFMT = _itkJPEG2000ImageIOPython.itkJPEG2000ImageIOInternalEnums_DecodingFormat_JP2_CFMT
    
    DecodingFormat_JPT_CFMT = _itkJPEG2000ImageIOPython.itkJPEG2000ImageIOInternalEnums_DecodingFormat_JPT_CFMT
    
    DecodingFormat_MJ2_CFMT = _itkJPEG2000ImageIOPython.itkJPEG2000ImageIOInternalEnums_DecodingFormat_MJ2_CFMT
    
    DFMFormat_PXM_DFMT = _itkJPEG2000ImageIOPython.itkJPEG2000ImageIOInternalEnums_DFMFormat_PXM_DFMT
    
    DFMFormat_PGX_DFMT = _itkJPEG2000ImageIOPython.itkJPEG2000ImageIOInternalEnums_DFMFormat_PGX_DFMT
    
    DFMFormat_BMP_DFMT = _itkJPEG2000ImageIOPython.itkJPEG2000ImageIOInternalEnums_DFMFormat_BMP_DFMT
    
    DFMFormat_YUV_DFMT = _itkJPEG2000ImageIOPython.itkJPEG2000ImageIOInternalEnums_DFMFormat_YUV_DFMT
    

    def __init__(self, *args):
        r"""
        __init__(self) -> itkJPEG2000ImageIOInternalEnums
        __init__(self, arg0) -> itkJPEG2000ImageIOInternalEnums

        Parameters
        ----------
        arg0: itkJPEG2000ImageIOInternalEnums const &

        """
        _itkJPEG2000ImageIOPython.itkJPEG2000ImageIOInternalEnums_swiginit(self, _itkJPEG2000ImageIOPython.new_itkJPEG2000ImageIOInternalEnums(*args))
    __swig_destroy__ = _itkJPEG2000ImageIOPython.delete_itkJPEG2000ImageIOInternalEnums

# Register itkJPEG2000ImageIOInternalEnums in _itkJPEG2000ImageIOPython:
_itkJPEG2000ImageIOPython.itkJPEG2000ImageIOInternalEnums_swigregister(itkJPEG2000ImageIOInternalEnums)



