LLM PROJECT - SETUP NOTES (06/09/2026)

Goal:
Build a small language model from scratch using Python and PyTorch while
following the FreeCodeCamp / Infatoshi LLM tutorial.

1. MINICONDA

Installed Miniconda on my Chromebook Linux environment.

Miniconda lets me create separate Python environments for different projects.

Created an environment called "llm":

conda create -n llm python=3.11

Activate it with:

conda activate llm

When "(llm)" appears in the terminal, I know I am working inside this
environment.


2. PYTHON ENVIRONMENT

Using Python 3.11 for this project.

The environment keeps the project's packages separate from my normal/base
Python installation. This helps prevent dependency conflicts.


3. PYTORCH

Installed PyTorch.

PyTorch is the main machine learning library I will use to build the model.

My Chromebook does not have a CUDA-compatible NVIDIA GPU, so I installed
the CPU version of PyTorch.

Checked this using:

import torch
print(torch.__version__)
print(torch.cuda.is_available())

torch.cuda.is_available() returns False because I am using the CPU.

This means the model can still run, but training will be slower than on
a GPU.


4. OTHER LIBRARIES

Installed:

- NumPy - numerical/matrix operations
- Matplotlib - plotting and visualisation
- Jupyter - lets me write and run code in notebook cells
- ipykernel - connects my Python environment to Jupyter


5. JUPYTER

Registered my "llm" environment as a Jupyter kernel:

python -m ipykernel install --user --name llm --display-name "Python 3.11 (llm)"

This allows Jupyter notebooks to run using the packages installed in my
llm environment.


6. PROJECT

Created a folder:

my-llm

Created my first notebook:

bigram.ipynb

This is where I will start implementing the language model.


7. CURRENT SETUP

Chromebook
-> Linux
-> Miniconda
-> llm environment (Python 3.11)
-> Jupyter Notebook
-> PyTorch (CPU)

Next:
Start learning/using PyTorch and building the bigram language model.
