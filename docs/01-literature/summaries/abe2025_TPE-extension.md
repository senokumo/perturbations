---
title: Tree-Structured Parzen Estimator Can Solve Black-Box Combinatorial Optimization More Efficiently
authors: Kenshin Abe, Yunzhuo Wang, Shuhei Watanabe
year: "2025"
link:
  - https://arxiv.org/abs/2507.08053
tags:
  - optimization
relevance: high
---
## Abstract //todo shorten to summary!
abstract:: Tree-structured Parzen estimator (TPE) is a versatile hyperparameter optimization (HPO) method supported by popular HPO tools. Since these HPO tools have been developed in line with the trend of deep learning (DL), the problem setups often used in the DL domain have been discussed for TPE such as multi-objective optimization and multi-fidelity optimization. However, the practical applications of HPO are not limited to DL, and black-box combinatorial optimization is actively utilized in some domains, e.g., chemistry and biology. As combinatorial optimization has been an untouched, yet very important, topic in TPE, we propose an efficient combinatorial optimization algorithm for TPE. In this paper, we first generalize the categorical kernel with the numerical kernel in TPE, enabling us to introduce a distance structure to the categorical kernel. Then we discuss modifications for the newly developed kernel to handle a large combinatorial search space. These modifications reduce the time complexity of the kernel calculation with respect to the size of a combinatorial search space. In the experiments using synthetic problems, we verified that our proposed method identifies better solutions with fewer evaluations than the original TPE. Our algorithm is available in Optuna, an open-source framework for HPO.

## Summary


## Quintessence


## 🛠️ Methods
- **Data:**  
- **Augmentations:**  
- **Features/Models:**  


## Takeaways for me

