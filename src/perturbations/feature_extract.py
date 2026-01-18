from typing import Dict
import numpy as np
import pandas as pd
from scipy.signal import correlate
from pathlib import Path
import essentia.standard as es
import librosa

from perturbations.types import AudioData, Rhythm, Performance
from perturbations.data.audio_io import load_audio
from perturbations.consts import SAMPLE_RATE



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

# via percussive separation 
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


def safe_normalize(X, axis=0, eps=1e-8):
    norm = np.linalg.norm(X, axis=axis, keepdims=True)
    return X / (norm + eps)

def remove_silent_frames(X, threshold=1e-6):
    energy = np.linalg.norm(X, axis=0)
    return X[:, energy > threshold]

def add_preroll(start_sample, sr, preroll_sec=1.0):
    preroll_samples = int(preroll_sec * sr)
    return max(0, start_sample - preroll_samples)


def cut_to_section(studio_section, performance, sr=22050):
    studio_harmonic, _ = librosa.effects.hpss(studio_section)
    perf_harmonic, _   = librosa.effects.hpss(performance)

    chroma_studio = librosa.feature.chroma_cqt(y=studio_harmonic, sr=sr)
    chroma_perf = librosa.feature.chroma_cqt(y=perf_harmonic, sr=sr)

    chroma_studio_norm = safe_normalize(chroma_studio, axis=0)
    chroma_perf_norm = safe_normalize(chroma_perf, axis=0)

    chroma_studio_norm_cleaned = remove_silent_frames(chroma_studio_norm)
    chroma_perf_norm_cleaned = remove_silent_frames(chroma_perf_norm)

    D, wp = librosa.sequence.dtw(
        X=chroma_studio_norm_cleaned,
        Y=chroma_perf_norm_cleaned,
        metric='cosine',
        subseq=True
    )

    perf_frames = wp[:, 1]
    start_frame = perf_frames.min()
    end_frame   = perf_frames.max()

    times = librosa.frames_to_time([start_frame, end_frame], sr=sr)
    start_sample = int(times[0] * sr)
    start_sample = add_preroll(start_sample, sr, preroll_sec=2.0)
    end_sample   = int(times[1] * sr)

    return performance[start_sample:end_sample], (start_sample, end_sample)





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

