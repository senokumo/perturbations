from dataclasses import dataclass
import numpy as np
from numpy.typing import NDArray
from typing import List
from perturbations.consts import SAMPLE_RATE

@dataclass
class AudioData:
    samples: NDArray
    sample_rate: int = SAMPLE_RATE

@dataclass(frozen=True)
class Rhythm:
    bpm: float
    beats: NDArray
    beats_confidence: NDArray
    beats_estimate: NDArray
    beats_intervals: NDArray

@dataclass
class Performance:
    filename: str
    audio: NDArray
    rhythm_features: Rhythm