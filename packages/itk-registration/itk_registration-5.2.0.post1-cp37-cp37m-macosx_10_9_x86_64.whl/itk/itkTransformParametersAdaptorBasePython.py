# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKRegistrationCommonPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkTransformParametersAdaptorBasePython
else:
    import _itkTransformParametersAdaptorBasePython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkTransformParametersAdaptorBasePython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkTransformParametersAdaptorBasePython.SWIG_PyStaticMethod_New

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
import itk.itkTransformBasePython
import itk.itkVariableLengthVectorPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkCovariantVectorPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkPointPython
import itk.vnl_matrix_fixedPython
import itk.itkArrayPython
import itk.itkOptimizerParametersPython
import itk.ITKCommonBasePython
import itk.itkDiffusionTensor3DPython
import itk.itkArray2DPython
class itkTransformParametersAdaptorBaseD2(itk.ITKCommonBasePython.itkObject):
    r"""


    Base helper class intended for multi-resolution image registration.

    During multi-resolution image registration, it is often useful to
    expand the number of parameters describing the transform when going
    from one level to the next. For example, in B-spline registration, one
    often wants to increase the mesh size (or, equivalently, the control
    point grid size) for increased flexibility in optimizing the
    transform. This requires the propagation of the current transform
    solution to the next level where the solution is identical but with an
    increase in the number of parameters. This base class and those
    derived classes are meant to handle these types of situations.

    Basic usage will involve the user specifying the required fixed
    parameters, i.e.

    which will adjust the transform based on the new fixed parameters.

    Nick Tustison

    Marius Staring 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetTransform = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD2_SetTransform)
    SetRequiredFixedParameters = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD2_SetRequiredFixedParameters)
    GetRequiredFixedParameters = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD2_GetRequiredFixedParameters)
    AdaptTransformParameters = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD2_AdaptTransformParameters)
    __swig_destroy__ = _itkTransformParametersAdaptorBasePython.delete_itkTransformParametersAdaptorBaseD2
    cast = _swig_new_static_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD2_cast)

# Register itkTransformParametersAdaptorBaseD2 in _itkTransformParametersAdaptorBasePython:
_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD2_swigregister(itkTransformParametersAdaptorBaseD2)
itkTransformParametersAdaptorBaseD2_cast = _itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD2_cast

class itkTransformParametersAdaptorBaseD3(itk.ITKCommonBasePython.itkObject):
    r"""


    Base helper class intended for multi-resolution image registration.

    During multi-resolution image registration, it is often useful to
    expand the number of parameters describing the transform when going
    from one level to the next. For example, in B-spline registration, one
    often wants to increase the mesh size (or, equivalently, the control
    point grid size) for increased flexibility in optimizing the
    transform. This requires the propagation of the current transform
    solution to the next level where the solution is identical but with an
    increase in the number of parameters. This base class and those
    derived classes are meant to handle these types of situations.

    Basic usage will involve the user specifying the required fixed
    parameters, i.e.

    which will adjust the transform based on the new fixed parameters.

    Nick Tustison

    Marius Staring 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetTransform = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD3_SetTransform)
    SetRequiredFixedParameters = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD3_SetRequiredFixedParameters)
    GetRequiredFixedParameters = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD3_GetRequiredFixedParameters)
    AdaptTransformParameters = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD3_AdaptTransformParameters)
    __swig_destroy__ = _itkTransformParametersAdaptorBasePython.delete_itkTransformParametersAdaptorBaseD3
    cast = _swig_new_static_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD3_cast)

# Register itkTransformParametersAdaptorBaseD3 in _itkTransformParametersAdaptorBasePython:
_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD3_swigregister(itkTransformParametersAdaptorBaseD3)
itkTransformParametersAdaptorBaseD3_cast = _itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD3_cast

class itkTransformParametersAdaptorBaseD4(itk.ITKCommonBasePython.itkObject):
    r"""


    Base helper class intended for multi-resolution image registration.

    During multi-resolution image registration, it is often useful to
    expand the number of parameters describing the transform when going
    from one level to the next. For example, in B-spline registration, one
    often wants to increase the mesh size (or, equivalently, the control
    point grid size) for increased flexibility in optimizing the
    transform. This requires the propagation of the current transform
    solution to the next level where the solution is identical but with an
    increase in the number of parameters. This base class and those
    derived classes are meant to handle these types of situations.

    Basic usage will involve the user specifying the required fixed
    parameters, i.e.

    which will adjust the transform based on the new fixed parameters.

    Nick Tustison

    Marius Staring 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetTransform = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD4_SetTransform)
    SetRequiredFixedParameters = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD4_SetRequiredFixedParameters)
    GetRequiredFixedParameters = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD4_GetRequiredFixedParameters)
    AdaptTransformParameters = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD4_AdaptTransformParameters)
    __swig_destroy__ = _itkTransformParametersAdaptorBasePython.delete_itkTransformParametersAdaptorBaseD4
    cast = _swig_new_static_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD4_cast)

# Register itkTransformParametersAdaptorBaseD4 in _itkTransformParametersAdaptorBasePython:
_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD4_swigregister(itkTransformParametersAdaptorBaseD4)
itkTransformParametersAdaptorBaseD4_cast = _itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseD4_cast

class itkTransformParametersAdaptorBaseF2(itk.ITKCommonBasePython.itkObject):
    r"""


    Base helper class intended for multi-resolution image registration.

    During multi-resolution image registration, it is often useful to
    expand the number of parameters describing the transform when going
    from one level to the next. For example, in B-spline registration, one
    often wants to increase the mesh size (or, equivalently, the control
    point grid size) for increased flexibility in optimizing the
    transform. This requires the propagation of the current transform
    solution to the next level where the solution is identical but with an
    increase in the number of parameters. This base class and those
    derived classes are meant to handle these types of situations.

    Basic usage will involve the user specifying the required fixed
    parameters, i.e.

    which will adjust the transform based on the new fixed parameters.

    Nick Tustison

    Marius Staring 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetTransform = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF2_SetTransform)
    SetRequiredFixedParameters = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF2_SetRequiredFixedParameters)
    GetRequiredFixedParameters = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF2_GetRequiredFixedParameters)
    AdaptTransformParameters = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF2_AdaptTransformParameters)
    __swig_destroy__ = _itkTransformParametersAdaptorBasePython.delete_itkTransformParametersAdaptorBaseF2
    cast = _swig_new_static_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF2_cast)

# Register itkTransformParametersAdaptorBaseF2 in _itkTransformParametersAdaptorBasePython:
_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF2_swigregister(itkTransformParametersAdaptorBaseF2)
itkTransformParametersAdaptorBaseF2_cast = _itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF2_cast

class itkTransformParametersAdaptorBaseF3(itk.ITKCommonBasePython.itkObject):
    r"""


    Base helper class intended for multi-resolution image registration.

    During multi-resolution image registration, it is often useful to
    expand the number of parameters describing the transform when going
    from one level to the next. For example, in B-spline registration, one
    often wants to increase the mesh size (or, equivalently, the control
    point grid size) for increased flexibility in optimizing the
    transform. This requires the propagation of the current transform
    solution to the next level where the solution is identical but with an
    increase in the number of parameters. This base class and those
    derived classes are meant to handle these types of situations.

    Basic usage will involve the user specifying the required fixed
    parameters, i.e.

    which will adjust the transform based on the new fixed parameters.

    Nick Tustison

    Marius Staring 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetTransform = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF3_SetTransform)
    SetRequiredFixedParameters = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF3_SetRequiredFixedParameters)
    GetRequiredFixedParameters = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF3_GetRequiredFixedParameters)
    AdaptTransformParameters = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF3_AdaptTransformParameters)
    __swig_destroy__ = _itkTransformParametersAdaptorBasePython.delete_itkTransformParametersAdaptorBaseF3
    cast = _swig_new_static_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF3_cast)

# Register itkTransformParametersAdaptorBaseF3 in _itkTransformParametersAdaptorBasePython:
_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF3_swigregister(itkTransformParametersAdaptorBaseF3)
itkTransformParametersAdaptorBaseF3_cast = _itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF3_cast

class itkTransformParametersAdaptorBaseF4(itk.ITKCommonBasePython.itkObject):
    r"""


    Base helper class intended for multi-resolution image registration.

    During multi-resolution image registration, it is often useful to
    expand the number of parameters describing the transform when going
    from one level to the next. For example, in B-spline registration, one
    often wants to increase the mesh size (or, equivalently, the control
    point grid size) for increased flexibility in optimizing the
    transform. This requires the propagation of the current transform
    solution to the next level where the solution is identical but with an
    increase in the number of parameters. This base class and those
    derived classes are meant to handle these types of situations.

    Basic usage will involve the user specifying the required fixed
    parameters, i.e.

    which will adjust the transform based on the new fixed parameters.

    Nick Tustison

    Marius Staring 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetTransform = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF4_SetTransform)
    SetRequiredFixedParameters = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF4_SetRequiredFixedParameters)
    GetRequiredFixedParameters = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF4_GetRequiredFixedParameters)
    AdaptTransformParameters = _swig_new_instance_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF4_AdaptTransformParameters)
    __swig_destroy__ = _itkTransformParametersAdaptorBasePython.delete_itkTransformParametersAdaptorBaseF4
    cast = _swig_new_static_method(_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF4_cast)

# Register itkTransformParametersAdaptorBaseF4 in _itkTransformParametersAdaptorBasePython:
_itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF4_swigregister(itkTransformParametersAdaptorBaseF4)
itkTransformParametersAdaptorBaseF4_cast = _itkTransformParametersAdaptorBasePython.itkTransformParametersAdaptorBaseF4_cast



