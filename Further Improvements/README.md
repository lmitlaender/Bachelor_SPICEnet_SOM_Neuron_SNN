# Introduction
In this folder you find the further improvements upon the previous Original SNN Training.

We provide the final version in the "final_improvements" folder, specifically the final solution used was the "extraextra_lin_unchangedinp_log1p.ipynb" notebook utilising a 3-256-256-1 network architecture with ReLU activations and training with the AdamW optimizer + 64 Batch size + gradient clipping + learning rate scheduler (`ReduceLROnPlateau`) and no oversampling / no weighted sampling. We additionally utilise Huber loss instead of mean squared error here as a combination of MSE and MAE.

Additionally the final improvements folder has the best of our dataset generation notebooks with STDs as low as 0.001, an additional notebook with the same architecture but the SGD optimizer, and two other optimizers utilising [DenseWeights](https://github.com/SteiMi/denseweight) for over-sampling. These are not used in the final solution but were explored in the same step. Additionally, a copy of the snn conversion notebook for this architecture and data range is added which evaluates the final SNN.

The final ANN results can then be found in "thesis_results_copy" and "results". This is split because the results get overwritten if another model with the same training name is started. As such, "thesis_results_copy" serves as a persistent copy of our results.

the "other attempts" folder has various other experiments done in this step that slowly served to build towards our final implementation, are, however, not further explained