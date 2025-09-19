
- perturbations are modular **pure** functions
- perturbations are collected as **first class members** in lists
	-> can be **passed** to composition-function ( **order of application** via dictionary or enum ) 
	-> modular pipeline important for ablation studies



```mermaid
graph TD
    A[Studio Recording] --> Pipeline
    A --> B[Extracted Cue Points]
    B --> Pipeline
    
    subgraph Pipeline
		E[Tempo Warp] 
		F[Pitch Shift] 
		G[Add Noise] 
		H[Add Reverb] 
		I[Amplitude Variation] 
		E --> F 
		F --> G 
		G --> H 
		H --> I
	end
	    
    I --> J[Augmented Audio]
    I --> K[Updated Cues]
    
    J --> L[Feature Extraction]
    
    L --> M[Evaluation]

classDef input fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#000
classDef perturbation fill:#fce4ec,stroke:#c2185b,stroke-width:2px,color:#000
classDef output fill:#e8f5e8,stroke:#388e3c,stroke-width:2px,color:#000
classDef evaluation fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000

class A,B input
class E,F,G,H,I perturbation
class J,K output
class L,M evaluation
```


## Order of perturbation application

1. any time-/warp-based perturbations
	else all other types of perturbations will also be stretched/compressed

2. any type of perturbation that is dependent on the audio file
	pitch shift, reverb/delay, eq, compression, dynamics (fade in/out, ..), 

3. all other that are independent
	noise, distortions, artifacts

## Dynamic Implementation per perturbation

- **tempo/timing** 
	-> section-based / cue-based

- **noise/ambient/crowd** 
	-> vary amplitude, panning, spectral content over time 
		volume relative to audio
		trigger on certain cues or sections ( -> crowd bursts )

- **Audio Effects/Acoustics** 
	-> mostly static, maybe slight variation

- **Volume/Amplitude** 
	-> Slow LFO / gaussian noise envelope

- **Pitch Shift** 
	-> very subtle micro fluctuation in some sections


#### Priority/Likelihood of Perturbations in real performances
Tempo/Timing **>>>** Noise/Crowd/Ambient **>>>** Volume/Amplitude **>>>** Pitch Drift **>>>** minor Distortions / Artifacts

