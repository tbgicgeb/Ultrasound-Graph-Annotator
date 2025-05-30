
# Introduction.
This file guides you on how to install and run UGA on Linux.

# Getting the Linux version.
Download the folder ```linux``` and unzip it.

# Installation. 
Following are the installation steps:
- Go to folder ```linux/installation```.
- Do right-click and select Open in Terminal.
  - This will open up a terminal in this folder.
  - Alternatively, you can open a terminal and move to this location.
- Run command ```chmod +x *.sh``` in this terminal.
  - This will make files in this folder executable.
- Now run, ```./install_miniconda_and_custom_env.sh``` in this folder.
  - This will install all the requirements to run the tool.
  - If this command exists without error, then the tool can be run.

# Running Image Annotation.
After installation, image annotation can be run by following steps:
- Goto folder ```linux/image_annotation```.
- Run ```chmod +x run_image_annotation.sh```.
- Run ```./run_image_annotation.sh```.
  - This will open up the image annotation interface, and you can continue with the annotation.
  - All the annotation and metadata files and marked frames will be generated in the patient's folder.

# Running Video Annotation.
After installation, video annotation can be run by following steps:
- Goto folder ```linux/video_annotation```.
- Run ```chmod +x run_video_annotation.sh```.
- Run ```./run_video_annotation.sh```.
  - This will open up the video annotation interface, and you can continue with the annotation.
  - The files ```all_data_video``` and ```all_data_video_marked_frames``` will be created in the folder ```linux/video_annotation```.
  - Every time the video annotation is run, the TIRADS annotation and the location of marked frames will be saved in these files.

# Note
The installation and annotation process for Fedora and Ubuntu has been tested. Users may try it over other Linux distros as well.

