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
    from . import _itkJointHistogramMutualInformationImageToImageMetricv4Python
else:
    import _itkJointHistogramMutualInformationImageToImageMetricv4Python

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkJointHistogramMutualInformationImageToImageMetricv4Python.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkJointHistogramMutualInformationImageToImageMetricv4Python.SWIG_PyStaticMethod_New

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
import itk.itkImageToImageMetricv4Python
import itk.itkTransformBasePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_vectorPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.itkPointPython
import itk.ITKCommonBasePython
import itk.itkVariableLengthVectorPython
import itk.itkArray2DPython
import itk.itkDiffusionTensor3DPython
import itk.itkArrayPython
import itk.itkOptimizerParametersPython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkObjectToObjectMetricBasePython
import itk.itkSingleValuedCostFunctionv4Python
import itk.itkCostFunctionPython
import itk.itkSpatialObjectBasePython
import itk.itkSpatialObjectPropertyPython
import itk.itkRGBAPixelPython
import itk.itkAffineTransformPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkBoundingBoxPython
import itk.itkVectorContainerPython
import itk.itkContinuousIndexPython
import itk.itkMapContainerPython
import itk.itkPointSetPython
import itk.itkInterpolateImageFunctionPython
import itk.itkImageFunctionBasePython
import itk.itkRGBPixelPython
import itk.itkImagePython
import itk.itkFunctionBasePython
import itk.itkImageToImageFilterBPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkVectorImagePython
import itk.itkDisplacementFieldTransformPython

def itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2_New():
    return itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2.New()

class itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2(itk.itkImageToImageMetricv4Python.itkImageToImageMetricv4D2D2):
    r"""


    Computes the mutual information between two images to be registered
    using the method referenced below.

    References: [1] "Optimization of Mutual Information for
    MultiResolution Image      Registration" P. Thevenaz and M. Unser
    IEEE Transactions in Image Processing, 9(12) December 2000. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2_Clone)
    GetModifiableJointPDF = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2_GetModifiableJointPDF)
    GetJointPDF = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2_GetJointPDF)
    SetNumberOfHistogramBins = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2_SetNumberOfHistogramBins)
    GetNumberOfHistogramBins = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2_GetNumberOfHistogramBins)
    SetVarianceForJointPDFSmoothing = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2_SetVarianceForJointPDFSmoothing)
    GetVarianceForJointPDFSmoothing = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2_GetVarianceForJointPDFSmoothing)
    __swig_destroy__ = _itkJointHistogramMutualInformationImageToImageMetricv4Python.delete_itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2
    cast = _swig_new_static_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2

        Create a new object of the class itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2 in _itkJointHistogramMutualInformationImageToImageMetricv4Python:
_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2_swigregister(itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2)
itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2___New_orig__ = _itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2___New_orig__
itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2_cast = _itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID2ID2_cast


def itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3_New():
    return itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3.New()

class itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3(itk.itkImageToImageMetricv4Python.itkImageToImageMetricv4D3D3):
    r"""


    Computes the mutual information between two images to be registered
    using the method referenced below.

    References: [1] "Optimization of Mutual Information for
    MultiResolution Image      Registration" P. Thevenaz and M. Unser
    IEEE Transactions in Image Processing, 9(12) December 2000. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3_Clone)
    GetModifiableJointPDF = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3_GetModifiableJointPDF)
    GetJointPDF = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3_GetJointPDF)
    SetNumberOfHistogramBins = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3_SetNumberOfHistogramBins)
    GetNumberOfHistogramBins = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3_GetNumberOfHistogramBins)
    SetVarianceForJointPDFSmoothing = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3_SetVarianceForJointPDFSmoothing)
    GetVarianceForJointPDFSmoothing = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3_GetVarianceForJointPDFSmoothing)
    __swig_destroy__ = _itkJointHistogramMutualInformationImageToImageMetricv4Python.delete_itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3
    cast = _swig_new_static_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3

        Create a new object of the class itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3 in _itkJointHistogramMutualInformationImageToImageMetricv4Python:
_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3_swigregister(itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3)
itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3___New_orig__ = _itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3___New_orig__
itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3_cast = _itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID3ID3_cast


def itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4_New():
    return itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4.New()

class itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4(itk.itkImageToImageMetricv4Python.itkImageToImageMetricv4D4D4):
    r"""


    Computes the mutual information between two images to be registered
    using the method referenced below.

    References: [1] "Optimization of Mutual Information for
    MultiResolution Image      Registration" P. Thevenaz and M. Unser
    IEEE Transactions in Image Processing, 9(12) December 2000. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4___New_orig__)
    Clone = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4_Clone)
    GetModifiableJointPDF = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4_GetModifiableJointPDF)
    GetJointPDF = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4_GetJointPDF)
    SetNumberOfHistogramBins = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4_SetNumberOfHistogramBins)
    GetNumberOfHistogramBins = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4_GetNumberOfHistogramBins)
    SetVarianceForJointPDFSmoothing = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4_SetVarianceForJointPDFSmoothing)
    GetVarianceForJointPDFSmoothing = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4_GetVarianceForJointPDFSmoothing)
    __swig_destroy__ = _itkJointHistogramMutualInformationImageToImageMetricv4Python.delete_itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4
    cast = _swig_new_static_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4

        Create a new object of the class itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4 in _itkJointHistogramMutualInformationImageToImageMetricv4Python:
_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4_swigregister(itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4)
itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4___New_orig__ = _itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4___New_orig__
itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4_cast = _itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4ID4ID4_cast


def itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2_New():
    return itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2.New()

class itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2(itk.itkImageToImageMetricv4Python.itkImageToImageMetricv4F2F2):
    r"""


    Computes the mutual information between two images to be registered
    using the method referenced below.

    References: [1] "Optimization of Mutual Information for
    MultiResolution Image      Registration" P. Thevenaz and M. Unser
    IEEE Transactions in Image Processing, 9(12) December 2000. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2_Clone)
    GetModifiableJointPDF = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2_GetModifiableJointPDF)
    GetJointPDF = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2_GetJointPDF)
    SetNumberOfHistogramBins = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2_SetNumberOfHistogramBins)
    GetNumberOfHistogramBins = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2_GetNumberOfHistogramBins)
    SetVarianceForJointPDFSmoothing = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2_SetVarianceForJointPDFSmoothing)
    GetVarianceForJointPDFSmoothing = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2_GetVarianceForJointPDFSmoothing)
    __swig_destroy__ = _itkJointHistogramMutualInformationImageToImageMetricv4Python.delete_itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2
    cast = _swig_new_static_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2

        Create a new object of the class itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2 in _itkJointHistogramMutualInformationImageToImageMetricv4Python:
_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2_swigregister(itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2)
itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2___New_orig__ = _itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2___New_orig__
itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2_cast = _itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF2IF2_cast


def itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3_New():
    return itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3.New()

class itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3(itk.itkImageToImageMetricv4Python.itkImageToImageMetricv4F3F3):
    r"""


    Computes the mutual information between two images to be registered
    using the method referenced below.

    References: [1] "Optimization of Mutual Information for
    MultiResolution Image      Registration" P. Thevenaz and M. Unser
    IEEE Transactions in Image Processing, 9(12) December 2000. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3_Clone)
    GetModifiableJointPDF = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3_GetModifiableJointPDF)
    GetJointPDF = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3_GetJointPDF)
    SetNumberOfHistogramBins = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3_SetNumberOfHistogramBins)
    GetNumberOfHistogramBins = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3_GetNumberOfHistogramBins)
    SetVarianceForJointPDFSmoothing = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3_SetVarianceForJointPDFSmoothing)
    GetVarianceForJointPDFSmoothing = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3_GetVarianceForJointPDFSmoothing)
    __swig_destroy__ = _itkJointHistogramMutualInformationImageToImageMetricv4Python.delete_itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3
    cast = _swig_new_static_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3

        Create a new object of the class itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3 in _itkJointHistogramMutualInformationImageToImageMetricv4Python:
_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3_swigregister(itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3)
itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3___New_orig__ = _itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3___New_orig__
itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3_cast = _itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF3IF3_cast


def itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4_New():
    return itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4.New()

class itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4(itk.itkImageToImageMetricv4Python.itkImageToImageMetricv4F4F4):
    r"""


    Computes the mutual information between two images to be registered
    using the method referenced below.

    References: [1] "Optimization of Mutual Information for
    MultiResolution Image      Registration" P. Thevenaz and M. Unser
    IEEE Transactions in Image Processing, 9(12) December 2000. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4___New_orig__)
    Clone = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4_Clone)
    GetModifiableJointPDF = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4_GetModifiableJointPDF)
    GetJointPDF = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4_GetJointPDF)
    SetNumberOfHistogramBins = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4_SetNumberOfHistogramBins)
    GetNumberOfHistogramBins = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4_GetNumberOfHistogramBins)
    SetVarianceForJointPDFSmoothing = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4_SetVarianceForJointPDFSmoothing)
    GetVarianceForJointPDFSmoothing = _swig_new_instance_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4_GetVarianceForJointPDFSmoothing)
    __swig_destroy__ = _itkJointHistogramMutualInformationImageToImageMetricv4Python.delete_itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4
    cast = _swig_new_static_method(_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4

        Create a new object of the class itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4 in _itkJointHistogramMutualInformationImageToImageMetricv4Python:
_itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4_swigregister(itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4)
itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4___New_orig__ = _itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4___New_orig__
itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4_cast = _itkJointHistogramMutualInformationImageToImageMetricv4Python.itkJointHistogramMutualInformationImageToImageMetricv4IF4IF4_cast



