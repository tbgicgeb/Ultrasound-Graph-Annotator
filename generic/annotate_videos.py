#My_Info_Window deleting the info window 
#why above got called

#package install order
# conda create -n aiims
# conda activate aiims
# conda install matplotlib
# conda install -c conda-forge pydicom
# pip install python-gdcm
# pip install pillow tk PyQt5 opencv-python-headless pandas
#
#dicom_obj_loaded_annotated: This variable is not used aymore. Therefore, deleting this variable.

#First complete the code for saving the annotations when the save button gets clicked.
#The annotations can be written to the common csv file as well as to some binary file.
#First complete the writing for csv file.
#Do all the writing for binary file at last.
#The updation for loading the annotation for the backward movement ned not be done now. The reason
#is that currently the backward and forward movement may be for some different nodule. 
#Hence, if the new nodule has been added and saved then why to load. Also, when adding a new nodule,
#we are not destroying or reinitializing the earlier nodule window. 
#Hence, the information for all the nodules is there in the currently created window objects.
#Whenever a nodule is selected by the user, the annotation for that nodule will be displayed to the user.
#Now, this also needs to be looked that when to close the nodule selection.
#The solution is very simple, The last nodule over which the button was clicked, whether to display the annotation window or to
#hide the annotation window, is the selected nodule to draw the curves. This information of nodule selection must also be passed 
#somehow to the main window, which actually does the drawing.
#Currently, the flow seems like add a nodule, the nodule selection happens at that time only. The user never goes back to the 
#the nodule earlier marked. Hence, this pass of information is not required. But, later, if we want to update the earlier marked nodules, 
#then this pass of information of the currently selected nodules can be easily done through a global variable. 
#Also, The markings has to be displayed only for the currently selected nodules. 
#Therefore, should we create separate folders for the markings of the different nodules.
#Ans is yes. We have only one channel to store the information. Therefore, the information for each nodule has to be saved separately. 
#A space saving way can be only to store the markings in the binary image as the list of end points(which are disjunct).
#Currently working with creating different folders for different nodules.
#And lets start with the gloal variable which says the nodule selected.  
#First complete the code for adding colors to the lines drawn and saving the annotations. The color should change when 
#a new nodule gets added.
# 

#TODO Later: Currently, the user has only one mouse. but it may also happen that the user clicks on save for one, while the save is being completed, the user clicks on another save in another window. In that case, mixing of writing may happen.
#Otherwise, if the save for two nodules is clicked too quickly, even then the events will be fired and served one after the another.
#Hence, no mixing of writing. separate files for separate types(axial, sagital) will be looked at later.  
#I can replace all tabs by 4 spaces to maintain the code consistency

#The save annotation has been completed. Now, the following things are remaining:
#1: The color of the nodule button should be same as the color of the marking.
#2: The add nodule should create a folder and other things for markings.
#            Now the dicom frames path is being set whenever a nodule gets added.
#            instead of array, have the dicom_frames_path as a dict and initialize it at the beginning when the video gets opened.
#            Therefore, the software will have the following changes:
#                1: no more saving of markings without add nodule button. this is not reqd. the marking is disabled without add nodule button.
#                2: the save frame has to pick the folder name according to the current nodule. Therefore:
#                    a: have an array of dicom frame path.
#                    b: also have a variable specifying the maximum number of nodules. This variable may have some utility later on.
#                    c: this point is done.
#2.1: The color of action button over the toolbar also needs to be updated.
#    Done in theory. needs to be tested.
#2.2: Chk all the uses of toolbar and chk if it requires any change.
#2.2.1: Handling of add nodule clicked should be completed properly.
#        Seems completed
#2.5: The color used to mark the images also needs to be updated. done.
#3: The saving of the image should also be updated. seems completed.

#Todo:
#The marking of images for different nodules has to be completed. done
#first complete the saving of image. seems completed.
#Todo Run: The loading of frame in case of scaled image should also be tested. 
#clear extra var should also be checked again for correctness.
#Whenever adding a nodule, the markings for prev nodules should disappear. done.
#Then above has to be done in conjunction with updating the Load annotated frame. done.
#Load annotated frame also has to be updated wrt the nodule for which the frame is to be loaded. done.
#frame marked array has to be different for different nodules. done.
#error message window when more than 5 nodules gets added.(may be tried later.)
#update all places where frame_marked_array is used. done
#Todo: seems done.
#First write the framesmarked in the csv file. do this while saving frames.
#Then read that csv file to load frame marked array
#When moving forward and backward, the frame marked array for the current nodule must be used. done. update for frame handles that. 

#now the color to be used for marking and  saving the images should be done correctly. done
#now doing the thing required to color the actions in the toolbar.
#done in theory

#The plotting of line in the required channel is also required when moving back and forth through the window and 
#the loading of marked frame and displaying that also needs to be required.

#The hiding of plotted annotations while annotating another nodule is also required.
#earlier the frame index annotated information was there in the csv file as well. currently, this is not there.
#In fact, create a new csv file that has the frame marked info, along with the frame filename. The image file type and inputfilename
#should be the first two columns

#do changes in mouse press and mouse moved so that the marking will occur only if current nodule index is greater than -1. done.

#Todo:
#Whenever reloading a partially annotated file, the infomartion of how many nodules present should also be loaded and the add nodule should be
#called that many times and the current nodule index must be set to the last nodule added. And that will automatically happen when add nodule
#is called.

#Todo: test for partially annotated video file with 1 and 2 nodules added should also be done. 

#Todo: going back to earlier marked nodule using a global variable is remaining. That can be done after testing the current code.
#After that binary encoding of information can be done.
#Whether the earlier interpolation was Inter_Area or Linear. Try again linear interpolation as well.
#we can add error message when addnodule is clicked if nothing is opened

#CAUTION:
#whenever adding a nodule, clicking save button on annotation is necessary. The reason is that, otherwise, the folder will be created but 
#no entry will be saved in csv. hence, when next time opening the video, it will not be possible to add the nodule, otherwise, 
#directory should not exist already error will come.

#Todo urgent:
#When close image without saving is done, added nodule actions does not go. They should also go.
#QWidgetAction clicked is not getting triggered

#At this point of time it is easier to think of dictionary of action in main windowitself. done.
#Whenever clicked of a nodule action is done, the windows corresponding to all other nodules should be made hidden. done.
#slightly increase the width for annotation so that all 5 nodules buttons are visible. done.
#Todo: Make sure that the nodule annotation window gets displayed at the required location
#Todo: I was not able to add nodules to image. The reason was that dicom frames path was not available. Correct this as soon as possible.

#May be the frameless aspect of the window making it to display at a slightly different location. Hence, make the window showing at the bottom.

#Todo:
#    1: len of df obtained for a file does not tell num nodules.
#    2: At the time of reloading, the last row of any nodule should get loaded.
#    3: When a particular nodule is selected, it should be highlighted somehow. 
#        a: Then we may not require to have the widget for that nodule in a different color.

#TODO urgent in following function:
#    def perform_nodule_selected(self, nodule_index):
#        """
#        This function is called to perform some basic functions when a nodule is selected either by seleting 
#        that nodule or by adding that nodule for the first time.
#        #Todo urgent: This function must also do following:
#        1: clear the image markings
#        2: if the frame displayed is marked for that nodule the marked frame for that nodule should be loaded.    
#        """
#TODO: The above functionality of loading the marked frame should also be tested. seems done. the loading needs to be tested.

#Todo urgent:
#When reinitializing the slider is not getting reinitialized and the toolbar should also have been reinitialized.
#
#This needs to be done in add slider        self.slider.setValue(self.frameIndex)
#The add nodule button, nodule parameters also needs to be reset
#Testing needs to be done on different images.

#ToThink: The actions just needs to be removed from the toolbar and need not be deleted. But, as per the documentation, the 
#action button may be set for delete later. Therefore, just first try anootationg a few videos and gap between at least two video 
#should be 15 min.
#Todo:
#The easiest and the bug free(not worrying  about the action button being garbage collected.) method is to add all the actions initially to
# the toolbar. Use numNodules to manage how many actions are there on toolbar. 
#Just set the toolbar as set visible as true whenever a nodule gets added. Also, change the set visible as false when the nodule gets 
#removed(because the video/image is done with and the nodule thing needs to be reset.)

#Todo:
#The process of hiding, showing and reinitializing can be done to the 5 annotation windows. This will make the program memory efficient.

#Todo:
#The dicom frames path needs to be set for images as well. the reason is that there can be multiple nodules within an image.   

#Todo: If the window gets crashed, the partial things  like folder getting  created should not be there.
#The set visible thing worked fine when adding the 

#Iamdeveloping custom widget to show message

#Apart from the things, that I am implementing now, 

#up, down , left, left, right keys may be used for frame advancement.

#currently not allowing the negative offset. This may be added but 
#first complete the current version.

#It will be even better if the info windows are showed up saying moved
#so many frames

#Also, if the message is more elaborate in the corner conditions that
#says 30 frames are not available. Movd 10 frames ahed. 
#similar messages can be there for the backward move as well.

#The problem is that the we need to need to exit from the event to show the top level window. And if we activate the top level window within
# the event processing then the program gets stuck in an infinite loop. 
#Therefore, we need a separate thread that shows that info window temporarily, so that we readily get out of the event processing,
#the top level window gets activated and the info msg gets shown. 

#Therefore, it will be better to have a separate class that has the instance of the info class. That class will handle the 
#thread to show the info message temporarily.

#Meanwhile, the thread is running, there is a risk that the user does not perform any other action.
#Therefore, this problem will be handled by two strategies:
#1: The time for display of that window will be less like 0.6 sec.
#2: Also, before processing any event we can join to that info thread class. This way we can be sure that no info msg is being displayed 
#before the processing the event. Also, it will be better if we 
#The show ans close of predefined dialog(within the event processing) as well suffered with the same issue of displaying the transparent 
#window. Also, I know that even the loading  window suffered the same  issue.  

#The thread thing worked for save button of save annotation.
#now do this for save frame and for frame advancement.
#Also for the loading window

#for the saved showing for annotation, color change, writing text as saved and then reverting back will be more appealing.
#The custom label window is anyway working fine.
#The saved window and num frames advanced is the only thing that needs to be resolved.

#I already have actions added to toolbar.
#I can add these actions to a menu instead.
#The menu bar will have add nodule and the menu items will be the nodules.
#or the selection of the nodule may be thought of.
#The items of the menu will still be colurful.
#The toolbar  may still be there.
#The same actions may be used for th toolbar and menubar.
#In this case, the action only for the selected nodule will be visible.
#Actually, we add only at beginning and only set visible needs to be changed later.
#TODO: change save button to saved when the annotation has been saved.
#resave will also be possible.

#select nodule should not trigger between show and hide. do later.
#The alternating between show and hide was only for the initial nodule.
#chk it later. But now the save button in annotation window is creating problem. chk why?

#select nodule should add the nodule, if not present already.
#also, the noduule indices already added should be displayed.

#Most of the information is now in perform_nodule_selected and therefore, now the add_nodule_clicked_is_not_required.

#The showing of nodule indices done and whenever selecting a previously done nodule then having saved instead of save can be done 
#later.

#on reinitialize the annotation window is not getting reinitialized and also the annotation window does not 
#get hidden and also the nodule does not get removed.
#assuming 1 nodule per image, which is mostly the case.
#the placing of menubar in grid and computesizes is remaining. done.

#When switching between multiple nodules, close current image does not close the annotation window. also, the switch takes 
# 2 clicks from menu seletion. why?
#The reason is very simple. When the action menu was trigerred, the other windows were not made hidden. as visible. That should be done now.


#one more serious problem. Clickng on the nodule button changes the annotation window, but it does not change the 
#nodul;e index written. Cliucking on the nodule button should not have changed the annotation window. 
#Actually, I have added all the nodules initially to the toolbar and I am displaying only the required one.
#But, if anythiong is not displayed, its action also does not take place.
#chk which triggered is being called?

#the number of nodules added now can bedisplayed in select ndule menu
#text

#close current window in remooving annotation window. do call delete all nodules once more in that function.
#But if a nodule is not selected why the annotation window is on display?

def convert_to_binary(given_str):
    """
    This function converts the given string to binary

    Returns
    -------
    None.

    """
    bin_str = ''.join(format(ord(i),'08b') for i in given_str)
    return bin_str

def write_to_binary_file(file_handle, given_str):
    file_handle.write(given_str)
    file_handle.flush()

#binary_filename = "all_data_binary"
#binary_filehandle = open(binary_filename, 'ab')

import pydicom
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import numpy as np
from pydicom.encaps import encapsulate, encapsulate_extended
from io import BytesIO
import pydicom.pixel_data_handlers.util as util
from PyQt5.QtWidgets import QComboBox
from pydicom.valuerep import VR
import time
from pathlib import Path, PurePath
import os
from threading import *
from copy import deepcopy
import pandas as pd
import os
import subprocess
#import magic  # Requires the python-magic library


class Global_thread_and_window_collector():
    """
    This class will hold the link to threads to be joined and the windows to be closed.
    There will be situtaions when immediatey after save, the user would resuest to go to some frame of interest. In that case, there may be multiple windows to hide in queue. just check this 
    slightly later. 
    Having two variables will lead to race condition where the producer has written to only one 
    variable, and the consumer reads both the variables.
    Therefore have a list where each element is a two tuple. This will inhenerently remove the 
    inconsistency because the reader will read only the tuples produced and the producer also will
    either produce a tuple or not produce a tuple.

    There is one global instance of this class. I can disable race 
    condition by having one update function that will call the pop 
    and push. 
    Multiple call to the same function by the same instance will 
    call the function one after the another. Hence, there will not be 
    any race condition.
    If different functions call the same function of the same instance,
    is it necessary that the call will be one after the another.
    No, it is not necessary because the instance is a shared variable,
    hence, the call may not be mutex.
    Therefore, I am creating a mutex variable.
    In the current situation it is also good that there is one consumer
    i.e. only one thread that can perform the pop function. Therefore,
    there cannot arise a situtation when is empty has been checked but
    the list is found empty after that. The current implementation
    does not handle the condition when multiple pop are run in 
    parallel.
    Anyways, we have only one producer and one consumer and the push
    and pop are mutually exclusive.     
    For the save annotation, the changes in the button may not work. 
    Therefore, currrently consider, multiple producer and ond one 
    consumer. Still, it will be fine, because the push operations among
    theselves are mutex and they do not require any other function 
    call of this class.
    This class is just a shared data structure. This class does not 
    have a thread.
    """
    def __init__(self):
        self.mutex=0
        self.reset()

    def reset(self):
        while(1==self.mutex):
            #This is busy wait
            continue
        self.mutex = 1
        self.thread_window_tuple_list = []
        self.mutex=0

    def isEmpty(self):
        """
        This function checks if the lists are empty.
        """
        while(1==self.mutex):
            #This is busy wait
            continue
        self.mutex = 1
        if(0==len(self.thread_window_tuple_list)):
            self.mutex=0
            return True
        else:
            self.mutex=0
            return False

    def pop(self):
        """
        isEmpty must be called before calling pop
        """
        assert not self.isEmpty(), "The list must not be empty when pop is called."    

        while(1==self.mutex):
            #This is busy wait
            continue
        self.mutex = 1
        top_tuple = self.thread_window_tuple_list[0] 

        threadToReturn = top_tuple[0]
        windowToReturn = top_tuple[1]
        self.thread_window_tuple_list = self.thread_window_tuple_list[1:]
        tupleToReturn = (threadToReturn, windowToReturn)
        self.mutex=0
        return tupleToReturn
         
    def push(self, threadToJoin, windowToHide):
        while(1==self.mutex):
            #This is busy wait
            continue
        self.mutex = 1
        tupleToPush = (threadToJoin, windowToHide)
        self.thread_window_tuple_list.append(tupleToPush)
        self.mutex=0
    

class Global_hide():
    """
    An instance of this class will have a thread which will keep on running till the end of the program. The thread will keep on monitoring whether any window has been created in some thread 
    and if yes then that thread needs to be joined, wait should be done and the window should be closed.
    Chk whether a thread shopuld be created inside this class or a thread should be created for an instance of this class.
    As it seems that, this class also has a function to stop the process of garbage collection of threads and performing window hide, threfore, thread should be created and joined inside this class.
    the run cannot wait indefinitely. Instead, any thread which depends on variable being up results in busy waiting which may degrade the performance of video playing.
    If for the first time after the video paused save is done, there might be slight delay in the  
 

    such facility of stoopping and stsarting garge collection, may incur delay in collecting the garbage which results in a hang like situation in most of the softwares.
    
    The two window instances of dicom annotater are running. 
    They sseem to be running in parallel. Hence, if one of the instance is playing video, the other instance may have windows to be closed.
    Hence, donot start the thread for this class from dicom annotator class, otherwise, two such threads will be created hence multiple pop operations for the global instance. 
At the current situation, two possibilities are there.
First one is to run this global thread initially and do not stop the thread in between. 
This may cause slight delay in video playing after every 3 or 4 frames.
The other option is to have an instance of  
Instead, what we can do is to    
    If one instance is running 
        start_regular_chk_windows
    Doing too muhch start and stop of this thread may cause some 
    unforeseen run issues. Also, now the play and pause causes one 
    thread to start and stop, for each dicom annotator, but if we 
    create one annotator per dicom annotator and start stop thread for this class with every play and pause, then some unforeseen race conditions may occur. Also, it is very unlikely that when playing video in one annotator, the other annotator has windows to be closed. Hence, slight checking after 0.2 seconds, where every  me update takes place after 0.06 seconds won't effect the video playing much.
Hence, just have only one global instance of Global_thread_and_window_collector and only one thread of this class that is startted initially and will end with the end of the program. Also, if this thread and play video thread are running on separate processors, then there is no issue of time lag in video.

    """
    def __init__(self):
        print("global hide initiated")
        self.set_checking_timeout(0.2)
        self.set_window_timeout(0.2)
        self.chk_close_thread = None
        self.stop_run=False
        
    def call_window_timer(self):
        time.sleep(self.window_timeout)
    
    def call_checking_timer(self):
        time.sleep(self.checking_timeout)
        
    def set_window_timeout(self, timeout):
        self.window_timeout = timeout
    
    def set_checking_timeout(self, timeout):
        self.checking_timeout = timeout
    
    def call_timer_and_hide(self, tupleToClose):
        self.call_window_timer()
        if(None != tupleToClose[0]):
            tupleToClose[0].join()
        print("window hide called.")
        tupleToClose[1].hide()
        
    def wait_hide_if_global_variable_set(self):
        #There will a global variable which will tell whether some window needs to be closed.
        #this variable will be none when no window needs to be closed. Otherwise, this variable will 
        #tell which window needs to be closed.
        #It may happen that window to close does not get closed and some other window gets opened up.
        #In that case, trying to open another window will get stuch till the current window gets blocked.
        #And this is the case of blocking call.
        if(not global_thread_and_window_collector.isEmpty()):
            tupleToClose = global_thread_and_window_collector.pop()
            assert None!=tupleToClose, "the tuple cannot be none"
            assert 2==len(tupleToClose), "tuple must be of 2 length"
            self.call_timer_and_hide(tupleToClose)
    
    def run_regular_chk_windows(self):
        while(not self.stop_run):
            self.call_checking_timer()
            self.wait_hide_if_global_variable_set()
        
    def start_regular_chk_windows(self):
        """
        The regular checking may be stopped when the video is playing by some function call. 
        This function creates a thread that does regular checking of 
        global_thread_and_window_collector instance.
        """
        print("in start_regular_chk_windows")
        if(None!=self.chk_close_thread):
            self.chk_close_thread.join()
        self.stop_run = False
        print("creating chk_close_thread")
        self.chk_close_thread = Thread(target=self.run_regular_chk_windows)
        print("created chk_close_thread")
        self.chk_close_thread.start()
        print("started chk_close_thread")
   
    def stop_chk_close_thread(self):
        print("stop of global hide has been called.")
        self.self.stop_run = True
        if(None!=self.chk_close_thread):
            self.chk_close_thread.join()

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Create a label for the dialog content
        label = QLabel("The marking over file and the annotations saved successfully.")

        # Set the dialog layout
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(label)

        # Set the dialog title
        self.setWindowTitle("Saved.")

class MyMessageWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, msg):
        super().__init__()
        # layout = QVBoxLayout()        
        #self.label = QLabel("The marking over image and the annotations saved successfully.")
        # self.label = QLabel(msg)
        self.label = QLabel()#"Please wait while video is being loaded.")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText(msg)

        self.setLayout(QVBoxLayout())
        
        self.layout().addWidget(self.label)
        # layout.addWidget(self.label)
        # self.setLayout(layout)
        self.setWindowTitle("Loading.")


class CheckableComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self._changed = False
        self.view().pressed.connect(self.handleItemPressed)
        
    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index) #, self.modelColumn()) #QStandardItem object
        if item.checkState() == QtCore.Qt.Checked:
            item.setCheckState(QtCore.Qt.Unchecked)
        else:
            item.setCheckState(QtCore.Qt.Checked)
        self._changed = True
        
    def hidePopup(self):        
        if not self._changed:
            super().hidePopup()
        self._changed = False
        
    def itemChecked(self, index):
        item = self.model().item(index, self.modelColumn())
        return item.checkState() == Qt.Checked
        
    def setItemChecked(self, index, checked = False):
        """
        

        Parameters
        ----------
        index : TYPE currently index of the item is used to check that item.
        Later, we should be able to use string to check a particular item.
            DESCRIPTION.
        checked : TYPE, optional
            DESCRIPTION. The default is False.

        Returns
        -------
        None.

        """
        item = self.model().item(index, self.modelColumn()) #QStandardItem object.
        #There may be ways to obtain this object by specifying the string. 
        
        if checked:
            item.setCheckState(QtCore.Qt.Checked)
        else:
            item.setCheckState(QtCore.Qt.Unchecked)


class UnscaledQLabel(QLabel):
    
    def __init__(self):
        super().__init__()
        self.written = False
    
    def paintEvent(self, event):        
        painter = QPainter(self)
        pixmap = self.pixmap()
        if pixmap:
            # Offset the image to center it within the label
            self.offset_x = (self.width() - pixmap.width()) // 2
            self.offset_y = (self.height() - pixmap.height()) // 2
            if( False == self.written ):
                self.written = True
                print("setting offset")
                print("pixmap = "+str(pixmap))
                print("pixmap.width() = "+str(pixmap.width()))
                print("pixmap.height() = "+str(pixmap.height()))            
                print("self.offset_x = "+str(self.offset_x))
                print("self.offset_y = "+str(self.offset_y))            
            painter.drawPixmap(self.offset_x, self.offset_y, pixmap)

class My_Info_Window(QtWidgets.QWidget):
    """
    This is the window when the save button will be clicked.
    This window will be shown for both the saving of annotations and saving of markings over the image.
    The text to be displayed will be taken from the user.
    Instead I can initially create 2 separate instances of this window and give the labels at that time.
    Later we just need to select, which window needs to be shown.
    In fact this window itself can be used for loading as well. 
    Therefore 3 instances of this window will be required.
    """
    def __init__(self, label_width, label_height, window_x, window_y, window_width, window_height, label_str):
        """
        Window x and y will be used to decide the label position. 
        the height and width may be used sometime.    
        """
        super().__init__()     
        #self.setAttribute(Qt.WA_DeleteOnClose)
        self.window_x = window_x
        self.window_y = window_y
        self.window_width = window_width
        self.window_height = window_height
        self.label_width = label_width
        self.label_height = label_height
        self.label_str = label_str
        self.window_size_computed = False
        self.add_items_to_widget()
        self.compute_sizes()    
        self.do_layout()

    def __del__(self):
        """
        This is called when the widget gets closed.
        """
        #The super does not have a delete method
        #super.__del__()
        print("deleting the info window ")

    def add_items_to_widget(self):
        self.qlabel = QtWidgets.QLabel()
        self.qlabel.setAlignment(Qt.AlignCenter)
        self.qlabel.setText(self.label_str)

    def compute_sizes(self):
        """
        This functions computes all sizes.

        Returns
        -------
        None.

        """
        if False == self.window_size_computed:
            self.y_pos_first_row = self.window_y #+ 0*self.info_height
            print("for info window \ny_pos_first_row = "+str(self.y_pos_first_row))
                
            self.qlabel.setGeometry(self.window_x, self.y_pos_first_row,\
                                                self.label_width, self.label_height)
            self.window_size_computed = True

    def do_layout(self):
        """
        This function adds the widgets to the toolbar.
        Returns
        -------
        None.

        """
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.qlabel, 1,0,1,1)

    #Set text is not required  explicitly now    
    def setText(self, text):
        self.qlabel.setText(text)

class Thread_My_Info_Window():
    def __init__(self, label_width, label_height, label_center_x, label_center_y, label_str):
        self.label_width = label_width
        self.label_height = label_height
        self.label_center_x = label_center_x
        self.label_center_y = label_center_y
        self.window_x = (int)(self.label_center_x - label_width/2)
        self.window_y = (int)(self.label_center_y - label_height/2)
        #They will be same as label width and height:  window_width, window_height
        self.label_str=label_str
        self.window = My_Info_Window(label_width, label_height, self.window_x, self.window_y\
            , label_width, label_height, label_str)    
        #self.window.setWindowFlags(Qt.FramelessWindowHint)  # Set the flag for a frameless window
        self.window.setWindowTitle(self.label_str)

        self.window.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.window.setGeometry(self.window_x, self.window_y, label_width, label_height)    
        self.thread = None
        self.timeout = 5
        

    def set_timeout(self, timeout):
        self.timeout = timeout

    def show_window_temporarily(self):
        self.join()
        self.thread = Thread(target=self.show_thread_function)
        print("calling thread start")
        self.thread.start()
        print("Thread start called")

    def show_thread_function(self):
        print("thread has been created. inside show function.")
        self.window.show()
        print("show called")
        time.sleep(self.timeout)
        print("timeout over")
        self.window.hide()
        print("hide called")
    
    def show(self):
        print("show window callled")
        self.window.show()
        #global_thread_and_window_collector.push(None, self)
    
    def show_not(self):
        print("show window callled")
        self.window.show()
        #global_thread_and_window_collector.push(None, self)
        
    def show_thread_permanent(self):
        self.join()
        self.thread = Thread(target=self.show)
        self.thread.start()
        print("started show window thread")
        #global_thread_and_window_collector.push(self.thread, self.window)      
        print("pushed the thread and window to garbage collector")

    def hide(self):
        print("hide called of Thread_My_Info_Window")
        self.join()
        print("calling actual window hide")
        self.window.hide()
        print("actual hide done")

    def join(self):
        if(self.thread!=None):
            print("joining my info thread.")
            self.thread.join()
            print("joined my info thread")
            self.thread=None

    def setText(self, text):
        self.window.setText(text)
    

class My_customlabel_Window(QtWidgets.QWidget):
    """
    This is the window when the save button will be clicked.
    This window will be shown for both the saving of annotations and saving of markings over the image.
    The text to be displayed will be taken from the user.
    Instead I can initially create 2 separate instances of this window and give the labels at that time.
    Later we just need to select, which window needs to be shown.
    In fact this window itself can be used for loading as well. 
    Therefore 3 instances of this window will be required.
    """
    def __init__(self, label_width, label_height, window_x, window_y, window_width, window_height, label_str):
        """
        Window x and y will be used to decide the label position. 
        the height and width may be used sometime.    
        """
        super().__init__()     
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.window_x = window_x
        self.window_y = window_y
        self.window_width = window_width
        self.window_height = window_height
        self.label_width = label_width
        self.label_height = label_height
        self.label_str = label_str
        self.window_size_computed = False
        self.add_items_to_widget()
        self.compute_sizes()    
        self.do_layout()

    def add_items_to_widget(self):
        self.qlabel = QtWidgets.QLabel()
        self.qlabel.setAlignment(Qt.AlignCenter)
        self.qlabel.setText(self.label_str)

    def compute_sizes(self):
        """
        This functions computes all sizes.

        Returns
        -------
        None.

        """
        if False == self.window_size_computed:
            self.y_pos_first_row = self.window_y #+ 0*self.info_height
            print("y_pos_first_row = "+str(self.y_pos_first_row))
                
            self.qlabel.setGeometry(self.window_x, self.y_pos_first_row,\
                                                self.label_width, self.label_height)

    def do_layout(self):
        """
        This function adds the widgets to the toolbar.
        Returns
        -------
        None.

        """
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.qlabel, 1,0,1,1)

    def addTextToLabel(self, textToAdd):
        currentText = self.qlabel.text()
        newText = currentText +(str)(textToAdd)
        self.qlabel.setText(newText)
    
    def removeTextToLabel(self):
        currentText = self.qlabel.text()
        if(len(currentText) > 0):
            newText = currentText[0:len(currentText)-1]
            self.qlabel.setText(newText)

    def clearText(self):
        self.qlabel.setText("")

    def getText(self):
        return self.qlabel.text()


class Thread_My_customlabel_Window():
    def __init__(self, label_width, label_height, label_center_x, label_center_y, label_str):
        self.label_width = label_width
        self.label_height = label_height
        self.label_center_x = label_center_x
        self.label_center_y = label_center_y
        self.window_x = (int)(self.label_center_x - label_width/2)
        self.window_y = (int)(self.label_center_y - label_height/2)
        #They will be same as label width and height:  window_width, window_height
        self.label_str=label_str
        self.window = My_Info_Window(label_width, label_height, self.window_x, self.window_y\
            , label_width, label_height, label_str)    
        self.window.setWindowFlags(Qt.FramelessWindowHint)  # Set the flag for a frameless window
        self.window.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.window.setGeometry(self.window_x, self.window_y, label_width, label_height)    
        self.thread = None

    def show(self):
        self.thread = Thread(target=self.show_thread_function)
        self.thread.start()

    def show_thread_permanent(self):
        self.window.show()
    
    def hide(self):
        self.thread.join()
        self.window.hide()

    def join(self):
        if(self.thread!=None):
            self.thread.join()
            self.thread=None

    def setText(self, text):
        self.window.setText(text)

    def addTextToLabel(self, textToAdd):
        self.window.addTextToLabel(textToAdd)
    
    def removeTextToLabel(self):
        self.window.removeTextToLabel()

class Annotation_window(QtWidgets.QWidget):
    """
    This  is the annotation widget for every nodule.
    """
    def __init__(self, annotation_label_width, dropdown_width, info_height, 
        window_x, window_y, window_width, window_height, csv_file_handle, image_type_name, nodule_index):
        """
       
        Parameters
        ----------
        class_ref : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        super().__init__()     
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.window_x = window_x
        self.window_y = window_y
        self.window_width = window_width
        self.window_height = window_height
        self.annotation_label_width = annotation_label_width
        self.dropdown_width = dropdown_width
        self.info_height = info_height
        self.csv_file_handle = csv_file_handle
        self.image_type_name = image_type_name
        self.nodule_index = nodule_index
        self.window_size_computed = False
        self.add_items_to_widget(annotation_label_width, dropdown_width, info_height)
        self.init_comboboxes()
        self.compute_sizes()    
        self.do_layout()
        self.add_save_window_initially()

    def __del__(self):
        """
        This is called when the widget gets closed.
        """
        #The super does not have a delete method
        #super.__del__()
        print("deleting the annotation window for nodule "+str(self.nodule_index))
        #print("checking if the label still exists")
        #print("self.textbox1="+str(self.textbox1.getText()))

    def add_items_to_widget(self, annotation_label_width, dropdown_width, info_height):
        self.qlabel_composition = QtWidgets.QLabel()
        self.qlabel_echogenicity = QtWidgets.QLabel()
        self.qlabel_shape = QtWidgets.QLabel()
        self.qlabel_margin = QtWidgets.QLabel()
        self.qlabel_echogenic_foci = QtWidgets.QLabel()
        self.qlabel_bethesda_category =  QtWidgets.QLabel()
                       
        self.qlabel_composition.setAlignment(Qt.AlignCenter)
        self.qlabel_echogenicity.setAlignment(Qt.AlignCenter)
        self.qlabel_shape.setAlignment(Qt.AlignCenter)
        self.qlabel_margin.setAlignment(Qt.AlignCenter)
        self.qlabel_echogenic_foci.setAlignment(Qt.AlignCenter)
        self.qlabel_bethesda_category.setAlignment(Qt.AlignCenter)
                        
        self.textbox1 = QLineEdit()        
        self.textbox2 = QLineEdit()        
        
        self.qlabel_composition.setText("Composition")
        self.qlabel_echogenicity.setText("Echogenicity")
        self.qlabel_shape.setText("Shape")
        self.qlabel_margin.setText("Margin")
        self.qlabel_echogenic_foci.setText("Echogenic Foci")
        self.qlabel_bethesda_category.setText("Bethesda Category")
        self.textbox1.setText("Free text 1("+self.image_type_name+")")      
        self.textbox2.setText("Free text 2("+self.image_type_name+")")
                
        print("self.qlabel_composition.geometry() = "+str(self.qlabel_composition.geometry()))
        
        self.combobox_composition = QComboBox()
        self.combobox_echogenicity = QComboBox()
        self.combobox_shape = QComboBox()
        self.combobox_margin = QComboBox()
        self.combobox_echogenic_foci = CheckableComboBox() #QComboBox()
        self.combobox_bethesda_category = QComboBox()

        self.total_points = 0
        self.tirad_score = 1
        self.qlabel_tirad = QtWidgets.QLabel()
        self.qlabel_tirad.setAlignment(Qt.AlignCenter)
        self.update_label_tirad_score()
        
        self.save_button = QtWidgets.QPushButton("Save")        
        self.save_button.clicked.connect(self.save_annotation)
    
    def update_label_tirad_score(self):
        text_to_set = "Total points = "+str(self.total_points)
        text_to_set = text_to_set + "      TiRad score = Tr"+str(self.tirad_score)        
        if(1  == self.tirad_score):
            text_to_set = text_to_set + "\nBenign : No FNA"
        elif(2 == self.tirad_score):
            text_to_set = text_to_set + "\nNot Suspicious : No FNA"
        elif(3 == self.tirad_score):
            text_to_set = text_to_set + "\nMildly Suspicious : FNA if >=2.5cm, Follow if >=1.5cm"
        elif(4 == self.tirad_score):
            text_to_set = text_to_set + "\nModerately Suspicious : FNA if >=1.5cm, Follow if >=1cm"
        elif(5 == self.tirad_score):
            text_to_set = text_to_set + "\nHighlySuspicious : FNA if >=1cm, Follow if >=0.5cm"                
        self.qlabel_tirad.setText(text_to_set) 
    
    def get_points(self,text):
        text_left_bracket_index = text.rfind("(")
        assert text_left_bracket_index >0 , "The left bracket must be present at non zero location"
        text_point_index = text_left_bracket_index + 1
        assert text_point_index < len(text), "point index must be less than length of the text."
        point = (int)(text[text_point_index])
        return point
    
    def compute_tirad_score(self):
        print("self.total_points = "+str(self.total_points))
        if(0==self.total_points):
            self.tirad_score = 1
        elif(1==self.total_points):
            self.tirad_score = 1
        elif(2==self.total_points):
            self.tirad_score = 2
        elif(3==self.total_points):
            self.tirad_score = 3
        elif(4<=self.total_points and 6>=self.total_points):
            self.tirad_score = 4
        elif(self.total_points>=7):
            self.tirad_score = 5            
        
    def get_total_points_echogenic_foci(self, all_echogenic_foci_checked_list):
        point = 0
        for item in all_echogenic_foci_checked_list:
            point = point + self.get_points(item)
        return point
    
    def compute_total_score(self):
        composition_text = str(self.combobox_composition.currentText())               
        composition_points = self.get_points(composition_text)
        print("composition_points = " + str(composition_points))
        
        echogenicity_text = str(self.combobox_echogenicity.currentText())
        echogenicity_points = self.get_points(echogenicity_text)
        print("echogenicity_points = " + str(echogenicity_points))
        
        shape_text = str(self.combobox_shape.currentText())
        shape_points = self.get_points(shape_text)
        print("shape_points = " + str(shape_points))
        
        margin_text = str(self.combobox_margin.currentText())
        margin_points = self.get_points(margin_text)
        print("margin_points = " + str(margin_points))
        
        #get points here
        all_echogenic_foci_checked_list = self.get_all_echogenic_foci_checked()
        all_echogenic_foci_points = self.get_total_points_echogenic_foci(all_echogenic_foci_checked_list)
        self.total_points = composition_points + echogenicity_points + shape_points + margin_points + all_echogenic_foci_points        
                
    def update_tirad_single_combobox(self,text):
        print(text)
        self.compute_total_score()
        self.compute_tirad_score()        
        self.update_label_tirad_score()
    
    def init_comboboxes(self):
        """
        This function initializes the comboboxes.
        """
        self.combobox_composition.addItem("Cystic or almost completely cystic (0 points)")   
        self.combobox_composition.addItem("Spongiform (0 points)")   
        self.combobox_composition.addItem("Mixed cystic and solid (1 point)")   
        self.combobox_composition.addItem("Solid or almost completely solid (2 points)")           
        self.combobox_composition.activated[str].connect(self.update_tirad_single_combobox)
        
        self.combobox_echogenicity.addItem("Anechoic (0 points)")
        self.combobox_echogenicity.addItem("Hyperechoic or isoechoic (1 point)")
        self.combobox_echogenicity.addItem("Hypoechoic (2 points)")
        self.combobox_echogenicity.addItem("Very hypoechoic (3 points)")
        self.combobox_echogenicity.activated[str].connect(self.update_tirad_single_combobox)
                
        self.combobox_shape.addItem("Wider-than-tall (0 points)")
        self.combobox_shape.addItem("Taller-than-wide (3 points)")
        self.combobox_shape.activated[str].connect(self.update_tirad_single_combobox)
        
        self.combobox_margin.addItem("Smooth (0 points)")
        self.combobox_margin.addItem("Ill-defined (0 points)")
        self.combobox_margin.addItem("Lobulated or irregular (2 points)")
        self.combobox_margin.addItem("Extra-thyroidal extension (3 points)")
        self.combobox_margin.activated[str].connect(self.update_tirad_single_combobox)
        
        self.combobox_echogenic_foci.addItem("None or large comet-tail artifacts (0 points)")
        self.combobox_echogenic_foci.addItem("Macrocalcifications (1 point)")
        self.combobox_echogenic_foci.addItem("Peripheral (rim) calcifications (2 points)")
        self.combobox_echogenic_foci.addItem("Punctate echogenic foci (3 points)")
        self.combobox_echogenic_foci.activated[str].connect(self.update_tirad_single_combobox)
        
        self.combobox_bethesda_category.addItem("I")
        self.combobox_bethesda_category.addItem("II")
        self.combobox_bethesda_category.addItem("III")
        self.combobox_bethesda_category.addItem("IV")
        self.combobox_bethesda_category.addItem("V")        
        self.combobox_bethesda_category.addItem("VI")
        
        self.unset_all_echogenic_foci()
    
    def compute_sizes(self):
        """
        This functions computes all sizes.

        Returns
        -------
        None.

        """
        # self.image_search_button_size = self.sagital_image_search_button.geometry().size()
        # self.image_search_button_width, self.image_search_button_height = self.image_search_button_size.width(), self.image_search_button_size.height()
        # print(f"image_search_button size: {self.image_search_button_width}x{self.image_search_button_height}")
        
        # self.save_button_size = self.save_button.geometry().size()
        # self.save_button_width, self.save_button_height = self.save_button_size.width(), self.save_button_size.height()
        # print(f"save_button size: {self.save_button_width}x{self.save_button_height}")
        
        #currently make 1/2 considering this as the image size.
        #Later on we will see whether to reduce to haf or scale by which factor.
        if False == self.window_size_computed:
            self.info_width = (int)((self.annotation_label_width \
                                     + self.dropdown_width)/2) 
            self.y_pos_first_row = self.window_y + 0*self.info_height
            self.y_pos_second_row = self.window_y + 1*self.info_height
            self.y_pos_third_row = self.window_y + 2*self.info_height
            self.y_pos_fourth_row = self.window_y + 3*self.info_height
            self.y_pos_fifth_row = self.window_y + 4*self.info_height
            self.y_pos_sixth_row = self.window_y + 5*self.info_height
            self.y_pos_seventh_row = self.window_y + 6*self.info_height
            self.y_pos_eighth_row = self.window_y + 7*self.info_height
            self.y_pos_nineth_row = self.window_y + 8*self.info_height
            self.y_pos_tenth_row = self.window_y + 9*self.info_height
            
            print("y_pos_first_row = "+str(self.y_pos_first_row))
            print("y_pos_second_row = "+str(self.y_pos_second_row))        
            print("y_pos_third_row = "+str(self.y_pos_third_row))
            print("y_pos_fourth_row = "+str(self.y_pos_fourth_row))
            print("y_pos_fifth_row = "+str(self.y_pos_fifth_row))
            print("y_pos_sixth_row = "+str(self.y_pos_sixth_row))
            print("y_pos_seventh_row = "+str(self.y_pos_seventh_row))
            print("y_pos_eighth_row = "+str(self.y_pos_eighth_row))
            print("y_pos_nineth_row = "+str(self.y_pos_nineth_row))                
            print("y_pos_tenth_row = "+str(self.y_pos_tenth_row))                
                
            self.qlabel_composition.setGeometry(self.window_x, self.y_pos_first_row,\
                                                self.annotation_label_width, self.info_height)
            self.qlabel_echogenicity.setGeometry(self.window_x, self.y_pos_second_row,\
                                                 self.annotation_label_width, self.info_height)
            self.qlabel_shape.setGeometry(self.window_x, self.y_pos_third_row,\
                                          self.annotation_label_width, self.info_height)
            self.qlabel_margin.setGeometry(self.window_x, self.y_pos_fourth_row,\
                                           self.annotation_label_width, self.info_height)        
            self.qlabel_echogenic_foci.setGeometry(self.window_x, self.y_pos_fifth_row,\
                                                   self.annotation_label_width, self.info_height)
            self.qlabel_bethesda_category.setGeometry(self.window_x, self.y_pos_sixth_row,\
                                                      self.annotation_label_width, self.info_height)
            
            self.combobox_composition.setGeometry(self.window_x + self.annotation_label_width,\
                                                  self.y_pos_first_row,\
                                                  self.dropdown_width, self.info_height)
            self.combobox_composition.setFixedSize(self.dropdown_width,self.info_height)
            self.combobox_echogenicity.setGeometry(self.window_x + self.annotation_label_width,\
                                                   self.y_pos_second_row,\
                                                   self.dropdown_width, self.info_height)
            self.combobox_echogenicity.setFixedSize(self.dropdown_width,self.info_height)
            self.combobox_shape.setGeometry(self.window_x + self.annotation_label_width,\
                                            self.y_pos_third_row,\
                                            self.dropdown_width, self.info_height)
            self.combobox_shape.setFixedSize(self.dropdown_width,self.info_height)
            self.combobox_margin.setGeometry(self.window_x + self.annotation_label_width,\
                                             self.y_pos_fourth_row,\
                                             self.dropdown_width, self.info_height)
            self.combobox_margin.setFixedSize(self.dropdown_width,self.info_height)
            self.combobox_echogenic_foci.setGeometry(self.window_x + self.annotation_label_width,\
                                                     self.y_pos_fifth_row,\
                                                     self.dropdown_width, self.info_height)
            self.combobox_echogenic_foci.setFixedSize(self.dropdown_width,self.info_height)
            self.combobox_bethesda_category.setGeometry(self.window_x + self.annotation_label_width,\
                                                        self.y_pos_sixth_row,\
                                                        self.dropdown_width, self.info_height)
            self.combobox_bethesda_category.setFixedSize(self.dropdown_width,self.info_height)        
            
            self.textbox1.setGeometry(self.window_x, self.y_pos_seventh_row,\
                                      2*self.info_width, self.info_height)
            self.textbox2.setGeometry(self.window_x, self.y_pos_eighth_row,\
                                      2*self.info_width, self.info_height)                   
            self.qlabel_tirad.setGeometry(self.window_x, self.y_pos_nineth_row,\
                                         2*self.info_width, self.info_height)
            self.qlabel_tirad.setFixedSize(2*self.info_width, self.info_height)
            
            self.save_button.setGeometry(self.window_x, self.y_pos_tenth_row,\
                                         2*self.info_width, self.info_height)
            self.save_button.setFixedSize(2*self.info_width, self.info_height)
            self.window_size_computed = True
            print("self.combobox_composition.geometry() = "+str(self.combobox_composition.geometry()))
    
    def do_layout(self):
        """
        This function adds the widgets to the toolbar.
        Returns
        -------
        None.

        """
        self.layout = QtWidgets.QGridLayout(self)
        
        #self.toolbar.addWidget()
        # self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.qlabel_composition, 1,0,1,1)
        self.layout.addWidget(self.qlabel_echogenicity, 2,0,1,1)
        self.layout.addWidget(self.qlabel_shape, 3,0,1,1)
        self.layout.addWidget(self.qlabel_margin, 4,0,1,1)
        self.layout.addWidget(self.qlabel_echogenic_foci, 5,0,1,1)
        self.layout.addWidget(self.qlabel_bethesda_category, 6,0,1,1)        
        
        self.layout.addWidget(self.combobox_composition, 1,1,1,1)
        self.layout.addWidget(self.combobox_echogenicity, 2,1,1,1)
        self.layout.addWidget(self.combobox_shape, 3,1,1,1)
        self.layout.addWidget(self.combobox_margin, 4,1,1,1)
        self.layout.addWidget(self.combobox_echogenic_foci, 5,1,1,1)
        self.layout.addWidget(self.combobox_bethesda_category, 6,1,1,1)
             
        self.layout.addWidget(self.textbox1, 7,0,1,2)
        self.layout.addWidget(self.textbox2, 8,0,1,2)    
                
        self.layout.addWidget(self.qlabel_tirad, 9, 0, 1,2)  # spans 2 cells
        self.layout.addWidget(self.save_button, 10, 0, 1,2)  # spans 2 cells
        
        print("self.combobox_composition.geometry() = "+str(self.combobox_composition.geometry()))
                    
    def clear_annotations(self):
        """
        This function clears the annotations. This fucntion is must when frame is updated.
        This function is also required in reinitialize.
    
        Returns
        -------
        None.
    
        """
        self.combobox_composition.setCurrentText("Cystic or almost completely cystic (0 points)")           
        self.combobox_echogenicity.setCurrentText("Anechoic (0 points)")        
        self.combobox_shape.setCurrentText("Wider-than-tall (0 points)")    
        self.combobox_margin.setCurrentText("Smooth (0 points)")
        self.unset_all_echogenic_foci()
        
        self.combobox_bethesda_category.setCurrentText("I")        
        self.textbox1.setText("Free text 1("+self.image_type_name+")")      
        self.textbox2.setText("Free text 2("+self.image_type_name+")")
        
        self.update_tirad_single_combobox("update on reset")
            
    def close_widget(self):
        self.close()  # Close the current widget

    def get_all_echogenic_foci_checked(self):
        list_index_checked = []
        for i in range(self.combobox_echogenic_foci.count()):
            if(self.combobox_echogenic_foci.itemChecked(i)):
                list_index_checked.append(i)
        list_name_checked = []
        for index in list_index_checked:
            if(index==0):
                list_name_checked.append("None or large comet-tail artifacts (0 points)")
            elif(index==1):
                list_name_checked.append("Macrocalcifications (1 point)")
            elif(index==2):
                list_name_checked.append("Peripheral (rim) calcifications (2 points)")
            elif(index==3):
                list_name_checked.append("Punctate echogenic foci (3 points)")
        return list_name_checked                            
    
    def unset_all_echogenic_foci(self):
        """
        This function unsets all echogenic foci

        Returns
        -------
        None.

        """
        self.combobox_echogenic_foci.setItemChecked(0,False) #"None or large comet-tail artifacts (0 points)")
        self.combobox_echogenic_foci.setItemChecked(1,False) #.addItem("Macrocalcifications (1 point)")
        self.combobox_echogenic_foci.setItemChecked(2,False) #.addItem("Peripheral (rim) calcifications (2 points)")
        self.combobox_echogenic_foci.setItemChecked(3,False) #.addItem("Punctate echogenic foci (3 points)")
        self.combobox_echogenic_foci.setCurrentText("None or large comet-tail artifacts (0 points)")
    
    def set_echogenic_foci_given_string(self, echogenic_foci_str):
        """
        This function sets the echogenic foci given a string that is an entry in echogenic foci.

        Parameters
        ----------
        echogenic_foci_str : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        if(echogenic_foci_str == "None or large comet-tail artifacts (0 points)"):
            self.combobox_echogenic_foci.setItemChecked(0,True)
        elif(echogenic_foci_str == "Macrocalcifications (1 point)"):
            self.combobox_echogenic_foci.setItemChecked(1,True)
        elif(echogenic_foci_str == "Peripheral (rim) calcifications (2 points)"):
            self.combobox_echogenic_foci.setItemChecked(2,True)
        elif(echogenic_foci_str == "Punctate echogenic foci (3 points)"):
            self.combobox_echogenic_foci.setItemChecked(3,True)
        else:
            assert False, "The string cannot have any other value."
    
    def set_all_echogenic_foci_checked_from_loaded(self, string_loaded_from_dicom):
        # semicolon(;) was used as a separator in csv, otherwise this comma 
        #would have interferred with the comma separator of different entities.
        #The separator of the string is
        #first print the string in list form . There may be [ and ] brackets.
        print("string_loaded_from_dicom = \n"+str(string_loaded_from_dicom))
        string_loaded_from_dicom = string_loaded_from_dicom.replace("[","").replace("]","").replace("'","").strip()
        print("string_after_stripping = \n"+str(string_loaded_from_dicom))
        if(string_loaded_from_dicom == ""):
            #An empty string was there
            return                 
        if('; ' in str(string_loaded_from_dicom)):            
            mylist = string_loaded_from_dicom.split("; ")
            print("mylist="+str(mylist))
            print("len(mylist)="+str(len(mylist)))
            for item in mylist:
                item_stripped=item.strip()
                print("item_stripped="+str(item_stripped))
                print("len(item_stripped)="+str(len(item_stripped)))                
                self.set_echogenic_foci_given_string(item_stripped)
        else:
            #There is aonly one annotation
            self.set_echogenic_foci_given_string(string_loaded_from_dicom)        
                
    # def set_all_echogenic_foci_checked_from_loaded(self, string_loaded_from_dicom):
    #     # semicolon(;) was used as a separator in csv, otherwise this comma 
    #     #would have interferred with the comma separator of different entities.
    #     #The separator of the string is
    #     #first print the string in list form . There may be [ and ] brackets.
    #     mylist = list(string_loaded_from_dicom)
    #     print(mylist)
    #     print(len(mylist))
    #     print("string_loaded_from_dicom = \n"+str(string_loaded_from_dicom))
    #     if(string_loaded_from_dicom == ""):
    #         #An empty string was there
    #         return         
    #     #if only one annotation was there then 
    #     if("," in string_loaded_from_dicom):            
    #         echogenic_arr = string_loaded_from_dicom.split(",")
    #         for mystr in echogenic_arr:
    #             self.set_echogenic_foci_given_string(mystr)
    #     else:
    #         #There is aonly one annotation
    #         self.set_echogenic_foci_given_string(string_loaded_from_dicom)
            
    def print_list(self, mylist):
        for item in mylist:
            print(item)

    def save_annotation(self):
        """
        The function will be used when the annotations will be saved by clicking the save button.
        csv_file_handle, image_type_name
        """
        composition_text = str(self.combobox_composition.currentText())               
        echogenecity_text = str(self.combobox_echogenicity.currentText())
        shape_text = str(self.combobox_shape.currentText())
        margin_text = str(self.combobox_margin.currentText())
        all_echogenic_foci_checked_list = self.get_all_echogenic_foci_checked()
        bethesda_text = str(self.combobox_bethesda_category.currentText())
        textbox1_text = self.textbox1.text()
        textbox2_text = self.textbox2.text()
        print("composition_text is "+composition_text)
        sys.stdout.flush()
        #now the frame number needs not be written in the csv file. In fact those frames will be saved in the 
        #a separate folder. Hence, no need to store those frame numbers in the csv file.
        #In fact, those frame numbers can be saved in the binary file that i write.
        #Hence, it does not matter whether it is the image file or the video file.
        #We just need to write the inpute filename, nodule index and annotation parameters and thats it.

        echogenic_foci_text = (str(all_echogenic_foci_checked_list)).replace(",",";")
        print("echogenic_foci_text = "+str(echogenic_foci_text))
        str_to_write = self.image_type_name+","+self.input_filename+","+str(self.nodule_index)+","+composition_text+\
                                       ","+echogenecity_text+","+shape_text+","+margin_text+","+\
                                       echogenic_foci_text+","+bethesda_text+","+textbox1_text+\
                                           ","+textbox2_text+"\n"
        self.csv_file_handle.write(str_to_write)        
        self.csv_file_handle.flush()
        self.show_saved_window()
        ##str_for_bin = "nodule_annotation\n"+str_to_write
        ##write_to_binary_file(binary_filehandle, convert_to_binary(str_for_bin))
        ##self.save_window.show() 
        ##time.sleep(3)# 0.8)
        ##self.save_window.hide() 
        #self.show_saved_window()
        ##self.save_window.setFocus()
        #self.save_window.activateWindow()
        #self.activateWindow()
        ##for i in range(1000000):
        ##    print(self.save_window.isVisible())
        ##time.sleep(10)# 0.8)
        #self.hide_saved_window()
        
    def add_save_window_initially(self):
        label_width = 100 
        label_height = self.info_height
        label_str = "Saved"
        self.display_save_window_thread = Thread_My_Info_Window(label_width, label_height, self.info_width+label_width,\
            self.y_pos_nineth_row + 2*label_height ,label_str)

    def show_saved_window_not(self):
        self.display_save_window_thread.show()
        #global_thread_and_window_collector.push(None, )
        
        #self.display_save_window_thread.show_thread_permanent()
 #self.showing_saved_window = True

    #def hide_saved_window(self):
    #    self.save_window.hide()
    #    self.showing_saved_window = False

    def show_saved_window(self):
        self.display_save_window_thread.show()
        time.sleep(0.35)
        self.display_save_window_thread.hide()

    def show_saved_window_old(self):
        # Create a QDialog instance
        dialog = QDialog(self)
        dialog.setWindowTitle("Saved")

        # Create a label with a message
        label = QLabel("The annotation saved successfully.")

        # Create a layout for the dialog
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(label)

        # Set the layout for the dialog
        dialog.setLayout(dialog_layout)

        # Show the dialog as a modal dialog (blocks the main window)
        dialog.show()

        time.sleep(2)
        dialog.close()
        #dialog.exec_()

    def load_annotation(self, df_row_loaded):
        """
        The function loads the annotation from the df row loaded.
        """       
        loaded_nodule_index = int(df_row_loaded[2])
        print("loaded_nodule_index = "+str(loaded_nodule_index)) 
        assert self.nodule_index == loaded_nodule_index, "the nodule index of current window and loaded row must match."
        self.combobox_composition.setCurrentText(df_row_loaded[3])      
        self.combobox_echogenicity.setCurrentText(df_row_loaded[4])
        self.combobox_shape.setCurrentText(df_row_loaded[5])
        self.combobox_margin.setCurrentText(df_row_loaded[6])
        self.unset_all_echogenic_foci()
        self.set_all_echogenic_foci_checked_from_loaded(df_row_loaded[7])
        self.combobox_bethesda_category.setCurrentText(df_row_loaded[8])       
        self.textbox1.setText(df_row_loaded[9])
        self.textbox2.setText(df_row_loaded[10])
        self.update_tirad_single_combobox("updating at the time of reloading")

    def set_input_filename(self, input_filename):
        """
        The function will be called whenever add nodule is done so that the nodule and file specific parameters are set.
        """
        self.input_filename = input_filename

    def reinitialize(self):
        """
        This function is used to reinitialize all the values in the annotation window. 
        The function also sets the input filename to null. The input filename needs to be changed 
        when the annotation of a new file is done.
        """
        self.input_filename = ""
        self.clear_annotations()

class Nodule():
    """
    This class is used to represent a nodule.
    This class will have a menu for that nodule and a colour for that nodule.
    """
    def __init__(self, nodule_index, color, toolbarRef, class_ref):
        """
        The nodule index is the index of nodule added.        

        Parameters
        ----------
        nodule_index : TYPE
        class_ref is the reference of the class over which the action needs to be displayed.
            DESCRIPTION.

        Returns
        -------
        None.

        """
        # self.toolbar=QToolBar("Nodule "+str(nodule_index))
        self.nodule_index = nodule_index
        self.color=color
        self.toolbarRef = toolbarRef
        self.class_ref = class_ref
        
    def add_annotation_window(self,x_toolbar, y_toolbar, annotation_label_width, dropdown_width, info_height, csv_file_handle,\
        image_type_name):        
        """
        The y_toolbar is the y location of the toolbar that has the action buttons for the nodules  "
        The x and y toolbar are practically the x and y positions of the toolbar that has the action buttons for the 
        nodules. The x and y of the annotation window will be decided based on these x and y values.
        """    
        #define widow x,y, width, height parametes here.
        #use the full annotation width and the combobox width
        #the x same as the window margin may be used.
        #using the x_toolbar as the x_position for the widget     
        window_x = x_toolbar
        #the y of the nodule toolbar should be obtained here.
        window_y = y_toolbar + 2* info_height
        #print("self.button.geometry() = "+str(self.button.geometry()))
        window_width = annotation_label_width+dropdown_width 
        #set the height based on the number of things required for the window.
        #9 rows are required in the window. Therefore setting 
        window_height = 9*info_height        
        print("window_x = "+str(window_x))
        print("window_y = "+str(window_y))
        print("window_width = "+str(window_width))
        print("window_height = "+str(window_height))
        self.annotation_window = Annotation_window(annotation_label_width, dropdown_width, info_height,\
                            window_x, window_y, window_width, window_height, csv_file_handle,\
                            image_type_name, self.nodule_index)
        self.annotation_window.setWindowFlags(Qt.FramelessWindowHint)  # Set the flag for a frameless window
        self.annotation_window.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.annotation_window.setGeometry(window_x, window_y, window_width, window_height)    

        self.showing_annotation_window = False
        #self.action.triggered.connect(self.button_clicked)
        #By default, show the window when it has been added.
        #No need to explicitly show the new window added here because the button clicked will be called due to nodule selection.
        #Hence, the window will be selected at that time.
        #self.show_annotation_window()

    def set_input_filename(self, input_filename):
        """
        The function will be called whenever add nodule is done so that the nodule and file specific parameters are set.
        """
        self.annotation_window.set_input_filename(input_filename)

    def reinitialize(self):
        """
        This function is used to reinitialize all the values in the annotation window. 
        The function also sets the input filename to null. The input filename needs to be changed 
        when the annotation of a new file is done.
        The function will also hide the annotation window.
        """
        self.annotation_window.reinitialize()
        self.hide_annotation_window()

    def close_annotation_window(self):
        """
        This function closes the toolbar. This is required when the current video is over and the toolbar needs to be closed.
        """
        self.annotation_window.close_widget()
    
    def show_annotation_window(self):
        """
        This function shows the toolbar when the action for that nodule takes place.
        """
        print("show window called for nodule "+str(self.nodule_index))
        self.annotation_window.show()
        self.showing_annotation_window = True

    def hide_annotation_window(self):
        """
        This function shows the toolbar when the action for that nodule takes place.
        """
        print("hide window called for nodule "+str(self.nodule_index))
        self.annotation_window.hide()
        self.showing_annotation_window = False

    def button_clicked(self):
        """
        This fucntion is called when the button is clicked for a particular nodule.
        This is required to display or hide a window.    
        """
        print("Inside action clicked")
        if(self.showing_annotation_window):
            self.hide_annotation_window()
            self.showing_annotation_window = False
        else:
            self.show_annotation_window()
            self.showing_annotation_window = True 
        global selected_nodule_index
        selected_nodule_index = self.nodule_index
    
    def load_annotation(self, df_row_loaded):
        self.annotation_window.load_annotation(df_row_loaded)
        
class DicomAnnotator(QtWidgets.QWidget):
#class DicomAnnotator(QtWidgets.QMainWindow):
    def __init__(self, window_x, window_y, window_width, window_height,\
                 image_name, csv_filename_video, csv_file_handle_video,\
                    csv_filename_video_marked_frames, csv_file_handle_video_marked_frames):
        super().__init__()
        self.window_x = window_x
        self.window_y = window_y
        self.window_width = window_width
        self.window_height = window_height
        #image_name will be one of axial or sagital
        self.image_name = image_name
        self.csv_filename_video = csv_filename_video
        self.csv_file_handle_video = csv_file_handle_video
        self.csv_filename_video_marked_frames = csv_filename_video_marked_frames
        self.csv_file_handle_video_marked_frames = csv_file_handle_video_marked_frames
        self.title="Graph Dicom Annotator"
        self.setWindowTitle(self.title)
        #setting the num nodule to a max number 5 and initializing other nodule var.
        self.init_nodule_var()
        #initialize color dict    
        self.init_color_dict()        
        #initialize user interface
        self.initUI()
        self.init_action_dict()
        self.add_action_to_toolbar_initially()
        self.add_action_to_menubar_initially()
        self.add_nodule_instances_initially()
        self.add_info_windows_initially()
        self.add_customlabel_window_initially()

    def init_nodule_var(self):
        """
        This fiunction initializes the variables required for nodules.

        Returns
        -------
        None.

        """
        self.max_num_nodules=5
        self.numNodules = 0
        self.current_marking_nodule_index = -1
    
    def init_color_dict(self):
        """
        This function initializes the color dict
        Initially, keeping 5 entries in the color dict
        """
        self.color_dict = {}
        self.color_dict[0] = "Red"
        self.color_dict[1] = "Green"
        self.color_dict[2] = "Blue"
        self.color_dict[3] = "Yellow"
        self.color_dict[4] = "Cyan"
    
    def init_action_dict(self):
        """
        This function initializes the dictionary containig actions. This will be used when add nodule is clicked and the actions 
        need to be aded to the toolbar.
        """
        self.action = {}
        self.action_menu = {}
        for i in range(self.max_num_nodules):
            self.action[i] = QtWidgets.QWidgetAction(self.toolBar)
            self.action_menu[i] = QtWidgets.QWidgetAction(self.select_nodule_menu)
            l=QtWidgets.QPushButton("Nodule "+str(i))
            l_menu=QtWidgets.QPushButton("Nodule "+str(i))
            str_for_stylesheet = "background-color : "+self.color_dict[i]+";" # padding: 0 0 0 0px;}"
            str_for_stylesheet_menu = "background-color : "+self.color_dict[i]+";" # padding: 0 0 0 0px;}"
            l.setStyleSheet(str_for_stylesheet)
            l_menu.setStyleSheet(str_for_stylesheet_menu)
            if(0==i):
                l.clicked.connect(self.action_0_triggered)
                l_menu.clicked.connect(self.action_menu_0_triggered)
            elif(1==i):
                l.clicked.connect(self.action_1_triggered)
                l_menu.clicked.connect(self.action_menu_1_triggered)
            elif(2==i):
                l.clicked.connect(self.action_2_triggered)
                l_menu.clicked.connect(self.action_menu_2_triggered)
            elif(3==i):
                l.clicked.connect(self.action_3_triggered)
                l_menu.clicked.connect(self.action_menu_3_triggered)
            elif(4==i):
                l.clicked.connect(self.action_4_triggered)
                l_menu.clicked.connect(self.action_menu_4_triggered)
            else:
                assert False,"This condition cannot occur"
            self.action[i].setDefaultWidget(l)
            self.action_menu[i].setDefaultWidget(l_menu)
    
    def init_action_dict_old(self):
        """
        This function initializes the dictionary containig actions. This will be used when add nodule is clicked and the actions 
        need to be aded to the toolbar.
        """
        self.action = {}
        for i in range(self.max_num_nodules):
            self.action[i] = QtWidgets.QWidgetAction(self.toolBar)
            l=QtWidgets.QLabel("Nodule "+str(i))
            str_for_stylesheet = "QLabel { background-color : "+self.color_dict[i]+"; padding: 4 4 4 4px;}"
            l.setStyleSheet(str_for_stylesheet)
            self.action[i].setDefaultWidget(l)
    
    def add_action_to_toolbar_initially(self):
        """
        This function will add all the actions to the toolbar initially and make these actions as not visible.
        The action will be made visible whenever the corresponding nodule gets added and the action will be made invisible
        whenever the nodule gets removed. 
        """
        for i in range(self.max_num_nodules):
            self.toolBar.addAction(self.action[i])
            self.action[i].setVisible(False)

    def add_action_to_menubar_initially(self):
        """
        This function will add all the actions to the toolbar initially and make these actions as not visible.
        The action will be made visible whenever the corresponding nodule gets added and the action will be made invisible
        whenever the nodule gets removed. 
        """
        for i in range(self.max_num_nodules):
            self.select_nodule_menu.addAction(self.action_menu[i])
            self.action_menu[i].setVisible(True)

    def hide_all_annotation_window(self):
        """
        This function is used to hide all the annotation windows.
        """
        for i in range(self.numNodules):
            self.nodule_dict[i].hide_annotation_window()

    def hide_annotation_window_other_than_clicked(self, nodule_index):
        """
        This function is used to hide the annotation windows other than those whcih are clicked.
        """
        for i in range(self.numNodules):
            if (i!=nodule_index):
                self.nodule_dict[i].hide_annotation_window()

    def perform_nodule_selected(self, nodule_index):
        """
        This function is called to perform some basic functions when a nodule is selected either by seleting 
        that nodule or by adding that nodule for the first time.
        #Todo urgent: This function must also do following:
        1: clear the image markings
        2: if the frame displayed is marked for that nodule the marked frame for that nodule should be loaded.    
        """
        self.current_marking_nodule_index = nodule_index
        self.nodule_dict[self.current_marking_nodule_index].set_input_filename(self.filename)        
        self.nodule_dict[self.current_marking_nodule_index].button_clicked()
        self.hide_annotation_window_other_than_clicked(self.current_marking_nodule_index)
        self.add_nodule_button.setText("Add Nodule (Selected Nodule = "+str(self.current_marking_nodule_index)+" )")
        self.create_directory_for_nodule()    
        
        #This function is itself sufficient for clearing the image markings.  
        #Yes, the following update itself clears any unwanted image markings.
        self.update_for_frame()

    def show_only_given_action(self, index):
        for i in range(self.max_num_nodules):
            if i == index:
                self.action[i].setVisible(True)
            else:
                self.action[i].setVisible(False)
                self.nodule_dict[i].hide_annotation_window()

    #TODO: 88888888how will show hide done for add nodule in partially annotated video. chk later.

    def action_0_triggered(self):
        """
        This function will be filred when action0 gets triggered
        """
        print("in action 0 triggered")
        if(self.video_opened or self.image_opened):
            if(self.is_video_playing()):
                return                 
            self.perform_nodule_selected(0)

    def action_menu_0_triggered(self):
        """
        This function will be filred when action0 gets triggered
        """
        print("in action menu 0 triggered")    
        if(self.video_opened or self.image_opened):
            if(self.is_video_playing()):
                return         
            self.perform_nodule_selected(0)
            #in additon to the above, the action button needs to be displayed and other action buttons needs to be hidden.
            self.show_only_given_action(0)
    
    def action_1_triggered(self):
        """
        This function will be filred when action0 gets triggered
        """
        print("in action 1 triggered")
        if(self.video_opened or self.image_opened):
            if(self.is_video_playing()):
                return                 
            self.perform_nodule_selected(1)

    def action_menu_1_triggered(self):
        """
        This function will be filred when action0 gets triggered
        """
        print("in action menu 1 triggered")        
        if(self.video_opened or self.image_opened):
            if(self.is_video_playing()):
                return                 
            self.perform_nodule_selected(1)
            #in additon to the above, the action button needs to be displayed and other action buttons needs to be hidden.
            self.show_only_given_action(1)

    def action_2_triggered(self):
        """
        This function will be filred when action0 gets triggered
        """
        print("in action 2 triggered")
        if(self.video_opened or self.image_opened):
            if(self.is_video_playing()):
                return                 
            self.perform_nodule_selected(2)

    def action_menu_2_triggered(self):
        """
        This function will be filred when action0 gets triggered
        """
        print("in action menu 2 triggered")        
        if(self.video_opened or self.image_opened):
            if(self.is_video_playing()):
                return                 
            self.perform_nodule_selected(2)
            #in additon to the above, the action button needs to be displayed and other action buttons needs to be hidden.
            self.show_only_given_action(2)

    def action_3_triggered(self):
        """
        This function will be filred when action0 gets triggered
        """
        print("in action 3 triggered")
        if(self.video_opened or self.image_opened):
            if(self.is_video_playing()):
                return                 
            self.perform_nodule_selected(3)

    def action_menu_3_triggered(self):
        """
        This function will be filred when action0 gets triggered
        """
        print("in action menu 3 triggered")        
        if(self.video_opened or self.image_opened):
            if(self.is_video_playing()):
                return                 
            self.perform_nodule_selected(3)
            #in additon to the above, the action button needs to be displayed and other action buttons needs to be hidden.
            self.show_only_given_action(3)

    def action_4_triggered(self):
        """
        This function will be filred when action0 gets triggered
        """
        print("in action 4 triggered")
        if(self.video_opened or self.image_opened):
            if(self.is_video_playing()):
                return                 
            self.perform_nodule_selected(4)

    def action_menu_4_triggered(self):
        """
        This function will be filred when action0 gets triggered
        """
        print("in action menu 4 triggered")        
        if(self.video_opened or self.image_opened):
            if(self.is_video_playing()):
                return                 
            self.perform_nodule_selected(4)
            #in additon to the above, the action button needs to be displayed and other action buttons needs to be hidden.
            self.show_only_given_action(4)

    def init_dicom_frames_path(self):
        """
        This variable initializes the dicom frames path for different nodules.
        add the color name in the folder name, this will make it easier for the decoding.
        """
        self.dicom_frames_path = {}
        for i in range(self.max_num_nodules):
            foldername_extension = "_frames_nodule_"+str(i)+"_color_"+self.color_dict[i]
            self.dicom_frames_path[i] = Path(PurePath(self.dicom_obj_dirname).joinpath(self.dicom_obj_only_filename_without_extension +\
                                                                                            foldername_extension))
            print("self.dicom_frames_path[i] = "+str(self.dicom_frames_path[i]))

    def hide_prev_annotation_window(self):
        """
        The fucntion is used to add actions to the menu bar when the add nodule button is clicked.

        Returns
        -------
        None.

        """
        #Hiding the windows for all prev nodules added.
        for prev_nodule_index in range(self.current_marking_nodule_index):
            self.nodule_dict[prev_nodule_index].hide_annotation_window() 
        #By default, when the widow gets added, it will be shown by default.
        #self.toolBar.addAction(self.nodule_dict[self.current_marking_nodule_index].action)
        #add annotation window done at the time of nodule creation
        #Adding the action buttin to toolbar when the triggering has been set.
        #Todo: may need to set the window visible after adding the action to toolbar.
        #I have used toolbar instead of menu bar just because, it is possible to directly add the actions in tool bar, whereas in case of 
        #menu, it will require to first add menus like file etc and then add actions inside them.
        #self.toolBar.addAction(self.nodule_dict[self.current_marking_nodule_index].action)
    
    def create_directory_for_nodule(self):
        """
        This function will 
        #1: update the color to be ploted
        #2: create the folder in which the marked images will be placed.
        #3: update this folder name to the class variable which will be used by the save function.
        """
        #The color to be plotted is selected by self.color_dict[self.current_marking_nodule_index].
        #Hence, this part requires change in show image, plot lines and save image function
        #create the folder to save that nodule
        #I think folder creation should be done in save_image.Chk when this was done earlier. 
        #Earlier the code to chk dir was  in save_frame. we should not waste time in save frame, hence creating the directory here.
        #It it happens that the directory gets deleted accidentally, then earlier annotations would alsohave gone. Therefore, binary file
        #to save the annotations is required.
        if(self.loading_partially_annotated_video):
            #When add nodule is called while the video is being loaded,then the directories for any nodules that were added earlier
            #should already exist.
            print("self.current_marking_nodule_index = "+str(self.current_marking_nodule_index))
            print("self.dicom_frames_path[self.current_marking_nodule_index] = "+str(self.dicom_frames_path[self.current_marking_nodule_index]))
            assert self.dicom_frames_path[self.current_marking_nodule_index].is_dir(), "The directory should exist already."
        else: #if(not self.loading_partially_annotated_video):
            #assert not self.dicom_frames_path[self.current_marking_nodule_index].is_dir(), "The directory should not exist already."
            #Now, if the directory does not exist already, then a new one will be created but no 
            if(not self.dicom_frames_path[self.current_marking_nodule_index].is_dir()):
                self.dicom_frames_path[self.current_marking_nodule_index].mkdir()
        #The folder name to be used for saving the frames will be automatically selected correctly using the variable 
        #self.dicom_frames_path[self.current_marking_nodule_index]

    def add_nodule_clicked(self):
        """
        This function is used when add nodule is clicked.

        Returns
        -------
        None.

        """
        #Have a dictionary for the nodule/menu.
        #Whenever a new nodule is to be added, add an entry to the dictionary.
        #The key is index for that nodule.
        #The value should be  all attributes for that nodule.
        #Basically, we require the annotations for a nodule and color for that nodule.
        #At first I can give colours from my own for a nodule, Later, I can give color chooser for each nodule.
        #create a class nodule. It will make things a lot more easier.
        #This class will have required menu and the asssociated color.
        #This is exactly same as we are creating a menu. Instead of using menu reference, we will be using obj.menu reference. 
        #The idea of having a menu is suitable only when we have a menu bar and we can easily add menus to that menubar.
        #But the thing is that whenever someone will later change that menu for say nodule1, the changes should be saved to 
        #the disk.
        #Therefore, the user must press the save button inside that menu to resave the annotations for that menu.
        #Also, it is  easy to show and hide items for a menu.
        #when saving the annotations, they must be saved to the csv file as well to a separate binary file. Since,
        #the annotations are not per frame now, hence we donot need to save the annotations to every dicom frame we are saving. 
        #At the same time, I can save the points, for which the polylines are being constructed, to a separate binary file for each such frame.
        #Or, we can a have a binary file per video which has all the data, such as nodules, the markings done, the clear 
        #done and so on, for all the frames of that video.
        #upload all the dicom code at 4:00 pm.
        if(self.video_opened or self.image_opened or self.loading_partially_annotated_video):
            if(self.is_video_playing()):
                return 
            #There may be multiple nodules within an image as well. Therefore, now the marking of the individual images will also be nodule wise. The add nodule will perform something only if either image or video is opened. The add nodule will also work when loading partially annotated video.
            #all the nodule instances are added initially now.
            assert len(self.nodule_dict) >= self.numNodules, "The len of nodule dict cannot be less than num nodule"
            if (self.numNodules<self.max_num_nodules):
                self.numNodules = self.numNodules+1
                self.current_marking_nodule_index = self.numNodules - 1
                #Todo: complete the following
                #seems completed
                #By default, when the action gets added to the toolbar, the annotation window will be shown by default.
                #whenever adding another action, remember to close any previous windows, if they are opened.
                #This will help, because the user mightnot close the previous windows. this is done.
                self.hide_prev_annotation_window()
                #Making the action as visible
                self.action[self.current_marking_nodule_index].setVisible(True)                
                #Todo: complete the following:
                #I need to implement this function. This function will 
                #1: update the color to be ploted
                #2: create the folder in which the marked images will be placed.
                #3: update this folder name to the class variable which will be used by the save function.
                #done
                #The earlier markings, if any over the current image, should be cleared. 
                #Else, when moving back and forth, the frames will be loaded only wrt the current nodule.
                #Todo: have separate framed_marked_array for each nodule.
                self.perform_nodule_selected(self.current_marking_nodule_index)
                assert len(self.nodule_dict) >= self.numNodules, "The len of nodule dict cannot be less than num nodule"
            else:
                #All the annotation windows will be hidden if the add nodule is called more.
                self.hide_all_annotation_window()
                print("only 5 nodules at max are allowed.")
                #Todo: show error message here
    
    def delete_all_nodules(self):
        """
        This function will delete all the nodules present.
        """
        for i in range(self.numNodules):
            #The nodule needs to be closed.
            self.nodule_dict[i].reinitialize()
            #The action needs to removed from the toolbar.
            self.action[i].setVisible(False)
        self.numNodules = 0
        self.current_marking_nodule_index = -1
        self.add_nodule_button.setText("Add Nodule")
    
    def delete_selected_nodule(self):
        if(self.current_marking_nodule_index!=-1):
            self.nodule_dict[self.current_marking_nodule_index].reinitialize()
            self.action[self.current_marking_nodule_index].setVisible(False)
            self.current_marking_nodule_index = -1
            #self.numNodules = 0
    
    def add_loading_window_initially(self):
        #once info window variables are set, they need not be cleared till the program exits.
        label_width = 700 
        label_height = self.info_height
        label_str = "Please wait while the video is being loaded."
        self.display_loading_window = Thread_My_Info_Window(label_width, label_height, self.image_center_x,\
            self.image_center_y, label_str)

    def add_save_window_initially(self):
        label_width = 100 
        label_height = self.info_height
        label_str = "Saved"
        self.display_save_window = Thread_My_Info_Window(label_width, label_height, self.image_center_x,\
            self.image_center_y, label_str)    

    def add_frame_advanced_window_initially(self):
        label_width = self.width_for_image  
        label_height = self.info_height
        label_str = "Moved"
        self.display_frame_advanced_window = Thread_My_Info_Window(label_width, label_height, self.image_center_x,\
            self.image_center_y, label_str)    
        self.display_frame_advanced_window.set_timeout(0.5)

    def add_customlabel_window_initially(self):
        label_width = 100 
        label_height = self.info_height
        self.textbox_window_x = (int)(self.image_center_x - label_width/2)
        self.textbox_window_y = (int)(self.image_center_y - label_height/2)
        label_str = ""
        self.textbox_window = My_customlabel_Window(label_width, label_height, self.textbox_window_x, self.textbox_window_y\
            , label_width, label_height, label_str)    
        self.textbox_window.setWindowFlags(Qt.FramelessWindowHint)  # Set the flag for a frameless window
        self.textbox_window.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.textbox_window.setGeometry(self.textbox_window_x, self.textbox_window_y, label_width, label_height)    
        self.textbox_window.hide()
    
    def add_info_windows_initially(self):
        """
        This function will initialize the info windows.
        """
        self.add_loading_window_initially()
        self.add_save_window_initially()
        self.add_frame_advanced_window_initially()

    def add_nodule_instances_initially(self):
        """
        The function will add thee nodule instances initially.
        """
        self.nodule_dict={}
        for i in range(self.max_num_nodules):
            self.nodule_dict[i] = Nodule(i, self.color_dict[i], self.toolBar, self)
            self.nodule_dict[i].add_annotation_window(self.window_x, self.y_pos_fourteenth_row,\
                self.annotation_label_width, self.dropdown_width, self.info_height, self.csv_file_handle_video, self.image_name)

    
    def initUI(self):
        self.window_size_computed = False
        # self.image_search_button = QtWidgets.QPushButton("Search")
        #Put the heading of the window iside this label
        self.qlabel_heading = QtWidgets.QLabel()
        self.qlabel_heading.setAlignment(Qt.AlignCenter)
        self.qlabel_sub_heading = QtWidgets.QLabel()
        self.qlabel_sub_heading.setAlignment(Qt.AlignCenter)
        
        self.play_forward_button = QtWidgets.QPushButton("Play Video Forward")
        self.play_backward_button = QtWidgets.QPushButton("Play Video Backward")        
        self.next_frame_button = QtWidgets.QPushButton("Show Next frame in Video")
        self.prev_frame_button = QtWidgets.QPushButton("Show prev frame in Video")
        self.add_nodule_button = QtWidgets.QPushButton("Add Nodule")
      
        self.menuBar = QMenuBar(self) #QtGui.QMenuBar(self)
        self.select_nodule_menu = self.menuBar.addMenu("&Select Nodule")
        
        #use this button to close the window
        self.close_window_button = QtWidgets.QPushButton("Close Current Window")
        self.clear_marking_button = QtWidgets.QPushButton("Clear markings over Current Image")                
        
        self.close_image_button = QtWidgets.QPushButton("Close Current Video")                
        
        self.dicom_open_button = QtWidgets.QPushButton("Open MP4/RGB DICOM Video")
        self.image_label = UnscaledQLabel() # QtWidgets.QLabel()
        self.toolBar = QToolBar(self)
        
        # setHeight(28)
        self.qlabel_heading.setText(" ULTRASOUND GRAPH ANNOTATOR (UGA, v1.0) ")
        font = QFont()
        font.setBold(True)  # Set the font to bold
        self.qlabel_heading.setFont(font)    # Apply the font to the label
        self.qlabel_sub_heading.setText(" Annotate "+self.image_name+" Video")
        
        self.window_timeout = 0.35
        self.qlabel_saved = QtWidgets.QLabel()
        self.qlabel_saved.setAlignment(Qt.AlignCenter)
        self.qlabel_saved.setText("saved")
        self.qlabel_saved.setVisible(False)
        
        self.qlabel_advanced = QtWidgets.QLabel()
        self.qlabel_advanced.setAlignment(Qt.AlignCenter)
        self.qlabel_advanced.setText("Advanced")
        self.qlabel_advanced.setVisible(False)
        
        self.dock_slider = QDockWidget("Slider", self)
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setVisible(False)
        self.slider.hide()
        self.dock_slider.setWidget(self.slider)    
        self.dock_slider.hide()            
        
        self.save_button = QtWidgets.QPushButton("Save")
        
        self.browser_mode = 1
        self.filter_name = 'All Files (*)'
        self.dirpath = QDir.currentPath()
        
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        self.compute_sizes()
        
        # Add widgets to the layout with specified positions and sizes
        #self.layout.addWidget(self.image_search_button, 0, 0, 2, 1)  # 2 rows, 1 column
        self.layout.addWidget(self.qlabel_heading, 0, 0, 1, 1)
        self.layout.addWidget(self.qlabel_sub_heading, 1, 0, 1, 1)
        #Todo: removing the image search button. Check if it works correctly.
        # self.layout.addWidget(self.image_search_button, 2, 0, 1, 1)  #1 row, 1 column
        self.layout.addWidget(self.dicom_open_button, 2, 0, 1, 1)  #1 row, 2 column
        
        self.layout.addWidget(self.play_forward_button, 3, 0, 1, 1)
        self.layout.addWidget(self.play_backward_button, 4, 0, 1, 1)
        # self.layout.addWidget(self.pause_button, 5, 0, 1, 1)
        self.layout.addWidget(self.next_frame_button, 5, 0, 1, 1)
        self.layout.addWidget(self.prev_frame_button, 6, 0, 1, 1)                
        #//have addNodule button
        #have a nodule toolbar
        #n1, n2 ...
        #self.layout.addWidget(self.add_nodule_button, 7, 0, 1, 1)
        self.layout.addWidget(self.menuBar, 7, 0, 1, 1)

        self.layout.addWidget(self.toolBar, 8, 0, 1, 1)
        #Todo: Also need to do set fixed size for menu bar since, the menu items will be added dynamically.
        
        #TODO: I need to have a toolbar here for nodules.
        #At first add all menus for n1 to n5 and and n1 to n10. Just for testing that does it display properly and does the menu for each nodule displays properly.
        
        
        #TODO: As asked by Dinesh sir, Later also try that the play , next/prev frame button should only be there only when  video is opened.
        #TODO: I am converting the paly button  to pause button. Hence there no  need for a separate pause button. Later remove this as well, when doing the above modification.
        
        self.layout.addWidget(self.clear_marking_button, 9,  0, 1, 1)
        self.layout.addWidget(self.close_image_button,10, 0, 1,1)
        self.layout.addWidget(self.save_button, 11, 0, 1,1)  # spans only 1 cell        
        self.layout.addWidget(self.close_window_button, 12, 0, 1,1)        
        # slef.layout.addWidget(self.)
        self.layout.addWidget(self.image_label, 0, 1, 13, 1)
        
        
        #Todo: how to display complete string when drop down is called?
        #May be i need to subclass and and make custom combobox
        
        self.dicom_open_button.clicked.connect(self.getVideo)
        self.play_forward_button.clicked.connect(self.play_video)
        self.next_frame_button.clicked.connect(self.next_frame)        
        self.prev_frame_button.clicked.connect(self.prev_frame)
        self.play_backward_button.clicked.connect(self.play_video_backward)
        self.save_button.clicked.connect(self.save_image)
        self.add_nodule_button.clicked.connect(self.add_nodule_clicked) 
        
        self.clear_marking_button.clicked.connect(self.clear_image_markings)
        self.close_image_button.clicked.connect(self.reinitialize)
        self.close_window_button.clicked.connect(self.close_widget)
        self.current_line = []
        
        self.setMouseTracking(True)
        self.installEventFilter(self)
                
        self.image_opened = False
        self.video_opened = False
        self.window_size_computed = False
        #self.compute_sizes()
        self.play_forward_thread = None
        self.show_saved_thread = None
        
        self.video_loading_message_window = MyMessageWindow("Please wait while the video is being loaded.")
        # self.video_loading_message_window.setWindowFlags(Qt.FramelessWindowHint)

        self.video_loading_message_window.setGeometry(self.window_x + self.image_label_x_start + 100, \
                                                        self.window_y + self.image_label_y_start+ 100, 10, 10) 
        self.create_loading_dialog()
             
        self.reinitialize()
                
    def close_widget(self):
        self.reinitialize()
        self.close()  # Close the current widget
        
    def get_image(self):
        if("rgb" in self.dicom_obj.PhotometricInterpretation.lower()):
            image = self.dicom_obj.pixel_array
        elif("ybr" in self.dicom_obj.PhotometricInterpretation.lower()):
            image = util.convert_color_space(self.dicom_obj.pixel_array,'YBR_FULL','RGB')        
        elif("monochrome" in self.dicom_obj.PhotometricInterpretation.lower()):
            image = cv2.cvtColor(self.dicom_obj.pixel_array,cv2.COLOR_GRAY2RGB)
        elif("gray" in self.dicom_obj.PhotometricInterpretation.lower()):
            image = cv2.cvtColor(self.dicom_obj.pixel_array,cv2.COLOR_GRAY2RGB)
        else:
            print("unknown file type")
            sys.exit(0)
        return image

    def get_frame_at_frameIndex(self):
        if("rgb" in self.dicom_obj.PhotometricInterpretation.lower()):
            image = self.dicom_obj.pixel_array[self.frameIndex].copy()
        elif("ybr" in self.dicom_obj.PhotometricInterpretation.lower()):
            image = util.convert_color_space(self.dicom_obj.pixel_array[self.frameIndex],\
                                             'YBR_FULL','RGB')        
        elif("monochrome" in self.dicom_obj.PhotometricInterpretation.lower()):
            image = cv2.cvtColor(self.dicom_obj.pixel_array[self.frameIndex],cv2.COLOR_GRAY2RGB)
        elif("gray" in self.dicom_obj.PhotometricInterpretation.lower()):
            image = cv2.cvtColor(self.dicom_obj.pixel_array[self.frameIndex],cv2.COLOR_GRAY2RGB)
        else:
            print("unknown file type")
            sys.exit(0)
        print("image_for_frame_obtained")
        print("type of image in video original loading")
        print("type(image)="+str(type(image)))
        print(" self.dicom_obj.PhotometricInterpretation.lower() = "+str(self.dicom_obj.PhotometricInterpretation.lower()))
        return image
        
    
    def whether_rescaling_required(self,  image):
        """
        currently scale down to max a factor of 2 only.
        """
        image_shape = image.shape
        image_height = image_shape[0]
        image_width = image_shape[1]
        if((image_width < self.width_for_image+150)\
             and (image_height < self.height_for_image+150)):
            #there is a gap of only 100 pixels
            #TODO: Whether the marking will be correct in this case.
            #Check that offset is going negative in this case.             
            return (image_shape,False)
        else:
            return (image_shape,True)
            
        
        
    # def compute_image_scaling_at_open_time
    #first open both images, then we will have a better idea of how to do scaling and create 
    #necesssary auxillay arrays.
    #before that scaling of one image is must
    #But, I also need to place two images side by side.
    #Therefore, I need to place 2 image labels side by side.
    #First do placing the image labels side by side and open the 2 images.
        
    def chk_image_within_limit_after_rescaling(self, shape_after_rescaling):
        if((shape_after_rescaling[0]>self.height_for_image) or 
           (shape_after_rescaling[1]>self.width_for_image)):
            print("screen too small")
            sys.exit(0)    

    def create_alpha(self):
        """
        This function creates the alpha channel.

        Returns
        -------
        None.

        """
        if(self.image_scaled_bool):
            self.image_alpha = np.zeros(self.image_scaled_shape, dtype = np.uint8)            
        else:
            self.image_alpha = np.zeros((self.image_shape[0], self.image_shape[1]), dtype = np.uint8)
        print("self.image_alpha.shape = "+str(self.image_alpha.shape))
                        
    #TODO: cpomplete scaling, alpha thing.
    def create_scaled_image(self):
        """
        This function creates the scaled image if required.
        The function is called after self.image has been initialized.
        The fucntion does not creates the saved_image.
        Returns
        -------
        None.

        """        
        self.image_shape, self.image_scaled_bool = self.whether_rescaling_required(self.image)
        if(self.image_scaled_bool):
            self.image_scaled_shape = (int(self.image_shape[0]*self.scaling_factor),
                                               int(self.image_shape[1]*self.scaling_factor))            
            print("self.image_scaled_shape = "+str(self.image_scaled_shape))
            self.chk_image_within_limit_after_rescaling(self.image_scaled_shape)
            #it seems cv2 resize requires width first.
            #it is known that np zeros requires num rows first
            #hence the code has been written in the way as its current state.
            self.image_scaled_array = cv2.resize(self.image,
                                                       (self.image_scaled_shape[1],
                                                        self.image_scaled_shape[0]),
                                                         interpolation=cv2.INTER_AREA)            
            print("self.image_scaled_array.shape = "+
                  str(self.image_scaled_array.shape))
            self.image_width_for_display = self.image_scaled_shape[1]
            self.image_height_for_display = self.image_scaled_shape[0]            
        else:
            self.image_scaled_array = None                        
            self.image_width_for_display = self.image_shape[1]
            self.image_height_for_display = self.image_shape[0]            
    
    def create_scaled_image_and_alpha(self):
        """
        This function creates the scaled image and also creates the alpha channel.
        The function is called after self.image has been initialized.
        The fucntion does not creates the saved_image.
        Returns
        -------
        None.

        """        
        self.create_scaled_image()
        self.create_alpha()           
    
    def load_dicom_object(self, tmp_tuple):
        """
        Loads dicom object. common to both image and video.

        Returns
        -------
        None.

        """
        self.filename_tuple = tmp_tuple
        print("self.filename_tuple = "+ str(self.filename_tuple))            
        self.filename  = self.filename_tuple[0].strip()          
        print("self.filename = "+ str(self.filename))            
        
        self.dicom_obj = pydicom.dcmread(self.filename)
        print("self.dicom_obj.is_implicit_VR before any changes= "+\
              str(self.dicom_obj.is_implicit_VR))
        self.dicom_pixel_array_shape = self.dicom_obj.pixel_array.shape
        print("self.dicom_pixel_array_shape = "+str(self.dicom_pixel_array_shape))
        # print("flush after frame shape print")
        # sys.stdout.flush()    
    
    def getImage_functionality(self):
        self.image_selected = True
        self.init_var_for_frame(1)
        self.load_if_video_is_partially_annotated()       
        self.frame_width = self.dicom_pixel_array_shape[1]
        self.frame_height = self.dicom_pixel_array_shape[0]
        self.update_for_frame()
        #self.image = self.get_image()
        #self.saved_image = self.image.copy()
        #self.create_scaled_image_and_alpha()        
        self.image_opened = True
         
    def getImage(self):        
        self.reinitialize()
        tmp_tuple = QFileDialog.getOpenFileName(self,\
                                                caption='Choose '+self.image_name+' Image File',\
                                                    directory=self.dirpath, filter=self.filter_name)
        if((tmp_tuple[0]!="") and (not tmp_tuple[0].isspace())):
            self.load_dicom_object(tmp_tuple)            
            self.getImage_functionality()
            # window.show()
   
    def init_var_for_frame(self, numFrames):
        """
        The function will be required by both image and video. The reason is that image will also have multiple nodules.
        """
        self.dicom_obj_only_filename_without_extension = Path(self.filename).stem
        print("self.dicom_obj_only_filename_without_extension = "+\
              self.dicom_obj_only_filename_without_extension)
        self.dicom_obj_dirname = os.path.dirname(self.filename)
        print("self.dicom_obj_dirname= "+str(self.dicom_obj_dirname))
        self.init_dicom_frames_path()
        self.numFrames = numFrames
        self.frame_marked_array = np.zeros((self.max_num_nodules, self.numFrames), dtype=np.uint8)
        self.frameIndex=0
 
    def init_video_specific_variables(self):
        """
        This function initiates the video specific variables.

        Returns
        -------
        None.

        """
        self.init_var_for_frame(self.dicom_obj.NumberOfFrames)
        #There should be a frame_marked_array for every nodule.
        assert self.dicom_pixel_array_shape[0] == self.numFrames,\
            "The number of frames must match."
    
    def getVideo_functionality(self):
        """
        This is the thread to obtain to obtain the video.

        Returns
        -------
        None.

        """
        self.video_selected = True
        self.init_video_specific_variables()
        #I need to process frame by frame.
        #Hence, I need to maintain a counter for current frame number. 
        #We obtain the frame at 0th index.
        print("flush before update for frame")
        sys.stdout.flush()
        self.load_if_video_is_partially_annotated()       
        self.frame_width = self.dicom_pixel_array_shape[2]
        self.frame_height = self.dicom_pixel_array_shape[1]
        self.update_for_frame()
        self.video_opened = True
        print("Video opened")            
        
    def load_common_video_image(self, tmp_tuple):
        """
        This is a function to load both images and videos.

        Returns
        -------
        None.

        """
        self.load_dicom_object(tmp_tuple)
        if((len(self.dicom_pixel_array_shape) == 1) or (len(self.dicom_pixel_array_shape) == 3)):
            #It must be a single frame i.e. image.
            self.getImage_functionality()            
        else:
            #It must be a video
            assert((len(self.dicom_pixel_array_shape) == 4)\
                   or (len(self.dicom_pixel_array_shape) == 2)),\
                "pixel array must have either 4 dim or 2dim for video"
            self.getVideo_functionality()
            self.add_slider_dock_for_video()        
        
    def check_video_format(self, filepath):
        """
        Checks if a file is a DICOM video or MP4 video.
    
        Args:
            filepath (str): The path to the file.
    
        Returns:
            str: "DICOM Video", "MP4 Video", "Other", or "File not found".
        """
        if not os.path.exists(filepath):
            return "File not found"
    
        try:
            self.dicom_obj = pydicom.dcmread(filepath)
            return "application/dicom"
        except Exception as e:
            try:
                cap = cv2.VideoCapture(video_path)
                if cap.isOpened():
                    return "MP4 Video"
                else:
                    return "Other" 
            except Exception as e:
                return "Other"
        return "Other"
 
        #except FileNotFoundError:
        #    return "FFprobe not found. Please install FFmpeg."
        #except Exception as e:
        #    print(f"FFprobe or Header check error: {e}")
    
        #return "Other"
    
        ## Example Usage:
        #file_path_mp4 = "example.mp4"  # Replace with your MP4 file
        #file_path_dcm = "example.dcm"  # Replace with your DICOM file
        #file_path_other = "example.txt" #replace with any other file.

    def read_video_frames(self, video_path):
        """
        Reads a video file and returns a list of frames as NumPy arrays.
    
        Args:
            video_path (str): The path to the video file.
    
        Returns:
            list: A list of NumPy arrays representing the video frames, or None if an error occurs.
        """
        try:
            cap = cv2.VideoCapture(video_path)
            if not cap.isOpened():
                print(f"Error: Could not open video file: {video_path}")
                return None
    
            frames = []
            while True:
                ret, frame = cap.read()
                if not ret:
                    break  # End of video
    
                frames.append(frame)
    
            cap.release()
            return frames
    
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def convert_frames_to_matrix(self, frames):
        """
        Converts a list of frames (NumPy arrays) into a 4D NumPy array.
    
        Args:
            frames (list): A list of NumPy arrays representing the video frames.
    
        Returns:
            numpy.ndarray: A 4D NumPy array of shape (num_frames, height, width, channels), or None if frames is empty.
        """
        if not frames:
            return None
    
        try:
            # Get the shape of the first frame to determine the dimensions of the matrix.
            height, width, channels = frames[0].shape
            num_frames = len(frames)
    
            # Create a 4D NumPy array to store the frames.
            video_matrix = np.zeros((num_frames, height, width, channels), dtype=np.uint8)
    
            # Copy the frames into the matrix.
            for i, frame in enumerate(frames):
                video_matrix[i] = frame
    
            return video_matrix
    
        except Exception as e:
            print(f"Error converting frames to matrix: {e}")
            return None

    def load_mp4_dicom_video(self,tmp_tuple):
        self.filename_tuple = tmp_tuple
        print("self.filename_tuple = "+ str(self.filename_tuple))            
        self.filename  = self.filename_tuple[0].strip()          
        print("self.filename = "+ str(self.filename))            
        format = self.check_video_format(self.filename)
        if(("application/dicom" == format)):
            self.mp4loaded = False
            self.load_common_video_image(tmp_tuple)
        elif("video/mp4"):
            print("loading mp4")
            self.mp4loaded = True
            self.load_mp4(tmp_tuple)
        else:
            self.mp4loaded = False
            print("Unsupported format.")

    def load_mp4(self, tmp_tuple):
        """
        This function reads mp4 and also initializes the required video variables.
        """
        self.mp4_frames = self.read_video_frames(self.filename)
        num_frames_loaded = len(self.mp4_frames)
        print("loadedmp4frames")
        print("num_frames_loaded = "+str(num_frames_loaded))
        #self.mp4_frames = self.convert_frames_to_matrix(self.mp4_frames_list)
        print("converted frames to matrix")
        self.numFrames = num_frames_loaded #self.mp4_frames.shape[0]
        self.init_var_for_frame(self.numFrames)
        self.load_if_video_is_partially_annotated()       
        #creating separate variables for frame width and height. 
        #The reason is that the load frame may be called prior to displaying and
        #scaling any image.
        #But the scaling may required. Then what to do in this case?
        #When saving the frame marking, the alpha was upscaled to original size.
        #therefore, the original image size must be given here.
        #The scaling can be done later after the frame has been loaded.
        self.frame_width = self.mp4_frames[0].shape[1]
        self.frame_height = self.mp4_frames[0].shape[0]
        self.update_for_frame()
        self.video_opened = True
        print("Video opened")            
        self.add_slider_dock_for_video()        

    def getVideo(self):                
        self.reinitialize()
        tmp_tuple = QFileDialog.getOpenFileName(self,\
                                                caption='Choose '+self.image_name+' Video File',\
                                                    directory=self.dirpath, filter=self.filter_name)
        if((tmp_tuple[0]!="") and (not tmp_tuple[0].isspace())):
            #self.image_label.setText("Please wait while the video is being loaded.")            
            self.video_loading_message_window.show()
            #self.display_loading_window.show()
            #self.video_loading_dialog.exec()
            # self.thread_get_video = Thread(target = self.getVideo_functionality)
            self.load_mp4_dicom_video(tmp_tuple)
            #self.load_common_video_image(tmp_tuple)
            # self.thread_get_video.start()
            # self.show()
            # self.thread_get_video.join()
            self.video_loading_message_window.hide()
            #self.display_loading_window.hide()
            #self.video_loading_dialog.hide()

    def fill_frame_marked_array(self, noduleIndexToFill, annotated_frame_list):
        """
        #This function fills the self.frame_marked_array

        Parameters
        ----------
        annotated_frame_list : TYPE
            DESCRIPTION.
        noduleIndexToFill:this is the index of the nodule for which the array should be filled.
        Returns
        -------
        None.

        """        
        for frameIndex in annotated_frame_list:
            self.frame_marked_array[noduleIndexToFill][frameIndex] = 1
   
    def load_if_video_is_partially_annotated(self):
        """
        The function loads the nodules and frame marked info. This is done when reloading a partially annotated video file.
        """
        #Having this variable because this variable is required in certain condition, i.e. when nodules are added that were added before
        #closing the partially annotated video.
        path_csv = Path(self.csv_filename_video)
        if (path_csv.is_file() and path_csv.stat().st_size > 0):
            df_annotation = pd.read_csv(self.csv_filename_video, header=None)
            print("df_annotation.iloc[:,1]=\n"+str(df_annotation.iloc[:,1]))
            eq_chk = df_annotation.iloc[:,1] == self.filename
            print("eq_chk=\n"+str(eq_chk))
            video_df_current_file = df_annotation[eq_chk]
            print("video_df_current_file="+str(video_df_current_file))
            if(not video_df_current_file.empty):
                self.loading_partially_annotated_video=True 
                #we can have duplicate rows for a given nodules
                #hence the length of the df cannot tell the num nodules present. Instead, the column for nodule index and their 
                #uniq entries should be counted.  
                
                num_nodule_present = video_df_current_file.iloc[:,2].nunique(dropna=True) #len(video_df_current_file)
                
                assert num_nodule_present <= self.max_num_nodules, "num nodules cannot be larger than the total number of nodules"
                #read the nodule one by one and do the loading of the nodule annotation.  
                for tmp_nodule_index in range(num_nodule_present):
                    self.add_nodule_clicked()
                    print("self.numNodules="+str(self.numNodules))
                    print("self.current_marking_nodule_index="+str(self.current_marking_nodule_index))
                    print("tmp_nodule_index="+str(tmp_nodule_index))
                    assert self.current_marking_nodule_index == tmp_nodule_index, "The indices of the nodules must match."
                    nodule_df_chk = video_df_current_file.iloc[:,2] == self.current_marking_nodule_index
                    nodule_df = video_df_current_file[nodule_df_chk]
                    print("nodule_df="+str(nodule_df))
                    print("nodule_df.iloc[0,:]="+str(nodule_df.iloc[0,:]))
                    #The person may have modified the annotation for a given nodule.
                    assert(1 == nodule_df.iloc[:,2].nunique(dropna=True)), "this df should have entries for only one nodule."
                    num_entries_same_nodule = len(nodule_df)
                    #when the annotation for the same nodule was done multiple times, then the last such entry should be loaded.
                    entry_index_to_load = num_entries_same_nodule - 1
                    #assert(len(nodule_df) == 1),"exactly one row should be there for given file and nodule index"
                    sys.stdout.flush()
                    self.nodule_dict[self.current_marking_nodule_index].load_annotation(nodule_df.iloc[entry_index_to_load,:])
                    #Now load the frame annotated array for the last nodule
                    self.load_frame_annotated_array_from_video_filename(self.current_marking_nodule_index)
                #The loading of partially annotated video is complete now.
                self.loading_partially_annotated_video=False
 
    #TODO: When doing for image, I maust also do for image that if image is already annotated 
    #then load that image.
    def load_frame_annotated_array_from_video_filename(self, noduleIndexToLoad):
        """
        This function loads frame annotated array from video csv filename.

        Parameters
        ----------
        file_read_handle : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        path_csv = Path(self.csv_filename_video_marked_frames) 
        if (path_csv.is_file() and path_csv.stat().st_size > 0):
            video_df = pd.read_csv(self.csv_filename_video_marked_frames, header=None)            
            print("video_df.iloc[:,1]=\n"+str(video_df.iloc[:,1]))
            eq_chk = video_df.iloc[:,1] == self.filename
            print("eq_chk=\n"+str(eq_chk))
            video_df_current_file = video_df[eq_chk]
            if(not video_df_current_file.empty):
                #get the frame indices for the given nodule index
                nodule_chk = video_df_current_file.iloc[:,2] == noduleIndexToLoad 
                nodule_df = video_df_current_file[nodule_chk]
                annotated_frame_list = nodule_df.iloc[:,3].to_numpy()
                print("annotated_frame_list.shape = "+str(annotated_frame_list.shape))
                print("annotated_frame_list="+str(annotated_frame_list))
                print("video_df_current_file=\n"+str(video_df_current_file))
                assert(len(nodule_df)==annotated_frame_list.size),\
                    "The number of rows must be same as the number of elements."
                self.fill_frame_marked_array(noduleIndexToLoad, annotated_frame_list)        
   
    def load_image_dicom(self):
        """
        This function is used to load the dicom image when the dicom has been loaded whether image or video.
        """ 
        if(self.video_selected):
            self.image = self.get_frame_at_frameIndex()
        elif(self.image_selected):
            self.image = self.get_image()
        else:
            assert False, "This condition cannot occur"

    def load_image_dicom_mp4(self):
        if (self.mp4loaded):
            self.image = self.mp4_frames[self.frameIndex].copy()
        else:
            self.load_image_dicom()

    def update_for_frame(self):
        """
        This function makes all the necessary arrangements for updating the view for the frame 
        advanced.
        I am updating this function because later the frames in forward move may also be find already annotated when loading an already annotated file.
        Returns
        -------
        None.

        """
        # #First clear any frame that previously could be loaded.
        # self.clear_loaded_frame()
        #clear all the extra variables        
        #The loaded frame variables will be cleared inside this function.
        # print("update for frame started for frmae index "+str(self.frameIndex))
        self.clear_extra_var()
        
        #print all the variables. This way, I will get an idea of whether 
        #I have cleared all the extra variables.
        # print("The mebers of self when loading a new frame are :")
        # print(self.__dict__)
        print("updating for frame")
        print("frame index = "+str(self.frameIndex))
        print("current_marking_nodule_index = "+str(self.current_marking_nodule_index))
        print("self.frame_marked_array[self.current_marking_nodule_index][self.frameIndex] = "\
            + str(self.frame_marked_array[self.current_marking_nodule_index][self.frameIndex]))
        if(1==self.frame_marked_array[self.current_marking_nodule_index][self.frameIndex]):
            #load the saved frame
            self.load_annotated_frame()
        else:
            self.load_image_dicom_mp4()
            self.saved_image = self.image.copy()
            self.create_scaled_image_and_alpha()
        print("showing frame "+str(self.frameIndex))
        self.next_frame_button.setText("Show Next frame, Current Frame Index = "+str(self.frameIndex))
        self.frame_updated = True        
        self.activateWindow()

    #def update_for_frame_mp4(self):
    #    """
    #    This function makes all the necessary arrangements for updating the view for the frame 
    #    advanced.
    #    I am updating this function because later the frames in forward move may also be find already annotated when loading an already annotated file.
    #    Returns
    #    -------
    #    None.

    #    """
    #    # #First clear any frame that previously could be loaded.
    #    # self.clear_loaded_frame()
    #    #clear all the extra variables        
    #    #The loaded frame variables will be cleared inside this function.
    #    # print("update for frame started for frmae index "+str(self.frameIndex))
    #    self.clear_extra_var()
    #    self.image = self.mp4_frames[self.frameIndex]
    #    self.saved_image = self.image.copy()
    #    self.create_scaled_image_and_alpha()
    #    print("showing frame "+str(self.frameIndex))
    #    self.next_frame_button.setText("Show Next frame, Current Frame Index = "+str(self.frameIndex))
    #    self.frame_updated = True        
    #    self.activateWindow()

    #def update_for_frame(self):
    #    if (self.mp4loaded):
    #        self.update_for_frame_mp4()
    #    else:
    #        self.update_for_frame_dicom()
        
    def increment_and_update_for_frame(self):
        self.frameIndex=self.frameIndex+1
        self.slider.setValue(self.frameIndex)
        self.update_for_frame()
        # self.show_image()
        # self.update()        
       
    def first_frame(self):
        if(self.video_opened):
            if(self.is_video_playing()):
                return        
        self.frameIndex=0
        self.slider.setValue(self.frameIndex)
        self.update_for_frame()

    def last_frame(self):
        if(self.video_opened):
            if(self.is_video_playing()):
                return        
        self.frameIndex=self.numFrames-1
        self.slider.setValue(self.frameIndex)
        self.update_for_frame()

    def next_frame(self):
        """
        This function increments and updates frame
    
        Returns
        -------
        None.
    
        """
        if(self.video_opened):
            if(self.is_video_playing()):
                return        
            if(self.frameIndex<self.numFrames-1):
                self.increment_and_update_for_frame()
            
    def play_video_thread_function(self):
        while(self.frameIndex<self.numFrames-1):
            if(self.pause_clicked):
                #complete the thread function if the pause_clicked //stop 
                break
            self.increment_and_update_for_frame()
            time.sleep(0.06)
        if(self.frameIndex == self.numFrames-1):
            self.pause_after_video_ended()
                        
    def update_for_frameOffset(self, offset):
        """
        This function updates the view for the view for the given frame offset.
        The offset needs to be added to the current frame index.
        This function allows for negative offset as well.
        888888888888
        it seems fine. chk this later why 8888 was written here and 
        not deleted.
        """
        self.frameIndex = self.frameIndex + offset        
        if(self.frameIndex>self.numFrames-1):
            self.frameIndex=self.numFrames-1
        elif(self.frameIndex<0):
            self.frameIndex=0
        self.slider.setValue(self.frameIndex)
        self.update_for_frame()

    def decrement_and_update_for_frame(self):
        self.frameIndex=self.frameIndex-1
        self.slider.setValue(self.frameIndex)
        self.update_for_frame()
        # self.show_image()
        # self.update()
        
    def prev_frame(self):
        if(self.video_opened):
            if(self.is_video_playing()):
                return
            if(self.frameIndex>0):
                self.decrement_and_update_for_frame()
        
    def play_video_backward_thread_function(self):
        while(self.frameIndex>0):
            if(self.pause_clicked):
                #complete the thread function if the pause_clicked //stop 
                break
            self.decrement_and_update_for_frame()
            time.sleep(0.06)
        if( 0 == self.frameIndex ):
            self.pause_after_video_ended()
            
    def wait_for_forward_thread_to_complete(self):
        """
        This is a blocking function call and waits for the forward thread to finish.
        This will be useful in pause as well.

        Returns
        -------
        None.

        """
        if(self.is_forward_running()):
            #Wait for the forward thread to finish. only then backward comoutation may be done.
            self.play_forward_thread.join()
            self.play_forward_thread=None
    
    def wait_for_backward_thread_to_complete(self):
        """
        This is a blocking function call and waits for the forward thread to finish.
        This will be useful in pause as well.

        Returns
        -------
        None.

        """
        if(self.is_backward_running()):
            #Wait for the forward thread to finish. only then backward comoutation may be done.
            self.play_backward_thread.join()
            self.play_backward_thread=None
        
     
    def is_forward_running(self):
        """
        The current function check if the forward thread is running

        Returns
        -------
        None.

        """
        if(self.play_forward_thread!=None):
            if(self.play_forward_thread.is_alive()):
                return True
        return False
        
    def make_play_forward_as_pause(self):
        """
        The play button will get converted to pause button.

        Returns
        -------
        None.

        """
        self.play_forward_button.setText("pause")
        # self.play_forward_button.clicked.connect(self.pause_video)
    
    def make_play_forward_as_forward(self):
        """
        The play button will get converted to pause button.

        Returns
        -------
        None.

        """
        self.play_forward_button.setText("Play Video Forward")
        # self.play_forward_button.clicked.connect(self.play_video)
    
    def make_play_backward_as_pause(self):
        """
        The play button will get converted to pause button.

        Returns
        -------
        None.

        """
        self.play_backward_button.setText("pause")
        # self.play_backward_button.clicked.connect(self.pause_video)
    
    def make_play_backward_as_backward(self):
        """
        The play button will get converted to pause button.

        Returns
        -------
        None.

        """
        self.play_backward_button.setText("Play Video Backward")
        # self.play_backward_button.clicked.connect(self.play_video_backward)    
    
    def show_saved_window(self):
        self.display_save_window.show()
        time.sleep(0.35)
        self.display_save_window.hide()

    
    def show_saved_window_not(self):
        print("in show saved window")
        self.display_save_window.show_thread_permanent()

    def show_saved_window_not_working(self):
        """
        This function will initiate a thread that will show saved window.
        I dont know why creating a thread and then doing setvisible as true makes a blocking call,
        whereas directly setting setvisible was not a blocking call. 
        Returns
        -------
        None.

        """
        print("in show saved window")
        if(self.show_saved_thread!=None):
            print("joining earlier show_saved_thread")
            self.show_saved_thread.join()
            print("joined earlier show_saved_thread")
        print("creating thread show_saved_thread")
        #self.show_saved_thread = Thread(target=self.show_saved_window_thread)
        #self.play_forward_clicked = True
        #self.play_backward_clicked = False
        #self.pause_clicked = False
        #self.make_play_forward_as_pause()        
        #self.slider.valueChanged.disconnect(self.update_for_slider)
        #self.show_saved_thread = Thread(target=self.play_video_thread_function)
        #The above code confirmed that it was possible to create and run another thread using this function.
        self.show_saved_thread = Thread(target=self.show_saved_window_thread)
        print("created thread show_saved_thread")
        self.show_saved_thread.start()
        print("started thread show_saved_thread")
    
    def show_saved_label_temporary(self):
        print("in show_saved_label_temporary")
        self.qlabel_saved.setVisible(True)
        print("in show_saved_label_temporary set: visible made true")
        print("in show_saved_label_temporary set: calling sleep")
        
        time.sleep(self.window_timeout)
        self.qlabel_saved.setVisible(False)        

    
    def show_saved_window_thread(self):
        """
        

        Returns
        -------
        None.

        """
        print("in show_saved_window_thread")
        
        self.qlabel_saved.setVisible(True)
        print("in show_saved_window_thread set: visible made true")
        print("in show_saved_window_thread set: calling sleep")
        
        time.sleep(self.window_timeout)
        self.qlabel_saved.setVisible(False)        
        
    def play_video(self):
        """
        This function plays video.

        Returns
        -------
        None.

        """
        if(self.video_opened):
            if(self.is_backward_running()):
                #The forward and backward cannot play simultaneously.
                # self.pause_video()
                return
            if (not self.is_forward_running()):
                self.play_forward_clicked = True
                self.play_backward_clicked = False
                self.pause_clicked = False
                self.make_play_forward_as_pause()
                # self.make_play_backward_as_pause()                            
                self.slider.valueChanged.disconnect(self.update_for_slider)
                self.play_forward_thread = Thread(target=self.play_video_thread_function)
                self.play_forward_thread.start()
            else:
                self.pause_video()
                
    def is_backward_running(self):
        """
        The function returns true if the backward thread is running.

        Returns
        -------
        None.

        """
        if(self.play_backward_thread!=None):
            if(self.play_backward_thread.is_alive()):
                return True
        return False
        

    def play_video_backward(self):
        """
        This function plays video in backward.
    
        Returns
        -------
        None.
    
        """
        if(self.video_opened):
            if(self.is_forward_running()):
                #both forward and backward cannot play simultaneously.
                #Currently we alternate between play and pause
                return()
            if (not self.is_backward_running()):
                self.play_forward_clicked = False
                self.play_backward_clicked = True            
                self.pause_clicked = False
                self.make_play_backward_as_pause()
                # self.make_play_forward_as_pause()                        
                self.slider.valueChanged.disconnect(self.update_for_slider)
                self.play_backward_thread = Thread(target=self.play_video_backward_thread_function)
                self.play_backward_thread.start()
            else:
                self.pause_video()
                
    def pause_after_video_ended(self):
        """
        This functiuon performs the pause functionality after the video has eneded.

        Returns
        -------
        None.

        """
        if(self.video_opened):
            self.play_forward_clicked = False
            self.play_backward_clicked = False
            self.pause_clicked = True
            self.make_play_forward_as_forward()
            self.make_play_backward_as_backward()
            self.slider.valueChanged.connect(self.update_for_slider)

    def pause_video(self):
        """
        This function pauses the video.

        Returns
        -------
        None.

        """
        if(self.video_opened):
            self.play_forward_clicked = False
            self.play_backward_clicked = False
            self.pause_clicked = True
            self.wait_for_backward_thread_to_complete()
            self.wait_for_forward_thread_to_complete()
            self.make_play_forward_as_forward()
            self.make_play_backward_as_backward()
            self.slider.valueChanged.connect(self.update_for_slider)
        
    def compute_sizes(self):
        """
        This functions computes all sizes.

        Returns
        -------
        None.

        """
        # self.image_search_button_size = self.sagital_image_search_button.geometry().size()
        # self.image_search_button_width, self.image_search_button_height = self.image_search_button_size.width(), self.image_search_button_size.height()
        # print(f"image_search_button size: {self.image_search_button_width}x{self.image_search_button_height}")
        
        # self.save_button_size = self.save_button.geometry().size()
        # self.save_button_width, self.save_button_height = self.save_button_size.width(), self.save_button_size.height()
        # print(f"save_button size: {self.save_button_width}x{self.save_button_height}")
        
        #currently make 1/2 considering this as the image size.
        #Later on we will see whether to reduce to haf or scale by which factor.
        if False == self.window_size_computed:
            self.scaling_factor = 0.4
            self.total_width_for_image = self.window_width
            
            #We need 8 such coulmns for information
            self.annotation_label_width = 120
            self.dropdown_width = 300
            
            self.info_width = (int)((self.annotation_label_width \
                                     + self.dropdown_width)/2) #int(self.total_width_for_image/8)
            
            self.info_height = 28
            #We have 
            
            self.y_pos_first_row = window_margin + 0*self.info_height
            self.y_pos_second_row = window_margin + 1*self.info_height
            self.y_pos_third_row = window_margin + 2*self.info_height
            self.y_pos_fourth_row = window_margin + 3*self.info_height
            self.y_pos_fifth_row = window_margin + 4*self.info_height
            self.y_pos_sixth_row = window_margin + 5*self.info_height
            self.y_pos_seventh_row = window_margin + 6*self.info_height
            self.y_pos_eighth_row = window_margin + 7*self.info_height
            self.y_pos_nineth_row = window_margin + 8*self.info_height
            self.y_pos_tenth_row = window_margin + 9*self.info_height
            self.y_pos_eleventh_row = window_margin + 10*self.info_height
            self.y_pos_twelth_row = window_margin + 11*self.info_height
            self.y_pos_thirteenth_row = window_margin + 12*self.info_height
            self.y_pos_fourteenth_row = window_margin + 13*self.info_height
            # self.y_pos_fifteenth_row = window_margin + 14*self.info_height
            # self.y_pos_sixteenth_row = window_margin + 15*self.info_height
            # self.y_pos_seventeenth_row = window_margin + 16*self.info_height
            # self.y_pos_eighteenth_row = window_margin + 17*self.info_height
            # self.y_pos_nineteenth_row = window_margin + 18*self.info_height
            # self.y_pos_twentyth_row = window_margin + 19*self.info_height
            # self.y_pos_twentyfirst_row = window_margin + 20*self.info_height
            
            print("y_pos_first_row = "+str(self.y_pos_first_row))
            print("y_pos_second_row = "+str(self.y_pos_second_row))        
            print("y_pos_third_row = "+str(self.y_pos_third_row))
            print("y_pos_fourth_row = "+str(self.y_pos_fourth_row))
            print("y_pos_fifth_row = "+str(self.y_pos_fifth_row))
            print("y_pos_sixth_row = "+str(self.y_pos_sixth_row))
            print("y_pos_seventh_row = "+str(self.y_pos_seventh_row))
            print("y_pos_eighth_row = "+str(self.y_pos_eighth_row))
            print("y_pos_nineth_row = "+str(self.y_pos_nineth_row))
            print("y_pos_tenth_row = "+str(self.y_pos_tenth_row))
            print("y_pos_eleventh_row = "+str(self.y_pos_eleventh_row))
            print("y_pos_twelth_row = "+str(self.y_pos_twelth_row))
            print("y_pos_thirteenth_row = "+str(self.y_pos_thirteenth_row))
            print("y_pos_fourteenth_row = "+str(self.y_pos_fourteenth_row))
            # print("y_pos_fifteenth_row = "+str(self.y_pos_fifteenth_row))
            # print("y_pos_sixteenth_row = "+str(self.y_pos_sixteenth_row))
            # print("y_pos_seventeenth_row = "+str(self.y_pos_seventeenth_row))
            # print("y_pos_eighteenth_row = "+str(self.y_pos_eighteenth_row))
            # print("y_pos_nineteenth_row = "+str(self.y_pos_nineteenth_row))
            # print("y_pos_twentyth_row = "+str(self.y_pos_twentyth_row))
            # print("y_pos_twentyth_row = "+str(self.y_pos_twentyth_row))
            
            
            #Whether image scaling required should be computed after computing the width and 
            #height for the image
            #And yes, it is done as required. The reason is that whether_recaling_reqd is called
            #from within getImage. Till that point of time size of every label is fixed.
            
            self.qlabel_heading.setGeometry(window_margin, self.y_pos_first_row,\
                                           2*self.info_width, self.info_height)
            self.qlabel_sub_heading.setGeometry(window_margin, self.y_pos_second_row,\
                                           2*self.info_width, self.info_height)
            
            self.dicom_open_button.setGeometry(window_margin\
                                                 , self.y_pos_third_row,\
                                           2*self.info_width, self.info_height)
                
            self.play_forward_button.setGeometry(window_margin, self.y_pos_fourth_row,\
                                           2*self.info_width, self.info_height) 
            self.play_forward_button.setFixedSize(2*self.info_width, self.info_height)
            
            self.play_backward_button.setGeometry(window_margin, self.y_pos_fifth_row,\
                                           2*self.info_width, self.info_height)
            self.play_backward_button.setFixedSize(2*self.info_width, self.info_height)
            self.next_frame_button.setGeometry(window_margin, self.y_pos_sixth_row,\
                                           2*self.info_width, self.info_height)
            self.next_frame_button.setFixedSize(2*self.info_width, self.info_height)
            self.prev_frame_button.setGeometry(window_margin, self.y_pos_seventh_row,\
                                           2*self.info_width, self.info_height)
                
            self.menuBar.setGeometry(window_margin, self.y_pos_eighth_row,\
                                           2*self.info_width, self.info_height)
            self.menuBar.setFixedSize(2*self.info_width, self.info_height)
            
            self.toolBar.setGeometry(window_margin, self.y_pos_nineth_row,\
                                            2*self.info_width, self.info_height)
            self.toolBar.setFixedSize(2*self.info_width, self.info_height)
                
            self.clear_marking_button.setGeometry(window_margin, self.y_pos_tenth_row,\
                             2*self.info_width, self.info_height)            
            self.close_image_button.setGeometry(window_margin, self.y_pos_eleventh_row,\
                                         2*self.info_width, self.info_height)            
            self.save_button.setGeometry(window_margin, self.y_pos_twelth_row,\
                                         2*self.info_width, self.info_height)
            self.close_window_button.setGeometry(window_margin, self.y_pos_thirteenth_row,\
                                         2*self.info_width, self.info_height)           
            self.update_image_label_dim()
            self.set_info_label_geometry()
            self.window_size_computed = True
                        
    def update_image_label_dim(self):
        """
        This function updates the image label dimension.

        Returns
        -------
        None.

        """
        self.image_label_x_start = window_margin + 2*self.info_width
        self.image_label_y_start = 0 #self.y_pos_first_row
        
        self.width_for_image = int(self.total_width_for_image -\
                                   (window_margin+2*self.info_width)) 
            
        self.height_for_image = int(self.window_height)
        #TODO: place a label that acquires the complete image label. 
        #Then chk whether the window boundaries affect the height that is there for the
        #label.
        
        #Why this computation being done 2 times for axial
        #The code is running thisway.
        print("width_for_image = "+str(self.width_for_image)+" for "+self.image_name)
        print("height_for_image = "+str(self.height_for_image)+" for "+self.image_name)
        
        self.image_label.setGeometry(self.image_label_x_start,
                                           self.image_label_y_start, 
                                           self.width_for_image, 
                                           self.height_for_image)        
        self.image_label.setFixedSize(self.width_for_image,
                                            self.height_for_image)            
        assert self.width_for_image <=self.total_width_for_image, "width should not exceed"            
        self.image_center_x = (int)(self.image_label_x_start + (self.width_for_image)/2)
        self.image_center_y = (int)(self.image_label_y_start + (self.height_for_image)/2)
    
    def set_info_label_geometry(self):
        """
        Add the floating slider for video

        Returns
        -------
        None.

        """
        #setting geometry tot he dock widget
        self.qlabel_saved = My_Info_Window(100, self.info_height, self.image_center_x, self.image_center_y\
            , 100, self.info_height, "saved")    
        self.qlabel_saved.setGeometry(self.image_center_x, self.image_center_y, 100, self.info_height)
        self.qlabel_saved.setWindowFlags(Qt.FramelessWindowHint)  # Set the flag for a frameless window
        self.qlabel_saved.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.qlabel_advanced.setGeometry(self.image_center_x, self.image_center_y, 700, self.info_height)
        
        
    def add_slider_dock_for_video(self):
        """
        Add the floaating slider for video

        Returns
        -------
        None.

        """
        #setting geometry tot he dock widget
        slider_y = self.image_label_y_start + self.height_for_image  - self.info_height
        self.dock_slider.setGeometry(self.image_label_x_start, slider_y, self.width_for_image, self.info_height)
        self.dock_slider.setFixedSize(self.width_for_image, self.info_height)
        self.dock_slider.setWindowFlags(Qt.FramelessWindowHint)
        self.initialize_slider_view()
        # setting floating property
        self.dock_slider.setFloating(True)
        self.dock_slider.setGeometry(self.image_label_x_start, slider_y, self.width_for_image, self.info_height)
        print("slider_y = "+str(slider_y))
        self.dock_slider.setFixedSize(self.width_for_image, self.info_height)
        self.dock_slider.setVisible(True)
    
    def initialize_slider_view(self):
        self.slider.setVisible(True)
        # self.slider.
        # setGeometry(self.image_label_x_start, self.y_pos_twentyth_row, self.width_for_image, self.info_height)
        self.slider.setRange(0,self.numFrames-1)
        self.slider.setSingleStep(1)
        self.slider.setPageStep(10)
        self.slider.setValue(self.frameIndex)
        self.slider.valueChanged.connect(self.update_for_slider)

    def update_for_slider(self, value):
        if(self.video_opened):
            if(not self.is_video_playing()):
                self.frameIndex=value
                self.update_for_frame()       
        
    def create_loading_dialog(self):
        self.video_loading_dialog = QDialog(self)
        self.video_loading_dialog.setWindowTitle("Loading")

        # Create a label with a message
        label = QLabel("Please wait while imgae is being loaded.")

        # Create a layout for the dialog
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(label)

        # Set the layout for the dialog
        self.video_loading_dialog.setLayout(dialog_layout)

    def show_saved_window_old(self):
        # Create a QDialog instance
        dialog = QDialog(self)
        dialog.setWindowTitle("Saved")

        # Create a label with a message
        label = QLabel("The marking over image saved successfully.")

        # Create a layout for the dialog
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(label)

        # Set the layout for the dialog
        dialog.setLayout(dialog_layout)

        # Show the dialog as a modal dialog (blocks the main window)
        dialog.exec_()
    
    # def show_loading_window(self):
    #     # Create a QDialog instance
    #     self.loading_dialog = QDialog()
    #     self.loading_dialog.setText("Loading")
    #     mylabel = QLabel("Please wait while the video is being loaded.")
        
    #     self.loading_dialog.setInformativeText("Please wait while the video is being loaded.")
    #     self.loading_dialog.setWindowFlags(Qt.FramelessWindowHint)
    #     # Show the dialog as a modal dialog (blocks the main window)
    #     self.loading_dialog.setGeometry(self.window_x + self.image_label_x_start, self.window_y + self.image_label_y_start,\
    #                                     self.width_for_image, self.height_for_image)    
    #     self.loading_dialog.show()    
    #     # self.loading_dialog.exec()    
    #     # self.loading_dialog.exec_()
    
    
    def show_loading_window(self):
        # Create a QDialog instance
        self.loading_dialog = QMessageBox()
        self.loading_dialog.setWindowTitle("Loading ....");

        self.loading_dialog.setText("Please wait while the video is being loaded.")
        # self.loading_dialog.setInformativeText("Please wait while the video is being loaded.")
        self.loading_dialog.setWindowFlags(Qt.FramelessWindowHint)
        # Show the dialog as a modal dialog (blocks the main window)
        # self.loading_dialog.setWindowModality(Qt::NonModal);

        self.loading_dialog.setGeometry(self.window_x + self.image_label_x_start, self.window_y + self.image_label_y_start,\
                                        self.width_for_image, self.height_for_image)    
        self.loading_dialog.show()    
        # self.loading_dialog.exec()    
        # self.loading_dialog.exec_()
    
    def close_loading_window(self):
        self.loading_dialog.close()
        self.loading_dialog = None
    
    def show_image(self):
        #rgba_image = self.image #cv2.cvtColor(self.image, cv2.COLOR_BGR2RGBA)
        # self.rgba_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGBA)
        # Get the size of a QWidget
        # print("inside_show_image")
        #if(False == self.window_size_computed):
        self.compute_sizes()
        
        if(self.image_opened or self.video_opened):
            #need to display the axial image
            if(self.image_scaled_bool):
                self.rgba_image = cv2.cvtColor(self.image_scaled_array, cv2.COLOR_RGB2RGBA)        
            else:
                self.rgba_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2RGBA)                        
            qimage = QtGui.QImage(self.rgba_image.data, self.rgba_image.shape[1],
                                        self.rgba_image.shape[0], QtGui.QImage.Format_RGBA8888)
            pixmap = QtGui.QPixmap(qimage)
            self.image_label.setPixmap(pixmap)
            #self.image_label.setText("saved")
            # print("updated pixmap")
            
    def clear_image_markings(self):
        if(self.image_opened or self.video_opened):
            self.image = self.saved_image.copy()
            self.create_scaled_image_and_alpha()
        
    def clear_loaded_frame(self):
        """
        This function clears the loaded frame, if any frame was loaded earlier

        Returns
        -------
        None.

        """        
        self.image_loaded = None
        self.frame_filepath = None
        
    def clear_image_and_scaled(self):
        """
        This function clears the image and scaled.

        Returns
        -------
        None.

        """
        self.image = None
        self.image_scaled_bool = False
        self.image_scaled_array = None
        self.image_width_for_display = None
        self.image_height_for_display = None
        
    def clear_global_offsets(self):
        self.image_offset_x_wrt_global = None
        self.image_offset_y_wrt_global = None        
        
    def clear_extra_var(self):
        """
        This function clears extra variables. 
        This function is useful when loading a new frame or when reinitialize is being done.
        The variable used across frames of a single video are not cleared here.
        The clear loaded_frame must be called within this function as those 
        variables are also the extra variables.
        Returns
        -------
        None.

        """
        self.image_shape = None
        self.image_alpha_scaled_up = None
        self.image_saved_to_dcm = None
        
        self.saved_image = None
        self.image_alpha = None
        self.image_scaled_shape = None
        self.current_line = []      
        self.frame_updated = False
        self.clear_loaded_frame()        
        
    def reinit_slider(self):
        self.dock_slider.setVisible(False)
        self.slider.setVisible(False)
        
    def reinitialize(self):
        """
        Reinitialize everythingafter save has been clicked.
        this is called only in case of image save. video save does not call this.
        In the case of video, the variables cleared separately and the 
        annotations are handled separately.

        Returns
        -------
        None.

        """
        # self.window_size_computed = False
       
        self.rgba_image = None
        self.rgba_image_to_save = None

        self.mp4loaded = False
        self.clear_image_and_scaled()
        self.clear_global_offsets()
        self.clear_extra_var()
        
        self.image_opened = False    
        self.image_label.clear()
        
        self.filename = None
        self.filename_tuple = None        
        self.dicom_obj = None
        self.dicom_pixel_array_shape = None
        self.dicom_obj_only_filename_without_extension = None
        self.dicom_obj_dirname = None
        self.dicom_frames_path = None
                
        self.numFrames = 0
        self.frameIndex = 0        
        self.frame_marked_array = None
        self.video_opened = False
        #By default any video is in pause state
        #The pause_clicked can be False only if the play button is clicked.
        self.pause_clicked = True
        self.play_forward_thread = None
        self.play_backward_thread = None        
        self.play_forward_clicked = False
        self.play_backward_clicked = False

        self.loading_partially_annotated_video=False
        self.reinit_slider()
        self.delete_selected_nodule()
        self.delete_all_nodules()
        #They are used to tell whether video has been selected or image has been selected.
        #They have been added to add extra feature in update for frame when loading annotated frame initially, without disrupoting the 
        #rest of the functionality.
        self.image_selected = False
        self.video_selected = False
        self.show_saved_thread = None

    def update_dicom_obj_and_save(self, dicom_obj_to_save, path_to_save):
        """
        This function updates the dicom object to be saved and then save the dicom obj to 
        the specified path.

        Parameters
        ----------
        dicom_obj_to_save : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        dicom_obj_to_save.SamplesPerPixel = 4
        dicom_obj_to_save.PhotometricInterpretation = 'RGBA'        
        dicom_obj_to_save.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian
        dicom_obj_to_save.PixelData = self.rgba_image_to_save.tobytes()
        if(self.video_opened):
            del dicom_obj_to_save.NumberOfFrames
        dicom_obj_to_save.save_as(str(path_to_save), 
                                     write_like_original=False)
        print("dicom_obj_to_save.is_implicit_VR after all changes= "+\
              str(dicom_obj_to_save.is_implicit_VR))
        self.image_saved_to_dcm = dicom_obj_to_save.pixel_array        
        rgba_image_to_save_eq_image_saved_to_dcm = \
            np.array_equal(self.rgba_image_to_save, self.image_saved_to_dcm)                                            
        print("rgba_image_to_save_eq_image_saved_to_dcm="+\
              str(rgba_image_to_save_eq_image_saved_to_dcm))

    def update_loaded_image_for_loaded_markings(self):
        """
        This function will update the loaded image for loaded markings.
        """
        print("updating the loaded image for markings.")
        if(self.color_dict[self.current_marking_nodule_index] == "Red"):
            #now update the red channel wrt  marking in alpha channel        
            self.image[:,:,0] = (np.maximum(self.image_alpha*255, self.image[:, :, 0])).copy()
        if(self.color_dict[self.current_marking_nodule_index] == "Green"):
            #now update the green channel wrt  marking in alpha channel        
            self.image[:,:,1] = (np.maximum(self.image_alpha*255, self.image[:, :, 1])).copy()
        if(self.color_dict[self.current_marking_nodule_index] == "Blue"):
            #now update the blue channel wrt  marking in alpha channel        
            self.image[:,:,2] = (np.maximum(self.image_alpha*255, self.image[:, :, 2])).copy()
        if(self.color_dict[self.current_marking_nodule_index] == "Yellow"):
            #now update the red and green channel wrt  marking in alpha channel        
            self.image[:,:,0] = (np.maximum(self.image_alpha*255, self.image[:, :, 0])).copy()
            self.image[:,:,1] = (np.maximum(self.image_alpha*255, self.image[:, :, 1])).copy()
        if(self.color_dict[self.current_marking_nodule_index] == "Cyan"):
            #now update the green and blue channel wrt  marking in alpha channel        
            self.image[:,:,1] = (np.maximum(self.image_alpha*255, self.image[:, :, 1])).copy()
            self.image[:,:,2] = (np.maximum(self.image_alpha*255, self.image[:, :, 2])).copy()

    def load_frame(self):
        self.frame_filepath = PurePath(self.dicom_frames_path[self.current_marking_nodule_index]).joinpath(\
                                       "frame_"+str(self.frameIndex)+"_marked.npy")            
        print("self.frame_filepath="+str(self.frame_filepath))
        #get the alpha shape based on image loaded in video.
        #The frame loading will be called even for the case dicom video as well.
        #Therefore frame width and height needs to be initialized for dicom 
        #video as well. 
        alpha = self.read_compressed_matrix(self.frame_filepath, self.frame_height, self.frame_width)
        return alpha

    def load_annotated_frame(self):
        """
        The function will be called when it is already checked that the current frame index has already been marked.

        Returns
        -------
        None.

        """
        print("load frame called.")
        self.frame_filepath = PurePath(self.dicom_frames_path[self.current_marking_nodule_index]).joinpath(\
                                       "frame_"+str(self.frameIndex)+"_marked.npy")            
        self.image_alpha = self.load_frame()
        #now the image must be loaded.
        self.load_image_dicom_mp4()
        #save a copy of image as in normal case
        print("self.image.shape = "+str(self.image.shape))
        self.saved_image = self.image.copy()
        #In current case, the alpha need not be created, just loaded.
        #The loaded alpha may be rescaled if required.
        #Todo: chk consistency with further markings, c;learing image and recreating alpha. done in theory.
        self.update_loaded_image_for_loaded_markings()
        
        #write code  for scaling in current case(if required). done.
        self.create_scaled_image()
        if(self.image_scaled_bool):
            #scale the alpha
            tmp = cv2.resize(self.image_alpha, 
                             (self.image_scaled_shape[1], self.image_scaled_shape[0]),
                             interpolation=cv2.INTER_AREA)                        
            self.image_alpha = tmp
        #Since, we have saved the copy of image(without alpha) and initialized the image as in normal case and then added 
        #alpha channel to red channel and also scaled the alpha if required, therefore, the normal working should proceed.
        #Also, since, I am saving the loaded image, therefore, I can give the option of redrawing the previously saved marking.
        #if the image gets cleared, then the alpha channel has to be redrawn TODO: Chk consistency with the current case.
        #In case of clearing the marking, the image will be obtained from a saved copy(which is the original image without alpha channel.)
        #The scaled image and alpha channel will be created afresh and which is required as well. Therefore, we are consistent with the 
        #clearing of marking.
        #TODO: chk consistency of more markings are added along with the current markings. done in theory.       
        #We have initialized the alpha channel with the previous markings done. Also, the alpha has been scaled to the requirements.
        #therefore, if more markings are added, they should be consistent with the already present markings. TODO: Test this case as well.
    
    def show_error(self, warning_text):
        warning_text = warning_text \
                 + "\n\nPlease stop using using the tool and consult the programmer immediately."
        warning_text = warning_text + "\nJust tell the step at which the error occurred." 
        box_title = ".STOP.STOP.STOP."
        msg_box = QMessageBox() 
        msg_box.setIcon(QMessageBox.Critical) 
        msg_box.setText(warning_text) 
        # setting Message box window title 
        msg_box.setWindowTitle(box_title) 
        # Set the buttons based on your options (choose 2 or 3)
        buttons = QMessageBox.Ok
        msg_box.setStandardButtons(buttons)
         
        # Show the message box
        answer = msg_box.exec_()
        print(traceback.format_exc())
        assert False, warning_text
        return answer

    def read_compressed_matrix(self, filename, num_rows, num_cols):
        """
        Reads a binary matrix from a compressed file using NumPy's unpackbits.

        Args:
            filename: The filename of the compressed file.
            num_rows: The number of rows in the matrix.
            num_cols: The number of columns in the matrix.

        Returns:
            A NumPy array representing the decompressed binary matrix.
        """

        compressed_data = np.fromfile(filename, dtype=np.uint8)
        decompressed_data = np.unpackbits(compressed_data.reshape(-1, 1), axis=1)
        num_cols_mul8 = self.next_multiple_of_8(num_cols)
        reshaped_data = decompressed_data.reshape(num_rows, num_cols_mul8)
        if(num_cols_mul8 != num_cols):
            data_recovered = reshaped_data[:,0:num_cols]
            return data_recovered
        else:
            return reshaped_data

    def next_multiple_of_8(self, number):
      """Finds the next multiple of 8 for a given number.
    
      Args:
        number: The input number.
    
      Returns:
        The next multiple of 8.
      """
    
      remainder = number % 8
      if remainder == 0:
        return number
      else:
        return number + (8 - remainder)

    def write_compressed_matrix(self, matrix, filename):
        """
        Writes a binary matrix to a file in a compressed format using NumPy's packbits.

        Args:
            matrix: A NumPy array representing the binary matrix.
            filename: The filename to write the compressed data to.
        """

        compressed_data = np.packbits(matrix, axis=1)
        compressed_data.tofile(filename)

    def chk_matrix_equality(self, original_matrix, decompressed_matrix):
        if np.array_equal(original_matrix, decompressed_matrix):
            print("Matrices are equal")
        else:
            print("original_matrix.shape = "+str(original_matrix.shape))
            print("decompressed_matrix.shape = "+str(decompressed_matrix.shape))
            self.show_error("save_not done properly")
            #print("Matrices are not equal")
 
    def save_frame(self, alpha_to_save):
        """
        This function will save the frame from a video.
        Returns
        -------
        None.

        """
        self.frame_filepath = PurePath(self.dicom_frames_path[self.current_marking_nodule_index]).joinpath(\
                                       "frame_"+str(self.frameIndex)+"_marked.npy")            
        print("self.frame_filepath="+str(self.frame_filepath))

        self.write_compressed_matrix(alpha_to_save, self.frame_filepath)
        new_arr = self.read_compressed_matrix(self.frame_filepath, alpha_to_save.shape[0], alpha_to_save.shape[1])
        self.chk_matrix_equality(alpha_to_save, new_arr)
        
        str_to_write = self.image_name+","+self.filename+","+str(self.current_marking_nodule_index)+","\
                                                        +str(self.frameIndex)+","+str(self.frame_filepath)+"\n"
        self.csv_file_handle_video_marked_frames.write(str_to_write)
        
        self.frame_marked_array[self.current_marking_nodule_index][self.frameIndex] = 1        
        self.csv_file_handle_video_marked_frames.flush()

    def save_image(self):
        #Appropriate wrapper should be written for save.
        #New dicom object needs to created for saving individual frames that have been annotated.
        
        if(self.image_opened or self.video_opened):
            if(self.image_scaled_bool):
                #rescaling is required
                alpha_to_save = cv2.resize(self.image_alpha,
                                                       (self.image_shape[1],
                                                        self.image_shape[0]),
                                                         interpolation=cv2.INTER_LINEAR)            
            else:
                #rescaling is not required.
                alpha_to_save = self.image_alpha
            #We donot need to reinitialize even after saving image because the user can add more nodules
            self.save_frame(alpha_to_save)
            self.show_saved_window()
            #self.show_saved_label_temporary()
            #display_save_window.show_window_temporarily()
            self.activateWindow()

    def plotLine_in_image_wrt_current_nodule(self, image_ref):
        """
        The line will be plotted wrt the current selected nodule
        image_ref is the reference of the image in which the plotting needs to be done.
        """
        if(self.color_dict[self.current_marking_nodule_index] == "Red"):
            #plot line in red channel
            cv2.polylines(image_ref, [np.array(self.current_line)], False, (255, 0, 0), thickness=2)
        elif(self.color_dict[self.current_marking_nodule_index] == "Green"):
            #plot line in green channel
            cv2.polylines(image_ref, [np.array(self.current_line)], False, (0, 255, 0), thickness=2)
        elif(self.color_dict[self.current_marking_nodule_index] == "Blue"):
            #plot line in blue channel
            cv2.polylines(image_ref, [np.array(self.current_line)], False, (0, 0, 255), thickness=2)
        elif(self.color_dict[self.current_marking_nodule_index] == "Yellow"):
            #plot line in red and green channel
            cv2.polylines(image_ref, [np.array(self.current_line)], False, (255, 255, 0), thickness=2)
        elif(self.color_dict[self.current_marking_nodule_index] == "Cyan"):
            #plot line in green and blue channel
            cv2.polylines(image_ref, [np.array(self.current_line)], False, (0, 255, 255), thickness=2)

    def plotLines(self):
        if(0==len(self.current_line)):
            #nothing will be done if there are no points to plot
            return
        print("in plot polylines ")
        print("type(self.image)="+str(type(self.image)))
        print("(self.image.shape)="+str((self.image.shape)))            
        print("type(self.current_line)="+str(type(self.current_line)))            
        print("len(self.current_line)="+str(len(self.current_line)))                        
        cv2.polylines(self.image_alpha, [np.array(self.current_line)], 
                      False, (1), thickness=2)        
        if(self.image_scaled_bool):
            self.plotLine_in_image_wrt_current_nodule(self.image_scaled_array)   
        else:
            self.plotLine_in_image_wrt_current_nodule(self.image)           
    
    def get_x_y_wrt_image(self, event, image_offset_x_wrt_global, image_offset_y_wrt_global):
        # Get the global mouse position
        global_pos = event.pos()
        x = global_pos.x() - image_offset_x_wrt_global
        y = global_pos.y() - image_offset_y_wrt_global
        return (x, y)
    
    def is_video_playing(self):
        """
        This function returns true if the video is being played, whether in forward or backward mode. 

        Returns
        -------
        None.

        """
        if(self.video_opened):
            if(self.is_forward_running() or self.is_backward_running()):
                #The marking is not allowed is the video is being played.
                return True
        return False
    
    def whether_mouse_over_image(self, event):
        """
        Currently the method has both checks that the video is not being played and the mouse is over the display region over the image.
        Later, we will need to separate these two functionalities. The reason is that While video is being played we will use the mouse click to
        pause the video.

        Parameters
        ----------
        event : TYPE
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        """
        if(False == self.image_opened and False == self.video_opened):
            #if the axial image has not been opened, we do not need to do anything
            #neither image is opened and nor the video is opened.
            return False
        #Whether video playing will be checked separately by the calling function.
        # if(self.is_video_playing()):
        #     return False
        # Get the global mouse position
        global_pos = event.pos()
        
        self.image_offset_x_wrt_global  = self.image_label_x_start +\
            self.image_label.offset_x
        self.image_offset_y_wrt_global  = self.image_label_y_start +\
            self.image_label.offset_y
        
        #chk if the x and y of image surround the mouse
        if ((global_pos.x() >= self.image_offset_x_wrt_global) and\
            (global_pos.x() <= self.image_offset_x_wrt_global +\
             self.image_width_for_display)):
            #The x is inside the image
            if ((global_pos.y() >= self.image_offset_y_wrt_global) and\
                (global_pos.y() <= self.image_offset_y_wrt_global +\
                 self.image_height_for_display)):
                #The y is also in the range.
                return True
        else:
            #the x is outside image.
            return False    
        
    def chk_x_y_constraint(self, x, y, image_width_for_display, image_height_for_display):
        """
        

        Parameters
        ----------
        x : TYPE The computed x within image
            DESCRIPTION.
        y : TYPE
            DESCRIPTION. The computed y within image

        Returns
        -------
        None.

        """
        assert x <= image_width_for_display and y <= image_height_for_display,\
            "It was already computed that mouse is over this particular image,\
             hence the x and y must be within the width and height displayed for that image."
  
    def show_moved_window(self, frameIndexBeforeUpdate, frameIndexAfterUpdate, frameOffset):
        numberOfFramesMoved = frameIndexAfterUpdate - frameIndexBeforeUpdate
        if(frameOffset>0):
            assert numberOfFramesMoved <= frameOffset, "we cannot move frames than asked" 
            label_str=""
            if (numberOfFramesMoved == frameOffset):
                label_str="Advanced "+str(frameOffset)+ " frames"
            else:
                label_str="Advanced only "+str(numberOfFramesMoved)+ " frames"
            self.display_frame_advanced_window.setText(label_str)
            #self.display_frame_advanced_window.show_thread_permanent()
            self.display_frame_advanced_window.show()
            time.sleep(0.35)
            self.display_frame_advanced_window.hide()

    def addTextAndGetFocus(self, digit):
        self.textbox_window.addTextToLabel((str)(digit))
        self.textbox_window.show()
        self.activateWindow()

    def keyPressEvent(self, event):
        #The event handling should take place if the event is within a label.
        #Also preallocate the label width and height.        
        print("key press")
        if(self.current_marking_nodule_index>-1):
            #any marking will happen only if at least one nodule has been added.
            if(self.video_opened):
            #if video has not been opened, we do not need to do anything
            #if(self.whether_mouse_over_image(event) ):
                if(not self.is_video_playing()):
                    if isinstance(event, QKeyEvent):
                        if (event.key() == Qt.Key_0):
                            #add the char 0 to label
                            self.addTextAndGetFocus(0)
                        elif (event.key() == Qt.Key_1):
                            #add the char 1 to label
                            self.addTextAndGetFocus(1)
                        elif (event.key() == Qt.Key_2):
                            #add the char 2 to label
                            self.addTextAndGetFocus(2)
                        elif (event.key() == Qt.Key_3):
                            #add the char 3 to label
                            self.addTextAndGetFocus(3)
                        elif (event.key() == Qt.Key_4):
                            #add the char 4 to label
                            self.addTextAndGetFocus(4)
                        elif (event.key() == Qt.Key_5):
                            #add the char 5 to label
                            self.addTextAndGetFocus(5)
                        elif (event.key() == Qt.Key_6):
                            #add the char 6 to label
                            self.addTextAndGetFocus(6)
                        elif (event.key() == Qt.Key_7):
                            #add the char 7 to label
                            self.addTextAndGetFocus(7)
                        elif (event.key() == Qt.Key_8):
                            #add the char 8 to label
                            self.addTextAndGetFocus(8)
                        elif (event.key() == Qt.Key_9):
                            #add the char 9 to label
                            self.addTextAndGetFocus(9)
                        elif (event.key() == Qt.Key_Enter) or (event.key() == Qt.Key_Return):
                            #code to get frame number according to the offset entered
                            frameOffset = (int)(self.textbox_window.getText())
                            #clear label, close the window to enter the offset
                            self.textbox_window.hide()
                            self.textbox_window.clearText()
                            #move to the required frame.
                            frameIndexBeforeUpdate = self.frameIndex
                            self.update_for_frameOffset(frameOffset)
                            frameIndexAfterUpdate = self.frameIndex
                            self.show_moved_window(frameIndexBeforeUpdate, frameIndexAfterUpdate, frameOffset)
                            self.activateWindow()
                        elif (event.key() == Qt.Key_Backspace):
                            self.textbox_window.removeTextToLabel()
                            if(len(self.textbox_window.getText()) > 0):
                                #If no character remains or the backspace is pressed at the beginning 
                                self.textbox_window.show()
                                self.activateWindow()
                            else:
                                self.textbox_window.hide()
                                self.activateWindow()
                            #call the function to delete the last entered character.
                        elif(event.key() == Qt.Key_Escape):
                            #hide writing text window on escape.
                            self.textbox_window.clearText()
                            #nothing needs to be done regrding frame movement and the text inside the custom label needs to be cleared 
                            self.textbox_window.hide()
                            self.activateWindow()
                        elif (event.key() == Qt.Key_Left):
                            #move to the left frame
                            self.prev_frame()
                            self.activateWindow()
                        elif (event.key() == Qt.Key_Right):
                            #move to the Right frame
                            print("right key clicked")
                            self.next_frame()
                            self.activateWindow()
                        elif (event.key() == Qt.Key_Up):
                            #move to the first frame
                            self.first_frame()
                            self.activateWindow()
                        elif (event.key() == Qt.Key_Down):
                            #move to the Last frame                            
                            self.last_frame()
                            self.activateWindow()
                        #No need to write cases for which nothing needs to be done.
                        #elif (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Space):
                        #    a
                        #    #do nothing
                        #key_text = event.text()
                        #not required now
                        #not writing the else. 
                        
                        #do backspace to delete an insterred
                        #RETURN OR ENTER BOTH FOR MOVING TO THE FRAME OFFSET
                        #ESCAPE TO HIDE THAT OFFSET WINDOW AND CLEARING ANY VALUE ENTERED.
                        #SPACE, TAB ETCC KEYS NO EFFECT
                                        

 
    def mousePressEvent(self, event):
        #The event handling should take place if the event is within a label.
        #Also preallocate the label width and height.        
        # print("mouse press")
        if(self.current_marking_nodule_index>-1):
            #any marking will happen only if at least one nodule has been added.
            if(self.whether_mouse_over_image(event) ):
                if(self.is_video_playing()):
                    #write the code to pause the video.
                    self.pause_video()
                else:                
                    #do the processing i.e. line draw over image.
                    if event.buttons() == QtCore.Qt.LeftButton:        
                        print("in mouse press")
                        x, y = self.get_x_y_wrt_image(event, self.image_offset_x_wrt_global, 
                                                      self.image_offset_y_wrt_global)
                        self.chk_x_y_constraint(x, y, self.image_width_for_display,
                                                self.image_height_for_display)
                        self.current_line.append((x, y))
                        self.update()
                    elif event.buttons() == QtCore.Qt.RightButton:
                        #I need to perform the save operation now.
                        self.save_image()
                        
    def wheelEvent(self,event):
        """
        This function generates scrolling over the video.

        Parameters
        ----------
        event : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        # print("wheel event start")
        #The following checks that the video is not in playing mode.
        if(self.whether_mouse_over_image(event) and not self.is_video_playing()):
            delta_y = event.angleDelta().y()
            if delta_y > 0:
                #Scroll down has occurred.
                #therefore update for next frame.
                self.next_frame()
            elif delta_y < 0:
                #Scroll down has occurred.
                #therefore update for next frame.                
                self.prev_frame()
        # print("wheel event end")
        
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            if(self.current_marking_nodule_index>-1):
                #any marking will happen only if at least one nodule has been added.
                if(self.whether_mouse_over_image(event) and not self.is_video_playing()):            
                    print("in mouse move event")
                    x, y = self.get_x_y_wrt_image(event, self.image_offset_x_wrt_global, 
                                                  self.image_offset_y_wrt_global)
                    self.chk_x_y_constraint(x, y, self.image_width_for_display,
                                            self.image_height_for_display)
                    self.current_line.append((x, y))
                    self.update()
                    self.plotLines()
                    self.current_line = []
                    self.current_line.append((x, y))
            
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if(self.current_marking_nodule_index>-1):
                #any marking will happen only if at least one nodule has been added.
                if(self.whether_mouse_over_image(event) and not self.is_video_playing()):            
                    self.plotLines()
                    self.current_line = []
            
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.Paint:
            self.show_image()
        return False

if __name__ == "__main__":
    QtWidgets.QApplication.setStyle('Fusion')
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')    
    #csv_filename_image = "all_data_image.csv"
    csv_filename_video = "all_data_video.csv"
    csv_filename_video_marked_frames = "all_data_video_marked_frames.csv"
    #Now write a wrapper code that will open both windows on same screen if only one screen is 
    #available.
    # screen_
    #csv_file_handle_image = open(csv_filename_image, "a")
    csv_file_handle_video = open(csv_filename_video, "a")
    csv_file_handle_video_marked_frames = open(csv_filename_video_marked_frames, "a")
    
    available_screen_list = app.screens()
    
    screen_0 = available_screen_list[0] #app.screens()[0] #app.primaryScreen()
    print('Screen: %s' % screen_0.name())
    size_0 = screen_0.size()
    print('Size_0: %d x %d' % (size_0.width(), size_0.height()))
    rect_0 = screen_0.availableGeometry()
    print("available_geometry_0 = "+str(rect_0))
    global screen_0_availableWidth, screen_0_availableHeight
    screen_0_availableWidth = rect_0.width()
    screen_0_availableHeight = rect_0.height()
    print('Available_0: %d x %d' % (screen_0_availableWidth, screen_0_availableHeight))
    screen_0_top = rect_0.top()
    screen_0_left = rect_0.left()
    print("screen_0_top = "+str(screen_0_top))
    print("screen_0_left = "+str(screen_0_left))
        
    screen_margin_top = 0
    screen_margin_bottom = 0 #50
    screen_margin_left = 0
    screen_margin_right = 0
    #Leaving out some margin, keep in mind the widgets of windows.
    window_x_axial = screen_0_left + screen_margin_left
    window_y_axial = screen_0_top + screen_margin_top
    window_width_axial = screen_0_availableWidth - (screen_margin_left+screen_margin_right)
    window_height_axial = screen_0_availableHeight - (screen_margin_top+screen_margin_bottom)
    global window_margin
    window_margin = 5
    print("window_width_axial = "+str(window_width_axial))
    print("window_height_axial = "+str(window_height_axial))
    
    
    window_axial = DicomAnnotator(window_x_axial, window_y_axial, window_width_axial,\
                                  window_height_axial, "Axial",\
                                      csv_filename_video, csv_file_handle_video,\
                                        csv_filename_video_marked_frames, csv_file_handle_video_marked_frames)
    window_axial.setWindowFlags(Qt.FramelessWindowHint)  # Set the flag for a frameless window

    window_axial.setGeometry(window_x_axial, window_y_axial, window_width_axial, window_height_axial)    
    window_axial.show()
    
    #time.sleep(10)
    if(len(available_screen_list)>1):
        screen_1 = available_screen_list[1] #app.screens()[1] 
        print('Screen: %s' % screen_1.name())
        size_1 = screen_1.size()
        print('Size_1: %d x %d' % (size_1.width(), size_1.height()))
        rect_1 = screen_1.availableGeometry()
        print("available_geometry_1 = "+str(rect_1))
        global screen_1_availableWidth, screen_1_availableHeight
        screen_1_availableWidth = rect_1.width()
        screen_1_availableHeight = rect_1.height()
        print('Available_1: %d x %d' % (screen_1_availableWidth, screen_1_availableHeight))
        screen_1_top = rect_1.top()
        screen_1_left = rect_1.left()
        print("screen_1_top = "+str(screen_1_top))
        print("screen_1_left = "+str(screen_1_left))
        
        window_x_sagital = screen_1_left + screen_margin_left
        window_y_sagital = screen_1_top + screen_margin_top
        window_width_sagital = screen_1_availableWidth - (screen_margin_left+screen_margin_right)
        window_height_sagital = screen_1_availableHeight - (screen_margin_top+screen_margin_bottom)
        print("window_width_sagital = "+str(window_width_sagital))
        print("window_height_sagital = "+str(window_height_sagital))
    else:
        window_x_sagital = screen_0_left + screen_margin_left
        window_y_sagital = screen_0_top + screen_margin_top
        window_width_sagital = screen_0_availableWidth - (screen_margin_left+screen_margin_right)
        window_height_sagital = screen_0_availableHeight - (screen_margin_top+screen_margin_bottom)
        print("window_width_sagital = "+str(window_width_sagital))
        print("window_height_sagital = "+str(window_height_sagital))
    
    window_sagital = DicomAnnotator(window_x_sagital, window_y_sagital, window_width_sagital,\
                                  window_height_sagital, "Sagital",\
                                      csv_filename_video, csv_file_handle_video,\
                                        csv_filename_video_marked_frames, csv_file_handle_video_marked_frames)
    window_sagital.setWindowFlags(Qt.FramelessWindowHint)  # Set the flag for a frameless window
    window_sagital.setGeometry(window_x_sagital, window_y_sagital, window_width_sagital,\
                                window_height_sagital)    
    window_sagital.show()
    #Todo: update this variable whenever a nodule gets selected.
    #Also, in the annotation window, have a variable that specifies the current window index.
    #Whenever an update to this variable is done, an action must be fired in the dicom annotator window which 
    #does all the changes when add nodule is done. Therefore, leave this at the moment. Currently add nodule 
    #is the only thing that changes the nodule.
    #Actually, this is required to be updated from the nodule class because the nodule class has actions.
    #The class ref in the nodule class may be used to call the function that updates all the variables in the main class 
    #including the color etc that correspond to updating a nodule.
    #But still,this task will be done at last.
    global selected_nodule_index
    selected_nodule_index = -1
    #global global_thread_and_window_collector
    #global_thread_and_window_collector = Global_thread_and_window_collector()
    #global global_hide
    #global_hide =  Global_hide()
    #global_hide.start_regular_chk_windows()
    sys.exit(app.exec_())
