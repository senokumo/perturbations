## global

| time features                                           | priority |
| ------------------------------------------------------- | -------- |
| avg tempo (bpm)                                         | high     |
| Overall Tempo Stability (Intra-Performance Variability) | high     |
| Global Timing Precision (Beat Jitter)                   | med      |

| dynamics features          | priority |
| -------------------------- | -------- |
| overall dynamic range (db) | high     |
| avg rms energy             | med      |

| spectral features             | priority |
| ----------------------------- | -------- |
| avg spectral centroid (Hz)    | high     |
| spectral centroid Variability | med      |
| avg spectral rolloff          | med      |
| abg spectral flatness         | low      |

| environment features                                  | priority |
| ----------------------------------------------------- | -------- |
| background noise floor (publikum, venue-noise)        | high     |
| Overall Signal-to-Noise Ratio (SNR)                   | med      |
| reverb characteristics (RT60 est.) - wie extrahieren? | low      |

## section

| time features              | priority |
| -------------------------- | -------- |
| section-specific avg tempo | high     |
| section Tempo Variability  | high     |
| Section Duration Ratio     | low      |

| dynamics features     | priority |
| --------------------- | -------- |
| Section Dynamic Range | high     |
| avg rms energy        | med      |

| spectral                       | prio |
| ------------------------------ | ---- |
| section spectral centroid mean | med  |
| section spectral variability   |      |

| structural               | prio |
| ------------------------ | ---- |
| section repetition count | low  |

## fazit

**Core Features (beide Ebenen):**
1. Tempo (Mean)
2. Tempo Variability
3. Dynamic Range
4. Spectral Centroid Mean
5. Spectral Centroid Variability

**Global-Only:** 6. Background Noise Floor 7. SNR 8. Reverb (RT60) 9. Overall Duration

**Section-Only:** 10. Duration Ratios 11. Transition Characteristics