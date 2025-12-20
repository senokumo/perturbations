from pylab import plot, show, figure, imshow
# %matplotlib inline
import matplotlib.pyplot as plt

from perturbations.data.audio_io import get_song_to_test, save_audio, get_saved_audio
from perturbations.feature_extract import extract_rhythm

perf = get_song_to_test()
save_audio(perf)
perf_saved = get_saved_audio()


print('perf raw', perf)
print('perf saved', perf_saved)
rhythm = extract_rhythm(perf)




