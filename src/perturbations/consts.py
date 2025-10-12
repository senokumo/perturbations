from dataclasses import dataclass
from pathlib import Path


# constants

## audio extraction config
FILE_FORMAT = '*.flac'
SAMPLE_RATE = 22050

## song names
W_RAF = 'ween_rosesarefree'



# dataclasses

@dataclass(frozen=True)
class AudioDir:
  ROOT = Path(__file__).resolve().parent.parent.parent
  AUDIO_DIR = ROOT / 'audio'

  @staticmethod
  def get_song(performance):
      return AudioDir.AUDIO_DIR / performance / 'raw'


# test
perf_dir = AudioDir.AUDIO_DIR
print(perf_dir)
