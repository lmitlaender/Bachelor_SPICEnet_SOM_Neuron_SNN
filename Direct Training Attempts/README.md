# Direct Training Attempts
We group our training attempts for SNN Regression by directly training the SNN here. 

All of these training notebooks are based on the code found here https://snntorch.readthedocs.io/en/latest/tutorials/tutorial_regression_1.html

This code is based on the following two papers:

[Alexander Henkes, Jason K. Eshraghian, and Henning Wessels. “Spiking neural networks for nonlinear regression”, arXiv preprint arXiv:2210.03515, October 2022.](https://arxiv.org/abs/2210.03515)

[Jason K. Eshraghian, Max Ward, Emre Neftci, Xinxin Wang, Gregor Lenz, Girish Dwivedi, Mohammed Bennamoun, Doo Seok Jeong, and Wei D. Lu. “Training Spiking Neural Networks Using Lessons From Deep Learning”. Proceedings of the IEEE, 111(9) September 2023](https://ieeexplore.ieee.org/abstract/document/10242251)

We copied the notebook found in the link above to additionally added some changes for our own exploration:

 - in snntorch_regression_1.ipynb we add an additional data generation method for taking the "features ** 2" over time as a function. It remains mostly unchanged from the original otherwise.
  
In the following copies from snntorch_regression_2 onwards additional changes were made. 
the 2 after snntorch_regression means that we now use 2 variables in the dataset, a change from the original where only one is used.
We additionally add some plotting for our own analysis, based on the original plotting already implemented.
We also already try to represent a gauss curve.

Lastly, in snntorch_regression_3_* we utilise 3 variable values in the dataset, standard deviation, mean and the input x and a mix of Leaky and Recurrent Leaky Neurons in the architecture.
This is also where the final graphs for the thesis were taken from.

All notebooks ending in input_output_constant utilise a constant expected target averaged after some setteling time and a constant input. The constant target is inspired by the following paper using constant expected outputs for their use case and then only counting the resulting membrane potential after some time.

[M. Gehrig, S. B. Shrestha, D. Mouritzen and D. Scaramuzza, "Event-Based Angular Velocity Regression with Spiking Networks," 2020 IEEE International Conference on Robotics and Automation (ICRA), Paris, France, 2020, pp. 4195-4202, doi: 10.1109/ICRA40945.2020.9197133](https://doi.org/10.1109/ICRA40945.2020.9197133)