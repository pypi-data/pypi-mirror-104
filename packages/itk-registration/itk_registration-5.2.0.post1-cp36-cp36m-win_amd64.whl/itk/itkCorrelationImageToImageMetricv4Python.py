# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKMetricsv4Python



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkCorrelationImageToImageMetricv4Python
else:
    import _itkCorrelationImageToImageMetricv4Python

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkCorrelationImageToImageMetricv4Python.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkCorrelationImageToImageMetricv4Python.SWIG_PyStaticMethod_New

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
import itk.itkImageToImageMetricv4Python
import itk.itkImageToImageFilterBPython
import itk.itkImageRegionPython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkOffsetPython
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
import itk.itkPointSetPython
import itk.itkVectorContainerPython
import itk.itkContinuousIndexPython
import itk.itkArrayPython
import itk.itkTransformBasePython
import itk.itkArray2DPython
import itk.itkDiffusionTensor3DPython
import itk.itkOptimizerParametersPython
import itk.itkInterpolateImageFunctionPython
import itk.itkImageFunctionBasePython
import itk.itkFunctionBasePython
import itk.itkDisplacementFieldTransformPython
import itk.itkObjectToObjectMetricBasePython
import itk.itkSingleValuedCostFunctionv4Python
import itk.itkCostFunctionPython
import itk.itkSpatialObjectBasePython
import itk.itkAffineTransformPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkBoundingBoxPython
import itk.itkMapContainerPython
import itk.itkSpatialObjectPropertyPython

def itkCorrelationImageToImageMetricv4ID2ID2_New():
    return itkCorrelationImageToImageMetricv4ID2ID2.New()

class itkCorrelationImageToImageMetricv4ID2ID2(itk.itkImageToImageMetricv4Python.itkImageToImageMetricv4D2D2):
    r"""


    Class implementing normalized cross correlation image metric.

    Definition of the normalized cross correlation metric used here:

    negative square of normalized cross correlation

    \\[ C(f, m) = -\\frac{<f-\\bar{f}, m-\\bar{m}
    >^2}{|f-\\bar{f}|^2 |m-\\bar{m}|^2} \\]

    in which, f, m are the vectors of image pixel intensities,
    $\\bar{f}$ and $\\bar{m}$ are the mean values of f and m. <,>
    denotes inner product, $|\\cdot|$ denotes the 2-norm of the vector.
    The minus sign makes the metric to optimize towards its minimal value.
    Note that this uses the square of the mathematical notion of
    normalized cross correlation to avoid the square root computation in
    practice.

    Moving image (m) is a function of the parameters (p) of the moving
    transforms. So $ C(f, m) = C(f, m(p)) $ GetValueAndDerivative will
    return the value as $ C(f,m) $ and the derivative as

    \\[ \\frac{d}{dp} C = 2 \\frac{<f1, m1>}{|f1|^2 |m1|^2} * ( <f1,
    \\frac{dm}{dp}> - \\frac{<f1, m1>}{|m1|^2} < m1, \\frac{dm}{dp}
    > ) \\]

    in which, $ f1 = f - \\bar{f} $, $ m1 = m - \\bar{m} $ (Note:
    there should be a minus sign of $ \\frac{d}{dp} $ mathematically,
    which is not in the implementation to match the requirement of the
    metricv4 optimization framework.

    See CorrelationImageToImageMetricv4GetValueAndDerivativeThreader::Proc
    essPoint for algorithm implementation.

    This metric only works with the global transform. It throws an
    exception if the transform has local support. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4ID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4ID2ID2_Clone)
    __swig_destroy__ = _itkCorrelationImageToImageMetricv4Python.delete_itkCorrelationImageToImageMetricv4ID2ID2
    cast = _swig_new_static_method(_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4ID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkCorrelationImageToImageMetricv4ID2ID2

        Create a new object of the class itkCorrelationImageToImageMetricv4ID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCorrelationImageToImageMetricv4ID2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCorrelationImageToImageMetricv4ID2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCorrelationImageToImageMetricv4ID2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCorrelationImageToImageMetricv4ID2ID2 in _itkCorrelationImageToImageMetricv4Python:
_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4ID2ID2_swigregister(itkCorrelationImageToImageMetricv4ID2ID2)
itkCorrelationImageToImageMetricv4ID2ID2___New_orig__ = _itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4ID2ID2___New_orig__
itkCorrelationImageToImageMetricv4ID2ID2_cast = _itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4ID2ID2_cast


def itkCorrelationImageToImageMetricv4ID3ID3_New():
    return itkCorrelationImageToImageMetricv4ID3ID3.New()

class itkCorrelationImageToImageMetricv4ID3ID3(itk.itkImageToImageMetricv4Python.itkImageToImageMetricv4D3D3):
    r"""


    Class implementing normalized cross correlation image metric.

    Definition of the normalized cross correlation metric used here:

    negative square of normalized cross correlation

    \\[ C(f, m) = -\\frac{<f-\\bar{f}, m-\\bar{m}
    >^2}{|f-\\bar{f}|^2 |m-\\bar{m}|^2} \\]

    in which, f, m are the vectors of image pixel intensities,
    $\\bar{f}$ and $\\bar{m}$ are the mean values of f and m. <,>
    denotes inner product, $|\\cdot|$ denotes the 2-norm of the vector.
    The minus sign makes the metric to optimize towards its minimal value.
    Note that this uses the square of the mathematical notion of
    normalized cross correlation to avoid the square root computation in
    practice.

    Moving image (m) is a function of the parameters (p) of the moving
    transforms. So $ C(f, m) = C(f, m(p)) $ GetValueAndDerivative will
    return the value as $ C(f,m) $ and the derivative as

    \\[ \\frac{d}{dp} C = 2 \\frac{<f1, m1>}{|f1|^2 |m1|^2} * ( <f1,
    \\frac{dm}{dp}> - \\frac{<f1, m1>}{|m1|^2} < m1, \\frac{dm}{dp}
    > ) \\]

    in which, $ f1 = f - \\bar{f} $, $ m1 = m - \\bar{m} $ (Note:
    there should be a minus sign of $ \\frac{d}{dp} $ mathematically,
    which is not in the implementation to match the requirement of the
    metricv4 optimization framework.

    See CorrelationImageToImageMetricv4GetValueAndDerivativeThreader::Proc
    essPoint for algorithm implementation.

    This metric only works with the global transform. It throws an
    exception if the transform has local support. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4ID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4ID3ID3_Clone)
    __swig_destroy__ = _itkCorrelationImageToImageMetricv4Python.delete_itkCorrelationImageToImageMetricv4ID3ID3
    cast = _swig_new_static_method(_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4ID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkCorrelationImageToImageMetricv4ID3ID3

        Create a new object of the class itkCorrelationImageToImageMetricv4ID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCorrelationImageToImageMetricv4ID3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCorrelationImageToImageMetricv4ID3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCorrelationImageToImageMetricv4ID3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCorrelationImageToImageMetricv4ID3ID3 in _itkCorrelationImageToImageMetricv4Python:
_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4ID3ID3_swigregister(itkCorrelationImageToImageMetricv4ID3ID3)
itkCorrelationImageToImageMetricv4ID3ID3___New_orig__ = _itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4ID3ID3___New_orig__
itkCorrelationImageToImageMetricv4ID3ID3_cast = _itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4ID3ID3_cast


def itkCorrelationImageToImageMetricv4ID4ID4_New():
    return itkCorrelationImageToImageMetricv4ID4ID4.New()

class itkCorrelationImageToImageMetricv4ID4ID4(itk.itkImageToImageMetricv4Python.itkImageToImageMetricv4D4D4):
    r"""


    Class implementing normalized cross correlation image metric.

    Definition of the normalized cross correlation metric used here:

    negative square of normalized cross correlation

    \\[ C(f, m) = -\\frac{<f-\\bar{f}, m-\\bar{m}
    >^2}{|f-\\bar{f}|^2 |m-\\bar{m}|^2} \\]

    in which, f, m are the vectors of image pixel intensities,
    $\\bar{f}$ and $\\bar{m}$ are the mean values of f and m. <,>
    denotes inner product, $|\\cdot|$ denotes the 2-norm of the vector.
    The minus sign makes the metric to optimize towards its minimal value.
    Note that this uses the square of the mathematical notion of
    normalized cross correlation to avoid the square root computation in
    practice.

    Moving image (m) is a function of the parameters (p) of the moving
    transforms. So $ C(f, m) = C(f, m(p)) $ GetValueAndDerivative will
    return the value as $ C(f,m) $ and the derivative as

    \\[ \\frac{d}{dp} C = 2 \\frac{<f1, m1>}{|f1|^2 |m1|^2} * ( <f1,
    \\frac{dm}{dp}> - \\frac{<f1, m1>}{|m1|^2} < m1, \\frac{dm}{dp}
    > ) \\]

    in which, $ f1 = f - \\bar{f} $, $ m1 = m - \\bar{m} $ (Note:
    there should be a minus sign of $ \\frac{d}{dp} $ mathematically,
    which is not in the implementation to match the requirement of the
    metricv4 optimization framework.

    See CorrelationImageToImageMetricv4GetValueAndDerivativeThreader::Proc
    essPoint for algorithm implementation.

    This metric only works with the global transform. It throws an
    exception if the transform has local support. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4ID4ID4___New_orig__)
    Clone = _swig_new_instance_method(_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4ID4ID4_Clone)
    __swig_destroy__ = _itkCorrelationImageToImageMetricv4Python.delete_itkCorrelationImageToImageMetricv4ID4ID4
    cast = _swig_new_static_method(_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4ID4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkCorrelationImageToImageMetricv4ID4ID4

        Create a new object of the class itkCorrelationImageToImageMetricv4ID4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCorrelationImageToImageMetricv4ID4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCorrelationImageToImageMetricv4ID4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCorrelationImageToImageMetricv4ID4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCorrelationImageToImageMetricv4ID4ID4 in _itkCorrelationImageToImageMetricv4Python:
_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4ID4ID4_swigregister(itkCorrelationImageToImageMetricv4ID4ID4)
itkCorrelationImageToImageMetricv4ID4ID4___New_orig__ = _itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4ID4ID4___New_orig__
itkCorrelationImageToImageMetricv4ID4ID4_cast = _itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4ID4ID4_cast


def itkCorrelationImageToImageMetricv4IF2IF2_New():
    return itkCorrelationImageToImageMetricv4IF2IF2.New()

class itkCorrelationImageToImageMetricv4IF2IF2(itk.itkImageToImageMetricv4Python.itkImageToImageMetricv4F2F2):
    r"""


    Class implementing normalized cross correlation image metric.

    Definition of the normalized cross correlation metric used here:

    negative square of normalized cross correlation

    \\[ C(f, m) = -\\frac{<f-\\bar{f}, m-\\bar{m}
    >^2}{|f-\\bar{f}|^2 |m-\\bar{m}|^2} \\]

    in which, f, m are the vectors of image pixel intensities,
    $\\bar{f}$ and $\\bar{m}$ are the mean values of f and m. <,>
    denotes inner product, $|\\cdot|$ denotes the 2-norm of the vector.
    The minus sign makes the metric to optimize towards its minimal value.
    Note that this uses the square of the mathematical notion of
    normalized cross correlation to avoid the square root computation in
    practice.

    Moving image (m) is a function of the parameters (p) of the moving
    transforms. So $ C(f, m) = C(f, m(p)) $ GetValueAndDerivative will
    return the value as $ C(f,m) $ and the derivative as

    \\[ \\frac{d}{dp} C = 2 \\frac{<f1, m1>}{|f1|^2 |m1|^2} * ( <f1,
    \\frac{dm}{dp}> - \\frac{<f1, m1>}{|m1|^2} < m1, \\frac{dm}{dp}
    > ) \\]

    in which, $ f1 = f - \\bar{f} $, $ m1 = m - \\bar{m} $ (Note:
    there should be a minus sign of $ \\frac{d}{dp} $ mathematically,
    which is not in the implementation to match the requirement of the
    metricv4 optimization framework.

    See CorrelationImageToImageMetricv4GetValueAndDerivativeThreader::Proc
    essPoint for algorithm implementation.

    This metric only works with the global transform. It throws an
    exception if the transform has local support. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4IF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4IF2IF2_Clone)
    __swig_destroy__ = _itkCorrelationImageToImageMetricv4Python.delete_itkCorrelationImageToImageMetricv4IF2IF2
    cast = _swig_new_static_method(_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4IF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkCorrelationImageToImageMetricv4IF2IF2

        Create a new object of the class itkCorrelationImageToImageMetricv4IF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCorrelationImageToImageMetricv4IF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCorrelationImageToImageMetricv4IF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCorrelationImageToImageMetricv4IF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCorrelationImageToImageMetricv4IF2IF2 in _itkCorrelationImageToImageMetricv4Python:
_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4IF2IF2_swigregister(itkCorrelationImageToImageMetricv4IF2IF2)
itkCorrelationImageToImageMetricv4IF2IF2___New_orig__ = _itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4IF2IF2___New_orig__
itkCorrelationImageToImageMetricv4IF2IF2_cast = _itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4IF2IF2_cast


def itkCorrelationImageToImageMetricv4IF3IF3_New():
    return itkCorrelationImageToImageMetricv4IF3IF3.New()

class itkCorrelationImageToImageMetricv4IF3IF3(itk.itkImageToImageMetricv4Python.itkImageToImageMetricv4F3F3):
    r"""


    Class implementing normalized cross correlation image metric.

    Definition of the normalized cross correlation metric used here:

    negative square of normalized cross correlation

    \\[ C(f, m) = -\\frac{<f-\\bar{f}, m-\\bar{m}
    >^2}{|f-\\bar{f}|^2 |m-\\bar{m}|^2} \\]

    in which, f, m are the vectors of image pixel intensities,
    $\\bar{f}$ and $\\bar{m}$ are the mean values of f and m. <,>
    denotes inner product, $|\\cdot|$ denotes the 2-norm of the vector.
    The minus sign makes the metric to optimize towards its minimal value.
    Note that this uses the square of the mathematical notion of
    normalized cross correlation to avoid the square root computation in
    practice.

    Moving image (m) is a function of the parameters (p) of the moving
    transforms. So $ C(f, m) = C(f, m(p)) $ GetValueAndDerivative will
    return the value as $ C(f,m) $ and the derivative as

    \\[ \\frac{d}{dp} C = 2 \\frac{<f1, m1>}{|f1|^2 |m1|^2} * ( <f1,
    \\frac{dm}{dp}> - \\frac{<f1, m1>}{|m1|^2} < m1, \\frac{dm}{dp}
    > ) \\]

    in which, $ f1 = f - \\bar{f} $, $ m1 = m - \\bar{m} $ (Note:
    there should be a minus sign of $ \\frac{d}{dp} $ mathematically,
    which is not in the implementation to match the requirement of the
    metricv4 optimization framework.

    See CorrelationImageToImageMetricv4GetValueAndDerivativeThreader::Proc
    essPoint for algorithm implementation.

    This metric only works with the global transform. It throws an
    exception if the transform has local support. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4IF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4IF3IF3_Clone)
    __swig_destroy__ = _itkCorrelationImageToImageMetricv4Python.delete_itkCorrelationImageToImageMetricv4IF3IF3
    cast = _swig_new_static_method(_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4IF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkCorrelationImageToImageMetricv4IF3IF3

        Create a new object of the class itkCorrelationImageToImageMetricv4IF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCorrelationImageToImageMetricv4IF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCorrelationImageToImageMetricv4IF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCorrelationImageToImageMetricv4IF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCorrelationImageToImageMetricv4IF3IF3 in _itkCorrelationImageToImageMetricv4Python:
_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4IF3IF3_swigregister(itkCorrelationImageToImageMetricv4IF3IF3)
itkCorrelationImageToImageMetricv4IF3IF3___New_orig__ = _itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4IF3IF3___New_orig__
itkCorrelationImageToImageMetricv4IF3IF3_cast = _itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4IF3IF3_cast


def itkCorrelationImageToImageMetricv4IF4IF4_New():
    return itkCorrelationImageToImageMetricv4IF4IF4.New()

class itkCorrelationImageToImageMetricv4IF4IF4(itk.itkImageToImageMetricv4Python.itkImageToImageMetricv4F4F4):
    r"""


    Class implementing normalized cross correlation image metric.

    Definition of the normalized cross correlation metric used here:

    negative square of normalized cross correlation

    \\[ C(f, m) = -\\frac{<f-\\bar{f}, m-\\bar{m}
    >^2}{|f-\\bar{f}|^2 |m-\\bar{m}|^2} \\]

    in which, f, m are the vectors of image pixel intensities,
    $\\bar{f}$ and $\\bar{m}$ are the mean values of f and m. <,>
    denotes inner product, $|\\cdot|$ denotes the 2-norm of the vector.
    The minus sign makes the metric to optimize towards its minimal value.
    Note that this uses the square of the mathematical notion of
    normalized cross correlation to avoid the square root computation in
    practice.

    Moving image (m) is a function of the parameters (p) of the moving
    transforms. So $ C(f, m) = C(f, m(p)) $ GetValueAndDerivative will
    return the value as $ C(f,m) $ and the derivative as

    \\[ \\frac{d}{dp} C = 2 \\frac{<f1, m1>}{|f1|^2 |m1|^2} * ( <f1,
    \\frac{dm}{dp}> - \\frac{<f1, m1>}{|m1|^2} < m1, \\frac{dm}{dp}
    > ) \\]

    in which, $ f1 = f - \\bar{f} $, $ m1 = m - \\bar{m} $ (Note:
    there should be a minus sign of $ \\frac{d}{dp} $ mathematically,
    which is not in the implementation to match the requirement of the
    metricv4 optimization framework.

    See CorrelationImageToImageMetricv4GetValueAndDerivativeThreader::Proc
    essPoint for algorithm implementation.

    This metric only works with the global transform. It throws an
    exception if the transform has local support. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4IF4IF4___New_orig__)
    Clone = _swig_new_instance_method(_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4IF4IF4_Clone)
    __swig_destroy__ = _itkCorrelationImageToImageMetricv4Python.delete_itkCorrelationImageToImageMetricv4IF4IF4
    cast = _swig_new_static_method(_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4IF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkCorrelationImageToImageMetricv4IF4IF4

        Create a new object of the class itkCorrelationImageToImageMetricv4IF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCorrelationImageToImageMetricv4IF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkCorrelationImageToImageMetricv4IF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkCorrelationImageToImageMetricv4IF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCorrelationImageToImageMetricv4IF4IF4 in _itkCorrelationImageToImageMetricv4Python:
_itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4IF4IF4_swigregister(itkCorrelationImageToImageMetricv4IF4IF4)
itkCorrelationImageToImageMetricv4IF4IF4___New_orig__ = _itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4IF4IF4___New_orig__
itkCorrelationImageToImageMetricv4IF4IF4_cast = _itkCorrelationImageToImageMetricv4Python.itkCorrelationImageToImageMetricv4IF4IF4_cast



