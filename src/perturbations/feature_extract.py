from typing import Dict
import numpy as np
import pandas as pd
from pathlib import Path
import essentia.standard as es
import librosa

from perturbations.types import AudioData, Rhythm, Performance
from perturbations.data.audio_io import load_audio


# https://essentia.upf.edu/tutorial_rhythm_beatdetection.html

def calculate_rhythm_features(audio: np.typing.NDArray) -> Rhythm:
  audio_perc = get_percussive_source(audio)
  bpm, beats, beats_confidence, beats_estimate, beats_intervals = es.RhythmExtractor2013(method="multifeature")(audio_perc) # type: ignore
  return Rhythm(
    bpm, 
    beats, 
    beats_confidence, 
    beats_estimate, 
    beats_intervals,
  )

# percussive separation function 
def get_percussive_source(audio):
  D = librosa.stft(audio)
  _, D_percussive = librosa.decompose.hpss(D)
  y_percussive = librosa.istft(D_percussive, length=len(audio))
  return y_percussive


def load_performances_features(audio_directory: Path) -> Dict[str, Performance]: # TODO correct return type later: tuple[Dict[str, Performance], pd.DataFrame]
  performances = {}
  for file_path in audio_directory.glob("*"):
    audio_data = load_audio(file_path)  
    audio_data_percussive = get_percussive_source(audio_data)
    rhythm_features = calculate_rhythm_features(audio_data_percussive)
    perf = Performance(
            filename=file_path.name,
            audio=audio_data,
            rhythm_features=rhythm_features
          )
    performances[file_path.stem] = perf
    print(rhythm_features)
    """   df = pd.DataFrame([
          {
            'filename': p.filename,
            'bpm': p.rhythm_features.bpm,
            'tempo_std': p.rhythm_features.tempo_std,
            'duration': len(p.audio.samples) / p.audio.sample_rate,
            'n_beats': len(p.rhythm_features.beat_times)
          }
            for p in performances.values()
    ]) """
  return performances

def correct_tempo_octave():
  return

def extract_bpm(audio):
  rhythm_extractor = es.RhythmExtractor2013(method="multifeature") # type: ignore

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

