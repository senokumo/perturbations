import essentia.standard as es
import numpy as np
from perturbations.types import AudioData, Rhythm


# https://essentia.upf.edu/tutorial_rhythm_beatdetection.html

def extract_rhythm(audio: np.typing.NDArray) -> Rhythm:
  bpm, beats, beats_confidence, beats_estimate, beats_intervals = es.RhythmExtractor2013(method="multifeature")(audio)
  return Rhythm(
    bpm, 
    beats, 
    beats_confidence, 
    beats_estimate, 
    beats_intervals,
  )

def extract_bpm(audio):
  return

def extract_rms(audio): # root mean square
  return

def extract_dynamicrange(audio):
  return

def extract_spectralcentroid(audio):
  return

def extract_spectralrollof(audio):
  return

def extract_zerocrossrate(audio):
  return

