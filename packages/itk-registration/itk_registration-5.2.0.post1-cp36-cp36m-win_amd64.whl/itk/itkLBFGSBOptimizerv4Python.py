# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKOptimizersv4Python



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkLBFGSBOptimizerv4Python
else:
    import _itkLBFGSBOptimizerv4Python

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkLBFGSBOptimizerv4Python.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkLBFGSBOptimizerv4Python.SWIG_PyStaticMethod_New

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
import itk.itkArrayPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_matrixPython
import itk.itkLBFGSOptimizerBasev4Python
import itk.itkSingleValuedNonLinearVnlOptimizerv4Python
import itk.itkOptimizerParametersPython
import itk.ITKCommonBasePython
import itk.itkObjectToObjectMetricBasePython
import itk.itkSingleValuedCostFunctionv4Python
import itk.itkCostFunctionPython
import itk.itkObjectToObjectOptimizerBasePython
import itk.itkOptimizerParameterScalesEstimatorPython
import itk.itkLBFGSOptimizerBaseHelperv4Python
import itk.itkVnlTypesPython
import itk.vnl_cost_functionPython
import itk.vnl_unary_functionPython

def itkLBFGSBOptimizerv4_New():
    return itkLBFGSBOptimizerv4.New()

class itkLBFGSBOptimizerv4(itk.itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgsb):
    r"""


    Limited memory Broyden Fletcher Goldfarb Shannon minimization with
    simple bounds.

    This class is a wrapper for converted Fortran code for performing
    limited memory Broyden Fletcher Goldfarb Shannon minimization with
    simple bounds. The algorithm mininizes a nonlinear function f(x) of n
    variables subject to simple bound constraints of l <= x <= u.

    See also the documentation in Numerics/lbfgsb.c

    References:

    [1] R. H. Byrd, P. Lu and J. Nocedal. A Limited Memory Algorithm for
    Bound Constrained Optimization, (1995), SIAM Journal on Scientific and
    Statistical Computing , 16, 5, pp. 1190-1208.

    [2] C. Zhu, R. H. Byrd and J. Nocedal. L-BFGS-B: Algorithm 778:
    L-BFGS-B, FORTRAN routines for large scale bound constrained
    optimization (1997), ACM Transactions on Mathematical Software, Vol
    23, Num. 4, pp. 550 - 560. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4___New_orig__)
    Clone = _swig_new_instance_method(_itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_Clone)
    BoundSelectionValues_UNBOUNDED = _itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_BoundSelectionValues_UNBOUNDED
    
    BoundSelectionValues_LOWERBOUNDED = _itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_BoundSelectionValues_LOWERBOUNDED
    
    BoundSelectionValues_BOTHBOUNDED = _itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_BoundSelectionValues_BOTHBOUNDED
    
    BoundSelectionValues_UPPERBOUNDED = _itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_BoundSelectionValues_UPPERBOUNDED
    
    SetInitialPosition = _swig_new_instance_method(_itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_SetInitialPosition)
    GetInitialPosition = _swig_new_instance_method(_itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_GetInitialPosition)
    StartOptimization = _swig_new_instance_method(_itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_StartOptimization)
    SetLowerBound = _swig_new_instance_method(_itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_SetLowerBound)
    GetLowerBound = _swig_new_instance_method(_itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_GetLowerBound)
    SetUpperBound = _swig_new_instance_method(_itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_SetUpperBound)
    GetUpperBound = _swig_new_instance_method(_itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_GetUpperBound)
    SetBoundSelection = _swig_new_instance_method(_itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_SetBoundSelection)
    GetBoundSelection = _swig_new_instance_method(_itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_GetBoundSelection)
    SetCostFunctionConvergenceFactor = _swig_new_instance_method(_itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_SetCostFunctionConvergenceFactor)
    GetCostFunctionConvergenceFactor = _swig_new_instance_method(_itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_GetCostFunctionConvergenceFactor)
    SetMaximumNumberOfCorrections = _swig_new_instance_method(_itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_SetMaximumNumberOfCorrections)
    GetMaximumNumberOfCorrections = _swig_new_instance_method(_itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_GetMaximumNumberOfCorrections)
    GetInfinityNormOfProjectedGradient = _swig_new_instance_method(_itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_GetInfinityNormOfProjectedGradient)
    __swig_destroy__ = _itkLBFGSBOptimizerv4Python.delete_itkLBFGSBOptimizerv4
    cast = _swig_new_static_method(_itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_cast)

    def New(*args, **kargs):
        """New() -> itkLBFGSBOptimizerv4

        Create a new object of the class itkLBFGSBOptimizerv4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLBFGSBOptimizerv4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLBFGSBOptimizerv4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLBFGSBOptimizerv4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLBFGSBOptimizerv4 in _itkLBFGSBOptimizerv4Python:
_itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_swigregister(itkLBFGSBOptimizerv4)
itkLBFGSBOptimizerv4___New_orig__ = _itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4___New_orig__
itkLBFGSBOptimizerv4_cast = _itkLBFGSBOptimizerv4Python.itkLBFGSBOptimizerv4_cast



