# Introduction.
This file guides you on how to use UGA on Windows.

# Getting the Windows version.
Download the two zip ```uga_windows_video.zip``` and ```UGA_windows_images.zip``` and save them in a folder.

# Setting up.
Following are the setup steps that need to be performed before running the tool:
- Unzip the 2 zip ```uga_windows_video.zip``` and ```UGA_windows_images.zip```.
- This will create directories ```uga_windows_video``` and ```UGA_windows_images```.

# Running Image Annotation.
After unzipping step, image annotation can be run by following steps:
- Goto folder ```UGA_windows_images\dist\annotate_images```.
- An application named ```annotate_images``` is present in this folder.
- Double-click the application file and start annotating images.
- Note: You do not need to touch the ```_internal``` folder present in this directory.
- All the annotation and metadata files and marked frames will be generated in the patient's folder.
  
# Running Video Annotation.
After unzipping step, video annotation can be run by following steps:
- Goto folder ```uga_windows_video\dist\annotate_videos```.
- An application named ```annotate_videos``` is present in this folder.
- Double-click the application file and start annotating videos.
- Empty files ```all_data_video``` and ```all_data_video_marked_frames``` are present in this location.
  - All the TIRADS annotations and the locations of marked frames will be appended in these files.
- Note: You do not need to touch the ```_internal``` folder present in this directory.

# Note
The executables have been tested over Windows 10 and Windows 11. If some problem is there, the user can install and run UGA as mentioned in the ```generic``` folder.
