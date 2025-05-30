# Ultrasound Graph Annotator: An Annotation tool for Multi-Nodule and Multi-Image Annotations of Ultrasound images of thyroid cancer nodules.
The repository is a tool that facilitates clinicians in annotating ultrasound DICOM images and videos. The tool will inter-relate the nodules in multiple images in a graphical display. The following screenshot gives an overview of how the interrelation of nodules is performed with images. The bottom left of the screenshot shows the graphical representation of image boxes, nodule boxes, and their interconnections.
![Image to display multiple images for a nodule.](images/show_all_nodule.png)

## Table of Contents
- [1. Introduction](#introduction) 
  - [1.1 Image annotation interface and nodule interrelation Overview](#image_annotation_overview)
  - [1.2 Video annotation overview](#) 
- [2. Caution while running the tool](#caution)
  - [2.1 Caution while running image annotation and interrelating nodules](#caution_directory) 
  - [2.2 Caution while running video annotation](#caution_video)
- [3. Requirements](#requirements)
- [4. Contact](#contact)


## 1. Introduction <a name="introduction"></a>
Radiologists require a tool to mark and annotate regions over ultrasound images and videos. The same region can be present in multiple images. We consider the case of thyroid ultrasound. Specifically, in the case of thyroid ultrasound, nodules are captured from different views, such as axial and sagittal. A doctor first looks at all views of the same nodule. After that, the doctor decides the TIRADS annotation for the nodule. A nodule has only one annotation, valid across all images in which the nodule appears. We have built a tool, Graph Dicom Annotator(GDA), keeping this in mind. Our tool provides the clinician with an interface where he can view images in any order, mark their orientation, and mark and interrelate nodules. In our tool, the nodule annotation is done only once. This annotation remains valid across all the images in which the nodule appears. Our tool also provides an easy way to navigate through a DICOM video to mark and annotate the frames in the video. The user can move backward and forward in the video frame by frame. The tool also allows users to write information about marked regions in text format. Therefore, this tool can mark and annotate any region in ultrasound DICOM images and ultrasound DICOM videos. The installation and running of UGA is explained in following 3 directories:
- ```linux```: If a user wishes to install and run UGA on linux system. Fully automated install and run scripts are there.
- ```windows```: If a user wishes to install and run UGA on window system. No installation is required. Prebuild executables are provided.
- ```generic```: If a the prebuild executable or autaomated installation script fails. This directory contains general instructions and can be used over any system. Though some dependency installation scripts are provided for ```linux``` and ```windows```.


### 1.1 Image annotation interface and nodule interrelation overview <a name="image_annotation_overview"></a>
This interface provides the annotation of individual ultrasound images that may have been captured from the ultrasound video. In practice, multiple images are captured from one or more ultrasound videos of a patient. Also, there may be some ultrasound images for which no ultrasound video exists. For example, in the case of thyroid ultrasound, the ultrasound images for sagittal views do not have a corresponding video. All the images captured for a patient need to be put in a single directory. Doing so will make interrelating the images and the nodules they contain easier. The user can specify the path of this directory, and the tool will list all image names in the directory. The user can open any image by clicking that image name, add nodules, and interrelate nodules among multiple images. The user can also mark the orientation of these images. All the annotations, nodule boundaries, image-nodule connection information, and orientations will be stored in files in that patient's directory. Note that if there is only one ultrasound DICOM image for a patient, then it is still required to put it in a directory containing only this patient image. The patient's directory is necessary because all the files for markings and annotations will be stored in this directory. The images can be in jpg/jpeg/png or RGB DICOM format. A user can right click a box and select the shape of the nodule i.e. whether polyline(which is freehand boundary) or a rectangle box. The following screenshot shows an instance of annotate image interface:
![Annotate image.](images/show_all_image_uga.png)


### 1.2 Video annotation overview <a name="video_annotation_overview"></a>
This interface provides the annotation of an ultrasound DICOM video. This interface provides an easy way to navigate through an ultrasound video and mark multiple nodules in the video. The video may be in DICOM or mp4 format. The user can play the video both in forward or backward direction. The user can also navigate through the video frame by frame both in forward or backward direction. Current frame number is also displayed. This provides an easy way to go to a specific frame. 
In this case as well, all the videos for the patient must be put in a directory named by the patient name. All the nodule boundaries will be stored in this directory. All the nodule annotations and marked frame information are written in the csv files common to all patients. These csv files are created at the location from where the interface is run. Therefore, the user must run the interface from the same location everytime.
The following screenshot shows an instance of annotating video:
![Annotate Video.](images/video_screenshot.png)

When the video interface is executed, two windows open up. One window is labeled axial, and the other window is labeled sagittal. The axial videos should be opened in the axial window. The windows do not have the control buttons to minimize, close, etc. This was done deliberately because the windows occupy the entire screen. If two screens are attached to the system, then each window will get opened on a separate screen. The window has the option to load the image, but this version should be used to annotate the video. The buttons are self-explanatory. The video to load can be in DICOM or mp4 format. It is preferable that the video is in the DICOM format. The tool has been tested for mp4 and RGB DICOM videos of ultrasound. 


## 2. Caution while running the tool <a name="caution"></a>

### 2.1 Caution while running image annotation and inter relating nodules <a name="caution_directory"></a>
- When selecting a patient's directory, the directory that contains the patient's image should be selected. There required images should not be in any subdirectory of the selected directory. Also, the user must click open after selecting the required directory in the selection panel. A double click should be done to select the directory, otherwise it will open up directory contents instead of selecting the directory.
- **Adding image nodule connection:** Following things needs to be taken care of when adding fresh nodule or adding image nodule connection.
  - When the user has started marking a fresh nodule or the user has started adding a connection from an image to an existing nodule, then the user must complete the marking of nodule boule boundaries, assigining the annotations to the nodule(if it is new), and saving the moarked boundaries and annotations(if it is new). Any other operation must be started after saving the nodule completely i.e. its boundaries and its annotation. The nodule saved indication will be given by the yellow second outer boundary of the nodule. even if the nodule got added by mistake, still the user must first complete the nodule marking and saving process. After that the nodule may be deleted.
  - Note that when an edge is added from an image to an existing nodule, then the nodule annotation need not be reassigned and the nodule annotation need not be saved again. The nodule annotation has already been assigned and saved. The user may relook at the nodule annotation and confirm that it is correct. At this stage if the user finds that the annotation of the nodule must be reassigned, then the user can directly reassign the nodule annotation and save the annotation just assigned. This new anotation of the nodule will be reflected for all images to which the nodule is connected.
  - Note that currently, the feature of deleting an edge between an image and nodule does not exist. Therefore, if by mistake an edge gets added between an image and a nodule, then the user will have to delete that nodule and add all the correct edges again for the nodule. This will incur a lot of work. Therefore, be careful while adding an edge from an image to an existing nodule. An easy way to prevent this is to visualize the nodule before adding the edge. A right click to the nodule box and selecting the option of displaying the nodule in all images will display the nodule boundaries in all the images in which the nodule has been marked. Now, the user can view the image in which a nodule needs to be added. This way it will be easier for the user to analyze whether the nodule just viewed exists in the current image?
- **Displaying multiple images or multiple nodules:**
  - When multiple images are displayed or when multiple nodules are displayed the user should not try to change the nodule boundaries or the nodule annotations.
- **Loading partially annotated patient's directory:**
  - When partially marked patient's directory is loaded then user must first click on an image box. this can be any image box. the user should not first click on a nodule box after reloading a partially annotated directory.



### 2.2 Caution while runing video annotation <a name="caution_video"></a>
When reloading partially annotated video, the by defult select nodule is the highest nodule number that has been added.

## 3. Requirements <a name="requirements"></a>
UGA works best on screen resolution 1920x964 or higher resolution. The input image or frame size in video should be less than 1400x900.

## 4. Contact <a name="contact"></a>
The following persons may be contacted for the tool:
- Dinesh Gupta :
  - Group leader, Translational Bioinformatics, International Centre for Genetic Engineering and Biotechnology, Aruna Asaf Ali Marg, 110 067 New Delhi, India, E-mail: dinesh@icgeb.res.in
- Ankit Singhal :
  - Project Scientist, Translational Bioinformatics, International Centre for Genetic Engineering and Biotechnology, Aruna Asaf Ali Marg, 110 067 New Delhi, India, E-mail: singhal.ankit9@gmail.com
- Ashish Kumar :
  - Senior Research Fellow, Translational Bioinformatics, International Centre for Genetic Engineering and Biotechnology, Aruna Asaf Ali Marg, 110 067 New Delhi, India, E-mail: ashthakur1321@gmail.com
