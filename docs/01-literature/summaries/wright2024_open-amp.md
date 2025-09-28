---
title: "Open-Amp: Synthetic Data Framework for Audio Effect Foundation Models"
authors: Alec Wright, Alistair Carson, Lauri Juvela
year: "2024"
link: https://arxiv.org/html/2411.14972v1
tags:
  - augmentation
relevance: high
---
## Abstract //todo shorten to summary!
This paper introduces Open-Amp, a synthetic data framework for generating large-scale and diverse audio effects data. Audio effects are relevant to many musical audio processing and Music Information Retrieval (MIR) tasks, such as modelling of analog audio effects, automatic mixing, tone matching and transcription. Existing audio effects datasets are limited in scope, usually including relatively few audio effects processors and a limited amount of input audio signals. Our proposed framework overcomes these issues, by crowdsourcing neural network emulations of guitar amplifiers and effects, created by users of open-source audio effects emulation software. This allows users of Open-Amp complete control over the input signals to be processed by the effects models, as well as providing high-quality emulations of hundreds of devices. Open-Amp can render audio online during training, allowing great flexibility in data augmentation. Our experiments show that using Open-Amp to train a guitar effects encoder achieves new state-of-the-art results on multiple guitar effects classification tasks. Furthermore, we train a one-to-many guitar effects model using Open-Amp, and use it to emulate unseen analog effects via manipulation of its learned latent space, indicating transferability to analog guitar effects data.

## Summary


## Quintessence


## 🛠️ Methods
- **Data:**  
- **Augmentations:**  
- **Features/Models:**  


## Takeaways for me

