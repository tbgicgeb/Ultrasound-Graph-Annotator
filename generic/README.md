
# Table of Contents
- [1. Introduction](#introduction)
- [2. UGA interface scripts](#uga)
  - [2.1 Image annotation interface script](#image_annotation_script)
  - [2.2 Video annotation interface script](#video_annotation_script)
- [3. Installation](#installation)
  - [3.1 Miniconda installation](#miniconda)
  - [3.2 Dependency installation](#dependency)
- [4. Usage](#usage)
  - [4.1 Activate environment](#activate)
  - [4.2 Running image annotation](#image_annotation)
  - [4.3 Running video annotation](#video_annotation)

# 1. Introduction <a name="introduction"></a>
This file guides you on how to install and run UGA on Linux. Download the folder ```generic``` and unzip it.

# 2. UGA interface scripts <a name="uga"></a>

## 2.1 Image annotation interface script <a name="image_annotation_script"></a>
The script `annotate_images.py` provides the annotation of individual ultrasound images that may have been captured from the ultrasound video. The running of image annotation is written in Section [Running image annotation interface and interrelating nodules](#image_annotation).

## 2.2 Video annotation interface script <a name="video_annotation_script"></a>
The script `annotate_videos.py` provides the annotation of an ultrasound DICOM video. All the nodule annotations and marked frame information are written in the csv files common to all patients. These csv files are created at the location from the script `annotate_videos.py` is run. Therefore, the user must run the script `annotate_videos.py` from the same location everytime.
The running of video annotation and its salient features are written in Section [Running video annotation](#video_annotation).

# 3.Installation <a name="installation"></a>
The tool works in python environment. Therefore, it is required to first install miniconda and then create an environment and then install the dependicies for the tool.

## 3.1 Miniconda installation <a name="miniconda"></a>
We provide here the instructions for installing miniconda on linux x86. For more details and installation on other operating system, the user can go to [Miniconda Webpage](https://www.anaconda.com/docs/getting-started/miniconda/install). Following are the instructions to install [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install):
- Download the latest version of Miniconda by the following command:

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

- Install Miniconda by running the following command:

```
bash ~/Miniconda3-latest-Linux-x86_64.sh
```

- Enter Yes for all the questions.
- Close and re-open your terminal window for the installation to fully take effect, or use the following command to refresh the terminal:

```
source ~/.bashrc
```
  
The terminal must now show `(base)` at the start of command prompt. This means that the miniconda installation is complete. 

## 3.2 Dependency installation <a name="dependency"></a>
After installing the miniconda the user must install the dependicies for the tool GDA. We explain the installation separately for linux and windows.

### 3.2.1 Dependency installation in linux
A user must open up a terminal. If the terminal is not showing `(base)` at the start of command prompt, then there is a problem with miniconda installation. redo miniconda installation in this case. Otherwise, the user can run the script `installation_script.sh` to install all the dependicies. The keyword `(base)` at the beginning of command line prompt confirms that terminal has conda environment active. The user can also manually run the commands in the script `installation_script.sh` in this terminal.


### 3.2.2 Dependency installation in windows

A user must select Anaconda Prompt from the start menu or all applications of windows. A cmd will get opened up with `(base)` at the start of command prompt. The user must then run the script `installation_script.bat` in this terminal to install all the dependicies. The keyword `(base)` at the beginning of command line prompt confirms that terminal has conda environment active. The user can also manually run the commands in the script `installation_script.sh` in this terminal.

# 4. Usage <a name="usage"></a>

There are two scripts provided. `annotate_videos.py` is for annotating videos. `annotate_images.py` is for annotating the images. We first need to activate the installed environment that has been installed by the installation script. After that we can run these annotation scripts.

## 4.1 Activate environment <a name="activate"></a>

Inside a terminal with `(base)` at the beginning, the user can run following command to activate the environment that was created by the installation script:

`conda activate aiims_env`.

This command activate the environment `aiims_env`. This will be visible by the `aiims_env` at the beginning of the prompt.

## 4.2 Running image annotation <a name="image_annotation"></a>
To run the script `annotate_images.py`, first activate the installed environment as mentioned in Section [Activate environment](#activate). Now, the user can run the image annotation script `annotate_images.py` as follows:
```python 
python annotate_images.py
```
After running this script, image annotation interface gets opened up.

## 4.3 Running video annotation <a name="video_annotation"></a>
After activating the environment, the user can run the video annotation script `annotate_videos.py` as follows:
```python 
python annotate_videos.py
```

After running this script video annotation interface gets opened up.

# Note
The installation and annotation process for Fedora, Ubuntu, Windows 10 and Windows 11 has been tested. Users may try it over other operating system as well.


