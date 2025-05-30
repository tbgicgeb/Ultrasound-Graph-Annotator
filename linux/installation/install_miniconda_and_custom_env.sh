#!/bin/bash

# --- Configuration ---
MINICONDA_INSTALL_DIR="$HOME/miniconda3"
MINICONDA_INSTALLER_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
MINICONDA_INSTALLER_NAME="Miniconda3-latest-Linux-x86_64.sh"

# --- Functions ---

log_info() {
    echo -e "\n\033[1;34mINFO:\033[0m $1"
}

log_success() {
    echo -e "\n\033[1;32mSUCCESS:\033[0m $1"
}

log_error() {
    echo -e "\n\033[1;31mERROR:\033[0m $1" >&2
    exit 1
}

check_command() {
    command -v "$1" >/dev/null 2>&1 || { log_error "$1 is not installed. Please install it."; }
}

# --- Main Script ---

log_info "Starting Miniconda installation and custom environment setup..."

# 1. Check for necessary commands
check_command "wget"

# 2. Download Miniconda installer
if [ ! -f "$MINICONDA_INSTALLER_NAME" ]; then
    log_info "Downloading Miniconda installer..."
    wget "$MINICONDA_INSTALLER_URL" -O "$MINICONDA_INSTALLER_NAME" || log_error "Failed to download Miniconda installer."
else
    log_info "Miniconda installer already exists: $MINICONDA_INSTALLER_NAME"
fi

# 3. Install Miniconda
if [ ! -d "$MINICONDA_INSTALL_DIR" ]; then
    log_info "Installing Miniconda to $MINICONDA_INSTALL_DIR..."
    bash "$MINICONDA_INSTALLER_NAME" -b -p "$MINICONDA_INSTALL_DIR" || log_error "Failed to install Miniconda."
else
    log_info "Miniconda already installed at $MINICONDA_INSTALL_DIR. Skipping installation."
fi

# 4. Initialize Conda for the current shell session
log_info "Initializing Conda..."
# Check if Conda init lines are already in .bashrc or .zshrc
SHELL_RC_FILE=""
if [ -f "$HOME/.bashrc" ]; then
    SHELL_RC_FILE="$HOME/.bashrc"
elif [ -f "$HOME/.zshrc" ]; then
    SHELL_RC_FILE="$HOME/.zshrc"
fi

if [ -n "$SHELL_RC_FILE" ]; then
    if ! grep -q "# >>> conda initialize >>>" "$SHELL_RC_FILE"; then
        log_info "Adding Conda initialization to $SHELL_RC_FILE..."
        "$MINICONDA_INSTALL_DIR/bin/conda" init "$(basename "$SHELL")" || log_error "Failed to initialize Conda."
    else
        log_info "Conda already initialized in $SHELL_RC_FILE. Skipping init."
    fi
    # Source the RC file to apply changes to the current shell
    source "$SHELL_RC_FILE" || log_error "Failed to source $SHELL_RC_FILE. Please try sourcing it manually or restart your terminal."
else
    log_error "Could not find .bashrc or .zshrc. Conda initialization might not work. Please initialize Conda manually: $MINICONDA_INSTALL_DIR/bin/conda init <your_shell_name>"
fi

# Ensure base environment is activated for the current script's execution
log_info "Activating Conda base environment for script execution..."
#conda activate base || log_error "Failed to activate Conda base environment. Ensure 'conda' command is available."

# --- CUSTOM CONDA ENVIRONMENT CREATION/INSTALLATION ---
# 
# IMPORTANT: Add your commands here to create or install your specific Conda environment.
# Examples are provided below. Uncomment and modify as needed.
# 
log_info "Starting custom Conda environment creation/installation..."
./installation_script.sh
# Example 1: Create a new environment from scratch
#conda create -n om_env python=3.9 -y || log_error "Failed to create my_custom_env."

# Example 2: Create an environment from an environment.yml file (assuming it's in the same directory as this script)
# if [ -f "environment.yml" ]; then
#     conda env create -f environment.yml -y || log_error "Failed to create environment from environment.yml."
#     # After creation, if you want to activate it for further installs in this script:
#     # conda activate my_env_name_from_yml # Replace with the actual name from your yml
# else
#     log_error "environment.yml not found. Cannot create environment from file."
# fi

# Example 3: Install packages into the base environment (less recommended for isolated apps)
# conda install -n base numpy pandas -y || log_error "Failed to install packages into base."

# Example 4: Create a specific environment and install packages into it
# conda create -n my_app_env python=3.9 matplotlib scipy -y || log_error "Failed to create my_app_env."
# # Then activate it to install pip packages if necessary
# conda activate my_app_env || log_error "Failed to activate my_app_env."
# pip install SomePythonPackage || log_error "Failed to install SomePythonPackage."
# # If you have a requirements.txt file:
# # pip install -r requirements.txt || log_error "Failed to install packages from requirements.txt."

# Example 5: If you want to install specific packages for your PyQt app after creating the environment
# conda create -n my_pyqt_env python=3.9 pyqt -c conda-forge -y || log_error "Failed to create my_pyqt_env."
# conda activate my_pyqt_env || log_error "Failed to activate my_pyqt_env."
# # You might also need to install the XCB plugin if it's not pulled by default or if you need a specific version
# # conda install -n my_pyqt_env qt-plugin-xcb -c conda-forge # (This package name might vary or be included by default)
# log_success "Custom PyQt environment 'my_pyqt_env' created. Remember to install system X11 dependencies if needed."

log_info "Finished custom Conda environment creation/installation section."
# --- END CUSTOM CONDA ENVIRONMENT CREATION/INSTALLATION ---

log_success "Miniconda installed and custom environment commands executed!"
log_info "To use your environments, you may need to restart your terminal or run 'source $SHELL_RC_FILE'."
log_info "To activate a specific environment, use 'conda activate <your_environment_name>'"
