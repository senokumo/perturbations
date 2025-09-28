---
title: "SpecAugment++: A Hidden Space Data Augmentation Method for Acoustic Scene Classification"
authors: Helin Wang, Yuexian Zou, Wenwu Wang
year: "2021"
link: https://arxiv.org/abs/2103.16858
tags:
  - augmentation
relevance:
---
## Abstract //todo shorten to summary!
In this paper, we present SpecAugment++, a novel data augmentation method for deep neural networks based acoustic scene classification (ASC). Different from other popular data augmentation methods such as SpecAugment and mixup that only work on the input space, SpecAugment++ is applied to both the input space and the hidden space of the deep neural networks to enhance the input and the intermediate feature representations. For an intermediate hidden state, the augmentation techniques consist of masking blocks of frequency channels and masking blocks of time frames, which improve generalization by enabling a model to attend not only to the most discriminative parts of the feature, but also the entire parts. Apart from using zeros for masking, we also examine two approaches for masking based on the use of other samples within the minibatch, which helps introduce noises to the networks to make them more discriminative for classification. The experimental results on the DCASE 2018 Task1 dataset and DCASE 2019 Task1 dataset show that our proposed method can obtain 3.6% and 4.7% accuracy gains over a strong baseline without augmentation (i.e. CP-ResNet) respectively, and outperforms other previous data augmentation methods.

## Summary


## Quintessence


## 🛠️ Methods
- **Data:**  
- **Augmentations:**  
- **Features/Models:**  


## Takeaways for me

