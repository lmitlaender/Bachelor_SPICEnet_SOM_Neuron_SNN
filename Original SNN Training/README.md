# Introduction
In this folder we present the original SNN training results before further improvements were made towards the end of the work.

# Data Generation and Dataset Analysis
We present four different datasets in the "data_generation" folder as well as their generation notebooks. They serve to create the data utilised for training, 1.000.000 records, of input value, mean and standard deviation as well as label (the result of the Gauss PDF).

Additionally, in the "analysis" folder we present a notebook to analyse the generated datasets for different factors.

# Model Training & Hidden Layer Evaluation
Model training in the final version of the original SNN training can be found in the "train_sinabs.ipynb" notebook.

The final version uses a 3-256-256-1 network architecture with SGD with 0.01 learning rate as the optimizer and 64 as the batch size. We use a 80% 20% split into train-test data and run one evaluation epoch per training epoch. We use MSE as the loss.

Additionally, we ran this training in this setup with different hidden layer sizes all checkpoints of which can be found in "results" and "thesis_results_hidden_layer_copy". The copy exists as "results" folders are overwritten when restarting training with the same training job name.

These hidden layer experiments are then evaluated in the "analysis" folder with the "evaluation_ANN.ipynb" notebook which creates a large second evaluation dataset to then run the evaluation for all different hidden layer size setups that were trained further than original experiments.

# SNN conversion

The snn conversion evaluation provides evaluation of how the final SNN transformed ANN performs by utilising different outputs to get final result values. These ways include: taking the last time-step, averaging all, averaging from x-th time-step.

Additionally, some experiments with spiking output were performed and it was attempted to transfer the SNN converted model to norse, however without any success.

The different channels snn conversion notebook attepts to use a different activation layer that `IAFSqueeze` that SINABS uses by default. This did not work well.

# Old Experiments
Older experiments were used to figure out preferred optimizer and batch size and are provided in an unordered manner.