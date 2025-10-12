from dataclasses import dataclass
from pathlib import Path


# constants

## audio extraction config
FILE_FORMAT: str = '*.flac'
SAMPLE_RATE: int = 22050

## song names
W_RAF: str = 'ween_rosesarefree'



# dataclasses

@dataclass(frozen=True)
class AudioDir:
  ROOT: Path = Path(__file__).resolve().parent.parent.parent
  AUDIO_DIR: Path = ROOT / 'audio'

  @staticmethod
  def get_song(song: str) -> Path:
      return AudioDir.AUDIO_DIR / song / 'raw'


# test
perf_dir = AudioDir.AUDIO_DIR
print(perf_dir)
