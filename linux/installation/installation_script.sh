#!/bin/bash

# Function to handle conda activation across platforms
activate_conda() {
  local conda_base="$(conda info --base)"
  if [[ -n "$conda_base" ]]; then
    if [[ -f "$conda_base/etc/profile.d/conda.sh" ]]; then
      source "$conda_base/etc/profile.d/conda.sh"
    elif [[ -f "$conda_base/etc/fish/conf.d/conda.fish" ]]; then
      eval "$(conda shell.fish hook)"
    elif [[ -f "$conda_base/etc/profile.d/conda.csh" ]]; then
      source "$conda_base/etc/profile.d/conda.csh"
    elif [[ -f "$conda_base/Scripts/activate" ]]; then #windows
      source "$conda_base/Scripts/activate" #windows
    else
      echo "Cannot find conda activation script."
      exit 1
    fi
  else
    echo "Conda installation not found."
    exit 1
  fi
}

activate_conda

# Create the conda environment
conda create -n aiims_env python=3.8 -y

# Activate the environment
conda activate aiims_env

# Install packages
conda install matplotlib -y
conda install -c conda-forge pydicom -y
pip install python-gdcm 
pip install pillow tk PyQt5 opencv-python-headless pandas

echo "AIIMS environment created and packages installed."
