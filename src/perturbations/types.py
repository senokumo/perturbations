from dataclasses import dataclass
import numpy as np
from typing import List, TypedDict

from perturbations.consts import SAMPLE_RATE



@dataclass(frozen=True)
class AudioData:
  samples: np.typing.NDArray
  sample_rate: int = SAMPLE_RATE

@dataclass(frozen=True)
class Rhythm:
  bpm: float
  beats: List[float]
  beats_confidence: List[float] # or just float?
  beats_estimate: List[float]
  beats_intervals: List[float]
