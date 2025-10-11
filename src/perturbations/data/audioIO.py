
from pathlib import Path
import essentia.standard as es
from perturbations.consts import W_RAF, FILE_FORMAT, SAMPLE_RATE, Directory


# uses essentia for audio io
# TODO compare essentia with librosa in terms of speed



def load_performances(audio_directory, loader_function):
  performances = {}
  for file_path in audio_directory.glob(FILE_FORMAT):
    audio = loader_function(file_path)
    performances[file_path.name] = audio

  return performances


def load_audio(audio_path):
  try:
    audio = es.MonoLoader(
      filename=str(audio_path), 
      sampleRate=SAMPLE_RATE
    )()
    return audio
  
  except Exception as e:
    print(f"failed to load audio from {audio_path}: {e}")
    return None


def load_metadata(audio_path):
  try:
    metadata = es.MetadataReader(
      filename=str(audio_path)
    )()
    return metadata
  except Exception as e:
    print(f"failed to load metadata from {audio_path}: {e}")
    return None


