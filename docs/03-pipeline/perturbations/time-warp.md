# Dynamically Section-Based
## Concept:

-> *essentially a wrapper around librosa phase vocoder or pyrubberband*

- is a function that 
	**takes** 
		audio (as waveform array + sample rate)
		cue points 
		sets of labeled warp functions  
	**returns** 
		warped audio 
		warped cue points

### Order of execution:
1. divide audio into sections based on cue points 

2. extract features of sections and store a "section state vector"
	rms / loudness
	tempo / beat strength
	spectral features
	
3. map section state to warp function (map function)
	statically / rule based
	dynamically -> nearest neighbor

4. apply warp using 
	librosa (only supports linear warp -> approximate by dividing into subsections)
	pyrubberband (supports tempo maps)
	-> (optionally add smooth transitions between sections to reduce effect of abrupt jumps)

5. apply warp function to values of cue point list

6. concatenate resulting warped sections


**optional enhancements:**
	- random perturbation (global?) ontop of section based warping
