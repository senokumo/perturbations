
from pathlib import Path
from essentia.standard import MonoLoader, MetadataReader

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

def load_audio(audio_path):
  try:
    audio = MonoLoader(
      filename=str(audio_path), 
      sampleRate=SAMPLE_RATE
    )()
    return audio
  
  except Exception as e:
    print(f"failed to load audio from {audio_path}: {e}")
    return None


def load_metadata(audio_path):
  try:
    metadata = MetadataReader(
      filename=str(audio_path)
    )()
    return metadata
  except Exception as e:
    print(f"failed to load metadata from {audio_path}: {e}")
    return None
  

def load_performances(audio_directory=AudioDir.get_song(W_RAF), loader_function=load_audio):
  performances = {}
  for file_path in audio_directory.glob(FILE_FORMAT):
    audio = loader_function(file_path)
    performances[file_path.name] = audio

  return performances


# test

metadata = load_performances(AudioDir.get_song(W_RAF), load_metadata)
print(metadata)