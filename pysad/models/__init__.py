"""
The :mod:`pysad.models` module includes anomaly detection models to score the anomalousness of instances.
"""
from .half_space_trees import HalfSpaceTrees
from .iforest_asd import IForestASD
from .kitnet import KitNet
from .knn_cad import KNNCAD
from .loda import LODA
from .loop import LocalOutlierProbability
from .median_absolute_deviation import MedianAbsoluteDeviation
from .null_model import NullModel
from .perfect_model import PerfectModel
from .random_model import RandomModel
from .relative_entropy import RelativeEntropy
from .robust_random_cut_forest import RobustRandomCutForest
from .rs_hash import RSHash
from .standard_absolute_deviation import StandardAbsoluteDeviation
from .xstream import xStream
from .exact_storm import ExactStorm

# Try to import Inqmad - this requires JAX dependencies which are optional
try:
    from .inqmad import Inqmad
    _has_inqmad = True
except (ImportError, NameError, AttributeError):
    # Handle missing dependencies, undefined names, and JAX-NumPy compatibility issues
    _has_inqmad = False

__all__ = ["ExactStorm", "HalfSpaceTrees", "IForestASD", "KitNet", "KNNCAD", "LODA", "LocalOutlierProbability", "MedianAbsoluteDeviation", "NullModel", "PerfectModel", "RandomModel", "RelativeEntropy", "RobustRandomCutForest", "RSHash", "StandardAbsoluteDeviation", "xStream"]

# Add Inqmad to __all__ if available
if _has_inqmad:
    __all__.append("Inqmad")
