
from pathlib import Path
from essentia.standard import MonoLoader, MetadataReader
from typing import TypedDict
import numpy as np

from perturbations.util.logger import (
  log_section,
  log_file_start,
  log_file_end,
)
from perturbations.consts import (
  AudioDir, 
  W_RAF, 
  FILE_FORMAT, 
  SAMPLE_RATE
)

# uses essentia for audio io
# TODO compare essentia, librosa, or soundfile lib in terms of speed

def load_audio(audio_path: Path) -> np.typing.NDArray:
  log_file_start(str(audio_path))
  try:
    audio = MonoLoader(
      filename=str(audio_path), 
      sampleRate=SAMPLE_RATE
    )()
    log_file_end(str(audio_path))
    return audio
  
  except Exception as e:
    log_file_end(str(audio_path), success=False)
    print(f"failed to load audio from {audio_path}: {e}")
    return None


def load_metadata(audio_path: Path):
  log_file_start(str(audio_path))
  try:
    metadata = MetadataReader(
      filename=str(audio_path)
    )()
    log_file_end(str(audio_path))
    return metadata
  except Exception as e:
    log_file_end(str(audio_path), success=False)
    print(f"failed to load metadata from {audio_path}: {e}")
    return None
  

def load_performances(
  audio_directory=AudioDir.get_song_raw(W_RAF), 
  loader_function=load_audio,
) -> dict[str, np.typing.NDArray]:
  log_section('Load Performances')
  performances = {}
  for file_path in audio_directory.glob(FILE_FORMAT):
    audio = loader_function(file_path)
    performances[file_path.name] = audio

  return performances


def save_performances(
  performances: dict[str, np.typing.NDArray],
  save_path: Path = AudioDir.get_song_saved(W_RAF)
):
  for key, val in performances.items():
    np.savez(save_path / key, audio=val)

def save_audio(
    audio: np.typing.NDArray,
    save_path: Path = AudioDir.get_song_saved('test')
):
  np.savetxt(save_path, audio)

def get_saved_audio(
    save_path: Path = AudioDir.get_song_saved('test')
):
  audio = np.load('audio/test/saved.npz')
  return audio


def get_saved_performances(
    dir: Path = AudioDir.get_song_saved(W_RAF)
) -> dict[str, np.typing.NDArray]:
    performances = {}
    for file_path in dir.glob("*.npz"):
        perf = np.load(file_path)
        performances[file_path.name] = perf['audio']
    return performances


def get_song_to_test() -> np.typing.NDArray:
  audio = MonoLoader(
    filename='/home/toni/projects/perturb/audio/ween_rosesarefree/raw/1-31-2008 Part_0108.flac', 
    sampleRate=SAMPLE_RATE
  )()
  return audio

# test

