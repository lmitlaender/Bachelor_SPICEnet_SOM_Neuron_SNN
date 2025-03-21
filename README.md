# Introduction
In this repository you can find all experiments, data generation, training, analysis and evaluation as well as ANN-to-SNN conversion for the bachelor's thesis "SPICEnet Integration in the Neuromorphic Intermediate Representation Framework" by Lutz Mitländer supervised by Prof. Dr. Cristian Axenie at the Nuremberg Institute of Technology Georg Simon Ohm's faculty of computer science.

The goal was to train a spiking neural network to compute the Gauss PDF for inputs of input value, mean, and standard deviation. This was part of a larger project during the integration of the [Sensorimotor Processing, Intelligence, and Control with Embedded Neural Networks (SPICEnet)](https://github.com/th-nuernberg/spicenet/tree/nir-integration) into the [Neuromorphic Intermediate Representation (NIR)](https://github.com/neuromorphs/NIR/tree/main).

All code for the overarching solution can be found in [this branch of the SPICEnet repository](https://github.com/th-nuernberg/spicenet/tree/nir-integration). Tests of the final implementation are supplied as Jupyter Notebook in the notebooks folder of the branch.

The repository is organized into folders representing chapter or sections of the thesis appearing in the following order:

  1. Original SNN Training
  2. Direct Training Attempts
  3. Further Improvements
   
The "Original SNN Training" folder has all ANN-to-SNN training as well as data generation and analysis as found in the first part of the work.

In the "Direct Training Attempts" folder we have our exploration into a training method for spiking neural network regression. The exact details and where the methods were inspired by can be found in the README.md in the folder.

The "Further Improvements" folder has all further ANN-to-SNN experiments once it was clear that the original model did not perform quite as well as we wanted, however still quite well. This includes different attempts at training using different normalization and standardization attempts as well as label transformation with log1p. We also attempt various over sampling methods. The final solution can be found in the subfolder "final_improvement".

In the SNN conversion notebooks some evaluation plots are adapted from the original SPICEnet implementation.

## Requirements
The requirements are either found in the .txt or installed in the notebooks themselves with "!" commands