
from pathlib import Path
import essentia.standard as es

ROOT = Path(__file__).resolve().parent.parent.parent.parent
AUDIO_DIR = ROOT / 'audio'
SONG1_DIR = AUDIO_DIR / 'ween_rosesarefree' / 'raw'

FILE_FORMAT = '*.flac'
SAMPLE_RATE = 22050

def load_from_directory(audio_directory, loader_function):
  audio_files = {}
  for file_path in audio_directory.glob(FILE_FORMAT):
    audio = loader_function(file_path)
    audio_files[file_path.name] = audio

  return audio_files


def load_audio(audio_path):
  try:
    audio = es.MonoLoader(filename=str(audio_path), sampleRate=SAMPLE_RATE)()
    return audio
  except Exception as e:
    print(f"failed to load audio from {audio_path}: {e}")
    return None


def load_metadata(audio_path):
  try:
    metadata = es.MetadataReader(filename=str(audio_path))()
    return metadata
  except Exception as e:
    print(f"failed to load metadata from {audio_path}: {e}")
    return None


audio = load_from_directory(SONG1_DIR, load_audio)


print(dir(audio))
