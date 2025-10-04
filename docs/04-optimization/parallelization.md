- Phase 4: 
  propose more candidates ($\theta_1,\theta_2,\theta_3,\theta_4$) per iteration (Batch BO)
	for each $\theta$:
		sample multiple targets from feature copula
		generate augmentation for each target in parallel
		extract features in parallel
  return 4 distances to BO
  
- phase 2 feature extraction parallelization
- phase 5 final augmentation parallelization