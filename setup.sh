#!/usr/bin/env bash
set -e  # Exit immediately on error

# --------------------------------------------
# Project setup script
# Usage: bash setup.sh
# --------------------------------------------

ENV_NAME="triagemd"
PYTHON_VERSION="3.11.6"

echo "Setting up Conda environment: $ENV_NAME"

# Check if conda is installed
if ! command -v conda &> /dev/null; then
    echo "Error: Conda not found. Please install Miniconda or Anaconda first."
    exit 1
fi

# Initialize Conda in this shell
source "$(conda info --base)/etc/profile.d/conda.sh"

# If the environment exists, remove it
if conda env list | grep -qE "^$ENV_NAME\s"; then
    echo "Environment '$ENV_NAME' already exists. Removing it..."
    conda remove -y -n "$ENV_NAME" --all
fi

# Create a new environment
echo "Creating conda environment '$ENV_NAME' with Python $PYTHON_VERSION..."
conda create -y -n "$ENV_NAME" python="$PYTHON_VERSION"

# Activate the environment
echo "Activating environment..."
conda activate "$ENV_NAME"

# Update pip, setuptools, and wheel
echo "Updating pip, setuptools, and wheel..."
pip install --upgrade pip setuptools wheel

# Install Conda-managed packages
echo "Installing core packages via Conda..."
    conda install -y -c conda-forge numpy=1.26.4 pandas=2.1.4 networkx=3.2.1 pydantic=2.5.2

# Install pip-only packages
echo "Installing additional Python packages via pip..."
pip install \
    google-cloud-aiplatform==1.97.0 \
    google-generativeai==0.8.5 \
    gradio==5.49.1 \
    langchain-anthropic==1.0.1 \
    langchain-community==0.4.1 \
    langchain-core==1.0.3 \
    langchain-deepseek==1.0.0 \
    langchain-google-vertexai==3.0.2 \
    langchain-openai==1.0.2

echo "Setup complete. Environment $ENV_NAME is ready!

