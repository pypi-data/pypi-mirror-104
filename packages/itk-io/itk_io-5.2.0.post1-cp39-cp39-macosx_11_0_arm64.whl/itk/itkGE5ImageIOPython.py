# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKIOGEPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkGE5ImageIOPython
else:
    import _itkGE5ImageIOPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkGE5ImageIOPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkGE5ImageIOPython.SWIG_PyStaticMethod_New

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
import itk.itkIPLCommonImageIOPython
import itk.ITKIOImageBaseBasePython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython

def itkGE5ImageIO_New():
    return itkGE5ImageIO.New()

class itkGE5ImageIO(itk.itkIPLCommonImageIOPython.itkIPLCommonImageIO):
    r"""


    Class that defines how to read GE5 file format.

    Hans J. Johnson 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGE5ImageIOPython.itkGE5ImageIO___New_orig__)
    Clone = _swig_new_instance_method(_itkGE5ImageIOPython.itkGE5ImageIO_Clone)
    __swig_destroy__ = _itkGE5ImageIOPython.delete_itkGE5ImageIO
    cast = _swig_new_static_method(_itkGE5ImageIOPython.itkGE5ImageIO_cast)

    def New(*args, **kargs):
        """New() -> itkGE5ImageIO

        Create a new object of the class itkGE5ImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGE5ImageIO.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGE5ImageIO.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGE5ImageIO.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGE5ImageIO in _itkGE5ImageIOPython:
_itkGE5ImageIOPython.itkGE5ImageIO_swigregister(itkGE5ImageIO)
itkGE5ImageIO___New_orig__ = _itkGE5ImageIOPython.itkGE5ImageIO___New_orig__
itkGE5ImageIO_cast = _itkGE5ImageIOPython.itkGE5ImageIO_cast


def itkGE5ImageIOFactory_New():
    return itkGE5ImageIOFactory.New()

class itkGE5ImageIOFactory(itk.ITKCommonBasePython.itkObjectFactoryBase):
    r"""


    Create instances of GE5ImageIO objects using an object factory. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkGE5ImageIOPython.itkGE5ImageIOFactory___New_orig__)
    RegisterOneFactory = _swig_new_static_method(_itkGE5ImageIOPython.itkGE5ImageIOFactory_RegisterOneFactory)
    __swig_destroy__ = _itkGE5ImageIOPython.delete_itkGE5ImageIOFactory
    cast = _swig_new_static_method(_itkGE5ImageIOPython.itkGE5ImageIOFactory_cast)

    def New(*args, **kargs):
        """New() -> itkGE5ImageIOFactory

        Create a new object of the class itkGE5ImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkGE5ImageIOFactory.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkGE5ImageIOFactory.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkGE5ImageIOFactory.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkGE5ImageIOFactory in _itkGE5ImageIOPython:
_itkGE5ImageIOPython.itkGE5ImageIOFactory_swigregister(itkGE5ImageIOFactory)
itkGE5ImageIOFactory___New_orig__ = _itkGE5ImageIOPython.itkGE5ImageIOFactory___New_orig__
itkGE5ImageIOFactory_RegisterOneFactory = _itkGE5ImageIOPython.itkGE5ImageIOFactory_RegisterOneFactory
itkGE5ImageIOFactory_cast = _itkGE5ImageIOPython.itkGE5ImageIOFactory_cast



