from pathlib import Path
import librosa
import numpy as np
from typing import Optional, Dict
from numpy.typing import NDArray

from perturbations.consts import SAMPLE_RATE


def load_audio(
    audio_path: Path, 
    sr: int = SAMPLE_RATE
) -> NDArray:
    try:
        audio, _ = librosa.load(str(audio_path), sr=sr)
        return audio
    except Exception as e:
        raise RuntimeError(f"Failed to load {audio_path}: {e}")

def load_performances(
    audio_directory: Path,
    sr: int = SAMPLE_RATE
) -> Dict[str, np.ndarray]:
    performances = {}
    
    for file_path in audio_directory.glob('*'):
        audio = load_audio(file_path, sr=sr)
        if audio is not None:
            performances[file_path.stem] = audio
    
    print(f"Loaded {len(performances)} files")
    return performances


def save_performances(
    performances: Dict[str, np.ndarray],
    save_dir: Path
):
    save_dir.mkdir(parents=True, exist_ok=True)
    
    for name, audio in performances.items():
        save_path = save_dir / f"{name}.npz"
        np.savez_compressed(save_path, audio=audio)
    
    print(f"Saved {len(performances)} files to {save_dir}")

# TODO relevant?
def load_saved_performances(
    save_dir: Path
) -> Dict[str, np.ndarray]:
    performances = {}
    
    for file_path in save_dir.glob("*.npz"):
        data = np.load(file_path)
        performances[file_path.stem] = data['audio']
    
    return performances