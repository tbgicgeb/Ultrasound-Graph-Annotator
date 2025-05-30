#

#Keywords: Later:, urgent:, todo, TODO, Todo, 888888888888888
#For making the tool usable for sharing over web, the initialization of alpha for reloading annotated directory
#should be looked at. The screen size will be different at different locations and resize or getting only the image 
#may be required.


#clear marking over current image did not mke it red second outer boundary because 0 is written to disk.
#

#urgent: chk annotation and marking after single delete correct thing is deleted
#        and correct thing is retained.
#
#This has been that whether correct annotation is being deleted and the correct annotation being retained 
#and the correct mapping of folder names.
#But whether the correct edges are retained needs to be checked again, in case when the edges are from different images
#and edges are different in number for different nodules.

#reloading at different screen may be an issue.
#
#most important test: add/delete nodule after reloading.
#
#
#urgent chk correct saving of annotation for different nodules and correct display
#when moving across nodules.
#class
#
#After 2 delete of nodules n1 and no, it seems that marking of edge i2-n0 was not saved. chk again.
#test clear the marking. The 2 delete of nodules is not necessary. this happens when after marking and saving 2-0,
#2-1 also gets marked.
#actually the problem is that when an edge is drawn and marking is done then another edge is drawn from the same 
#image and again the marking is done then marking to prev nodule gets lost. why?
#The marking for the next nodule is correcty on the other hand.
#There must be a call to clear markings somewhere which is doing all this. 
#yes perform add edge calls clear_image_markings. Checks at which all places the call has been made.
#In add edge make_image_to_display should have been called instead of clear_image_markings.
#Also, the add edge can only be done only if a single nodule and single image is displayed. Hence no issue about
#how to change the highlight display. they will automatically get updated when self.nodule_dict_index will be updated.
#Instead clear_image_display should have been done and it has been done now.  
#Now, this seems resolved.
#
#iNSTRUCTIONS FOR using the current version:
#1: when mulitple nodules or multiple images are shown then do not do any chnage in annotation.
#2: please save all changes before doing any other operation even delete.
#3: When reloaded a directory, first display an image and not show all images of a nodule.

#urgent: when multiple nodules are shown, and one nodule gets  deleted, then after that nodule addition cannot take 
#place because nodule can be added afresh only. if only one nodule and one image was displayed and the nodule gets 
#deleted, then nodule addtion can take place. try this. 
#
#URGENT: When reloaded a directory and if first show all images of a nodule is done without displaying any image, 
#then it raises error.
#
#
#
#Urgent: When the display size is too small then i may pick only the ultrasound region from dicom. try this.
#
#Good for later: Later: 
#1: Add edge or fresh nodule when multiple nodules or images have been displayed.
#2: showAnnotationWindow should be updated for the last else which handles the case of showing annotation window 
#when one nodule is being updated during multiple nodule display.
#Urgent: 
#How can 
#1: 
#dR DEVA CAN BE ASKED THAT not to change any nodule annotation when multiple nodules are shown. 
#Also, unsaved warning can be done later.  
#
#delte edge ws in middle. this can also be done later.  
#
#Urgent: add a nodule, start marking that nodule. delete that nodule when:
#1: neither annotation nor marking has been saved.
#2: only annotation has been saved and marking not even started.
#3: only annotation saved and marking has been started but not saved.
#4: Only marking has benn saved and annotation is unchanged and not saved.
#5: Only marking has been saved and annotation is changed but not saved.
#test above when initially nodules are marked and when directory is reloaded.
#
#Urgent: Test the following case: 
#1: multiple nodules are shown. One nodule being updated by the user and the nodule got saved.
#   all the boxes should again not have any second outer boundary. this means that nodule index again got moved to 
#   the self.nodule_dict_indices_shown_extra and self.nodule_dict_index now does not have anything. This can also 
#   be checked by printing/checking the value in these variables.
#
#2: multiple nodules are shown. One nodule being updated by the user and the nodule does not got saved and the 
#   nodule got deleted. chk that everything should be same as in 1 above.

#
#
#Urgent: Also, test adding more nodules after reloading.
#add delete nodule after reloading.
#
#urgent: test everything after reloading as well.
#Important info : save variables are reset by 1: del_annotation, redo_nodule_index_mapping

#

#urgent: chk whether correct operation being carried out on no click?

#
#urgent the image mapping needs to be updated for all display indices.
#currently i was storing the display indices for images. but actually it is image to nodule dict index.
#############################################################################################################
##start checking here.
#
#When multiple  nodules are displayed and change in annotation of one nodule is done then second outer box does not 
#turn yellow to red. The second outer box remains at yellow. Also, in this way even if the changed annotation is 
#saved, it remains at that changed one even reloaed. therefore the color change should have happened even for the 
#case when multiple nodules are shown. this simply means that special highlight nodule is looking only at self.nodule_dict_index.
#Actually, I have not implemented the case when multiple nodules are shown and change in annotation should move the 
#nodule index from extra_indices_shown to self.nodule_dict_index.
#
#when drag occurs over mul image or mul nodule then then redding of nodule box shouldnot occur. done. chk later: how 
#handled for mul nodule display.
#
#There is an absurd issue that when drag is ended to beyomd the end then the next draw will start from that 
#beyond the point. This will practically not .
#
#
#
#urgent: When the n1 show all images for n1 was done then images were shown for n1, but images got highlightesd for n0 only and when closing annotation window for n1, it said n1 is not open. and when closing annotation window for n0, it successfully closed. I T DOES NOT OCCUR NOW AND IT SEEMS THAT IT WAS SOLVED EARLIER.

#when mul nodules 

#It seems that show annotationwindow was the case that reqd multile checks.
#actually show multiple images and delete nodule was the thing that required extensive checking forall cases.
#may be show mul nodule as well.


#urgent: clear image marking is must to be implemented before and after saving.

#urgent : remove unnecessary window closing opening to rediuce time. the window for save etc confirmation messages and splash windows etc. They are not working equally on all platforms.

#urgent: update messages for functioncalled by show_all_images_given+nodule
#urgent: add the function to chk if all thedispolayed imagres are same in the approprite case. in the above function.
#
#urgent: chk in case of show mul nodule, is this the case that if mul image or mul nodule displayed already is handled correctly.
#chk mul noduledisplay. 
#

#urgent: When a nodule was deleted when it was shown in multiple images and the nodule gets deleted.
#        Suppose intially 3 nodules were there as in saved pic. then n0 gets deleted. then new n0 gets deleted.
#        This time the n0 that remains has the red secound outer box. why?
#        but when hide annotation window is clicked the second outer agains turns yellow. solved.
#

#urgent: now when nodule is shown in all images. even when delete has not occurred then no alpha is added to images. 
#why?
#Actually the problem was that in alpha channel i have drawn line with 1 instead of 255. this created a problem in display. but there will still be problem in cases when 127 is there for some channels chk it later. The case for 127 has been handled already for the case when alpha had 255 and 0. 
#multiply a matrix by 255 is an expensive operation. solved. the problem was getting masked region and getting the alpha image when alpha values are 1 instead of 255. Also it is hoped that alpha value 127 will be handled sucessfully. it needs to be checked.
#
#urgent: error when closing window. img 1,2 connected to n0, img 1 connected to n1.
#n1 got deleted and window closed. then error is raised.
#
#urgent: The message annotation window already shown should be dispalyed carefully.when changing the nodule, it redisplays annotation window of required nodule and closes annotation window of earlier nodule, but since the annotation window of reqd nodule is shown twice, hence it says that annotation window is already shown for the required nodule which gives a wrong impression to the user.
#
#urgent: handle nodule save variables in case of nodule delete.
#
#urgent: img 1,2 connected to n0, and img1,2 connected to n1. when all images of n1 displayed. this switched to n0 and then to n1. After that, in some switch a 
#different nodule display displayed than required one. something like that.
#
#urgent: error in saving scaled image can be looked at later on.
#


#        7: The above suggests the same case as when only nodules were switched 
#           by the show nodule in all images, then the self.nodule_dict_index 
#           does not get updated. 
#        8: It will be better if we drop surroundings when display is lower in 
#           size so that we have picture without scaling. 
#       do redraw graph after show all images
#
#Urgent: Again there is a case when show nodule in all images resulted in red second outer box. earlier nodule weas in 3 images and the nodule at which error occurred is in 2 images. This issue occurs when a nodule in multiple images is shown after a delete operation. the reason for this might be that the delete operation must be reseting the save variables. bUT THE delete function is not changing the save variables, the how did this case occur. the solution was to 
#set the save variables as saved after showing multiple images for multiple nodules. 
#After a delete operation, any case would have either display existing nodules or add a new connection to an exiting nodule. in all of these cases correct display of seond outer box would occur because of correct updation of save variables. As per the current testing this seems fine.

#either added a new connection for a nodule or display existing nodule. henc

#image connection must be removed in nodule reinit. see how it was done earlier?
#Earlier when reinitializing the alpha dict for a nodule, all the image connections were removed. 
#the remove connection for an edge will be required only when removing a particular edge. 
#Since the loaded matrix is equal hence the show over image like in remove alpha can be done later on, as in load partially annotated directory.
#Earlier deletion of all nodules was performed after clearing nodule variables. but that was wrong. 
#Now, deletion of all nodules is performed before resetting of nodule variables. 
###########
#currently remove_all_nodules is empty in graph class.
#first complete that.
#Earlier reinit of graph class did the remove all ndules as well. the redraw graph will itself be called after reinit.
#now moving appropriate code from reinit to remove_all_nodules and remove_all_nodules will be called inside reinit.
#The reason is that remove_all_nodules is called in delete_all_nodules, which may be called somewhere else.
#Also reinit of graph will be more meaningful. done.
#earlier clearing of self.nodule_dict_index was in init_nodule_var but it should be in 
#self.clear_nodule_variables_new_implementation. done.
#chk correct placement and implementation of init_nodule_var and also the relative call of
#self.clear_nodule_variables_new_implementation() and why was the need of these two functions.
#The function clear_nodule_variables_new_implementation is the main function clearing all nodule related variables in 
#the newer implementation. The function init_nodule_var has just one extra line and that is setting max num nodules.
#And we do not require two functions. we can have just one function with the name 
#reinit_nodule_var_newer_implementation. The two functions were made earlier from the thought that we can have have 
#annotating individual videos or images with the same code. but now there will be separate code for this.
#done. now only one function is there.
#now only one doubt remains: where the nodule object reinit is done. it should have been called in 
#reinit_nodule_var.....
#Also while doing reinit for nodule the graph class should be updated, but now it is called somewere else. 
#it should be integarted with the reinit_nodule_var.
#Currently reinitialize of nodule object is done in add_nodule_functionality, delete_all_nodules, 
#delete_selected_nodule. And this is fine. reinit of nodule var is separate from reinit of nodule object. 
#but the reinit of nodule object must be done before reinit of nodule var. it is done in the required order in
#delete_all_nodules. for the function delete_selected_nodule_ it should be checked. 
#In the graph class, remove_all_nodule remove_selected_nodule
#
#Improve time:
#Later: currently nodule box coordinates are recomputed at nodule redraw time. This will take the redraw slower. 
#insted we can compute them initially and update them at the nodule delete time so that time for computing nodule box coordinates is not spend at every redraw of graph. 
#
#Later: chk again that why witout redraw graph in getDirectory, earlier all the image boxes got drawn. mul ing mul nod mouse hover version.
#
#Later: show all images for a nodule should not rescale the image if only one image is there for a nodule.
#
#the reinit_nodule_var_newer_implementation is called in __init__ of dicomannotator, delete_all_nodules, 
#clear_set_image_related_variables.  
#Currently the order of function is such that in case of delete all nodule happens only when reinitialing the dicom 
#annotator and in this case graph and nodule class instances also gets cleared. currently delete all nodules is required anywhere else. in case delete all nodules isrequired without reinitializing then further details can be looked upon. Anyways, currently focus that deletion of single nodule handles updation to nodule object and graph class correctly.
#Later: The box reinit instead of discarding may be looked at later on for low memory leak or low memory to be 
#freed by garbage collector.
#First complete deletion. chk comments above "########    Nodule deletion"
#The display of image with alpha later on needs to be shown appropriately.
#This includes loading partially annotated directory.
#
#For Presentation: have the first version of the tool that was working with videos as well.
#1: The reason of crash was that newer library has advaced checks so had to modify the code accordingly.
#I have also changed samples per pixel. will the pixel array be retrieved correctly by the remove alpha. 
#Also, when getting the pixel array the validate of pydicm was the photometric interpretation. That must be an extra
#check because the pixel array must not be changed by the photometric interpretation if it is lossless.
#not setting sampleperpixel created error. this must be set.
#Now the error is raised even on setting samples per pixel as 4. When reading it says that samples per pixel must be 
#1 or 3.  

#Therefore, now it seems better to save the marking separately, either as npy of the alpha channel or the list of 
#points which drew the line. the line drawing mechanism may change with library, hence, it is better to save the 
#annotation in the npy format. The dicom format is not required just for alpha. Also, the values are just 0 and 1 
#so no float error. Therefore the loading of alpha also needs to be changed.
#2: The location of  annotation window got changed in differnt display. so it needs to be adjusted.
#3:First all images of n0 were displayed. After that all images of n1 gets displayed. But still the nodule n0 gets 
#  highlighted. 
#4:When mouse drag occurs on one of multiple images shown then message shows that marking not possible and the nodule    box gets highlighted in red, even when the marking is not done.
#5:delay in display of drawn line. extra functions called like window show hide, print etc must be removed.

#24sep : 
#1:complete filling save variables for nodule.
#  done self.reset_nodule_save in add_nodule_functionality.
#       addNoduleWithPrevNodules also needs to checked for correctness. 
#       Loaded nodule also needs to be updated. done.
#  done self.reset_nodule_marking_saved in add_img_nodule_connection.
#       add_img_nodule_connection has been called by add_nodule_functionality and 
#           perform_add_edge_requested_by_line_drag
#  self.set_nodule_save() done in show_information_edge_exists_and_display_image, only when another nodule 
#       gets displayed. On the other hand, if the nodule is already displayed, then the save variables are not 
#       updated.
#   self.set_nodule_save() in show_nodule_single_image instead of show_information_edge_exists_and_display_image
#Later: when a nodule is displayed already, changes are made to marking but not saved, still the user draws an 
#       edge from the same image to same nodule, will the unsaved changes lost, will the red to yellow take place,
#       and will the message be appropriate. 
#  Now the plot lines, change in annotation and save function needs to be updated. 
#   self.nodule_marking_saved = False has been done in plotLines. self.reset_nodule_marking_saved()
#   self.dicom_annotator_reference.nodule_annotation_saved = False in update_tirad_single_combobox. done.
#       self.dicom_annotator_reference.reset_nodule_annotation_saved()
#   self.dicom_annotator_reference.reset_nodule_annotation_saved() in update_save_status(). 
#       The function update_save_status() is called by update_tirad_single_combobox and connected to  
#           combobox_bethesda_category, textbox1 and textbox2.
#  Update saving of nodule marking and annotation.
#   self.nodule_annotation_saved = True in save_annotation. done.
#       self.dicom_annotator_reference.set_nodule_annotation_saved()
#   self.nodule_marking_saved = True in save_image. done.
#       self.set_nodule_marking_saved()
#  SEEMS COMPLETED.
#  Display of multiple nodules/images must be updated or this.
#2: complete/chk show/hide AnnotationWindow. show seems correct.
#    writing gateway for show. make sure the only call to show_annotation_window is in this function.
#    The hide_other_annotation_window itself calls undo highlight for other nodules by  
#    undo_highlight_all_nodules. This was an error prone practice. The show and hide of annotation window should
#    focus on that only. The highlight and undo highlight of nodule boxes should be handled by the nodule 
#    selection separately. Currently it seems that there are 2 main functions that control nodule selection. 
#    First one is perform_nodule_selected and the other one will be the function that displays multiple nodules.
#    There can be different functions doing so for just display or to add nodule with other nodules. just look at
#    that time of writing those functions. In fact the special highlight function for nodule in graph class can 
#    handle that. now the hide other annotation window does not undo highlight of nodules.
#   I can work later on the messages like window already closed or a different window is open or things like that
#   in show and hide annotation window. Either all possible major messages in both show and hide must be there 
#   or none must be there. Make sure that show_annotation_window is there only in showAnnotationWindow_gateway.
#   done for show.
#   And similarly for hide. The only place where hide_annotation_window() is allowed other than gateway is 
#   hide_other_annotation_window and reinitialize and button clicked. seems complted for hide as well.
#   hideAnnotationWindow seems completed. 
#   For hide currently I am writing the hide with bare minimum messages. Later: I can update hide and show to 
#     show all possible messages like other window shown, the window already closed / show etc.
#3: highlight function for nodule in graph class.
#   This function should be designed such that the calling function will pass the img index(for which the nodule 
#    is to be displayed), The dicom annotator variables will itself tell how and which nodules to highlight.
#    The special highlight will be required even for the case when redraw set graph is required. This call can be 
#    there without any special event. Therefore, it is not good for the calling function to pass the img 
#    name or index. Instead using the dicom annotator reference and nodule variables, the special highlight will
#    itself identify what to highlight and how to highlight. and in fact it will be highlight for both images 
#    and nodules.  There can be a special highlight function that will highlight both images and nodules. 
#    This function can in turn call special functions for highlighting images and nodules. 
#    Also, passing the image name to special highlight for nodule makes sense only when a single image is 
#    displayed. When multiple images are displayed, then as per the current strategy only a single nodule can be 
#    displayed. Later: This can be further extended to display all nodules of all images.
#    Now: In fact when display a single or multiple image and when display of single or multiple nodule is 
#    required, the fields self.nodule_dict_index and self.nodule_dict_indices_shown_extra will have already been 
#    updated. Therefore, the passing of image is not required to the function special highlight for nodule.
#    CHK USAGES OF ALL HIGHLIGHT FUNCTIONS OF THE NODULE CLASS. Replace them by the special highlight function.
#    This seems to be done as per current search and replace.
#    chk usages of hide_other_annotation_window. Chk if the calling function need to call special highlight for 
#    nodule as the nodule undo_highlight was implied by hide_other_annotation_window. Currently the only used 
#    function calling hide_other_annotation_window is showAnnotationWindow_gateway. Therefore, it does not seem
#    necessary to perform undo highlight over there. 
#    Later: Also, hide_other_annotation_window must be revisted 
#    for usage and undo highlight when multiple nodule are only shown and when a nodule is marked with all
#    prev nodules shown.
#
#    Both the functions highlight_nodule_for_display and highlight_nodule_for_marking will not used, instead the 
#    special highlight for nodules will cover all the cases.
#
#    update the display of image to update nodule_dict_index and extra indices shown for nodule. In fact the 
#    perform nodule selected should be called and also the clearing of extra indices should be done. There must 
#    be another function to carry out clearing of extra indices shown. write pseucode for that.
#    first chk usages of special highlight nodule. The current usage is in highlight_nodules_consistently.
#    In fact, highlight_nodules_consistently is used everywhere. Hence special clear not reqd now. Also when 
#    perform_nodule_selected is done then redraw graph is called so that any prev nodule highlight gets cleared.
#    Later: redraw graph must be done when displaying multiple nodules or multiple images.  
#
#    chk last line in comment #add_img_nodule_connection: 
#    The above in explanation of 
#    "The function perform_nodule_selected is called in working portion of code by"
#    The main point in that comment is following:
#                           We can still have unselect_nodule in special_highlight_image_boxes because unselect_nodule
#                           should be idempotent. Currently, redraw edges is not called in unselect_nodule. 
#                           The redraw edges should be called even after all nodule box unhighlight in 
#                           unselect_nodule.88888888
#88888888888888888888888888888
#
#    The function special highlight for nodule will assume that all the previous highlight have been cleared.
#
#    I think unselect_nodule is not required now
#
#4: check correctness for case of single nodule.
# The changing of annotation window again did not change color from yellow to red. the reason must be that the 
#change function did not call highlight again. The marking should also call highlight again. 
#while loading annotation and marking also take care of this.
#redo highlight nodule was done after annotation window alter but the color did not change from yellow to red. 
#why? Actually, the color change did occur in the initial annotation items. The bethesda category and free text 
#change did not lead to change in color. Actually, they did not change the tirad score. Hence, the update 
#function was not called. But now the update function will be called even when a change occurrs in these.
#It will be better to have a another function, update_save_status.
#now any change in annotation window results in a change in color from yellow to red.
#It seems that the highlight did not take effect because when the redraw was forcibly called by drawing edge in 
#set image the color change took place.
#In fact that is an error. When the edge draw occurred, the annotation and marking should have been reloaded and 
#color should have been made yellow. it is not that after drawing edge still the chage done by user and not saved
#is being displayed.
#The other functions to update will be looked at later. first also try if change of marking work well.
#The marking did not took place immediately. this needs to be checked again.
#Now there is a delay in draw line. some lines also gets missed. It seems that graph redraw must have been 
#called many times while drawing lines. chk what is the cause. handling of mouse press and mouse drag event 
#should be looked at. Mainly mouse press should be looked at. every mouse press and mouse move calls clear_set_image_drag. Now solve 2 questions:
#Q1: is this call the cause of delay?
#Ans: yes this was the cause of delay.
#Q2: If yes then is this call required? can there be any other way?
#Ans: The delay has reduced when the call of clear set image drag has been removed from mouse move event of dicom
#image. Further speedup will be there if the clear set image drag gets removed from mouse press of dicom image. 
#The clear set image drag is useful only in mouse release at dicom image. do this. CURRENTLY NOT REMOVED FROM 
#move in docom image.
#Later : The warning that save has not been done. and other image/nodule being opened.
#Later: green can be used in place of yellow for second outer.
#The saving and rechanging should alter color between yellow and red.
#
#Do the yellow to red on marking change. do highlight the nodules again. This is working fine now.
#Later: iN CASE OF A SINGLE NODULE BEING DISPLAYED, THE YELLOW BOXIS STILL THERE EVEN WHEN THE ANNOTATION WINDOW 
#IS HIDDEN. wILL IT EFFECT THE CASE FOR MULTIPLE NODULES. JUST MOVE ON TO DISPLAY MULTIPLE NODULES.
#when marking the image and the edge is drawn between same img and nodule, the msg shown may be changed.
#When redisplaying a nodule wrt an image, only image gets displayed. why?
#ALSO REMOVE THE CODE OF DISPLAYING WINDOW. THAT WILL FURTHER INCREASE THE SPEED.
#What I can do is that on any mouse event I can check that if partial line is drawn. If yes, then I can call 
#clear_set_image_drag, otherwise, nothing needs to be done. Chk if this doesnot lowers the speed.
#The set image was definitely modified when the mouse was moved over dicom image because the line got cleared 
#when moving mouse from set image to dicom image. and it was not due to mouse moving out of set image. 
#just chk this again.
#Now the mouseMoveEvent of the dicom image does not have the clear_set_image_dra but still the line gets cleared 
#when the mouse moves out of the set image. It may be due to the space in between the set image and dicom image.
#Anyways, it seems that the window for set image does not get focus when the marking is being done over 
#dicom image. This could be a reason for highlighting nodules again. But the mouse release of the dicom image 
#still requires the graph redraw because the drawn line has been converted to an edge.
#now the plotLines has self.set_graph.highlight_nodules_consistently()
#
#Later: #clear image marking should also chage color from yelow to red
#
#The clear image markings should also change color from yellow to red.
#
#Later: revisit of point 4 has benn done completely andcorrectly.
#
#5: start thinking/code show multiple nodule.
#    Where will be the common function that will check whether both the annotation and marking for the nodule  
#    has been done. Now remove the function from the nodule_dict_index(in case of multiple nodules).
#    Instead of setting the saved variables directly as true, have a function to update them. That function can  
#    check the saved status of the other nodule as well. 
#    0: Visit all Later:. Chk what needs to be included.
#    a: In case of single nodule, it was not possible wrt some functions to have that index only in extra indices.#       but such limitation is not there in case of multiple nodules. Hence, after both save the index must be 
#       removed from nodule_dict_index and moved to extra indices. 
#    b: when all images of a single nodule are shown, then the entry of the nodule index will be there in
#       nodule_dict_index of dicom annotator and extra indices will be empty. Therefore, the 
#       nodule marking functions will be active. But, we donot want to do marking in this case. 
#       Therefore, update all the nodule marking functions, so that they will perform marking only when a 
#       single image is displayed.
#    c: When an image has only a single nodule then show all nodule should put the nodule index in 
#       nodule dict index of dicom annotator and not in the extra indices.
#    d: Visit all Later:. Chk if anything is of relevance wrt current point.
#    working showImageWithNodules
#       when showing annotation window in multiple nodule show, the second boundary(yELLOW) is not getting 
#       displayed when showing the annotation window.
#       Also when changing the annotation window the boundary must have been made red, but the yellow boundary 
#       is shown.
#       Actually this was a problem of save variables and the nodule dict index and the extra indices variables 
#       for nodule. get_extra_nodule_index_window_shown should have worked well and the save variables should 
#       also have worked well. chk again.
#       In show and hide annotation window gateway, the highlight nodule must be called again.       
#       In show annotation window 
#       Now in hide annotation window the yellow box is not removed
#       Suggestion by Dinesh sir : background of set image can be white to display all nodules.
#Later: chk only highlight_nodules_consistently  should be used everywhere.
#
#Later: if add_nodule is not adding img nodule connection then who is adding that. 
#Later: chk whether clear image markings work?
#Test case 5. Do Later at last.
#Testing case 5:
#the second outer box xhanged color from red to yellow even when the nodule was not drawn.
#It may be because of the reason that whne loading a previously marked nodule, the save status for marking over 
#image might have already been set to true even when there is a new edge added to this nodule. just chk this.
#It also seems that second outer box turns yellow on partial saving or none saving when edge is drawn.
#When the switch nodule and add connection was done, the second outer box was already yellow. correct this.8888888888
#Actually, no change was done to save variables in add_img_nodule_connection. if the variable was already 
#saved, it will remain saved. ONLY marking saved should be made false when adding 
#img nodule edge because the annotation is already saved. if the user will change the
#annotation, then he will have to save it as well.
#done this part.
#8oct: test5, 6,7,8, test6 chk some Later:, do this on 9 oct as well, do this on 10oct as well, 11oct as well.
#14oct: 9,10,11, chk some Later:
#15oct: 12,13,14, chk some Later: 
#16oct: 15, 16 More testing multiple nodules and images display, chk all 8's
#test5: When multiple nodules are highlighted then second highlighting a nodule hides some highlight of adjacent 
#nodule but still it is fine. There is problem when multiple nodules are shown:
#p1: shown the annotation window 
#draws the yellow box, but hiding the annotation window does not hides that box. Also, when annotation window of
#another nodule is shown, then the prev nodule also has yellow boundary and the new nodule also has yellow 
#boundary. Another thing thing is that for the case of single nodule, the yellow boundary is not hidden when 
#hiding annotation window.
#p2: Even when no nodule is shown still the nodule box remined highlighted.
#ans: the error was because of the fact that the previous higjlight was not undone when a new nodule was to be 
#highlighted or whenever highlight_nodules_consistently was called. Therefore, do clear any previous nodule 
#highlight in highlight_nodules_consistently.
#6: show_all_images_given_nodule is already here. it needs to be completed.
#       chk if the nodule index is to be passed?
#       code handle mul nodule or mul image display already for showing multiple nodules as well
#       The code to display multiple images is assuming 3 channels. It has to be updated for monochromatic images.
#           The function fill_panes needs to be updated for this.  
#       While adding alpha same image has been picked.
#       Also both marking has been added on the first image.
#The situation seems fine till asigninging images to panes. The problem must be in or after fill panes.
#The problem was in add_alpha_to_single_image given image should have been used and not self.image.
#Now the first image is shown both times and the second shown image has two alpha channels.
#The show of multiple images is working fine. Look at corner cases later.
#Now the show multiple nodules is not working fine. 
#Only one nodule shown in show of multiple images. 
#The main reason must be that earlier self.image was there in add_alpha_to_single_image and now it is taking directly the image name. somewhere the same image must be used to draw the second nodule as well.
#The solution is that directly pass the image instead of image_name to add_alpha_to_single_image.
#The image_name must also be passed to get the alpha for that nodule image combination.
#Now both failed show mul nodules and display all images of a nodule.
#when some i0 n0 was shown and show nodule in all images is done then the image 4 gets opened with both its nodules. why?
#this must be a problem in first function show allimages multiple nodules.
#The earlier nodule index shown is not removed somehows from conceptual list of nodules being shown. Practically
#whuch list and variables are effected needs to be seen.
#The reason is that perform nodule selected is done at a very late stage therefore, some portion of the code 
#used nodule dict index. Therefore perform nodule selected is the first step to do. but why directly nodule dict index was used. It must be at the place of adding alpha. but why the two addition done for alpha. chk again the process of filling panes. fill panes and adding alpha just use the nodue index passed to it. the flow needsa to be seen again. Even when no nodule was shown earlier still both nodules of the image are shown. this means that 
#by mistake sowhere adding all nodules has been called.
#The reason is that when a nodule was to be displayed that is not displayed and that has a single image and 
#that image has multiple nodules then showImage withNodules was called that displays all nodules of that image.
#instead explicitly the show image and adding nodule was to be done.
#done all above.
#There are 2 errors now:
#1: when i4 drew line to n0 and marking saved. after that show all nodule for n1 was called. but it said that 
#nodule is already displayed and just highlighted box n1 instead of n0. but the view still had n0 drawn over i4.
#2: when i3 was opened and show all nodule of n1 was called. the it showed error image_name_displyed == image_names_for_nodule[0]. why?
#Ans2: in this case nodule_index_image(i.e. nodule_dict_index) was already set by me by doing perform
#nodule_selected at the beginning. this should be done. instead the perform nodule selected should be done only after handlig all cases. Hence instead of calling that at the end of display_all_images_given_nodule, it should be called at the end of show_all_images_given_nodule. done. If some other function does this in its middle then it may be the requirement of that function. Also, any subfunction should not use nodule_dict_index to make changes.
#----------------------------------------------------------
#mouse hover needs to completed fast and first.
#mark line has become too slow. 
#Now focus on nodule deletion.
#---------------------------------------------------------------
#Later test all cases mul images.
#chk all messages shown. theymust and sense correct.
#currently marking is possible when show all images displayes only one image. this needsto be stopped. 
#stopping of marking and annotation when mul nodule or images are shown or when mul nodule show displays one nodule is a concern.
#mouse mul image
#test by clicking at the extreme left right top bottom of total image 
#nd individual images so that box boundaries and x,y offsets are correctly 
#tested. also the exterme points at invidual images must be tested. 
#now marking will take place only if exactly one image is displayed.
#
#ensure that any called function recursively by show_all_images_given_nodule does not directly use 
#nodule_dict_index and also it does call perform_nodule_selected.
#when moving to another nodule for displaying all images shown, message comes that annotation window is already shown. then it means that some called function has called perform_nodule_selected.
#clear marking over image does not clear alpha for that image and nieither change the saved image but in view it seemed so. chk and correct this.
#The pointer may be made small. user may be given the option to choose the pointer size.
#Look at When moving from multiple images displayed to a single image
#Look at When a different image is displayed than asked by user
#Look at all later:, LATER:, later: todo, Todo, TODO
#
#
#
#
#7: think and implement special highlight for images in case of multiple images show.
#8: Handle mouse hover event so that when mouse is over a particular image then that image gets highlighted more.
#   chk if the function get_image_name_for_mouse is used already or can it be used now.
#9: chk whether unselect_nodule is used anywhere and is it correct?
#   deleted the function. More explanation in last of #Argument: special highlight image boxes 
#Extra useful: When select directory is clicked then the set graph does not get cleared. just correct this.
#10:think and code for deletion as well.
#   delete_selected_nodule is already there. it needs to be completed.
#   following is there ##########    Nodule deletion 
#   Look at #Easy Deletion
#   function remove_nodule and remove_all_nodules has been written in graph class.
#11: the save variables of nodule needs to updated in case of delete nodule as well(delete_selected_nodule). 
#good if done: delete a given edge and not the whole nodule. only that edge should be shown in this case.
#12: chk the case when annotation window is changed when multiple nodules are shown or hidden. 
#    a:)When multiple nodules are shown then moving of that nodule index from extra indices to nodule_dict_index
#    will be required.
#    b:)When multiple nodules are shown then changing the annotation window must be banned by setting set enabled 
#    as false. Later set enabled may be set as true.
#    The setEnabled may be reset when adding to extra indices shown and set when removing from extra indices 
#    shown. This thing is valid when setting everything at once to extra indices and clearing everthing at once 
#    from extra indices.
#    c:) chk undo highlight all nodules does NOT clear/ reduce the width of original nodule box.
#
#13: unsaved marking warning is must.
#14: Reloading a partially annotated directory
#       there is a comment #loading partially annotated directory
#       there is also 8888888  Reloading a partially annotated directory
#15: add nodule with multiple nodules shown.
#16: Currently, a separate csv file is there for annotation of every nodule. Should it be merged. Will there
#    be a directory done button to be clicked by the user to do this?
#17: the ime format(monochromramatic and some shared by Diesh sir needs to be tested).
#18: stop the splashing of saved window. it is causing time delay.
#
#More features important for publishing.
#19: The user may specify which axial correspnds to which sagital and then image display will happen accordingly. 
#    Read: Argument: Divide the image space in equal sized panes.
#20: Have box bpoundaries for displaying multiple images.
#Deva sir expected thumnail for images. chk if it can be created.
#look at comments points till 21 or so, at, above below line 1111, at line 491(for monochromatic images).
#Look at line 1298 , 1329(1363), 1355, 1469(Displaying multiple nodules simultaneously)
#Look at line 7683, 4863, 7843(adding color to channel important.), 1273(comment for adding color to channel.) 
#line 1611, 1621.  
#Start completing suggestion in showAnnotationWindow newer comments.
#Also, complete showAnnotationWindow.
#The nodule highlight in graph class has to be rewritten wrt nodule_dict_index comments.
#The setting of nodule index in perform nodule selected also has to be updated.
#Many other things needs to be updated which uses nodule_dict_index. 
#The movement of nodule_dict_index to nodule_dict_indices_shown_extra on changing the annotation or updating the 
#marking may be required because that does play a role in saving. just check again. 
#Also after saving both annotation window and marking, the index may be moved from 
#nodule_dict_indices_shown_extra to nodule_dict_index.
#Another role of nodule_dict_index was to highlight for which a newer sophisticated function will be there. 
#chk if any other use of nodule_dict_index is not missed.88888888888888888888888888888888
#Later: comments starting with "Later:" can be done after delivering to deva sir.
#showAnnotationWindow seems completed. hideAnnotationWindow needs to be updated. nperform nodule selected and 
#other functions needs to be updated. nodule highlight in graph class needs to be written
#add nodule with prev needs to be done.
#First make a list which functions needs to be updated due to change in nodule_dict_index.
#perform_nodule_selected
#create_directory_for_nodule
#addNoduleWithPrevNodules(may be)
#add_nodule_clicked(not used now)
#delete_all_nodules
#load_if_video_is_partially_annotated(not used now)
#update_for_frame(not used now)
#save_image
#showAnnotationWindow
#hideAnnotationWindow
#init_nodule_var
#perform_nodule_selected
#create_directory_for_nodule
#addNoduleWithPrevNodules
#add_nodule_clicked
#delete_all_nodules
#load_if_video_is_partially_annotated
#update_for_frame
#update_loaded_image_for_loaded_markings
#load_annotated_frame
#save_frame
#plotLine_in_image_wrt_current_nodule
#plotLines
#keyPressEvent
#handle_mousePress_dicom_image
#handle_mouseMoveEvent_dicom_image
#handle_mouseReleaseEvent_dicom_image
#show_information_edge_exists
#chk_nodule_index_correct
#add_img_nodule_connection
#ask_nodule_close()
#perform_add_edge_requested_by_line_drag(new nodule added, i mean new marking is to be done.)
#tHERE ARE SOMEFUNCTIONS LIKE show_nodule_single_image. They work with nodule_index and call functions like
#perform_nodule_selected, chk_nodule_index_correct which inherently updates nodule_dict_index.
#function show_information_edge_exists directly uses self.nodule_dict_index.
#tHE NODULE_DICT_INDEX is mainly for the nodule displayed in case of single nodule. 
#Which functions will be afftected by multiple nodules.
#tHE NODULE_DICT_INDEX if maintained by the current method, for new marking and loaded marking, all the above 
#functions will work fine, without requiring any change. The only thing required for the case when a marking is 
#loaded is to have another variable. A change in this variable can also signal the graph class for appropriate 
#highlighting because the highlight in the graph class will also consult this variable before highlighting. 
#This variable will in fact also serve the purpose that whether the current marking and annotation has been saved.
#Here both saved is referred to. This variable will be save_nodule_done. If this is false then one of the 
#condition is there, either the nodule is being added or a marked nodule is loaded but the change is being done.
#The highlighting in both cases is same which is red. This variable can also be used to show a warning if the 
#user tries to close a nodule without saving it. In fact we should maintain two variables, one for save of 
#annotation window and the other is for save of marking(line drawn). This will provide a more detailed 
#information that what is saved and what is not. These variables will be nodule_annotation_saved and 
#nodule_marking_saved. First complete filling of these variables and then update showAnnotation window.


#Start completing at comment line 1594, which talks about add_img_nodule_connection.
#Start completing comment at line 4496 which says about separate highlight for show annotation window.
#start completing at line 4317(NOW 4511)(in showAnnotationWindow)> That comment stats that separate highlight color for nodule boxes for different situation. Now in 
#Also start completing at line 5057 in hide_other_annotation_window
#Though, I am making sure everywhere that the scaled image should also work well but there was error in marking 
#over the scaled imaged. 
#chk the colour of marking after reloading the nodules marked. chk it for all nodules till n9.
#chk the comments starting at line 7964.
#Currently, the ALPHA SCALING IS NOT DONE INITIALY AND WHEN redisplay of a nodule is done(sometime after marking).
#The alpha scaling is also required to be done when add ndule fresh is done. The alph scaling may be done and 
#tested at last. The alpha scaling also needs to be updated in show_nodule_single_image at the time of 
#add_alpha_to_single_image, so that alpha gets correctly added to the scaled image.
#Currently, the function show_nodule_single_image seems coorect. this function and the called functions may be 
#checked later on. Also, add_img_nodule_connection should also be checked for alpha resizing.
#make_image_to_display also needs to be updated for alpha resizing.
#show_information_edge_exists_and_display_image ALSO needs to be checked, but later.
#Assuming add_img_nodule_connection as correct.
#show_information_edge_exists_and_display_image also needs to be checked again for correctness.
#chk the correct usgae of nodule index in dict and the nodule index displayed in the related functions.
#The function get_displayed_nodule_index should be used everywhere to get the displayed index.
#Also chk usages of .index_in_nodule_dict_to_number_displayed and get_displayed_nodule_index.
#complete add_img_nodule_connection, seems completed if the called functions are correct and complete.
#Similar to the function for obtaining displyed nodule index, we should use the following line everywhere to obtain the image name displYED currently:
#(isSameImageDisplayed, numImagesDisplayed, image_name_displayed) = self.chkSameImageOpened("")
#Also check theusages of self.image_names_currently_displayed[0] with and without zero.
#Functions completed on or after 21aug.
#ask_nodule_close
#When image name to display is obtained from function get_image_name_to_display, then it is checked that whether 
#the last mouse event was mousePress, but there will always be mouse release after the mouse press. This means 
#that the functions which display image must get complete before the mouse release event fires.   

#https://doc.qt.io/qt-5/qevent.html
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

#The current implentation is displaying the second nodule when selected from the menu bar. But the issue is that what if we have already saved the annotation for another image for nodule 0 and 
#we want to modify that because actually, we want to save nodule 1. In that case, we first need to display the nodule indices saved. I can also do it like, if the user has already selected and saved some annotation for a
#particular nodule, then the user should be given the option the modify the particular nodule, but the user should not be able to select the same nodule again for marking.
#Also, I am prefetching the charateristics for the same nodule. Therefore, I am already putting a restriction that all the images for a particular patient are in a single directory. And that directory does not contain images 
#for any other patient.
#Further an option can be added that the user can select the patient folder first. After that the images from the folder will listed to the user. The user can select the image and nodule then the particular thing will 
#be shown. Actually, I want to extend the tool for the case when there are multiple nodules even within the same image.
#Now, it is clear that I will have separate menus foe image files and menus.
#I can possibly have nodules inside images. But that is not the way, Instead, I have to make it such a way that I should be able to switch between nodules and images.
#also, there can be multiple nodules within the same image. Therefore, if the user is able to see it visually the set 1 and 2, where set 1 has file names(only file names) and set 2 has nodules that have already been 
#marked and the lines between the imaes and nodules for the nodules that have been marked for that image.
#Further, this can be extended to open the image just by clicking on an image in the set 1.
#The mouse scroll over set1 will also be useful.


#The implementation will be quite simple. I need to add a button select folder.
#In the code, I will get the names of all the files and sizes of all the files in the folder.
#I can also read the dicom headers of those files to identify, which of these are videos and which are videos and which are images. Although the loading of dicom bideo currently takes some time. But that is fine if 
#we are doing it once and saving the read dicom header info in some csv file written by our software.
#currently, the software is not for videos, therefore, I do not need to read the dicom header for all. Currently, I can list all the dcm files or all the files in that folder. the file may or may not have a dcm extension.
#In order to save space, I can take the help of menus. The top level menu will have file name 
#for file size above 4mb, I can straight away put them in video. 

#The images in a folder may also correspond to axial or sagital. Therefore, as the marking proceeds, the display should also show that which image has been put in which category. Also, whenever I opens an image, I 
#should be able to mark that whether it is axial or sagital.

#How will I construct such a disply for images and nodules.
#When hovered over a nodule, the display should highlight the edges for that nodule and similarly for the image as well.
#Here comes the need for custom image, where the x and y for all the components are stored.
#Earlier the plotting has been done, over the image matrix that has been loaded.
#Now also, we can do the same thing.
#We can start with an image matrix that is all white. 
#We will store the x, y and width, height of every box for nodules and image names.
#The current available width is sufficient.
#The annotation height was 28. In a height of 420, 15 such contigous chunks can be there.   
#currently, 14 rows are there. Therefore, 15 contigous can be placed.
#If we use a gap of 14 then total is 42 for one. Therefore 10 such boxes can be placed in this size of 420. 
#Start working with this.  
#just start the image creation and display some boxes over that image.
#creating buttons may chage alignment periodically. Therefore, I will  write text in the qlabel.
#And do write the text using cv2 itslef. The box coordinates of that text will be saved somewhere.
#Even a right arrow(v shaped) may also be displayed for the images for which the annotation has been done.
#just hovering can hightlight the edges. But selection of image and nodule should open up the image.
#The still unmarked image can be opened by just one click over the image. Double click of an image will open
#the earlier marked image with showing all the nodules.
#In this case, the annotations will not be shown. The markings can be removed from current view by 
#clear markings and a nodule can be added by some add nodule button that will be displayed.

#It was also asked that if deva sir/user later wants to visualize what has been annotated, then it should be possible via a user friendly approach as discussed above.

#Even, we can save this image as well.
#When loading a folder. all the images must be loaded and saved in memory initially.
#just like frame marked array, there should be some data structure, that saves the mapping from image to nodules.
#We can have a dict that given an image name, produces the nodule list marked for that image.
#This list can also be saved in some text format.

#Make changes to save the set image whenever a nodule is added to some image.

#The current version is displaying the base image for set dispplay as black. I don't understand why black image is being shown even when all the values are 1 for all the pixels. Still, the drawing of red line was shown correctly.
#Start plotting the required boxes. But wait first get all the files in a file and categorize them.

#Make play video forward and backward in one row and add button for getDirectory.

#8888888888888888888888888888
#Segregation of video and images is complete. Now, write code for boxes, graph and show them
#just like drawing a line from image to nodule, the right click over image file name should show the option to add a new nodule.
#Box class seems complete.
#The function till draw box is complete. Now do the appropriate calling.


#888888888888888888888888
#When displaying multiple nodules, only colour may not sufficient.
#We may need to display the id of the nodule in text format as well.
#We may display that inside the alpha boundary. More details will be 
#looked at later. 
#We can keep white colour for nodule 6. More colors like magenta, pink 
#etc will be decided later on.

#8888888888888888888888888888888888888888888888
#The mechanism of undraw is very simple. Redraw the objectto be deleted,
#but this time with the background color. 

#The mechanishm of highlighting can be implemented by the following 
#mechanism.
#1: Draw that object with more thickness.
#2: Amore optional step is to have outer boundary slightly lighter.
#3: unhighlight
#4: undraw that object.
#5: redraw the object with original param.
#--------------------
#Box Highlight
#A more simple mechanism to highlist is as follows(mainly for box):
#1: draw one more bounday, one inside and one outside.
#2: This boundary should be light in color.
#3: Unhighlight will be done by deleting this newer boundary.
#################################################################888888888888888888888888888888888888
#Edge Highlight
#The highlight of edges can be dne as follows:
#1: draw 3 edges. the same edge should be drawn in a different color.
#2: Two new surrounding edges can be drawn as the original edge color.
#3: This way all the overlapping edge conflicts can be resolved without  
#   affecting the other edges intensity.
#4: Unhighlight can be undo by clearing all the things drawn and then
#   redrawing the original edge.
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Purpose edge highlight
#When user selects an edge, then it should be thick enough to  get selected
#and show user the connecting edges after resolving conflicts from overlapping edges.

#Keep edge coordinates and corresponding boxes separately.
#The Edges are required to redrawn, deleted etc.
#
# *********************************************
#First of all implement that clicking on an image box will open up that
#image.
#Also, the cuurently add the nodule via add nodule button itself.
#The add edge function needs to be completed as well.
#*******************************************************
#***********************************************8888888888888888888888888
#888888888888888888888888888888888888888888888888888888888888
#check from new functions added that all the new variables used are properly reinitialized in the 
#reinitialize function.
#Todo: Improvements later
#The font can be improved later.

# 
#88888888888888888888888888888888888888888888888888888888888888
#Currently, the nodule thing is tightly coupled with dicom annotator.
#Therefore, creation of nodule manager can be done later on.   
#If some extra variables are required, then they can be set in nodule class. 
#Otherwise having just a global ariable for whether window shown. one for each axial and sagital will be 
#sufficient. 
#The deletion of nodule is already there in delete_selected_nodule function.
#Now I just need to see how to update the add, delete nodule function wrt the current requirement.
#Creation of nodules initially is exactly the nodule pool creation.
#I just need to add the list that has the nodules added. We can remove by element from this list. 
#first chk the removal. checked by dummy list. 
#now working with a default set of 10 nodules. This can increased later.
#It would have been further better if the background would have been the white and the nodule box is 
#displayed int the color in which that nodule is being marked.
#When having boxes for nodules, the action buttons should be obsolete, therefore we should now delete the code 
#for action buttons. The display of annotation window should be done from the button displayed in graph.
#esc button can be used to hide all the annotation window shown.
#
#The filled box is touching the eyes too much. instead, just use the box boundary color for the case of nodules.
#Use the boundary color as white for images. use the boundary color as the nodule color for the nodule boxes.
#There may be some confusion in colors for the case of nodules. But, we can INCREASE THE WIDTH OF THE BOXES SO 
#as to make that color slightly more prominent. Therefore, Im now settig the default thickness as 4.
#now the default background color for set image has been set as black. This needs to be checked on windows as 
#well.

#First complete the add nodule and delete nodule. Do everything after that.
#aDD THE Global variable for showing annotation window in this process.
#The global pos is different than the position returned by mouse press. hence do not register the custom context menu 
#and show the menu popup while event handling.
#Todo: Most Important: 888888888888888888888888888888888888888888888888888888
#event.pos() and event.globalPos() are returning different values.
#event.pos() was used in drawing over image, where when we use event.global_pos, it displays the right 
#click menu more correctly. i.e. at this point the top left corner is at the
#point where the mouse is there.
#event.pos is more accurate wrt the placement ofthe contents inside the window.
#the event.globalpos might be including siome margin etc which were earlier used to decide window 
#boundaries.
#Anyway, use global pos to display menu and use pos to decide the relative position wrt to things which 
#is being displayed.
#Also, display the box coordinates when a box gets added. this way it will be easy to verify that 
#I am taking the correct position.
#aLSO, IT IS BETTER TO DISPLAY MENU ON MY OWN. i WILL HAVE A BETTER CONTROL THEN.
#Though testing of mouse clicked by clicking over all imag boxes has been done. 
#More thourough testing for empty region will be done later on.
#88888888888888888888888888888888888888888888
#showing all marked  nodules can be done on the image on screen. That will be done slightly later.
 
#Still, there are some issues in the code. the qlabel has some geometry set and the set_image has those parameters 
#as x_start etc. These things needs to be in sync.

#Whenever we add a nodule, we need to maintain the following things about annotation window:
#1: selection of annotation window from the pool.
#2: show and hide of annotation window.
#3: saving and clearing of annotation window.
#perform nodule selected was also responsible for creation of appropriate folders, clearing already loaded image 
#and settig other parameters.
#But now, things have changed. the appropriate folders should be redefined.
#the image might already be loaded with nodules and may be required to be clean as per the user requirement.

#clicking on image box should show the image clean.
#Right click on image box should also have following options:
#0: show image only
#1: show image with all nodules marked(show all nodules) or (show image with nodules)
#2: add nodule with previously marked nodules.
#3: add nodule over fresh image.
#The shown image name and the shown nodule names should be highlighted.

#The annotation window should now overlap the upper portion. 

#888888888888888888888888888888888
#Right click of nodulle box an have following options:
#1: show annotation marked.
#2: delete nodule.

#drag an edge from img to nodule must be there. the edge start and end for drag should have start in 
#some img box and end in some other img box.

#first of all complete the task that clicking on an image will show that image.
#The list of features that needs to be implemented:
#1: QSplashScreen
#2: nodule delete(from csv as well). 
#**************************************************
#issues to resolve
#The problem with garima dhupper is that the pixel array has only 2 dimensions.
#Hence, the input got classified as video and the code stuck.
#The current version is segregating based on file sizes. Hence, the code will not stuck for this condition. But,
#there is one more problem. There may be monochromatic videos. They may be small in size.
#We my classify them as immages by mistake and try to load them like images.
#tHERE ia a problem in saving monochromatic images.

#Also, even for the case of images classified correctly(due to small size) but now the image has 
#pixel array shape of dimension 2 i.e. pixel array shape is 768, 1024. In this case, how to modify the get_image
#For loading such images. 888888888888888888888888888888888888888888888
#Do the above case slightly later. First complete the tool for commonly occurring cases.
#Even some of the images shared by deva sir donot have complete metadata and the tool was not able to load them.
#chk those images as well. 888888888888888888888888888888888888888888888888888888888888

#The reason for not showing the images was just that the show_image was set to work only for the case when
#either image or video is opened. Now, that function should also be updated for the case when directory is
#opened. Also, the scaled image creation and the alpha creation should also be done as before.

#For the image; we shoud guess whether it is an image or a video.
#image type, whether number of frames is present can help.

#tHE INFORMATION about all images in a folder, whther monochoromatic/rgb etc should be loaded initially. And the image should also be loaded initially.
#Loading, saving and processing(also display) for monochomatic images should be taken care of.
#In case of monochromatic images, we may copy the same value to r, g and b.
#But, care needs to be taken care of while saving. The reason is that, we again need to save the image like monochromatic only.
#hence, we will be saving 2 channels, one is alpha and the other one is grayscale.

#88888888888888888888888
#To test garima dhupper, images from dinesh sir(mainly monochrome images, monochromatic video if possible.).
#The monochromatic video may have less size. Hence, check if the guess_dicom_type can be run fast even if videos 
#are present in the folder.
#A round about is that, for small files, anyways we are loading the dicom for all of them. Hence, we should
#guess dicom type for all small files. And if we find that a small file is a monochromatic video, then we can 
#move that file to the list of videos. This should be done before creating any dict for images.

#88888888888888888888888888888888888888888888888
#at last look at the comments in guess_dicom_type
#Links for image type
#https://www.kaggle.com/code/dskagglemt/basic-understanding-on-dicom-convert-to-numpy
#https://pydicom.github.io/pydicom/stable/reference/generated/pydicom.pixel_data_handlers.apply_voi_lut.html
#https://dicom.innolitics.com/ciods/digital-intra-oral-x-ray-image/dx-image/00283010/00283002
#https://dicom.innolitics.com/ciods/ct-image/voi-lut/00281056
#https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.11.2.html
#https://www.leadtools.com/help/sdk/dicom/api/dicomvoilutattribs.html
#https://dicom.nema.org/dicom/2013/output/chtml/part05/chapter_8.html#:~:text=The%20size%20of%20the%20Pixel,Allocated%20(0028%2C0100).
#https://dicom.innolitics.com/ciods/rt-dose/image-pixel/00280102
#https://www.leadtools.com/sdk/medical/dicom-spec17
#https://pydicom.github.io/pydicom/stable/guides/glossary.html
#https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.3.html#sect_C.7.6.3.1.2
#https://dicom.innolitics.com/ciods/rt-dose/image-pixel/00280004
#https://www.medicalconnections.co.uk/kb/Photometric-Interpretations
#https://pydicom.github.io/pydicom/2.1/reference/generated/pydicom.pixel_data_handlers.convert_color_space.html
#https://pydicom.github.io/pydicom/stable/old/working_with_pixel_data.html
#https://pydicom.github.io/pydicom/stable/old/image_data_handlers.html

#mouse click is a combination of press and release.
#Therefore, some parameter should be set on press and that parameter 
#complete at least add nodule completely today.
#left click over image box can be done later.
#firstcomplete the right click options.
#By the end of 29 may, the addition of nodules should be complete in all respects, whether left over image box,
#drag a line from image box to nodule box etc.
#The initialization for paths etc should also have been done appropriately.
#

#The image box should box be highlighted which tells currently which imahge is being shown.
#highlight done.
#display of dicom obj after loading should be stopped
#
#Deletion: For deletion, it is thought that some circular list can be maintained so that we can renumber the 
#nodules displayed and appropriately display the nodules and also have the colors not running out of order
#for the new nodules added.
#This may also prevent reassigning the annotation windows.
#A mapping may also be maintained that maps the number displayed(and also saved) with the number in the nodule 
#dict
#aND ACTUALLY, A DELETE IS JUST the change in this mapping. The annotation window will not get affected.
#The only thing that remains is the deletion of the annotation from the csv file.
#The corresponding also needs to be deleted and a renaming of folders is also required.
#The renaming of folders is a task prone to errors. The addition of nodules may take place upto nodule 10
#and then nodule 0 may get deleted.
#Therefore, renaming of folders for nodules from 1 to 9 for all images(may be 4) will be required. Therefore,
#renaming of 36 folders will be required in the easiest case. it may go upto 90.
#the renaming task may get stopped in between due to program closure(may be due to power crash or due to 
#software crash(force close manually.). In such a case, the annotations that have been marked will be in 
#inconsistent state.
#Currently, the creation of nodule wise folder will make the data set inconsistent with the earlier lots received.
#There has to be an alternative of folder renaming.
#An easy way to circumvent folder renaming is to store a mapping from nodule name shown and the folder name 
#present. we can allow the folder name as it was created originally, and we can store the mapping 
#This storage of mapping can be in both human readable as well as binary format.
#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
#Most important: if dict x was mapped to y. then y got deleted and later x got mapped to display index z, then
#it is important that if x was written in saved file name then it gets interpreted correctly. 
#if x does not get mapped to anything and annotation for the directory gets complete then having x in filename does 
#not make any sense. 
#Any way the dict index are written in filenames, just chk this again. And whenever a dict index gets deleted, then 
#we are deleting that nodule. hence the alpha of that nodule must get deleted. hence, we can simply delete the 
#folder(and hence the alpha file) for that dict index. Since we are anyways rewriting the dict index to display index 
#mapping. hence, no other file must be changed or renamed. 
#Q: Is this mapping same as that of mapping that maps numbers shown to the indices in the nodule dict.
#Ans: yes, it should be.
#Explain in detail about the mapping.
#Let add nodule 0 to 5. Therefore, the initial mapping will be identity mapping. When we delete nodule 1.
#then mapping will be 
#index display  - index in dict
#       0       -    0
#       1       -    2
#       2       -    3
#       3       -    4
#       4       -    5    --- relook for dict
#If we change the numbers displayed to the user, then the colors also needs to be changed appropriately.
#This mapping won't allow that.
#
#Let initially the situation was like
#
#initial dict numbers  -  number displayed  -  dict numbers required  -  index in dict  
#         0            -  0                 -  0                      -  0
#         1            -  1                 -  1                      -  1
#         2            -  2                 -  2                      -  2
#         3            -  3                 -  3                      -  3
#         4            -  4                 -  4                      -  4
#
#When nodule display index 1 gets deleted then situation will be like
#
#initial dict numbers  -  number displayed  -  dict numbers required  -  index in dict  
#         0            -  0                 -  0                      -  0
#         1            -  1(deleted)        -  1(none)                -  1(removed)
#         2            -  2                 -  2                      -  2
#         3            -  3                 -  3                      -  3
#         4            -  4                 -  4                      -  4
#
#Then the displayed indices 2 to 4 will be renamed to 1 to 3 for the display convinience of the user.
#Therefore the situation will be like
#
#initial dict numbers  -  number displayed  -  dict numbers required  -  index in dict  
#         0            -  0                 -  0                      -  0
#         1            -  none              -  (none)                 -  added to list of free indices
#         2            -  1                 -  2                      -  2
#         3            -  2                 -  3                      -  3
#         4            -  3                 -  4                      -  4
#
#Therefore, the following situation becomes. We can think later on why the dict numbers required are written as 
#1,2,3 in the following table.
#
#initial      - number displayed - dict numbers required  -  index in dict 
#dict numbers -                  - for file name by user  - (number actually 
#             _                  _                        _  written for file name)
#                                                   
#         0   -  0               -  0                     -  0
#(deleted)1   -  x(nothing)      -                        -  1(deleted)(file will
#             -                  -                        -   also be deleted.)
#         2            -  1                 -  1                      -  2
#         3            -  2                 -  2                      -  3
#         4            -  3                 -  3                      -  4
#
#I think we should pick colors from the numbers displayed to the user.
#The list of selected indices will still be required, as through them only, we know the available nodules to be 
#filled.
#
#after a first delete, we observe that number displayed is same as the 
#number required by the user(for dict), since that is the number the user is 
#expecting. Also, the initial dict numbers is same as the index in dict.
#The equality of "index in dict" and "initial dict numbers" indicates that a 
#remapping of dict indices is required because earlier dict index 2 was 
#displayed as index 2, but now the dict index 2 is displayed as index 1.
#Hence, after first delete, the mapping (number displayed) <==> (index in dict)
#should be updated to recover the number displayed from the number written in 
#file. We must delete the filename having 1 because that was the dict index 
#corresponding to the display index deleted. Hence this means that, that 
#dict index must get deleted which corresponds to the display index being 
#deleted.
#But after many delete, will the above approach still work.
#888888888888888888888888888 following
#Does the above approach will work in general for any number of delete.
#the following table is after 2 delete.
#
#initial dict numbers  -  number displayed  -  dict numbers required  -  index in dict  
#         0            -  0                 -  0                      -  0
#         1(deleted)   -  x(nothing)                                  -  1(deleted)
#         2            -  1                 -  1                      -  2
#         3(deleted)   -  x(nothing)        -                         -  3(deleted)
#         4            -  2                 -  2                      -  4

#In the above case as well, the number displayed is same as the number required. 
#The dictionary number deleted
#is same as the index in dict which has become useless. Also, the mapping of remaining(initial) dict numbers 
#to required dict numbers is same as the mapping from index in dict to number displayed.

#The above also needs to be tested for insertion case after delete. The insertion case further has following  
#subcases:
#1: new index is after the greatest index filled in dict.
#2: new index is the first index freed.
#new index is any one of index freed.

#Let us consider these cases one by one.
#Case 1: new index is after the greatest index filled in dict.

#present dict numbers  -  number displayed  -  dict numbers required  -  index in dict  
#         0            -  0                 -  0                      -  0
#         1(d)         -  x(n)                                        -  1(d)      
#         2            -  1                 -  1                      -  2
#         3(d)         -  x(n)              -                         -  3(d)      
#         4            -  2                 -  2                      -  4
#         5(i)         -  3                 -  3                      -  5(i) 

#Case 2: new index is the first index freed(but new number displayed acquired an already occupied index in nodule dict.).

#present dict numbers  -  number displayed  -  dict numbers required  -  index in dict  
#         0            -  0                 -  0                      -  0
#         1(d)         -  1(i)x(n)          -  1                      -  1(i)(d)      
#         2            -  2                 -  2                      -  2
#         4            -  3                 -  3                      -  4      

#new index is the first index added further have 2 cases. The first case is that, the new number displayed 
#gets assigned an already occupied index in the nodule dict. The second case is that, the new number displayed 
#acquires the earlier freed index in dict. 
#In the above example, we have covered the first case. We OBSERVE THAT the last nodule displayed earlier had the 
#last index in the nodule dict, the second last index displayed earlier had the second last index in the nodule
#dict. And still the last nodule displayed has the last index in nodule dict and the second last nodule displayed
#has the second last index in the nodule dict. The color picking is based on the (number displayed). Hence no 
#link of color displayed wth the index in nodule dict.
#But wrt user understanding there seems a conflict here. Earlier, after the deletion, the user was observing 
#3 nodules, 0, 1 and 2. Now the user has added one more nodule that is nodule 3. The annotation of nodule 0,1,2
#should be unchanged wrt the user. The user will add more details in nodule 3. but as in the above case, the 
#displayed number 2 earlier had an index in nodule dict as 4 but now the displayed number 2 has an index 2 in 
#the dictionary.
#Hence, the user view of annotation got changed. therefore, the only valid case that remains is that the new
#number displayed acquires the earlier freed index in dict. Construct an example for this case.

#Case 2: new index is the first index freed(new number displayed acquires the earlier freed index in dict).

#present dict numbers  -  number displayed  -  dict numbers required  -  index in dict  
#         0            -  0                 -  0                      -  0
#         1(deleted)   -  x(nothing)                                  -  1(deleted)
#         2            -  1                 -  1                      -  2
#         3(deleted)   -  x(nothing)        -                         -  3(deleted)
#         4            -  2                 -  2                      -  4
#         1            -  3                 -  3                      -  1(inserted)

#In the above example, we observe that the earlier numbers that were displayed, holds their reference in the
#nodule dict. hence the user view for the already present nodules does not change. Also, the new number displayed
#gets an index in the nodule dict which was already free. This free index need not be the first or the last 
#index, but this can be any free index in the nodule dict.
#We can try to generalize the idea as follows: 
#Whenever we delete a number displayed, then we clear the corresponding entry in the nodule dict and delete the 
#directory with that number. the correspondence of number displayed with the number in nodule dict does change,
#but in the following manner:
#The nodule numbers displayed after the deleted nodule gets shifted down and the index in dict does not change 
#position in the table. Therefore, the nodules gets annotation one after the deleted nodule and the same 
#behaviour was expected by the user.
#The 1,2,3,4 in the first delete operation table can be looked upon as general indices having no connection to 
#their known order. 

#During delete operation, the directory delete must be atomic and some bookeeping variable must also be there, 
#so that if THE PROGRAM RESTARTS LATER, it is easier to verify that whether the delete operation was complete,
#or some error in deleting directory and the delete should be tried now.

#From the above 3 examples, we can say that following equivalence hold
# present dict numbers == index in dict
# number displayed == dict numbers required
# 
#The reason for the above equivalence is as follows:
# The number displayed is the number user expectes for the directory. The number free in the nodule dict is a 
# number for which the corresponding directory also gets deleted. Therefore, whenever we assign an index in 
# nodule dict, we can assign the same number to the directory as well because a directory does not already exists 
# with that name. Hence, the mapping (number displayed) <==> (index in dict) is same as the mapping
# (dict numbers required) == (present dict numbers).
#There is one case remaining. When no delete occurs then the directory numbers must actually be same as the 
#numbers displayed. Having the nodule dict indices in a set will not ensure this. Also, when a nodule gets 
#deleted, and a new nodule gets assigned, it should not be that an already freed index is used if a newer index
#in nodule dict is available.
#Therefore, for the free nodule set indices, use a list, initialized with the nodule dict indices in the
#increasing order. Obtain a free index from the beginning of the list and append a freed index at the end of the 
#list. To remove confusion, maintain the allocated indices also in a list. Always add a new index allocated to 
#the end of the list.

#The above argument starting from first table completes the reasoning of how the mapping for insert and delete a 
#nodule will be performed. Now, I can start the addition of nodules.
#The deletion of entry from csv can be done by creating another csv without having the entry that needs to 
#deleted. This new csv file will replace the earlier csv file. Even if the csv is opened in read only mode 
#somewhere else, it does not matter.
#Treat the dicom annotator class itself as the nodule manager and pass appropriate variables to function calls 
#whenever required.
#now we cannot have color in the directory name as the name will be changed later on.
#But, we can still have color in the directory name as the case when no delete occurs will match with the 
#earlier case. Also, in case of delete, we will not look for color in the directory name, instead we will 
#just look at the number in the directory name.

#I may also encode in dicom the nodule index that is being displayed to the user. Therefore, the correct 
#information about nodule can be recovered. 
#The dicom that have already been saved, for them saving a number in dicom would mean that loading the dicom for 
#all nodules svaed, changing the number in them and resaving those. this is a daunting task. The saving of 
#mapping is a better alternative.
#
#
#Before starting renaming of folders, it should be ensured that the operation should not be terminated in 
#between and we have a backup copy of folders before folder renaming so that if the operation gets terminated in 
#between then we can have original folders without an inconsistent state. 

#along with list of allocated indices in nodule dict, we should also maintain a list of available indices in 
#nodule dict. This way it will be easier to allocate new index in the nodule dict. The array(for list) will not 
#be allocated too often. Hence, no such big issues. But still delete will require shifting all elements because 
#list has array implementation. Therefore, we may use set for allocated indices and free indices.

#Actually first clarify the strategy for delete in some time. And then complete both add and delete nodule.

#fully complete nodule addition today on 30 may
#now the nodule_dict_index is different than the displayed numbers. Therefore, the display of colors while marking and loading must be appropriately shpown.
#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
#displayed number also needs to be stored.

#nodule should have an option show annotation window. When option is selected then either the image is blanked or all the images marked with that nodule should be made visible.
#In this case, all the corresponding image names should be highlighted.
#When the mouse hovers over a particular image then the corresponding image should be further highlighted.


#There may be a provision of warning to the user that when nodule got added but either annotation is not saved or the image not saved.

#888888888888888888888888888888888888888888888888888888
#AXIAL OR SAGITAL is necessary otherwise all the images will be saved by default as axial.
#This is required as a part of add nodule.
#Having menu and submenu will complicate the process.
#There can be many nodules in an image but the image has to marked as axial or sagital only once.
#different types of clicks are hard to remember. Therefore, on right click have options mark axial or sagital.
#this mapping may also be saved separately.
#before adding a nodule, this marking is must. After this axial, sagital, the a or s will be visible in image name
#which will tell whether it is axial or sagital.
#The ordering that first marking as axial or sagital is necessary before adding nodules can be imposed by ordering
#the options in right click menu.
#Here a loop hole is there, an image that is first marked as axial and saved a nodule, the same image can be 
#later marked as sagital and saved another nodule.
#BUT WHENEVER AXIAL or sagital is marked, we must update the mapping for axial and sagital. This will allow us 
#to later change the image type even after marking the image nodule.
#888888888888888888888888888888888888888888888888
#whenever this mapping is updated a notification to the user will be send and it must be ensured that the same 
#image is opened up currently. If the same image is currently open and user is marking it as axial or sagital for 
#the first time, then it should be just a message display for a short period of time.
#If the same image is open but the user is changing the marked value then it should be a question.
#If a different image is open, then still it should be a question. on the yes of user, required image should
#be opened and the required marking(axial or sagital) should be done.
#JUNE3: COMPLETE 
#       1: ORIENTATION: AXIAL OR SAGITAL(including message boxes and appropriate image opening.).
#           pop up window/ qsplashwindow must be used to tell image swithcing occurred.
#       2: draw line for image box to nodule box for adding nodules.
#       3: try saving some nodules.
#       4: test if mapping of folders and mapping of orientation saved correctly.
#       5: 

#There is a problem in picking up the sagital view for the image whose AXIAL annotation has already been saved.
#There can be multiple axial and sagital images for the same patient.
#The only thing is that an image will remain axial irrespective of the number and indices of the nodules present 
#in the image.
#Also, if I am marking nodule1 in axial and nodule3 in sagital, then the annotation cannot be same.
#The reason is that annotation is nodule wise and not axial or sagital wise.
#Therefore, if I encounter another image, even if axial or sagital has not been marked, still, we can have  
#an edge drawn from the image to an exiting nodule and the corresponding annotation will be loaded.

#should complete add nodule in all respect by june6, i.e. today
#In the annotation window actual hide is still being called, this means that the other window code is still 
#working there. But, we may try splash window somehow and make that easier.88888888888888888888888888888888888
#the draw over dicom not working. chk.
#888888888888888888888888888888888888888888888888888888888888888888888888888
#the mouse position whether global pos or other what should be used should be rechecked wrt the postion used 
#displaying pop up window and and the x,y selected there wrt the window pos. 
#88888888888888888888888888888888888888888888888888888888888888888888888888
#display of clear marking over image must be must.
#Without adding a nodule, i was able to do marking.
#Therefore, whenever opeing an image, the nodule param must be reset and the annotation window must be made 
#invisible. currently other annotation window is not hidden and new window is not shown when changing file.
#now corrected.
#When adding nodule fresh, the other annotation seems hidden because a new annotation window is shown. 
#Currently save of marked image not working. Now corrected. the reason was that image open was not recognized 
#correctly. but still some errors are there. We must have a saved image for every image file in the directory
#that got loaded. see load_dir. yes, we do have a saved image in My_Image class. We must modify save_image 
#appropriately. we should get the saved image and frame path from the directory object.
#reloading a saved image is a must functionality for which the tool is build.

#A further enhancement is also possible here. 8888888888888888888888888888888888888888888888888888888888888
#If we try to move to another image or another nodule without saving the current annotation or current making, 
#then a question must be asked that the current aNNOTATION AND/OR MARKING HAS NOT BEEN SAVED. wOULD YOU LIKE TO
#save them. If the user selects nor then the nodule should be deleted only if one reference to the 
#nodule was there.
#If only the marking was not saved ,then the nodule will exist without any marking.
#If only the annotation is not saved then logically it is not possible to have a marking without an annotation.
#In this case, just tell the user that marking was saved but the annotation was not saved. 
#A question may be asked that plase recheck and save the annotation. The question is asked to prevent any 
#incorrect marking being saved.
#Therefore, whenever a changed to annotation even after save has been done, the question must be asked that the 
#annotation has ben changed after last save. please recheck and save the annotation.
#two boolean var are reqd for annotation:
#1: stateChanged.
#2: save performed.
#They should be checked when hiding an annotation window.
#Also, when rehiding(hiding an already hidden window), they must not be rechecked.  
#This enhancement must be tried at last, if difficult.
#It will be better, if we can add background color to annotation window. 


#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888
#the process of saving dict must also be more robust. First the new dict should be saved to some new file.
#After that, old dict must be renamed to a temp name. After that the new dict must be renamed to old dict name. 
#After that, the temp dict must be removed.

#8888888888888888888888888888888888888888888
#allowing nodules beyond 10 will require user to have a color chooser. Think and try this.
#Writing index for numbers inside the image will require to hide the important view of texture. this must be 
#thought about carefully.

#88888888888888888888888888888888888888888888888888888888888888
#mouse scrolling for image switch is remaining.

#complete the new features of nodule addition, deletion and set view, multiple image view by june7.
#The other small features, input image type, dinesh sir images and testing should get done during 10june to 14 june.

#I should also maintain a reference to the image which is currently being opened up. This is required to check
#that whether right click has been performed on a different image which is curently being opened up.

#888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
#
#The function markOrientationVariousPossibilities has the checking code whether the shown image is same as the 
#image over which right click has been done and the mark axial operation is required.
#But the question of checking whether displayed image is same as image over which right click is done for adding 
#nodule or the the image box from which an edge is dragged to a nodule box, so that we can check that the initial
#click is over the right box.
#In case of edge drag from image box, the drag will be paused and the question box will get opened.
#first make that image checking wrt add nodule. Later for drag image, it can be updated.
#yes check file same can be constructed. do this.
#The function has been created. Now, apply it over addition of nodules.

#88888888888888888888888888888888888888888888888888888888
#The splash screen is not working now. The problem may be same as earlier when IT WAS OBSERVED THAT it must 
#be run in a separatethread. The calling window must be made free.
#This must be looked on 10 june.
#complete rest till 7 june.
#88888888888888888888888888888888888888888888888888888888888
#lAST TIME, I left the work at point where save frame has something tobe updated like frame path or so.
#Also, I should add the call to write dict in add nodule. i think that isdone already. yes.
#chk if all the dict are being written correctly?88888888888888888888888888888888888888888888888888888888
#wrting to csv_file_handle_video_marked_frames can be stopped for the case of directory opened.
#when we have a patient wise nodule dict written, then we must also have patient wise nodule annotation written.
#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

#saved image path
#--------------------------------------------------------------------------------------------------------------
#the saved image path in save_frame can be updated based on discussion with icgeb and after discussing with
#Dr. Deva.

#nodule keep track of.
#----------------------------------------------------------------------------------------------
#CURRENTLY, I must be working on the nodule which is either selected by right click or the nodule 
#selected through the image. Therefore, I must set the nodule index selected by right click as -1 when 
#the operation gets over. but, the nodule may remain highlighted even after the operation gets completed.
#Therefore, THE nodule index must not get be made -1.
#In any situtation, whenever an operation is oerformed on a nodule, whether it is add  nodule, highlight 
#nodule, ETC THE NODULE BOX WILL GET HIGHLIGHTED.
#The graph class is not keeping track of which nodule is highlighted.
#The dicom annotator is acting as nodule manager. This class has nodule dict index and the nodule index
#selected by right click.
#In the function show_context_menu the variable self.selected_nodule_index_in_dict_by_right_click is updated but
#The variable nodule_dict_index is not updated. In the function function addNoduleFresh, only the 
#variable nodule_dict is updated and not selected_nodule_index_in_dict_by_right_click. This may result in 
#inconsistency in operations further down the path. Therefore, keep only nodule_dict_index for any
#nodule operations. keep the variable selected_nodule_index_in_dict_by_right_click just to chk that whether the
#requested nodule can be cariied out and update to nodule_dict can be done. The variable 
#selected_nodule_index_in_dict_by_right_click can be in an inconsistent state later on.        
#8888888888888888888888888888888888888888888888888888888888888888888888
#chk that above argument implemented correctly.
#don't write the central file for nodule marking, it will just add confusion.
#This is for the case of directory marking for images only.


#Reordering of nodules is an add on feature

#@presentation, show version with video, 
#show version with image only and nodule drop down
#show current version with map and all.
#making the app is easy, showing the source code can also be shown.

#Add nodule fresh was repreating numbers. just check again.
#no, it was not the case. But, when number of images is more, the edge crosses other image boxes and
#when other image box gets highlighted, it may seem that the image originated from that box.
#In some cases, without even highlighting that box, it may seem that image originated from that box. 
#Actually, the drawn edge line got erased partially by an highlighted box. Also, the image line does not 
#seem to be originating from the point where it was supposed to be. Also, the same color of boxes and same color 
#of edges is putting a problem. 
#improvement in drawing edges 88888888888888888888888888888888888888888888888888888888888888888888888888888
#1: Therefore, draw edges with the color same as the nodule color.
#2: After any update in set image, redraw all the edges, so that edge does not get erased/overlapped by any other 
    #object in the image.

#comments edge draw
#The edge line width cannot be increased othersise the edge will seem to be merged and new color will getcreated that is possiblythe color for other nodule.
#Add nodule to second last and third last for farishta and see.
#The edge for second last for farishtaseems still hard to be recognized. just check again.


######################################################################################################
###############     adding multiple nodules and saving maintaining their alpha channel.     ##############
###############################################################################################################
#When I was adding a nodule, to the same image, it was add nodule fresh. The earlier marking did not disappear. 
#correct this. 88888888888888888888888888888888888888888888888888888888888888888888888888888
#The saving of image when the previous marking was not cleared, then the saved alpha may have marking for 
#both the nodules. This must be corrected as when multiple nodules are shown, then we should not be saving the 
#already marked nodules in the current marked nodule. It will be better if we have an array of alpha channels. 
#We could pick the color based on the number displayed. Can we do this for the case of index in alpha array
#as well.
#If we keep the index of alpha array in sync with the index in nodule dict, then it will be more appropriate.
#The reason is that nodule dict is in more sync with the nodule add or delete.
#In fact, for every nodule, we can have an alpha channel and SCALED IMAGE. The reason for error earlier was 
#precisely this. the scaled image and the alpha channel were not created when the add nodule was performed.
#When having alpha and scaled image, for each channel, We can prcoeed as follows:
#1: in the show image, draw lines and save image, get the appropriate alpha. self.variable will not work now.
#2: When drawing the marking, the correspondig alpha channel may be used to draw the line.
#3: We already have image and saved image for every input image file. The scaled image should also be there
#   for every input image file.
#4: The alpha channel should be for every edge drawn i.e. for every image, for all the nodules it is connected to.
#5: Similar to images loaded in the memory, these alpha channels can be loaded and stored in memory.
#6: The saving of annotation needs to be improved. 88888888888888888888888888888888888888 don't use
#   set_input_filename. see comments in that function.
#7: For the case of image as well, we need to keep track of the image name which is currently being operated 
#   upon.
#   a: The variable image_names_displayed can be used to identify the image being operated upon.
#   b: When multiple images are displayed, then multiple images will be highlighted.
#   c: The images which will be displayed in small will be highlighted less.
#   d: Therefore, currently assuming that zeroth entry in the image_names_displayed is the largest image 
#      being shown. 
#8: In add nodule fresh, we have to update the thing so that correct image and alpha are displayed and are in use.#9: For the image as well, draw in the image for that image_name.
#10: after saving the marking, reinitialize the image for that image_name_ with a saved copy.
#    The reason is that we may need to draw another marking for some other nodule.
#11: Only image was reinitialized and not alpha. therefore, new marking over image were added to the previous 
#    markings.
#12: Also, when marking immediately gets disappeared, it makes a feeling whether anything wrong was saved.
#13: The image should be reinitialized when one of the following happens:
#    a: the image gets removed from display.
#    b: it is requested to add nodule fresh over the image when the earlier nodule has been marked over the same 
#       image.
#    c: I am not interested in clearing the alpha channel because at current stage the alpha is in sync with what 
#       has been saved.
#    d: When an image and nodule is highlighted then the  corresponding image and alpha should be displayed.
#    e: We already maintain name of the image which is being shown. Whenever changing the value of image being 
#       shown, we can clear the earlier image shown. 
#    f: Instead of drawing of the image object in loaded images, whenever we show an image, we make a copy of the #       image, draw on that copy and reject the copy when add nodule fresh is done or the image is changed.
#       i) Is there any harm in doing in this manner?
#      ii) The only thing I was worried about the case when add nodule with earlier nodules is performed. 
#          In that case, the drawn image will be having the alpha channels drawn for all nodules added till now. 
#          The current marking will be performed over that image and only the current marking has to be saved.
#          A short answer to this question is that the image with the drawing is the temporary image. Since, 
#          we saved the marking information in the alpha channel, therefore, we need not save that in images. 
#          Also, whenever we do new marking, we perform it in the specified alpha channel. Therefore, even if 
#          something extra has already been drawn over the image(other alpha), it does affect the marking, 
#          because the required alpha does not have that. Therefore, the easiest thing is to make a copy of the 
#          image whenever display is required. What was done in the case of video. Actually, no copy was made in 
#          the case of video. And whenever loading an annotated frame, the original image from first 3 channels 
#          and alpha from last channel was read. 
#     iii) now in showImageOnly(done), displaying function (show_image_directory)(done), save function(NA), 
#          plot function(done) and any other function which requires display of images with or without nodules, 
#          including the function that displays earlier marked nodules or loading partially annotated directory,
#           we should be using the self.image. Also, the scaled array must be created from the scaled array.
#               a) self.image is for display only, i.e. what is visible if alpha is superimposed over rgb in the 
#                  specified colors. The self.image is not used in the save function.
#               b) The main reason for creating image and scaled image inside every image object was just to 
#                  handle the case when multiple images got displayed.
#                      1)In that case, I can create self.image as the concat from multiple images. 
#               c) Mainly plot related function will be working with self.image.

#      iv) Though we can still keep the alpha separately for every nodule and image.
#       v) When we save a nodule marking, we donot expect the marking to immediately go away. Till we perform any
#          other operation, the image and the nodule are still highlighted. Therefore, the marking must still 
#          remain visible. The idea is that the image shown must get reinitialized if some valid operation takes 
#          place. 
#      vi) The combination of self.image and nodule wise alpha should be handled carefully.
#
#14: Now the independent/different nodules are marked correctly. 
#15: Now, do save the annotation in each patient directory.
#    i) Whenever a nodule gets deleted, the annotation which was earlier for nodule 2 will become the 
#       annotation for nodule 1(according to display.
#   ii) This will require a huge amount of change in csv file. Instead, we can save a csv for each nodule 
#       separately with the filaname same as that of nodule dict index.
#  iii) A plain concat of these csv files will not be possible. But at the current stage, for faster 
#       implementation, it is fine.
#16: Also, complete the show hide annotation window.
#17: How will the nodule boxes move when a nodule gets deleted. 8888888888888888888888888888888888
#18: The image nodule dict etc also needs to be updated in class graph.
#19: First update the functions in graph class that depends on nodule deletion. done.  
#    Also add nodule dict reference to graph class. It has already been added. done.
#    ****************** update all the places where the selected nodule index by the mouse is used. Actually, 
#    it is the index in nodule dict.
#Currently working for the point that information should be shown that the window is already closed.
#Also, when hiding window for all nodules or nodules OTHER THAN SHOWN, we can check whther the nodule is already 
#shown. Actually, the dicom annotator is the nodule manager, hence, this has to be handled by dicom annotator. 
#20: currently work has been left at hideAnnotationWindow at line 3492.
#20.a: At some places: #selected_nodule_index_in_dict_by_right_click can be in an inconsistent state later on.
#           please chk.
#21: now the class graph has some getter etc for nodule dict. whenever a separate nodule manager is being tried 
#    to be created, this must be taken care of.
#    a) Instead now the dicom annotator reference is being passed to the graph class so that the function like 
#       show error etc from the dicom annotator can be called by the graph class as well.
#Instead of passing the dicom annotator reference to the annotation window, we can return a a value that will 
#tell that information needs to be showed. In fact the showing and hiding is handled by the nodule class itself. 
#but stil we can return a value by the hide_annotation_window function. The calling class i.e. dicom annotator that is nodule manager as well, will decide what to do when the window was previously shown or not.
#    b) Therefore, the getter etc of nodule dict will BE THERE in the dicom annotator class.  
#    c) Also, no other reference is required.
#    d) It should be further checked that which nodule index is returned by mouse press receiver.
#                   
#    e) Add nodule fresh should be further rechecked for correctness and completeness.
#******************************************** error
#The error was also there that 0 cannot be available and n0 box also got added. how is this possible?????????????
#They both seem to happen simultaneously.
#The error occurred after the box had been drawn. While drawing the line, I was trying to get the displayed index
#from the dict whereas the displayed index has till not benn aded to the dict. 
#A simple solution is to add the mapping to the dict a step before calling add_nodule of graph. Then all functions will be able to use the mapping. 
#For the functionality showing multiple images given nodule, to work, it is important that same nodule is
#added to multiple images. Hence, drag a line from an image box to a nodule is must. 
#The mouse drag even needs to be handled. And adding of edge from nodule to img is required.
#If the drag is successful, the annotation window will also get opened up.
#By having different variable for selected image/nodule by right click, it makes the thing easy to handle 
#for the case when left click happens.
#Also, decoupling of image_names_displayed/nodule_dict_index from the image names or the nodule indices selected 
#by right click makes it easy to have earlier value or junk value in selected node(image/nodule) by right click.
#
#The main role of right click IS TO SHOW POP UP MENU AND CARRY OUT THE SELECTED ACTION. 
#aND that is workable by the current solution. 
#But that will not work with the left click. In case of left click the first click on image will show up the
#original image, the second click over the nodule will show up the nodule(as proposed.) Even in case of drag,
#it is required that the earlier selcted name gets erased if later click is done in some empty space.
#Hence, the clearing of variables will be done in case of left click.
#888888888888888888888888888888888888           Currently leaving at show_all_images_given_nodule
#In fact showing of images for a nodule is also required for drawing a dragged line(just for observation).
#left_button_pressed_set_image

#Last: The reason for diminished color when loading is as follows:
#     When drawing the red line image afresh, we set red as 255 and other channel as 0.
#but when reloading the alpha, we just set the res as max of alpha and loaded image, but leave the other two 
#channels as it is.
#A possible solution is to make the other two channels as zero based whether alpha got selected for those pixel.
#How can this be done at matrix level?
#will statements like if (alpha>0)(green =0 ) work or (alpha>0)
#(a==0)*c can be done where a is the alpha channel and c is the channel to be cleared. 
#This should be seen what happens for the case when colors having values other than 255 are used.

#Things saved
#1: orientation
#2: img to nodule
#3: etc 


#######################################################################################################
# 88888888888888 888888888   Annotating single image/video  8888888888888888888888888
#######################################################################################################
#Currently update this code as if this code is used for dicrectory only. We can have separate dicom annotator class for single image or video and can call them appropriately. 

#######################################################################################################
# 8888888888888888888888888   unsaved marking warning is must.    88888888888888888888888888888
#######################################################################################################

#######################################################################################################
# 8888888888888888888888888   Displaying image by left click   88888888888888888888888888888
#######################################################################################################

            #88888888888888888888888888888888888
            #The below argument needs to be completed and implemented.
            #If the image has already been shown, then it does not make a sense to clear the image when click is 
            #done in empty space or not to show the nodule(by left click on a nodule when a left click has 
            #already been done on an image or an image is already shown. ) when the image is already shown. 
            #But, there is a catch here, it may be that the image has been shown by a right click and the
            #left click variable has some earlier image name, then what to do? 
            #A simple answer can be that look at the image name displayed. This will solve the problem of 
            #multiple images as well. But, it may happen that a nodule has been added just now and the 
            #marking of the nodule is still there and the nodule has already been highlighted.
            #Therefore, keeping a track of highlighted nodules/images seems to be a solution. But, still other 
            #cases may arise too. Hence showing of image by a left click may be postponed. But a drag will 
            #start only after an image has been shown. If we don't display the corresponding image before the 
            #drag starts then, it may happen that some other image is visible and we add nodule to some other 
            #image. Therefore, it not a harm to SHOW IMAGE ON LEFt click. Anyway, the problem of unsaved marking
            #or annotation was there even when we displayed images by right click.
            #88888888888888888888888888888888888
            #The below argument needs to be completed and implemented.
            #For showing the image, name selected by right click is used.
            #should I use same variable for selected by right click and left click.
            #When doing a left click, an image is being displayed a fresh, then it does not make sense to keep 
            #track of nodule or image selected by right click. Also, after performing a left click, another right
            #click may be performed. If that right click is over an image, then it is not necessary that we are 
            #going to display that image. 
            #hence, it seems better to have separate variables for left and right click. When displaying image 
            #through left click, we can clear the right click variables and when displaying image through right
            #click, we can clear the left click variables.
            #8888888888888888888888888888888888888888888888888888888888888888888
            #What to do when image selected by left click and a nodule selected by right click.
            #First of all clear right click variables and do the line drawing by drag and then think about this.
            #Also chk in show image that whether any of left and right click is non null and show that.
            #But, When right click will be done and image is asked to be displayed then it will be a confusion.
            #Actually keeping track of what kind of click(left or right) for last two clicks and 
            #the box clicked(image or nodule) for last 2 clicks may help.
            #actually, we can extend the right click menu to show the desired nodule number for an image. 
            #Therefore, the need of saving two clicks for showing an image and a nodule will not be there.
            #In fact the current version does not highlight(more width) the edges for the selected images and 
            #nodules. The highlighting of the edges also needs to be handled. 8888888888888888888888888888
            #The main issue in showing image is that it requires the image name selected by the user. The track 
            #of left or right click just for the current click can be done and there is no harm. Also, this can 
            #be easily extended for saving current and second last click. 
            #The current click will be different for set image and dicom image. The current click will be 
            #updated on every click. set left click as -1, right click as 1 and middle button as zero. 
            #when the mouse is not clicked over set image and instead mouse activity happened over another image
            #like the dicom image, then set click as 100.
            #There mouse move, mouse release and wheel event as well. The function to update the track for mouse 
            #action over which image and which mouse button was involved should be done for all of them.
            #Now the show image only function can use the current mouse info about press etc and decide which 
            #image name to use for showing. 888888888888888888888888888888888 do this.
            #The left press also need to decide that whether the correct image is being shown.
            #Also, the SEPaRATE HANDLERS FOR WHETHER the press was over image or the press was over nodule or 
            #the press was over empty region. 
            #We can skip the press over nodule and empty region.
            #The release over nodule is more important to draw a line from an image box to a nodule box.
            #888888888888888888888888888888888888888888
            #Ask for unsaved images or markings. it is must. 
            #see the point 21 etc above.
            #now implement mouse move 

#######################################################################################################
# 8888888888888888888888888  Scaled image plotLines 88888888888888888
#######################################################################################################
#The plotLines function may produce error when images are scaled in case when a directory is loaded.
#The plotLines function and image scaling needs to be looked again to correct this and run this correctly.

#######################################################################################################
# 8888888888888888888888888  Reloading a partially annotated directory 88888888888888888
#######################################################################################################
                # Chk how the variable initialization etc will work, how the data structures 
                #will be filled correctly etc.
                #when the user reloads a partially annotated folder.
                #8888888888888888888888888888888888888888

#Initially it was considered that whenever a user will add a nodule from that point onwards always at least one image
#will be open. This condition has been used in some checks. Now when reloading a directory, if none of the image
#is shown then it may falsify some of the chekcs and some error msg may get raised. 
#therefore, whenever we show the images we may save the shown images and nodules list in a file. therefore, whenever 
#reloading a directory, we may display the same set of images and nodules again. 
#Whenever make image to display is done then that image name can be written. but what to write in case of 
#multiple image display. make image to display is not callled then. Therefore, we can write at two instances,
#one at make_image_to_display and one at display multiple images. and this write will be an overwrite operation.
#Similarly for the case on nodules, there will be two write opertaions: one at perform_nodule_selected and one at 
#show multiple nodules. this will be an overwrite operation. 
#when none of the nodule is shown the perform nodule selected for -1 will be done and that will be written. 
#Do this savling and loading of disPLAYED PARAMETERS at last of perform_nodule_selected.

#We need to load the following files:
#map_orientation.txt
#map_folder.txt
#Image_to_nodule.txt
#I also need to load alpha npy files stored in the respective folders based on edges present.

#I also need to look at how to integrate this function.
#Whenever loading a directory as asked by user, call this function at the end


#pseudocode reload_partially_annotated
#1: load map_orientation.txt if present.
#2: load map_folder.txt if present.
#3: load Image_to_nodule.txt if present.
#4: get the list(lf) of folders present for frame file path (if any of them is present).
#5: chk non empty conditions.
#8: update display for orientation.
#6: if nodules present:
#6:     initialize nodule classes for nodules present.
#7:     update graph class for nodule and edge present.
#8:     load all alpha channels.
#8:     redraw graph.

#pseudocode: load map_folder
#1: fill number_displayed_to_index_in_nodule_dict by the table loaded from map_folder.txt

#pseudocode: 

#pseudocode: chk non empty conditions:
#1: if map_folder is non empty then:
#2:     lf must be non empty.
#3: else:
#4:     lf must be empty.
#5: if Image_to_nodule is non empty then:
#6:     lf must be non empty.
#7: else:
#8:     lf must be empty.   

#pseudocode: if nodules present
#1: if map_folder is non empty:
#2:     return nodules are present.
#3: else:
#4:     return no nodules are present.

#pseudocode: initialize nodule classes for nodules present.
#1: for all the nodule dict indices(ndi) in map_folder:
#2:     load annotation for ndi in the annotation class for this nodule.
#                "annotation_nodule_dict_index_"+str(self.nodule_index)+".csv" 
#3: set the save variables as saved because loading annotation will reset them.  

#pseudocode: update graph class for nodule and edge present
#1: initialize the nodule boxes with the nodules present.
#2: update the image boxes with orientation present.
#3: for all edges in table Image_to_nodule:
#4:     add the edge in img to nodule
#5:     add the edge in nodule to img

#pseudocode: initialize the nodule boxes with the nodules present
#1: for all nodule display index, nodule_dict_index(ndisi, ndi) in map_folder:
#2:     get nodule box coordinates for ndisi.
#3:     set these coordinates for ndi in ndodule_to_box.
#4:     set the text for box for ndi as ndisi.

#pseudocode: update the image boxes with orientation present
#1: for all the imagename, orientation in map_orientation:
#2:     update the image box for imagename for the orientation.


#updating the pseudocodes further wrt implementation

#pseudocode reload_partially_annotated
#1: load map_orientation.txt if present.
#2: load map_folder.txt if present.
#3: load Image_to_nodule.txt if present.
#4: get the list(lf) of folders present for frame file path (if any of them is present).
#5: chk non empty conditions.
#6: update display for orientation.
#7: if nodules present:
#8:     initialize nodule boxes in graph class.
#9:     initialize nodules for edges.
#9:     add edges nodule graph class
#10:    load annotation
#11:    load alpha.
#12:    set the save variables as saved because loading annotation will reset them.  
#13:    redraw graph.

#pseudocode: load map_orientation.txt
#1: if map_orientation.txt exists then:
#2:     load the tabble in this file to self.image_to_orientation

#pseudocode: load map_folder
#1: if map_folder.txt exists then:
#2:     fill number_displayed_to_index_in_nodule_dict by the table loaded from map_folder.txt

#pseudocode:load Image_to_nodule
#1: if Image_to_nodule.txt exists then:
#2:     load table in this file and keep it in table format

#pseudocode: chk non empty conditions:
#1: if map_folder is non empty then:
#2:     lf must be non empty.
#3: else:
#4:     lf must be empty.
#5: if Image_to_nodule is non empty then:
#6:     lf must be non empty.
#7: else:
#8:     lf must be empty.   

#pseudocode: if nodules present
#1: if map_folder is non empty:
#2:     return nodules are present.
#3: else:
#4:     return no nodules are present.

#pseudocode: initialize nodule boxes in graph class
#1: for all nodule display index, nodule_dict_index(ndisi, ndi) in map_folder:
#2:     get nodule box coordinates for ndisi.
#3:     set these coordinates for ndi in ndodule_to_box.
#4:     set the text for box for ndi as ndisi.
#in short: initialize the nodule boxes in graph class  with the nodules present.

#pseudocode: add edges nodule graph class
#1: For all the (image, nodule) edges in Image_to_nodule:
#2:     decide alpha shape.
#3:     add edge to nodule class.
#4:     add edge to graph class.

#pseudocode: load annotation.
#1: for all the nodule dict indices(ndi) in map_folder:
#2:     load annotation for ndi in the annotation class for this nodule.
#                "annotation_nodule_dict_index_"+str(self.nodule_index)+".csv" 
#3:     set the save variables as saved because loading annotation will reset them.(done in load function)


#pseudocode: update graph class for nodule edges present
#1: for all edges in table Image_to_nodule:
#2:     add the edge in img to nodule
#3:     add the edge in nodule to img

#pseudocode: initialize the nodule boxes with the nodules present

#pseudocode: update display for orientation
#1: for all the imagename, orientation in map_orientation:
#2:     update the image box for imagename for the orientation.

#look at add_img_nodule_connection in nodule class 

#loading partially annotated directory
#------------------------------------------------------------------------------------
#The role of frame marked array was mainly for the videos. In case of images, it was just
#0 for frame index and keeping a track of how may nodules marked for that frame.
#but for the case of directory opened, I am already keeping track of nodules marked 
#for each image. Hence frame_marked_array is not reqd for the case of directory.`
#The load annotated frame must also be modified appropriately for the case of loading single and 
#multiple images. For the case of loading partially annotated directory, we can load all the
#text files in that directory and fill appropriate data structures.

#######################################################################################################
# 8888888888888888888888888  clear image marking     88888888888888888888888888888
#######################################################################################################
#there may be multiple alpha / nodules for that image. but only the currently selected nodule marking needs 
#to be cleared.
#when multiple nodules are displayed and one nodule index is in self.nodule_dict_index, then that marking will 
#be cleared. check this again.

#The only thing that needs to be checked is that 
#the reinit is same as the alpha init even for scaled image
#The reinit takes the prev alpha shape to create the matrix of zeros. hence no size issue should come even for scaled image display and marking and reloading etc.
#1: reset the alpha channel for that image by zeros.
#2: if the alpha has been saved for this image and alpha then 
#3:     rewrite that alpha as all zeros. 
#4: display the image again by the procees of adding alpha to image..
#Now problem in showing already annoteated nodule because the marking gets ckleard.

#Note: if user closes this nodule without new marking, then ask him to do marking or delete the edge.


#######################################################################################################
# 8888888888888888888888888  delete edge     88888888888888888888888888888
#######################################################################################################
#wrapper/calling code, gui linking will also be done.
#1: remove edge from nodule class
#2: remove edge from graph class
#3: write the image to nodule mapping.
#4: delete the folder which has alpha marked for this nodule and image.
#5: if the nodule has no edges then:
#6:     delete nodule.
#7: set saved variable. 
#8: redraw graph.

#pseudocode: remove edge from nodule class
#1: perform clear image marking for that image and nodule.

#pseudocode: remove edge from graph class
#1: update the img to nodule and nodule to img mapping.


#remove_nodule
#remove_edges_img_nodule
#remove_nodule_from_img_to_nodul

#check def remove_image_connection

#######################################################################################################
# 8888888888888888888888888  Add nodule fresh comments     88888888888888888888888888888
#######################################################################################################

                #The nodule_dict_index is most necessary. It tells that in which file to store the annotation. 
                #It is also rquired to check whether the annotation has already been saved.
                #nodule_dict_index is updated only after the above opertions are complete.
                #actually the nodule_dict_index is nodule_dict_index.
                #use the right variable and do the appropriate renaming.
#FIRST updating all the dicts so that whenever any function requires them they are avaialable.
                #****************************8888888888888888888888888888888888888888888888888
                #update the code so that if program crashed in between adding a nodule, then the program can 
                #restart correctly.
                # Chk how the variable initialization etc will work, how the data structures 
                #will be filled correctly etc.
                #when the user reloads a partially annotated folder.
                #8888888888888888888888888888888888888888
                #Therefore, we must do some more important things up here.
                #1: update the mapping for display number and index in dict.
                #2: The displayed numbers should always range in 0 to len(added_nodule_indices)
                #3: In the above, the color should have been picked according to the number displayed and not wrt the
                #   free index.
                #4: Also pass the number to add_nodule in graph based on the displayed numbers and not wrt the free index.
                #5: Save the current state of mapping. This must be done on every nodule add and delete.
                #6: When the mapping has been saved then the folder must be created now only so that the system is not in 
                #   inconsistent state when closed without saving.
                #now mapping for number display and directory index has been saved.
                #the directory has also been created. 
                #currently a nodule has been added but it has not been added to the csv file, as per the earlier 
                #implementation.
                #the graph will only see the displayed numbers. no. the graph will actually see the nodule 
                #indices in the dict.
                #i am saving the ndule dict indices in theedges image to nodule and for keys in nodule dict.
                #hence passing nodule dict index over here. The text in the box will depend upon the number
                #displayed. Hence the dict index to number displayed mapping must get updated before this point.
                #the graph class will itself obtain the number displayed fordisplay purpose.
           ################################################################################################
           #Also, first reinitialize that window so as to remove any annotations marked earlier but deleted 
           #later on. The updation to dicts is also required because these dicts are used at other places.
           #8888888888888888888888888888888888888
           #write code to chk whether the annotation has already been saved. This is required for the case 
           #when the nodule gets assigned to more than one image.

  #create the folder to save the marked image.
  #actually the folder creation should happen during the sane stage.
  #We require a separate folder for each image and each image.
  #The problem of folder being existing and the annotation not being present in csv was there earlier. 
  #But now, this should be resolved.
  #Also, when the user sees that the nodule has been created at the screen, then that should be visible 
  #Todo: complete the following
  #seems completed
  #whenever adding another action, remember to close any previous windows, if they are opened.
  #This will help, because the user mightnot close the previous windows. this is done.
  #Todo: complete the following:
  #I need to implement this function.  
  #1: update the color to be ploted. done by free_index and nodule_dict_index
  #2: create the folder in which the marked images will be placed. done
  #3: update this folder name to the class variable which will be used by the save function. done 
  #done
  #The earlier markings, if any over the current image, should be cleared. 
  #Else, when moving back and forth, the frames will be loaded only wrt the current nodule.
  #Todo: have separate framed_marked_array for each nodule.
  #self.perform_nodule_selected(self.nodule_dict_index)
  #since, I am adding a fresh nodule and assuming that correct image, with or without nodules has already 
  #been opened. Therefore, no update for frame is required at the current stage. now just marking by the user and saving is left. Now start testing adding fresh nodule.
  #888888888888888888888888888888axial and sagital connection needs to be looked at
  #axial, sagital button is also remaining.


#######################################################################################################
# 8888888888888888888888888  Remarking the previous colour 88888888888888888888888888888
#done test remains for function add_alpha_to_single_image
#######################################################################################################
#In some cases, at some pixels the image itself might have value greater than 127 but the channel has 
#value 127. then taking the max will give the earlier value and not the required value. this must be corrected.
#Also, when adding the color initially, the other channels were made zero or so. now that may be taken 
#care of so that reloading retains the color used for marking.
#We can get a mask of alpha channel as zero and non zero. that is already there. The alpha channel is zero or 255.
#having a greater than zero will give the mask array.
#When we have a zero in mask array, then the color matrix should not be changed for that position. 
#But when we have a 1(or true) in the mask array, then the value for the channel from color dict should be copied 
#to the image matrix at that position. Actually, the resultant matrix consists of 2 parts: 
# 1: the portion surrounding the marked portion: we can prepare a matrix with surrounding portion as it is and 
#    the marked portion as zero.
#    preparation for the matrix as above:
#       a: alpha is 255 for mark and 0 for non mark.
#       b: inverse alpha is 0 for mark and 255 for non mark.
#       c: get inverse alpha by 255-alpha.
#       d: do image and inverse alpha. how to do and?
#           i) we can do channelwise and.
#              will and work for values like 255? 
#               tHIS code from chatgpt to mask image
#               #copy the mask to 3 channels
#               #The mask contains 1 for the required portion of the image.
#               mask_3channel = cv2.merge([mask] * 3)
#               # Apply the mask to the image
#               masked_image = cv2.bitwise_and(image, mask_3channel)
#               masked_image is the required image.
#       e: using mask technique create an image with just the surroundings and not the alpha channel. 
#          Let this be S.
#           i) The inverse alpha should be used as mask.
#          ii) The masked image is the result.
#       f: using mask technique create an image with just the alpha channel and not the surroundings.
#           i) The alpha should be used as mask. 
#          ii) The masked image is the result. the steps are explained in 8 below.
#       g: Get the image for alpha channel with the required color from color dict. Let this be C.
#           i) Get the broadcasted matrix(same shape as image) for the required color. Let this be RA.
#          ii) Get the broadcasted matrix only for the alpha colored for the dict.
#              (.) alpha should be used as mask.
#              (.) mask RA by alpha. the masked image is the result.
#         iii) The result in 2 is the result.
#       h: Get the image to display as was ther at the time of marking:
#           i) Plain Add S in e with C in g.
#          ii) The result is the required image. 
#       


#
# 2: the marked portion: We can prepare a matrix with surrounding portion as zero and marked portion as required 
#    values.
#We can then add the matrices in 1 and 2.

#######################################################################################################
# 8888888888888888888888888  clear the prev marking done.  88888888888888888888888888888
#######################################################################################################
#The button for clearing prev marking(boundary of nodule) done, should be recoded for directory.

#######################################################################################################
# 8888888888888888888888888  Draw line FROM img to nodule   88888888888888888888888888888
#88888888888888888888888888  Mouse relese set image 888888888888888888888888888888888888
#######################################################################################################
#In one case, the prev marking did not get cleared when to the second image sagital was marked after 
#drawing the line and the line was drawn from img1 to n1. The orgder was i0 to n0, i0 to n1, i1 to n0 
#and then i1 to n1. The problem is that the edge drag function does not clear marking over image. it was the 
#show image that cleared marking over the image. 
#currently donot even think that drag line will be possible with multiple nodules visible. 
#888888888888888888888888888888888888 do later drag line with multiple nodules visible.

            #When we have a marking displayed already over the image, but we do not want to clear that,
            #otherwise the user would have selected add nodule fresh. But, if a nodule is already there, then 
            #during the release at some nodule, a check can be made that whether it is the already added nodule, 
            #or it is a new nodule going to be added. If it is a new nodule that is going to be added, then 
            #we may further check that whether a nodule is present already and whether the corresponding 
            #annotation window is currently being shown. Also check that that no other annotation window can be 
            #shown right now.
            #8888888888888888888888888888888888888888888888888888 complete the above at mouse release over nodule

            #It is important that the nodule to which line is drawn, has some annotation window and marking shown.
            #But we donot know beforehand, to which nodule the user will put the line.
            #Therefore, we may have a view of all annotated nodules till now(in small) and the selected image
            #(slightly bigger ), but still it will be a scaled version. After that, we may allow the user to mark
            #axial or sagital without changing the current view. The marking of axial, sagital must also be 
            #updated. The user can then do the appropriate nodule addition, but with the image being marked shown
            #in full. At that time, we can show the other images marked for this nodule as another window but in 
            #very small. But, the process of showing the other images in small can be done slightly later. We
            #can now focus on the case that the user can select the nodule to be added with or without other 
            #nodules being shown. And then only the marked image will get opened up. 
            #The display of all nodules will take time. that can be done after discussing with deva sir.
            #The draw of line as the current concept is(let it work first.). 

            #It is important to clear the image, redraw the current graph before the edge draw. the reason is 
            #that we want to clear any previous unwanted images.

            #when such a connection gets added, the mappings also needs to be updated. 

#It will be better if the error stack trace gets written to a file. chk log writing python 888888888888888888888
#redraw graph or add edge upon mouse release for set image. 8888888888888888888888888888888888888


#tHERE IS ERROR FOR EDGE EXIsT already. 8888888888888888888888888888888888888888888888888
#seems corrected. chk all premarked nodules are shown correctly along with their annotations and correct markings.
#chk all condtions of line drag are tested.
#line drag did not highlight the nodule box for an already existing edge.  todo. 88888888888888888888888888888888888
#Also, the correct earlier mark and 
#annotations needs to be rechecked. 
#when already a nodule is highlighted, the click on image redisplays the image but the nodule box still remains 
#highlighted. correct this.
#Actually, when an image is already shown then clicking on the same image box does not displays that image 
#again, whether or not single or multiple nodules are shown.
#Actually, in the earlier case, the series of clicks might have resulted in the click of show image only.
#When the show image only is called for the already displayed image along with a nodule being displayed, 
#the image gets displayed as a fresh but the nodule box still remains highlighted. This needs to be corrected.
#Actually, the hide annotation window was called for this case. The annotation window got hidden but the 
#the nodule box highlight was not done undo highlight.
#here actually, the concern is about three things: image(nodule marking  highlighted or not), 
#nodule box highlighting and the annotation window shown. And this concern remains same for the case when 
#linedrag is there. The reason is that, there as well we need to display nodule marking, show annotation window 
#and highlight the nodule box. The image thing is handled by the appropriate handler in the dicom annotator. 
#The same handler calls the hiding and display of appropriate annotation window. The left out thing is nodule box.
#Hence, the inconsistency appears. 
#Therefore, In fact hide annotation window should be:
#   1: linked with unhighlight of nodule box.
#       similarly show annotation window should be linked with highlight of nodule box.
#   2: called only inside perform_nodule_selected(other than display of multiple nodules).
#       As a precautionary measure, this should be accompanied with updation of nodule_dict_index only within 
#       the function perform_nodule_selected. A major hinderance for this is the functions that have been written 
#       for a single image or for video. 
#       I may as well delete those functions. But that will create code inconsistency because those functions 
#       have been called by other functions which are still useless and also those functions have been used by 
#       button actions. Then button actions will also have to be updated. Only a few button actions will need to
#       be updated. And, we can assign an empy function for those buttons right now. 
#       For every button click, we need to call a function. That function call may inherently call 
#       a function of the appropriate class. This is the idea currently. Todo that, we any way have to remove the 
#       unnecessary extra function calls. But that can be done later, after the directory version is complete
#       (i.e. delieverable). Therefore, first foucus on the functions that are referred to in the current error.
#       The requirement of calling those functions only at a specific place can be looked later on.
#       Also, the highlighting of the nodule must be linked with the nodule selection in the graph. The reason is
#       that, if we undo highlight all the nodules then it must not be the case that redraw graph rehighlights 
#       that nodule. 
#       An easy solution is that whenever undoing highlighting a nodule, if that nodule index is selected nodule 
#       index then the selected nodule index must be set as -1.
#       There is another problem in undo_highlight_nodule. The nodule must not be visible over image. This must 
#       be ensured. The hide annotation window is called in general at many places like add nodule fresh, 
#       show image only etc. Even the topmost calling function may not have anything related to display of image 
#       like add nodule fresh.
#       Even if the topmost calling function(in the above discussion) does not directly handle the showing of 
#       image, still that topmost function for hide annotation window must have been called by some handler like 
#       addNoduleFresh is called by a handler for option selector. This handler itself ensures the correct 
#       display of image before calling the top level function function which in turn calls the 
#       hideAnnotationWindow. Hence, the problem that undo selection of highlighted nodule index when the nodule 
#       index marking is visible in image will not be there by the flow of the code and not by a single function. 
#       It will be good if we can perform checking still as well. 
#       v.iMP POINT TO SOLVE. 
#       Is this the case that whenever a nodule index marking gets displayed(or all markings removed or image
#       gets opened afresh), the selected nodule index will be set correctly in the graph class.
#       Actually, the IMAGE MARKING DISPLAY/HIDE AND image opening afresh was handled by dicom annotator class.
#       When carrying out the required changes on image, the dicom annotator class calls THE INTERNAL FUNCTION
#       perform_nodule_selected to update which nodule got selected. 
#       This function perform nodule selected and does not update the show annotation window for the case of -1
#       as the nodule dict index. 
#       hence unselect in set graph may never get called. correct this.
#       88888888888888888888888888888888888888888888888888888888888888  
#       The function highlight_nodule_for_marking was not called by the function perform_nodule_selected.
#       The function highlight_nodule_for_marking was called only by add_edge_img_nodule.
#       As argured above, show annotation window should be linked with highlight_nodule_for_marking
#       and hide annotation window should unselect the nodule.
#       The reason of discussion here was just that the hide and show of annotation window may be called outside
#       perform_nodule_selected. We may 
#       
#       we already have nodule dict index as the variable in the dicom annotator class. This variable serves the 
#       purpose of storing nodule index which is being displayed. Hence, making the image display afresh by 
#       showImageOnly, this variable is cleared to -1. There is a separate list for nodule indices displayed 
#       when multiple nodules are made visible. tHEFLOW OF THE PROGRAM SHOULD BE SUCH THAT the nodule_dict_index
#       should not be there in the list of multiple nodules being displayed, so that we actually know that which 
#       nodule is being marked or none of the nodule is being marked and which nodules are shown that have been
#       marked previously.
#       The nodule_dict_index and list of multiple nodules being displayed together can serve the purpose of 
#       obtaining the nodule box indices to be highlighted and in what way the highlight should be done.
#       This combination will also tell which alpha needs to be present over the image and in which mode.
#       If two nodules are made visible with one previously marked and the other one currently being marked then
#       that list will have only one element for the previously marked.
#       Also, for the case of multiple 
#       nodules, the current strategy is to make all nodules not visible when moving to some other operation.
#       But it may also happen that mark nodule with previously marked nodules is called. In that case, first 
#       all the present nodules will be shown. After that, hide of annotation windows may(and should be) called 
#       for other nodules. In this case, we are hiding some annotation windows but still not removing all 
#       nodules from display. In this case , one more complication arise. It may be required to check that we 
#       donot accidentally close the annotation window or remove alpha of the nodule that needs to be shown. 
#       Even we will be closing the annotation windows for the displayed nodules in this case, but we donot 
#       want to remove the alpha for that image. Also we donot want to hide the boxes for those nodules.
#       Therefore, the logic: hide annotation window should be linked with unhighlight of nodule box
#       should not be implemented. Also, till now the hide annotation window is an idempotent function. i.e.
#       even if an annotation window was hidden earlier then rehiding the annotation window will not have any 
#       effect. But, now when multiple nodules are shown, rehiding the annotation window will unhighlight the 
#       nodule box(in case if unhighlight gets linked with hide annotation window.)
#       Hence, the highlight/unhighlight of boxes in set image should not be linked with show/hide of 
#       annotation window.
#       In fact, the dicom annotator class is currently acting as a nodule manager. This is the task of 
#       nodule manager to decide for which nodule annotation window to show and for which nodule the box
#       needs to be highlighted. Hence, the task of show/hide annotation window and highlight/unhighlight of 
#       nodule box should be handled by the dicom annotator class. 
#       iN ANY CASE( whether or not the nodule box is displayed highlighted depends upon the fact that whether
#       highlight is done later or unhighlight done later.) But for any nodule we will either highlight the box
#       or unhighlight the box. Therefore, this should not be a problem.
#       We can instead build a logic that whenever a nodule is displayed, its box will be highlighted 
#       whether less highlighted or more highlighted. But still, the thing is that dicom annotator is the nodule 
#       manager. Hence, the calling function(i.e. in dicom annotator) has to decide 
#       that for a nodule whose annotation window is being hidden, whether the unhighlight and alpha removal 
#       needs to be done. And also the calling function knows that which nodule alpha is visible over screen.
#       do above 888888888888888888888888888888888888888888888888888888888.
#       The only case when box highlight info required by the graph class is when redraw graph is done. 
#       But we have dicom annotator reference inside the graph class. Therefore the graph class can know which 
#       and how to highlight the boxes. do this 8888888888888888888888888888888888888888888888888888888
#       Now the graph class itself has dicom annotator reference. And the image names to highlight and the 
#       nodule indices to highlight information is already there in the dicom annotator class. Hence, the graph 
#       class can use this information from there as well. 
#       Hence the highlight and undo highlight functions must consult the variables In the dicom annotator 
#       which tells which image names or nodule names to be highlighted.
#       If this could have been done that whenever the variables for highlight or undo highlight are done in the 
#       dicom annotator, at that time itself the corresponding highlight or undo highlight functions are 
#       called in the graph class, this is the best poosible way to implement. Also, the case when rehighlight 
#       needs to be done in graph class then the variables in the class dicomannotator may be consulted.
#       Also, the highlighting of box and addition of alpha to the image needs to be clubbed somehow.
#       Hence, it is necessary to have setter and getter for the nodule_dict_index and the 
#       image_names_currently_displayed and self.nodule_dict_indices_shown_extra.
#       
#       Way to implement the above things:
#       1: we have show annotation window and hide annotation window functions in the dicom annotator class.
#          Any call to show or hide or even for multiple show and hide should pass through these.
#       2: The perform nodule selected should BE a central function to be called of selecting a single nodule.
#          This function should handle display of annotation window, highlight of box and addition of alpha to 
#          image if the alpha has already been created.
#          a: The calling function will tell that whether alpha has already been created.
#       3: There should be another function show prev nodules and mark new nodule.
#          This function will show prev nodules 
#
#
#Tasks to consider: 
#   1: updation of nodule_dict_index only within perform_nodule_selected.
#   2: #It will be better if the error stack trace gets written to a file. chk log writing python 8888888888888        
#       redraw graph or add edge upon mouse release for set image. 8888888888888888888888888888888888888
#Done things:
#   1: The function make_image_to_display actually displays the image. This function may be called at other 
#      places as well. Therefore it seems better and more correct to update the 
#      self.image_names_currently_displayed in this function. This function is also called by 
#      clear_image_markings. Since, the function clear_image_markings alreadytests that the same image name is 
#      displayed already hence there is no harm in resetting self.image_names_currently_displayed. done.
#   2: now the perform_nodule_selected can be used to unselect any nodule selected so far and also to 
#      hide the corresponding annotation window. It is the job of calling function to make sure that image is
#      shown appropriately with or without the desired nodule markings.
#   3: The function clear_image_markings inherently implies that no nodule must be selected. Hence, instead of 
#      calling make_image_to_display, WE MUST CALL show_image_functionality in clear_image_markings. Actually the 
#      clear image marking is just to lear the previous marking and to change the nodule. Because we may want to 
#      mark the same nodule differently. Hence make_image_to_display should be called inside clear_image_markings.
#      done

#######################################################################################################
# 8888888888888888888888888  Handling the drag to draw line 8888888888888888888888888888888888888888888888
#######################################################################################################
                #It may happen that the drag started in dicom image or somewhere else and the release event 
                #occurred in the set image. the seleted by left click may be actually the highlighted image, 
                #but we donot want to add edge in this case. When mouse moves out of the set image or other than
                #move event occurred(while in drag), then the drag_started variable must be set to false and the
                #graph must be redrawn with the previous highlights as it is. Therefore, also keep track of 
                #highlighted images or nodules. Also, look how to complete it for the case when the multiple
                #nodules or multiple images are shown.

                #There should be another variable partial line drawn. If this variable is true then the GRAPH 
                #MUST BE REDrawn with the previous highlights as it is, when the variable 
                #self.set_image_drag_started is set to false.
                #

                #both the event and eventfilfer are being called but somehow, the call to event is not displaying 
                #the directory. I should now not depend over the mouse move withourt mouse buuton press. 
                #ishould clear the line or add nodule over the mouse release event. 

                #https://doc.qt.io/qt-5/qevent.html

#######################################################################################################
# 88888888888888 888888888888888  Saving in memory nodule dict  8888888888888888888888888
#######################################################################################################
#When the alpha channel is stored per image, but for each image there can be multiple nodules marked and for 
#each nodule there has to be a separate alpha channel. Actually, a separate alpha dict has been created for each 
#nodule. tHEREFORE, having the image name as the key in the alpha dict automatically creats a separate alpha channel
#for EACH nodule and for each image.

#######################################################################################################
# 88888888888888 888888888888888  save_frame earlier code with comments  8888888888888888888888888
#######################################################################################################
#
#    def save_frame(self, image_name, alpha_to_save):
#        """
#        image_name is the name ofthe image to be saved. thisshould be absoulte for image or video opened.
#        for the case of directory chk the entry being written.
#        This function will save the frame from a video.
#        Returns
#        -------
#        None.
#
#        """
#        # if(self.dicom_obj_loaded_annotated !=None):
#        #even the dicom obj has to be obtained from the directory loaded.
#        if(self.image_opened or self.video_opened):
#            dicom_obj_to_save = deepcopy(self.dicom_obj)
#            frame_filepath = PurePath(self.dicom_frames_path[self.nodule_dict_index]).joinpath(\
#                    "frame_"+str(self.frameIndex)+"_marked.dcm")            
#        elif(self.directory_opened):
#            #get fre path from directory object.
#            #is there a way to confirm that nodule dict index is correct?
#            #I don't think so, because this is the base variable and every other thing is controlled by this 
#            #variable and this variable is chosen carefully.
#            dicom_obj_to_save = deepcopy(self.directory_loaded.get_dicom_object(image_name))
#            #For the case of directory with images we have just one frame, hence, it seems useless to 
#            #save the frame index. but for the case of sync with the earlier approach, currently keeping that.
#            #Later, before submitting I can change dir path and filename. 
#            frame_dir_path = self.directory_loaded.get_frame_file_path(image_name, self.nodule_dict_index)
#            frame_file_name = "frame_"+str(0)+"_marked.dcm"
#            frame_filepath = PurePath(frame_dir_path).joinpath(frame_file_name)
#            #The main role of writing this csv entry is to store which image contain which nodules and input output 
#            #filenames. The image orientation sagital or axial has been saved in the mapping.
#            #I am trying to make this code as much as possible the backward compatible. 
#            #For making this backward compatible, we may allow to store the image orientation but that will lead to 
#            #confusion if the orientation gets changed later on.
#            #The easiest solution is have a separate csv file for the case of directory opened and have only 
#            #meaningful fields. The string will get written to the appropriate csv file based on whether 
#            #image_opened or video opened or directory_opened_for_image.
#            #after removing unnecessary fields, i got to know, this is just image to nodule mapping.        
#            #The frame file path has the complete path including patient name. It would have been better if we 
#            #save the mapping in each directory as well.
#            #And for the central mapping, we have the 
#            #The following should be nodule display index.
#            nodule_index_displayed = self.get_displayed_nodule_index(self.nodule_dict_index)
#            #CURRENTLY, I must be working on the nodule which is either selected by right click or the nodule 
#            #selected through the image. Therefore, I must set the nodule index selected by right click as -1 when 
#            #the operation gets over. but, the nodule may remain highlighted even after the operation gets completed.
#            #Therefore, THE nodule index must not get be made -1.
#            In fact the nodule should remain highlighted even after saving is complete.
#            #In any situtation, whenever an operation is oerformed on a nodule, whether it is add  nodule, highlight 
#            #nodule, ETC THE NODULE BOX WILL GET HIGHLIGHTED.
#            #The graph class is not keeping track of which nodule is highlighted.
#            #The dicom annotator is acting as nodule manager. This class has nodule dict index and the nodule index
#            #selected by right click.
#            #In the function show_context_menu the variable self.selected_nodule_index_in_dict_by_right_click is updated but
#            #The variable nodule_dict_index is not updated. But, when any nodule operation is done, the
#            perform_nodule_selected is done which will update the nodule_dict_index.
#            In the function function addNoduleFresh, only the 
#            #variable nodule_dict is updated and not selected_nodule_index_in_dict_by_right_click. This may result in 
#            #inconsistency in operations further down the path. Therefore, keep only nodule_dict_index for any
#            #nodule operations. keep the variable selected_nodule_index_in_dict_by_right_click just to chk that whether the
#            #requested nodule can be cariied out and update to nodule_dict can be done. The variable 
#            #selected_nodule_index_in_dict_by_right_click can be in an inconsistent state later on.        
#            #8888888888888888888888888888888888888888888888888888888888888888888888
#            #chk that above argument implemented correctly.
#            #don't write the central file for nodule marking, it will just add confusion.
#            #This is for the case of directory marking for images only.
#        print("frame_filepath="+str(frame_filepath))
#        if(self.image_opened or self.video_opened):
#            str_to_write = image_name+", "+str(nodule_index_displayed)+", "+str(frame_filepath)+"\n"
#            self.csv_file_handle_video_marked_frames.write(str_to_write)
#            self.csv_file_handle_video_marked_frames.flush()
#            self.frame_marked_array[self.nodule_dict_index][self.frameIndex] = 1        
#            #str_for_bin = "frame_annotation\n"+str_to_write
#            #write_to_binary_file(binary_filehandle, convert_to_binary(str_for_bin))
#            #
#        #There should be an analog to the frame_marked_array for the case of directory. 
#        #The role of frame marked array was mainly for the videos. In case of images, it was just
#        #0 for frame index and keeping a track of how may nodules marked for that frame.
#        #but for the case of directory opened, I am already keeping track of nodules marked 
#        #for each image. Hence frame_marked_array is not reqd for the case of directory.`
#        #The load annotated frame must also be modified appropriately for the case of loading single and 
#        #multiple images. For the case of loading partially annotated directory, we can load all the
#        #text files in that directory and fill appropriate data structures.
#        #888888888888888888888888888888888888888888888888888888888888888888888
#
#        np.savetxt(alpha_to_save)
#        self.update_dicom_obj_and_save(dicom_obj_to_save, frame_filepath)            
#
#######################################################################################################
# 88888888888888 88888888888888888888888  calling actual window hide 88888888888888888888
#######################################################################################################
#when closing the window without hiding annotation window, the actual widow hide is shown but the window does not get hidden. chk whats the matter.

#######################################################################################################
# 888888888888888888888 hideAnnotationWindow comments 88888888888888888888
#######################################################################################################
#The select nodule index is index in nodule dict. 
#It should be checked that the current nodule selected by right click is actually the nodule highlighted. 
#When only one nodule is shown then nodule_dict_index is the nodule highlighted.
#Whether the window is actually shown.         ifo can be shown.
#
#When single or none nodule shown and hide is called, we just need to perform action when the mouse is 
#right clicked over the nodule Which corresponds to nodule dict index. Otherwise nothing needs to be done.
#
#What to do if currently multiple nodules are shown?
#In that case, if the annotation window for major highlighted nodule is shown then that window will get 
#hidden otherwise nothing else will be performed.
#
#When multiple nodules are only displayed and none beig marked, then a hide for an annotation 
#window of a nodule may be asked when annotation window of that nodule not shown already. This is 
#irrespective of the fact that annotation window of another nodule may be shown already.
#In this case, the hide may be simply ignored at present, or info can also be shown.
#
#In case of many nodules shown, if annotation window of a different nodule is shown then an info
#msg may be raised that window open for another nodule with that nodule display index. To carry out this 
#task, common function can be built for show and hide for the case of multiple nodules shown.
#The showing of information can be handed by showAnnotationWindow_gateway.
#Another easier option is to have no effect for hide annotation window of that nodule.
#show_information_only_marking_display is surely that function. but for hide one more case needs to be 
#covered. 

#pseudocode simple
#
#if nodule index asked by user same as nodule dict index maintained:
#   close the window.(The window may alreay be hidden. no matter as of now.).
#   function complete
#The above if is common for both one or many nodules shown.
#if one or none shown.
#   show msg nodule not displayed.
#otherwise if many shown:
#  if the nodule index not in list of extra nodules shown
#     show info nodule not displayed
#  otherwise
#     close the window.(The window may already be closed and some other window may be shown but at this time 
#       ignore that.)

#pseudocode partial to display all messages.
#if one or none shown.
#  if nodule index asked by user same as nodule dict index maintained:
#     close the window.(The window may alreay be hidden. no matter as of now.).
#  otherwise
#     show msg nodule not displayed.
#otherwise if many shown:
#   if none being marked:
#     if the nodule index not in 

#######################################################################################################
# 888888888888888888888 showAnnotationWindow newer comments 88888888888888888888
#######################################################################################################

#If multiple nodules are shown with a nodule being added afresh, then the nodule dict index will be 
#corresponding to the display nodule index added.
#If multiple nodules are shown, still we can drag a line to an already present nodule. If the nodule has 
#already been added to this image, then only that pair will be shown otherwise, we can start marking that 
#nodule boundary within the current image. 
#These cases are to be thought of just because the show and hide of annotation window can be called when 
#multiple nodules are shown. In such a case, the show and hide for the nodule being added should work 
#normally. But when only the nodules are shown and none of the nodule is being marked, the user may 
#choose to view annotation window of any of the nodule shown. In this case the nodule dict index is -1. 
#Also, when the user is marking a nodule with the prev nodules shown, then also a user may wish to show 
#the annotation window of a previusly marked nodule. 
#A simple viable solution is following:
#1: Have separate highlight colour and boundary values for the nodule whose annotation windw is being 
#   shown and for the nodule for which the boundary is being marked. Use yellow color after leaving some 
#   gap from box to highlight the nodule whose annotation window is being shown. This gap will be used to 
#   draw a white color boundary to highlight the nodule whose boundary is being marked. 
#   When the annotation window is shown for a nodule whose marking is being done, then both white and 
#   yellow boundary will be there. First the white boundary and then the yellow boundary.
#   We decided here 2 colors for nodules, one for showing marking and one for showing annotation window.
#   But there also exists one another case for a nodule that is the nodule is being marked. This can be 
#   taken into account by the red color box as mentioned below.
#
#   We can also write s for shown already marked, a for anntation window and m for marking being done.
#   These can be written in their respective boundaries. When red color is there, the annotation window
#   may be shown or hidden. Also, when marking is being done and red color highlight is there, the 
#   annotation window for any other nodule is not permitted to be shown.
#   As per the latest discussion, when the user is marking a nodule, the user will then focus on that 
#   nodule only. Hence, it is unlikely that at the time of marking and filling in annotation, the user 
#   will look at another window of any other nodule. but still if the user wants to look at the 
#   annotation window of any other nodule then there are two options, first is that the user leaves 
#   marking the current nodule in middle. This will require deleting the edge currently marked by the 
#   user. That will make the process a little complex. 
#   The second way would be to first open the image with all the nodules shown. During this process, 
#   the user can see the annotation window for any of the nodule he wants. After that the user can drag 
#   an edge or add a nodule fresh. Now the user will not have facility of viewing another annotation 
#   window till the marking and annotation of the nodule added gets saved.
#   After saving the things for the nodule added, the mode should switch to when multiple nodules are 
#   just shown along with the nodule added.
#   Also, if later there is requirement for viewing another nodule annotation window when marking a 
#   nodule, then the following steps may be helpful. 
#   Also, when the user want to show annotation window of any other nodule, then the yellow boundary will 
#   be removed from the nodule being marked and the yellow boundary will be drawn around(after leaving 
#   some gap) around the nodule box for which annotation window is requested by the user.
#   Therefore, there will be two types of nodule highlight. And also, the nodule highlight for yellow
#   will be called by show annotation window only, on the basis of nodule index requested by the user. 
#   Hence, there is a need of gateway for the show annotation window in the dicom annotator class, even 
#   if it is used at only two places. First complete the yellow highlight in the graph class. 
#   There needs to be a third type of highlight which is required to highlight the nodules which are 
#   marked earlier but shown now just to show the other nodules. This can be a red color box at the same 
#   place where the yellow color box is there. In this case, we need to make sure that either red or 
#   yellow box will be there but not both. complete the highlights and showannotation window at max by 
#   lunch 11 sep. This includes testing. The yellow box can be tested even for marking single nodule. The 
#   red box will have all the same dimensions as that of yellow box.
#
#   After all the above discussion, following can be said:
#   1: white boundary present: if the nodule marking is displayed.
#   2: yellow boundary present(around white boundary): if the annotation window for that nodule is shown.
#       Only in the case when nodules are only displayed and no nodule is being marked.
#   3: red boundary present(around white boundary): Only in the case when a nodule is being marked with 
#       or without the other nodules being shown.

#######################################################################################################
# 888888888888888888888 nodule_dict_index comments 88888888888888888888
#######################################################################################################
#Hence finally nodule_dict_index will be some valid value in 2 cases, 
#1: a nodule is being added.
#2: only one nodule being shown(and not marked).
#   a: There is an additional functionality that whenever a single nodule is displayed only, then the  
#      user has the ability to clear or redo marking or rewrite the annotations. 
#      Therefore, this case can be looked upon as nodule being marked. What should be the nodule  
#      highlight color in this case? 
#       In this case the white boundary has to be there because the marking is being displayed. 
#       Initially the outer boundary has to be color yellow because ita has already been marked.
#       When the user clears the marking or redo the marking or chnges the annotation then the color
#       should get changed to red.
#       wHEN ONLY THE NODULE dICT INDEX IS SET THEN the graph class does not know whether the marking has 
#       already been done or it is being done. Therefore, the dicom annotator should set the variable 
#       nodule_dict_index only when a nodule is being marked otherwise the nodule index should go to 
#       nodule_dict_indices_shown_extra when an already marked nodule gets shown. When the user starts 
#       changing the already marked things then the index can be moved from the array to the nodule dict 
#       index. This will give an hint / trigger from the dicom annotator to the graph class because the 
#       redraw will itself perform the marking appropriately.
#       The changing of color from yellow to red can deferred now because the events on change in marking
#       and annotations have to be cached.
#
#   b: What should be the nodule highlight color when a new nodule being marked individually?
#       Since the boundary have to be marked therefore, the boundary will be shown when marked. 
#       Therefore, the white boundary will be there. 
#       Also, the nodule is being marked therefore, the red boundary outside white boundary will also be 
#       there.
#       
#   c: What should be the nodule highlight color when a new nodule being marked with other nodules shown?
#       Here also same white and red boundaries will be there.
#
#The latest strategy is to have nodule_dict_index as it is in case of a single nodule displayed.
#When multiple nodules displyed, nodule dict index will have a value only when a nodule is being marked.
#After marking that nodule and saving, the nodule dict index won't have anything.
#That nodule can be modified later independently.
#As per the latest strategy, when only one nodule is displayed, it is assumed that it will be only in 
#nodule_dict_index and not in extra indices. But, when an image is having only one nodule and show all nodules is
#done by right clicking that nodule, then the nodule index must go to nodule_dict index and the nodule will get 
#opened in marking mode. Though the nodule highlight will still be yellow but changing anything by the user 
#will change the respective annotation or marking. This should be told to user that opening a single nodule by
#right click will open it in edit mode.
#Therefore, there will be correctness constraint that it can not be the case that nodule_dict_index is -1 and 
#there is only one entry in extra indices displayed for nodule.
#This has been coded in fucntion chk_single_nodule_validity.
#Also, when all images of a single nodule are shown, then the entry of the nodule index will be there in
#nodule_dict_index of dicom annotator and extra indices will be empty. Therefore, the nodule marking functions 
#will be active. But, we donot want to do marking in this case. Therefore, update all the nodule marking 
#functions, so that they will perform marking only when a single image is displayed.
#But the annotation can still be changed and saved. 
#And even for the case multiple nodules show only, the same issue is there.
#Someone can show annotation window for some nodule and perform changes. The user can also save the changes. 
#But the nodules were supposed to be in view only mode. 
#Actually, it seems inconsistent to chane only annotation and not the marking. But we can currently live it and 
#tell it to user as well that when viewing multiple nodules only annotation can be saved. 
#There can be some workaround to make it view only.
#1: Disabling the save button of annotation window: Cons: Allowing the user to change the comboboxes but not 
#   saving it will even increase the confusion.
#2: Disabling change to comboboxes: setEnabled of comboboxes may be used. but that is error prone and requires 
#   some coding and testing. just leave that for now.  The reason is that when disabled, they have to be 
#   reenabled later. And that will be a complex set of enable, disable which is error prone.
#Where will be  the common function that will check whether both the annotation and marking for the nodule has 
#been done. Now remove the function from the nodule_dict_index(in case of multiple nodules).
#Instead of setting the saved variables directly as true, have a function to update them. That function can check 
#the saved status of the other nodule as well. 
#When multiple nodules are shown in that case nodule dict index will be -1 if no nodule is marked and 
#the nodule dict index will have a valid value only for the nodule which is being marked.
#does the case of single nodule shown matches with the showAnnotationWindow comments. 
#The highlight and rehighlight of the set graph(also nodule boxes) is handled by the graph class.
#The graph class does not know which set of conditions caused this display to happen. Even the 
#dicom annotator class itself does not know which set of conditions caused this display to happen.
#The only way to remember is that whether self.nodule_dict_indices_shown_extra is empty.
#Now the issue of initial highlights of the nodules comes. Even the initial highlights have to be done 
#by the graph class. Therefore, let graph class itself have the sophisticated function to display and the 
#dicom annotator class will give call that highlight. The graph class, using the dicom annotator 
#reference will itself identify how and when to highlight the nodule boxes. 
#
#Later: Read all above and chk if something is left.888888888888888888888888888888888888888888888
#
#Later: Most Important: 
#When multiple nodules are shown and user changes annotation window then also the yellow color of the 
#second outer must get changed to red and the nodule index must get moved from extra indices to nodule_dict_index
#and the marking must be possible. 888888888888888888888888888888888888888888888888888 do this. 
#try running this case.

#######################################################################################################
# 888888888888888888888 showAnnotationWindow comments 88888888888888888888
#######################################################################################################

#Earlier I thought of a common show and hide function in the dicom annotator class. Looking at this, 
#we may call hide other annotation window in showAnnotationWindow. But, the hide other annotation window 
#will itself create a loop like condition. Therefore, the showAnnotationWindow by the right click option will onlly be there for the already displayed nodule.

#There is a function show_annotation_window in class nodule. That is called only once in the class 
#dicom annotator. aND THAT call is there in the function perform_nodule_selected. This also seems logically 
#correct that the hightlight of a nodule can be called only if that nodule gets selected, either at the time 
#of addition of that nodule or by any other means. The case of highlight of multiple nodules 

#Currently, show_annotation_window 

#There is a catch here. We wanted to merge the display of a nodule, highlight of the nodule box and showing of 
#annotation window. the function perform_nodule_selected does not highlight/unhighlight any nodule box.
#The function perform nodule selected also does not display the nodule markings.
#The display of nodule markings were left to the calling function because the nodule selection may have been 
#done due to nodule addition or already added nodule. but in both of the cases, the highlight and unhighlight of 
#nodule boxes is required.                                
#Therefore, I am adding the nodule box highlight call to perform_nodule_selected. For the case of nodule box 
#highlighting, the function highlight_nodule_for_marking_consistently is idempotent. Therefore, function calling  
#perform_nodule_selected and functions called by perform_nodule_selected have no effect to be considered.
#The only reason that the function calling perform_nodule_selected are listed, is just because TO see whether the
#display of nodule is handled correctly by the calling functions. Also, it does not matter the functions called 
#by perform_nodule_selected.
#oNE MORE THING LEFT is to cheCk and make the call to unselect nodule in perform_nodule_selected. 
#BY COMPLETING THIS, WE WILL BE ABLE TO COMPLETE THE merging of display of a nodule, highlight of the nodule box
#and showing of annotation window.
#8888888888888888888888888888888888888888
#the perform nodule selected was one of the place where the three things (display nodule marking, 
#highlight nodule box and show annotation window were to be merged.) The only other places where these three can 
#be thought to be made in sync are following:
#1: marking nodule: (sync must have been done already.).
#2: Showing the annotation window: the nodule must have already been shown which means that nodule marking must 
#   have already been displayed and the nodule box must also have been already highlighted.
#3: The case for displaying multiple nodules or multiple images will be looked at sooner.
#First complete the show annotation window and hide annotation window in the dicom annotator and make it a 
#gateway for all other show hide annotation window calls in the dicom annotator.
#There are only two functions in the dicom annotator which call hide_annotation_window of the nodule 
#class. hence, the need of gateway for hide does not seem to be urgent right now.
#also, these hide functions(hideAnnotationWindow(by right click) and hide_other_annotation_window) are complete 
#right now.
#Is gateway required for show as well?
#For the show_annotation_window of the nodule class, currently only two functions of dicom annotator call it.
#They are: perform_nodule_selected and showAnnotationWindow(by right click). 
#hence the gateway is not required now.
#complete showAnnotationWindow(by right click).8888888888888888888888888888888
#The main reason of gateway function to show annotation windows was to ensure that the selected nodule index 
#has been set up correctly in the graph class. But one thing must be thought here. When we do 
#perform nodule selected, then the process of highlighting selected nodule box will itself update the selected
#nodule index in the graph class. And when we perform showAnnotationWindow(by right click), then the nodule
#must have already been selected by the user and hence the selected nodule index must have already been set
#up correctly. Hence show annotation window does not require any additional change to the graph class.
#the info msg that anotation window already shown may be added.

#After completing this perform_nodule_selected, just have a look at the variables, nodule_index_for_marking and
#selected_image_name in te graph class. they were thought to be useless when multiple nodules or multiple images
#are shown.
#The function perform_nodule_selected is called in working portion of code by:
#add_img_nodule_connection: This function calls add_edge_img_nodule function of the graph class.
#                           That function itself calls the highlight_nodule_for_marking of the graph class.
#                           The function highlight_nodule_for_marking calls the highlight and unhighlight to 
#                           appropriate nodule boxes. The highlight_nodule_for_marking is to be followed by draw 
#                           all edges so that the drawing of edges remain correct. 
#                           We can have function highlight_nodule_consistent. This function can call to highlight
#                           function as above and also the call to redraw all edges. Thereby this will be a 
#                           complete function to perform the drawing consistently.
#                           Then this function to consistently highlight a nodule can be called by 
#                           perform nodule selected. There will alo be call to this consistent highlight in the 
#                           function add_edge_img_nodule, just for completeness of the function 
#                           add_edge_img_nodule. The consistent highlight does not change its behaviour when 
#                           called more than once, hence it can be called at that time as well.
#                           The function highlight_nodule_for_marking_consistently has been written.
#                           The unselect_nodule was earlier called only in the function special_highlight_image_boxes 
#                           of the graph class. But now, with the call of consistent highlight in 
#                           perform nodule selected(-----to be written the call-----88888888888), 
#                           we should perform unselect_nodule even in 
#                           consistent highlight so that nodule unhighlight can be done on nodule unselect.
#                           seems not reqd when special highlight is there. chk again.
#                           Now there is no slected nodule info saved in graph class. the highlighting of nodules 
#                           depends upon the nodule indices saved in dicom annotator. hence the discussion for 
#                           unselect nodule is meaningless now. 
#                           Also, the perform_nodule_selected simply redraws the graph which handles everything.
#
#                           aT THIS POINT OF TIME, it is correct to do unselect_nodule in 
#                           special_highlight_image_boxes.
#
#                           We can still have unselect_nodule in special_highlight_image_boxes because unselect_nodule
#                           should be idempotent. Currently, redraw edges is not called in unselect_nodule. 
#                           The redraw edges should be called even after all nodule box unhighlight in 
#                           unselect_nodule.88888888
#show_nodule_single_image: (This function does not perform te nodule highlighting. 
#                           That must have been performed by the calling function)

#showImageOnly:             (making the nodule selection as -1 i.e. none.)
#addNoduleWithPrevNodules:  (This call will be removed and converted to call by add_img_nodule_connection)

        #Whenever an annotation window is shown then the other annotation window must be hidden.
        #Since, we are showing annotatin window only if the nodule is displayed already, therefore, 
        #the other annotation window would have been hidden at the time of display of this nodule. 

        #Also, if there is a single image with that nodule, then the image with marking must be shown. if there 
        #are multiple images with that nodule, then try to show all those images.
        #Here also, the condition arises that when a different nodule is being shown, a confirmatory window must 
        #be there.
        #When same nodule is already shown then all the images for that nodule must be shown.
        #HERE THE issue arised for discrepancy only due to the fact that i am trying to show all images for 
        #a nodule when show annotation wondow is called. In fact, this should never be like that.
        #The show all images can be a separate menu item in the right click of a nodule. 
        #In the handler of that event we must show the all the images for the nodule.
        #In the current function we just need to ensure that a single image is shown and that nodule is being 
        #displayed over that image. There must be a separate menu item or series of clicks which handles the 
        #display of image or nodule. In fact this function needs to be called by those functions.
        #When multiple images of a nodule are shown then also show and hide annotation window may be called.
        #When adding a nodule along with prev nodules shown, then also the annotation window of the nodule to be 
        #added must be shown. Therefore, THIS FUCNTION MUST ONLY CHECK WHETHER THE self.nodule_dict_index is 
        #same as the index to be displayed. if yes then simply display the annotation window, else 
        #two cases arise:
        #1: nodule _dict_index refers to some other nodule:
        #       In this case tell the user that annotation window can be shown for that nodule only. first you 
        #       need to switch to this nodule and the annotation for this nodule can be shown.
        #2: nodule_dict_index is -1:
        #       In this case, tell user that no nodule is being shown. first show the nodule and then annotation 
        #       window can be shown.
        #
        #It was thought that show annotation window will call highlight for a nodule when change of nodule is 
        #done. but just show annotation window should not change the displayed nodule in principal. In principal,
        #show annotation window is only for the nodules which are already displayed. Otherwise, for displaying a 
        #nodule there are plenty of other ways. One is show all images by right click that nodule. the other is 
        #drawing a line from an image to that nodule. 
        #Even if we have displayed some other nodule and we want to display a different nodule for that image 
        #then we can do that by dragging a line from that image to the nodule. hence, no need to add another 
        #function for showing a nodule. 

#######################################################################################################
# 888888888888888888888 showAnnotationWindow comments earlier 88888888888888888888
#######################################################################################################
        #8888888888888888888888888888888888888888888888888
        #Whenever an annotation window is shown then the other annotation window must be hidden.
        #Also, if there is a single image with that nodule, then the image with marking must be shown. if there 
        #are multiple images with that nodule, then try to show all those images.
        #Here also, the condition arises that when a different nodule is being shown, a confirmatory window must 
        #be there.
        #When same nodule is already shown then all the images for that nodule must be shown.
        #HERE THE issue arised for discrepancy only due to the fact that i am trying to show all images for 
        #a nodule when show annotation wondow is called. In fact, this should never be like that.
        #The show all images can be a separate menu item in the right click of a nodule. 
        #In the handler of that event we must show the all the images for the nodule.
        #In the current function we just need to ensure that a single image is shown and that nodule is being 
        #displayed over that image. There must be a separate menu item or series of clicks which handles the 
        #display of image or nodule. In fact this function needs to be called by those functions.
        #When multiple images of a nodule are shown then also show and hide annotation window may be called.
        #When adding a nodule along with prev nodules shown, then also the annotation window of the nodule to be 
        #added must be shown. Therefore, THIS FUCNTION MUST ONLY CHECK WHETHER THE self.nodule_dict_index is 
        #same as the index to be displayed. if yes then simply display the annotation window, else 
        #two cases arise:
        #1: nodule _dict_index refers to some other nodule:
        #       In this case tell the user that annotation window can be shown for that nodule only. first you 
        #       need to switch to this nodule and the annotation for this nodule can be shown.
        #2: nodule_dict_index is -1:
        #       In this case, tell user that no nodule is being shown. first show the nodule and then annotation 
        #       window can be shown.
        #
        #It was thought that show annotation window will call highlight for a nodule when change of nodule is 
        #done. but just show annotation window should not change the displayed nodule in principal. In principal,
        #show annotation window is only for the nodules which are already displayed. Otherwise, for displaying a 
        #nodule there are plenty of other ways. One is show all images by right click that nodule. the other is 
        #drawing a line from an image to that nodule. 
        #Even if we have displayed some other nodule and we want to display a different nodule for that image 
        #then we can do that by dragging a line from that image to the nodule. hence, no need to add another 
        #function for showing a nodule. 


#######################################################################################################
# 88888888888888   Highlight selected nodule (also some argument for image highlighting)  88888888888888888888
#######################################################################################################
#THE SELECTED Nodule index must be reset when another image gets shown without highlighting any nodule.
#uptil now, an image gets highlighted first and then a nodule gets highlighted. it has been taken care of.  
#There might be a special case when all images for a nodule are shown.
#Therefore, we must have a function whenever highlighting of a single image is called. In that case, 
#undo highlight selected nodule. It was not done already. it is done.
#Whenever an image is left clicked, it gets selected and the highlight will be called and then unselect nodule 
#will be called. 
#nOW, THE SPECIAL HIGHLIGHT SHOULD BE CALLED because unselect is implicitly implied by the nodule_dict_index and
#the indices shown extra. 
#Therefore update the display of image to update nodule_dict_index and extra indices shown for nodule. In fact the perform nodule selected should be called and also the clearing of extra indices should be done. There must be another function to carry out clearing of extra indices shown. write pseucode for that.
#888888888888888888888888888 do above line
#The highlighting was kept idempotent because redraw graph or highlight again may be required when chainging 
#the text from axial to sagital. ok, updating the text just requires clearing the inner portion and the highlight #does not get affected. What sort of highlighting image is this can be passed by the calling function.
#We can simplify the task of adding information to the calling function.
#We can just chk whether the current highlight image request has the same name as the image name already 
#highlighted. If yes, then it must be an idempotent call and we must not change the selected nodule. 
#Otherwise, a shift in image has occurred and we can now do unselect nodule. 
#IN ANY CASE, A SEPARATE CALL to unselect a nodule for special cases can be performed. not required. only call to 
#special highlight nodule is required.
#
#pseudocode
#The following discussion refers to nodule_dict_index, extra nodule shown and save variables of dicom annotator 
#if no nodule shown then function complete.
#if nodule_dict_index is not (-1)
#   then highlight the nodule_dict_index by white(first outer boundary)
#highlight all index in extra nodule shown by white(first outer boundary)
#if one nodule shown 
#   if save done then highlight nodule_dict_index by yellow(second outer).
#   if save not done then highlight nodule_dict_index by red(second outer).
#if multiple nodule shown:
#   if nodule_dict_index is -1(no nodule being marked).
#      check if annotation window of some nodule is shown.
#       (There must be a function in dicom annotator to check this.)
#         highlight that nodule by yellow(second outer).
#   if nodule_dict_index is not -1(some nodule being marked)
#      if save done then highlight nodule_dict_index by yellow(second outer).
#      if save not done then highlight nodule_dict_index by red(second outer).
#Write function in dicom annotator to get num nodule show.
#write function in graph class to highlight nodule dict index for second outer.
#write function in graph class to highlight all white as first outer boundary.
#write function to handle case for second boundary highlight.
#After adding above functions: 
#modified pseudocode: 
#The following discussion refers to nodule_dict_index, extra nodule shown and save variables of dicom annotator 
#undo highlight all nodules
#if no nodule shown then function complete.
#highlight all nodule shown by white(first outer boundary)
#handle case for second boundary highlight
#
#pseudocode handle case for second boundary highlight
#if nodule_dict_index is not (-1)
#   highlight second outer nodule_dict_index wrt save done or not
#if multiple nodule shown:
#   if nodule_dict_index is -1(no nodule being marked).
#      check if annotation window of some nodule is shown.
#       (There must be a function in dicom annotator to check this.)
#         highlight that nodule by yellow(second outer).
#
#pseudocode highlight all nodule shown by white color
#if nodule_dict_index is not (-1)
#   then highlight the nodule_dict_index by white(first outer boundary)
#highlight all index in extra nodule shown by white(first outer boundary)
#
#pseudocode: highlight second outer nodule_dict_index wrt save done or not
#if save done then highlight nodule_dict_index by yellow(second outer).
#if save not done then highlight nodule_dict_index by red(second outer).
#
#Pseudocode: undo highlight all nodules
#1: for all nodules:
#2:     undo highlight nodule
#3:     undo highlight second outer for the nodule
#
#There is no function call to undo highlight nodule. Also, unhighlighting second outer boundary is necessary. 
#But currently as well, the there wassome second outer boundary unhighlight happened. chk when.
#also undo highlight nodules(including unhighlighting second outer boundary) must be placed at the first line of 
#special highlight nodules.
#
#Before placing undo_highlight_all_nodules() at first line of special highlight nodules first test how 
#unhighlight happened till now. 
#But one thing that has been clear now is that, the extra nodule indices were not made clear when multiple 
#nodules were shown and the another image was shown because those nodules still had white outer boundary.
#This was due to problem in perform nodule_selected. in this function extra indices should be cleared. Also check
#what should be done when a nodule gets selected when multiple nodules are shown.
#When a nodule annotation window gets updated when multiple nodules are shown then, the second outer boundary 
#does not change from yellow to red.
#also, not unhighlighting of yellow was a problem . look that later. Looked. This must be ceause of not doing 
#undo  highlight.
#It has been tested the redraw graph graph was responsible for the unhighlightof nodules.
#Later: chk if any comprison of nodule_dict_index is done like >0. that will be wrong because nodule dict index 
# can be zero as well. 
#
#
#######################################################################################################
# 8888888888888888888888888   Storing the selected image  888888888888888888888888888888888888888888888888
#######################################################################################################
#The dicom annotator class itself stores a reference to the selected image by left or right click.
#A particular right click may not result inhighlighting an image. Also, whenever a single image gets highlighted 
#then the variable selected_image_name in class graph gets updated. Therefore, currently, we can use this 
#variable to re highlight the image. For the case when multiple images are displayed and a redraw to the graph is 
#required, we can look at the situation later on.

#######################################################################################################
# 8888888888888888888888888   Edge deletion  888888888888888888888888888888888888888888888888
#######################################################################################################
#I am focussing only on nodule deletion. There must be some functionality for edge deletion, i.e. if we want to
#delete only that edge.

#######################################################################################################
# 8888888888888888888888888   box coordinates within set image   8888888888888888888888888888
#######################################################################################################
#within set image, the coordinates when drawing boxes were just with respect to the image. But, when getting the 
#box id for mouse event, the coordinates are looked wrt the set image position as well. Therefore, the drawing 
#of lines in the image as well(for connecting the image to nodule) are wrt the image only. Therefore, the 
#drawing of line from the selected image box to arbitrary point in the set image will also depend on the 
#coordinates wrt the image. By subracting the set image x and y from the global coordinates, we will obtain the 
#coordinates within the set image.

#######################################################################################################
# *************************   Handling wheel event  *************************************
#######################################################################################################
#Currently, I have set mouse button as wheel button for the case when wheel event OCCURRED. BUT THAT does not 
#seem to be correct. Actually wheel button should have been set when the wheel button was pressed. Therefore,
#rectify this. done.

#######################################################################################################
# 888888888888888888888   Displaying multiple images simultaneously  earlier 888888888888888888888
#######################################################################################################
        #We will ask appropriate highlight of boxes to the graph class.
        #tHIS CLASS WILL COMPUTE THE COORDINATES for every image. They will be updated to the image object in the 
        #directory object.
        #the generation of small images will take place in this class. The concatenation of the small images 
        #will take place in this class. the concatenated image will be set as (self.image) so that display of 
        #the image works properly. The mouse event needs to be handled that mouse hovered over which image.
        #The mouse clicked over which image. The mouse hovering may fully highlight the image box but a slight 
        #lag may result in incorrect highlghting.
        #Remember to reinit/clear the image dimensions when A single image is shown.
        #888888888888888888888888888888888888888complete this.
        #Here it may be checked that whether an image is currently open that has marking for that nodule.
        #If yes then the nodule annotation window can be shown along with its markings. 
        #Otherwise, We can call the function to display all images for that nodule and show the annotation 
        #window. 

#######################################################################################################
# 8888888888888888888888888   Displaying multiple images simultaneously  88888888888888888888888888888
#######################################################################################################
#Currently, len of number of images dispplayed is used to check whether mouse over image. this may be used
#in displaying multiple images simultaneously.

            #show all images
            #In this case, we need to call a function from dicom annotator
            #Currently, I am in dicom annotator class.
            #iT WILL be better to have show function for multiple images in this class itself.
            #The graph class can be used to obtain the list of image names to be displayed. 
            #Yes that is true. Because graph class does not have the loaded images. The graph class only has the 
            #image names. The directory class has the loaded images.
            #Will it give any advantage if we fill the width height parameters for every image. Basically, we
            #currently are implementing same size for image whn multiple images are being shown.
            #The scaled images needs to be generated ony once. 
            #When hide of anotation window will be done, then the multiple images will still be shown and the 
            #nodule box and image boxes will still be in highlighted state.
            #There should be a call to graph function to highlight the corresponding nodule and image boxes. 
            #The image boxes will be highlighted in less.
            #The image box will get highlighted in full when a mouse click over a particular image occurs.
            #from that mouse click, we can full highlight the corresponding image with or without nodules.
            #Therefore, it is necessary to have some coordinates stored with every image so that we can 
            #decide that mouse click occurs over which image.
            #The logic to decide the coordinates for images can reside in dicom annotator and the coordinates of 
            #the image objects in directory object can be updated via function call.
            #Therefore, just like box coordinates in graph object, we will have image coordinates in the 
            #directory object.
            #These image coordinates will be reset when a single image will be shown. 888888888888888888888888
    #****** #self.show_all_images_given_nodule(self.nodule_dict_index)
#
#pseudocode show all images :
#1: get the nodule index for which all images needs to be displayed.
#2: get all the image names which are connected to this nodule.
#3: chk that at least one image will be there for any nodule otherwise raise error.
#4: If the displayed nodule is different than the required nodule then:
#5:      If only one image for this nodule then:
#6:         ask user if he wants to swith nodule. Also show message as that change in marking and annotation 
#           can be done.
#7:         If yes then:
#8:             procced as in the case of single nodule display and switch image.
#9:         If no then:
#10:            just return. Nothing to be done.
#11:     If multiple images for this nodule then: 
#12:        ask user if he actually wants to display images for required nodule. Also 
#5:   If yes then:
#10:     
#6:      do display all images given nodule. In this case also, the message that only images for this nodule 
#        will be shown and it is fine.
#7:   If no then:
#8:      just return. Nothing to be done.
#9: If no nodule is displayed then 
#10:     display info multiple images shown
#           exp: If the currently displayed image does not belong to the image list for the given nodule 
#                even then we can display all nodules. information can be be shown in general in the 
#                display all images given nodule that now only mages for ths nodule will be shown.
#                Therefore, when no nodule is displayed, it does not matter which image is displayed. 
#11:     do display all images given nodule 
#12: If the displayed nodule is same as required then:
#13:     If only one image for this nodule then:
#14:        check that the image name displayed must be same as the image for this nodule.
#15:        show the message that the image has already been displayed. nothing needs to be done for saved 
#           variable.
#16:     If multiple images for this nodule then:
#17:        do display all images given nodule
#
#The case when the nodule displayed is same as the requested nodule and the images displayed are also same
#can be handled together for the case when the nodule has a single image and when the nodule has multiple images.
#But this require changes in multiple pseudocodes and t`herefore 
#
#pseudocode show all images given nodule(chk num images first)(to be implemented) :
#1: get the nodule index for which all images needs to be displayed.
#2: get all the image names which are connected to this nodule.
#3: chk that at least one image will be there for any nodule otherwise raise error.
#4: If (handle mul nodule or mul image display already for mul image) does something then:
#5:     return. the case has been handled
#6: If only one image for this nodule then:
#7:     If the displayed nodule is same as required then:
#8:        check that the image name displayed must be same as the image for this nodule.
#9:        show the message that the image has already been displayed. nothing needs to be done for saved 
#          variable.
#10:     otherwise If the displayed nodule is different or no nodule displayed then:
#11:        ask user if he wants to move to that nodule. Also show message as that change in 
#           marking and annotation can be done.
#12:        If yes then:
#13:            procced as in the case of single nodule display and switch image.
#14:        If no then:
#15:            just return. Nothing to be done.
#16:If multiple images for this nodule then: 
#17:    If the displayed nodule is same as required then:
#18:        chk that the image name displayed lies in the set of image names for this nodule. When a nodule is 
#               displayed then no other image can be displayed.
#19:        display info multiple images shown
#20:        do display all images given nodule
#21:    otherwise If the displayed nodule is different or no nodule displayed then:
#22:        do handle general case show multiple images 
#
#
#pseudocode show all images given nodule(chk num images first)(to be implemented)(after changes) :
#1: get the nodule index for which all images needs to be displayed.
#2: get all the image names which are connected to this nodule.
#3: chk that at least one image will be there for any nodule otherwise raise error.
#4: If (handle mul nodule or mul image display already for mul image) does something then:
#5:     return. the case has been handled
#6: If only one image for this nodule then:
#7:     If the displayed nodule is same as required then:
#8:        check that the image name displayed must be same as the image for this nodule.
#9:        show the message that the image has already been displayed. nothing needs to be done for saved 
#          variable.
#10:     otherwise If the displayed nodule is different or no nodule displayed then:
#11:        do handle nodule display single image
#12:If multiple images for this nodule then: 
#13:    If the displayed nodule is same as required then:
#14:        chk that the image name displayed lies in the set of image names for this nodule. When a nodule is 
#               displayed then no other image can be displayed.
#15:        display info multiple images shown
#16:        do display all images given nodule
#17:    otherwise If the displayed nodule is different or no nodule displayed then:
#18:        do handle general case show multiple images 
#
#
#pseudocode show all images given nodule(chk num images first)(to be implemented)(after changes)(after including mul image/nodule displayed already case) :
#argument: make sure that execution reaches till last so that 
#self.nodule_dict_index can get updated.
#
#1: get the nodule index for which all images needs to be displayed.
#2: get all the image names which are connected to this nodule.
#3: chk that at least one image will be there for any nodule otherwise raise error.
#6: If only one image for this nodule then:
#7:     If exactly one nodule shown and exactly one image shown and the displayed nodule is same as required then:
#8:        check that the image name displayed must be same as the image for this nodule because this nodule has only one image.
#9:        show the message that the image has already been displayed. nothing needs to be done for saved 
#          variable.
#10:     otherwise :
#11:        do handle nodule display single image
#12: otherwise If multiple images for this nodule then: 
#13:    If exactly one nodule shown and multiple images being displayed and the 
#       displayed nodule is same as required then:
#14:        chk that the number of images displayed must be same as the number of 
#           the images for this nodule.
#15:        chk all the image names displayed is same as that the image names for this nodule.
#16:        show information already displayed
#           (as in case of handle mul imsages etc.)
#17:    otherwise:
#18:        do handle general case show multiple images 
#

#PSEUDOCODE: handle nodule display single image:
#1: ask user if he wants to move to that nodule. Also show message as that change in 
#   marking and annotation can be done.
#2: If yes then:
#3:     procced as in the case of single nodule display and switch image.
#4: If no then:
#5:     just return. Nothing to be done.
#
#pseudocode: handle general case show multiple images:
#1:    ask show multiple images for given nodule and also display what can be 
#      changed and what not.
#2:    If yes then:
#3:        do display all images given nodule
#4:    else:
#5:        just return. Nothing to be done.
#
#
#pseudocode handle mul nodule or mul image display already for mul image(earlier):
#This is pseudocode to handle the case when multiple images or multiple nodules are displayed already and
#multiple images needs to be displayed now. 
#1: get the number of nodules displayed. 
#2: get the number of images displayed. 
#3: if (number of nodules displayed>1)  then :
#4:     do handle general case show multiple images
#5       return done something
#6: if (number of images displayed>1) then:
#7:     get the nodule displayed
#8:     chk that the nodule number is valid
#9:     If the nodule displayed is same as the reqd nodule then:
#10:         chk that the number of images displayed must be same as the number of the images for this nodule.
#11:        show information already displayed
#12:        return done something
#13:    Otherwise:
#14:        do handle general case show multiple images
#15:        return done something
#16:return not done anything
#
#pseudocode handle mul nodule or mul image display already for mul image:
#This pseudocode has been modified for the case when multiple images are displayed 
#after deleting a nodule and show all images for a nodule occurs.
#In the current implementation, multiple images can be shown only for a single 
#nodule. hence if multiple images are shown then only self.nodule_dict_index can 
#have a valid value. and if nodule_dict_index is not having any valid value and 
#multiple images are displayed, then it means that earlier those multiple images 
#got displayed due to a nodule and that nodule got deleted. Though, I can save 
#the last operation and check in such a case last operation must be a nodule delete
#, but that will make process complicated. Instead we can simply switch nodule 
#when self.nodule_dict_index is not the required nodule. and the same is 
#implemented in many other cases.
#This is pseudocode to handle the case when multiple images or multiple nodules are displayed already and
#multiple images needs to be displayed now. 
#1: get the number of nodules displayed. 
#2: get the number of images displayed. 
#3: if (number of nodules displayed>1)  then :
#4:     do handle general case show multiple images
#5       return done something
#6: if (number of images displayed>1) then:
#7:     get the nodule displayed
#8:     If the nodule displayed is same as the reqd nodule then:
#9:         chk that the number of images displayed must be same as the number of the images for this nodule.
#10:        show information already displayed
#11:        return done something
#12:    Otherwise:
#13:        do handle general case show multiple images
#14:        return done something
#15:return not done anything
#
# Also write cases when multiple images or multiple nodules displayed already.
#PSEUDOCODE: ask nodule move and show multiple images
#1:ask user whether move to that nodule and show all images. Also tell marking will not be possible but the 
#       annotaion can be changed.


#pseudocode: display info multiple images shown:
#1: display info message that all images for this nodule will be shown and marking will not be possible. 
#   Also say that change in annotation will be possible.

#pseudocode: procced as in the case of single nodule display and switch image. 
#1: switch image.
#2: show nodule for that image(same as in the case when edge was drawn for the existing img-nodule connection).
#3: the save variable should be marked saved for both annotation and marking.

#pseudocode display all images given nodule
#Here we know that multiple images are there for a given nodule and they all needs to be displayed.
#1: sort the image names in the order in which images are displayed.
#2: store all these image names in the image namearray.(something selected_image......)
#     Earlier it was thought that the first element is for marking. But currently leave it only for the case 
#     of single image displayed. Currently, when more than image is displayed, then treat them equally.
#3: Divide the image space in equal sized panes for the images to be displayed. 
#    One or more panes may be left blank.
#4: Fill the panes starting from top left corner with resized images and their resized alpha channels for 
#   given nodule.
#5: perform_nodule_selected for the nodule index. This will also redraw graph and show annotation window only 
#   for the given nodule.
#6: special highlight image boxes.
#7: Have some indication on display so that user can figure out which image box corresponds to which image 
#   displayed.
#   The order of display of images is same as order of image name written in the left side of set graph.

#pseudocode: sort the image names in the order in which images are displayed.
#the number of images to be displayed andthe number of images total are very less. hence complexity that is a 
#product of these 2 will be fine. 
#all image array is practically  a dict. Hence the algorithm is expected to run in time 
#O(number of images to be displayed+number of images total)
#1: create a bit array of length number of total images.
#2: initialize this array with all zeros.
#3: for every image in images to be displayed:
#4:     scan the all image array to find where this name is present.
#5:     Let the match found at index i.
#6:     mark 1 at index i in the bit array.
#7: Have an empty output array for images.
#7: scan the bit array and images to be displayed in parallel.
#8: Whenever a 1 is found in the bit array, append the image name at that index in the 
#           images to be displayed at the end of output array.
#return the output array

#pseudocode: sort the image names in the order in which images are displayed.
#the number of images to be displayed andthe number of images total are very less. hence complexity that is a 
#product of these 2 will be fine. 
#all image array is practically  a dict. Hence the algorithm is expected to run in time 
#O(number of images to be displayed+number of images total)
#1: create a bit array of length number of total images.
#2: initialize this array with all zeros.
#3: for every image in images to be displayed:
#4:     scan the all image array to find where this name is present.
#5:     Let the match found at index i.
#6:     mark 1 at index i in the bit array.
#7: Have an empty output array for images.
#7: scan the bit array and images to be displayed in parallel.
#8: Whenever a 1 is found in the bit array, append the image name at that index in the 
#           images to be displayed at the end of output array.
#return the output array

#pseudocode: sort the image names in the order in which images are displayed(new)(to be used)
# This one scan image name to displayed mul times. Also image name to displayed is a dict hence checking 
# if a key exists is expected to run in constant time.
#Actually total images is a dict. hence finding a name in that is expected to run in constant time.
#Actually images to be displayed is a list hence finding a name will be linear in length of the list.
#when the all images is a dict then there is no index for an entry. following the order geneated by the 
#for iteration over keys. 
#expected time product of length of two list(key list and image name to be displayed list).
#1: Have an empty output array for images. 
#2: for every image_name in total images:
#3:     if image_name in images to be displayed then:
#4:         append the image_name at the end of output array.
#5: return output array


#Argument: Divide the image space in equal sized panes.
#Spliting the space into equal sized panes require splitting the space into some m*m space of panes.
#If the number of images is (m-1)*(m-1)+1, then a lot o panes will be empty. Practically, I am expecting roughly 
#10IMAGES in a patient. there may be 12 images if 6 nodules are there. Do test with 16 images for a patient.
#Practically, I am not expecting more than this as the number of images in a single folder for a patient.
#the squares are 1,2,4,9,16.
#The number of images are already expected to be even in most of the case. One for the sagital view and one for 
#the axial view.
#Therefore, the number of images that may be present are 2,4,6,8,10,12,14,16.
#When the number of images are 6, we can have 3*2 as the plane partition and display the images, but they will not be of equal size all. 
#In case of 8 images, we can split the space into 4*2 and all the images will dsiplayed. Though they will not be 
#all of equal size. We could have partitioned as 3*3, and leave one pane blank.
#Though we expect an even number of images but there will not be any such restriction.
#For 10 images, we can have 5*2 pane partition and display the images, though they will not be all of equal size.
#Practically, a single nodule will be there in at max(expected) 4 positions i.e. 8 images which have both 
#axial and sagital views. Also 9 images are very uncommon. therefore, currently the easiest way is split the image
#portion into 2 rows. The first row for axial view. The seocnd row for sagital view.
#For each column the row 1 and row 2 will have axial and sagital for the same position. but then the axial
#and sagital for the same position has to be specified by the user.
#Having that information will also help to build the model. In some case all the images may belong to the same 
#view or the view may be unrelated. Therefore, we can plainly display the images starting from the top box. 
#currently treat the images as unrelated and simply fill the images. Later: In the next version, I may add the 
#functionality of user specifying which axial and sagital are together. and displaying multiple images wrt that. 
#This functionality is important for publishing.
#
#Data structure: Divide the image space in equal sized panes.
#Where to store the coordinates for rows and columns. Do we need another class for that?
#where to store correspondence that which image in which pane. Hovering over the image might require to double 
#highlight the image box. Also such information may be used elsewhere.
#Therefore, we may have a special class image pane manager.
#Also have a class boxto store coordinates. The box class is already there.
#

#pseudocode: Divide the image space in equal sized panes.
#1: Let n be the number of images to be displayed.
#2: Let e be the number of panes defined as next even number greater than or equal to n. 
#3: Divide the vertical spcae into 2 rows.
#4: Divide the horizontal space into e/2 columns.
#5: compute boxcoordinates for each pane. store them.
#5: Assign a pane (row, column index) to every image.

#pseudocode: compute boxcoordinates for each pane
#1: Let nr, nc be the total number of rows and columns respectively.
#2: The width of each pane is total width/nc.
#3: The height of each pane is total height/nr.
#4: for all row index r in nr and col index c in nc:
#5: The x of current pane is (c-1)*(width of each pane).
#6: The y of current pane is (r-1)*(height of each pane).

#pseudocode: Assign a pane (row, column index) to every image.
#1: Scan the image names. 
#2: Assign next free pane in order, i.e. first top row starting from first column, then second row and so on.

#pseudocode: Assign next free pane in order
#1: start with row index 0 and col index 0. 
#2: scan the image names in order.
#3:     Let i be the image index.
#4:     if the row index is with range and col index is within range then
#5:         assign the index i to row and col index.
#6:         increment the col index to fill the next column.
#7:     otherwise if the col index falls outside range, i.e. row has completely filled then
#8:         increment the row index to move to next row.
#9:         set the col index as zero for the first col in the next row.
#10:        assign the index i to row and col index.
#11:        increment the col index to fill the next column.
#12:    otherwise if the row index falls outside range then raise error that this isnot possible.
#
#Have a separate function for assignemnt which check for ranges and raises error for invalid indexes.

#pseudocode: resize image and its alpha channel.
#1: We have boxcoordinates for every image as computed in pseudocode: Divide the image space in equal sized panes.
#2: get the size of required from its box coordinates.
#3: resize the image(with alpha channel added to it).

#pseudocode: fill panes:
#Thee is physical pane. Therefore stitch the resized images(along with their alpha) in the order to be displayed.
#the double highlight of image box can be done by the x,y coordinates over the image and box coordinates stored in
#the pane manager.

#pseudocode: fill panes(elaborated):
#0: Start with an empty list of merged images.
#1: For image_name in images to be displayed(sorted):
#2:     add image and alpha channel as for the case of single image.
#3:     scale this merged image.
#4:     append this merged image to the list of merged images. 
#5: create an empty output image of total width * total height.
#6: decide start, end row and start, end col for every pane in this big image.
#   The cooresponding box coordinates(after adding big image top left) can be used as start, end.
#7: for all images to be displayed:
#8:     copy the scaled image to the row range and col range decided by its pane(box in implementation).
#9: return big image that has all copy done.

#Argument: special highlight image boxes
#All the image boxes can be highlighted normally. Whenever the mouse is hovered over an image then that
#image box may be highlighted more only on outer right handside.
#Whenever redraw graph is required then the mouse must not be over any scaled image. Therefore, remembering which
#image is highlighted more is not necessary. 
#Whenever the mouse is hovered over an image then special highlight will be called with the image name which 
#needs to highlighted special.  
#replace all calls to highlight image by special_highlight_image_boxes. remove any other function to highlight 
#image boxes.
#function chk_highlighted_image_same is called by draw_line_img_to_given_point and add_edge_img_nodule. Therefore,
#it seems better to keep a variable that tells which image has been highlighted in case a single image gets 
#highlighted. undo_highlight_other_image is called by chk_highlighted_image_same. In special highlight we should 
#first undo all highlight then undo_highlight_other_image will not be required. the undo highlight must remove 
#the extra highlight. done.
#now setting the selected image name through special_highlight_image_boxes. hence all issues resolved.
#Calls to highlight image has been updated in make_image_to_display, highlight_again.
#for the image box also, the second outer must be yellow. done. 
#earlier the unselect_nodule was called in highlight of image. If the image name was changed then unselect nodule 
#was done so that the earlier nodule does not gets highlighted anymore. 
#Now the graph class does not maintain any nodule highlighted variable. Hence unselect nodule is meaning less. 
#In fact the nodule display information(nodule index etc) should be updated whenever new image is opened. 
#Also, nodule_index_for_marking is always set and never used. Hence no harm in deleting the variable.
#Yes, the updation of nodule selection variables are correctly updated when an image is shown.
#deleted function unselect_nodule. no longer required. The deletion of variable nodule_index_for_marking can be 
#done later on.
#pseudocode:special highlight image boxes 
#0: undo highlighlight all image boxes
#1: For all images in selected_image... array:
#2:     highlight the image box.
#3: If the image_name is given for more highlight:
#4:     more highlight that image box
#5: set selected image name.
#6: redraw edges.

#pseudocode: set selected image name
#1: if num images to highlight is 1:
#2:     set selected image name as the name of the image to highlight.
#3: otherwise
#4:     set selected image name as empty string.


#######################################################################################################
# 8888888888888888888   Mouse hover/click multiple images    88888888888
#######################################################################################################

#pseudocode
#1: get the mouse coordinates wrt image, same as when marking image.
#2: get the box index in which these coordinates lie.
#3: get the image index for that.
#more highlight image box for the corresponding image_name.

#test by clicking at the extreme left right top bottom of total image 
#nd individual images so that box boundaries and x,y offsets are correctly 
#tested. also the exterme points at invidual images must be tested. 

#mouse move shuld workonly for singleimage displayed.
#test this over 10 images so that coordinate selection criterion can be tested.

#######################################################################################################
# 8888888888888888888   When moving from multiple images displayed to a single image   88888888888
#######################################################################################################
            #Here also, we can show the message box that closing all the currently shown images and showing the 
            #required image and then we can move to the required image. We also need to clear the prev array of
            #names for images being shown and have only one entry in the array that has the name of only 
            #image being shown. chk if this has been done correctly for the case of no image or single image.
            #yes this has been done correctly for the case of no image or single image.
            #And, this will work fine even for the case when multiple images are shown simultaneuosly.
            #The reason is that, we discard prev array of displayed images and then realloacte the array with
            #a single image name in the function showImageOnly.

#######################################################################################################
# *******************   When a different image is displayed than asked by user   ***********
#######################################################################################################
                #A different image is being displayed. Ask user that should the user want to change the image.
                #if the user want to change the image then 
                #Many of these require changing the image. A common function can be there.
                #after changing the image, should i reask whether he want to mark the type or leave it to user 
                #to do the remark. In the initial message, it can be displayed that changing to the required 
                #image and the user can then redo the marking or any other opertaion he wants. 
                #done in same way.

#######################################################################################################
# 8888888888888888888888888   Displaying multiple nodules simultaneously  88888888888888888888888888888
#######################################################################################################
#We are currently doing the work with nodule dict index only. If only one nodule is being shown then 
#nodule dict index is the highlighted and shown nodule. We also have the option to show multiple 
#nodules simutaneously. just keep the nodule dict index only for the nodule for which marking and 
#annotation is being done.
#we can keep another list for showing multiple nodules. The list will be nodule_dict_indices_shown_extra.
#self.nodule_dict_indices_shown_extra = [] is the variable that is currently being maintained.
#The annotation window will not be shown for any of the index in nodule_dict_indices_shown_extra.
#when marking the nodule, along with some other marked nodules, we can highlight those other nodule 
#boxes less.

#Pseudocode
#1: get all the module indices in dict for the required image.
#2: if only one nodule, proceed as in case of displaying a single nodule
#    (also chk if the nodule being dsiplayed currently) not reqd because the image has been shown afresh.
#3: if no nodule then display msg no nodule for this image.
#4: assert multiple nodules are there
#5: put all nodules indices in list of extra indices.
#6: add alpha of all ndules to the image.
#7: do special highlight of nodules. 
#8: close the annotation window of all possible nodules.

#We should rename this list as nodule_dict_indices_shown_extra. done.
#888888888888888888888888888888888888888888888888888888888888888888888 do above.

#888888888888888888888888888888             test the removal of alpha channel.
#hiding of annotation window remaining.
#deletion of nodules, loading partially annotated directory are basic features to be implemented.
#
#

#Changes in output:
#1: now orientation will not be saved along with annotation.
#2: the mapping of orientation is saved separately.
#3: The mapping of dict number and number displayed is saved separately.

#############@#####################    Nodule deletion ################################################

        #88888888888888888888888888888888888888888888888888888888888888 do below
        #The select nodule index will be the displayed index. we need to convert it to the index in dict.
        #How will the nodule boxes move when a nodule gets deleted. 8888888888888888888888888888888888
        #moving up of nodule boxes is important because we have saved the nodule index in the 
        #box object for the nodule. Also the edges has been saved as per the nodule index displayed. when a 
        #nodule gets deleted, there is a displayed index which got deleted. We have to look from that point of 
        #view. Whenever a displayed index(nodule) gets deleted, its associated edges will also get deleted.
        #hence, no need to reshift edges to another node. But nodule box renumbering and repositioning of 
        #nodule box is an issue that needs to be addressed. Also, the indices in the img to nodule needs to be 
        #updated. This has led to an error prone situation where, deletion of a nodule requires updation to a 
        #lot of edges. In fact even in the img to nodule mapping, we can have nodule dict indices in the values 
        #for every image. this is a better option that does not require change to a lot of edges.
        #In this case, the graph class will also require reference to the mapping that has number displayed to 
        #index in nodule dict.
        #I still have to write the function that updates mapping number displayed to index in nodule dict.
        #Fot the case of nodule to box as well, we need to address how to update/view the key values of this dict,
        #i.e. the nodule indices. In this dict as well, we can have nodule dict indices as the key values. 
        #Updating many keys of a dict is a hard task. Still, we have to update the numbers inside the nodule 
        #boxes and we have to save the displayed numbers inside the nodule boxes. This we can do because 
        #no dict needs to be updated and only a few numbers needs to be updated.
        #The boxes are anyways going to be redrawn. Hence updating their text is not a problem.
        #The mapping to axial and sagital also need to follow the mapping index displayed to nodule dict.
        #But that mapping to axial and sagital is for image, hence no need to follow the mapping index displayed 
        #to nodule dict. The position of the nodule boxes should also be determined by the index displayed.
        #chk what all other mappings needs to be displayed.


#In general the delete must not change the save variables. The only case that is not implemented is the case when 
#currently i have changed the annotation or marking. the save to either one of them or two of them has not been saved.
#therefore, if the current nodule nodule is being deleted without saving then the save variable must be set to saved.
#because now the displayed image/images is/are empty and nothing is there which is unsaved. 
#And if the current nodule is being deleted after saving or the save has already been done then still there is no 
#harm in setting the save variables as saved.

#Reordering of nodules is an add on feature

#############@#####################    Nodule deletion ################################################
#############@#####################    delete Nodule   ################################################
#Easy Deletion
#-------------------------------------------------------------------------------------------------
#Save everything in the patient directory. Including annotation.
#888888888888888888888888888888888888888888888888888888888888888888888888
#make annotation saved in patient directory.

#Argument: Do I write the nodule dict index or nodule displayed index.
#There are 3 cases of a nodule display when a nodule gets deleted.
#Case 1: A nodule delete may occur when all nodules for an image are shown.
#        In this case just delete the nodule and update the currrently shown image 
#        but now one nodule less will be shown.
#Case 2: When all images for a nodule is  shown.
#        In this case delete the nodule. still display the images but without the
#        nodule.
#Case 3: When one image for a nodule is shown. 
#        In this case, delete the nodule. still show the image but without the 
#        nodule shown.
#In all of the above cases, after deleteing the nodule the image view is updated
#so that deleted nodule is not there. The highlight of remaining images and 
#nodules will not get affected.
#pseudocode delete_selected_nodule:
#1: chk that the nodule to be deleted is the displayed nodule otherwise ask for 
#   nodule display first.
#2: Let nodule display index y is to be deleted.
#3: Let nodule index in dict is x for displayed index y.
#4: delete the folder for dict index x.
#5: delte the annotation file for nodule x.
#5: redo mapping of nodule dict indices so that nodule display y+1 becomes 
#   nodule display y and so on.
#6: update image display for delete.
#
#pseudocode: delete the folder for dict index x
#1: get image names for this nodule from graph class.
#2: for all such image names:
#3:     delete directory for image name, nodule
#
#redo mapping pseudocode .
#1: Let nodule dict index x was deleted and the corresponding 
#   display index was y.
#2: hide annotation  window for this nodule.
#3: reinitialize the nodule class for this dict index x.
#4: delete nodule from graph class
#   update graph class to delete all edges incident at nodule x and delete nodule box x.
#   The edges incident at other nodule dict indices need not be changed.
#5: write img to nodule mapping
#5: update nodule index list and nodule shown
#6: delete entry x to y from mapping dict index to display index.
#7: delete entry y to x from mapping display index to dict index.
#8: update rest mapping. 
#9: write the updated mapping to file.
#the above steps again creats a confusion. the edges are wrt nodule dict index and if we change the nodule dict index 
#for a given displayed index then it will be a problem. Therefore we are not changing the nodule dict index for a 
#display index. Instead we are decrementing the display index when it is greater than deleted index(without changing 
#the corresponding dict index). And then this updated mapping needs to be written.
#9: redraw graph.
#
#pseudocode: update nodule index list and nodule shown
#nodule dict index(for display) refers to self.nodule_dict_index
#Argument: Will there be an error when followinh happens:
#a: self.nodule_dict_index is -1 and there are entries in self.nodule_dict_indices_shown_extra or when 
#b: self.nodule_dict_index is -1 and self.nodule_dict_indices_shown_extra is also empty.
#Case a: This case is covered by the case when multiple nodules are just shown and none is being marked.
#Case b: This case says that no nodule needs to be displayed. The redraw of currently displayed images will be done.
#        keep in mind that image names currently displayed will be displayed again and no need to consult nodule 
#        indices being displayed.
#1: add x to the list of free indices.
#2: remove x from the list of added indices.
#3: if nodule dict index(for display) is same as nodule dict index being deleted then:
#4:     set nodule dict index(for display) as -1.
#       Actually this was to be covered by the perform nodule selected and not directly setting 
#       the nodule dict index because other things also needs to be looked at when nodule index is being setup. 
#       I also need to check that whether perform nodule selected has also been called somewhere else in 
#       delete nodule.
#       PERFORM_NODULE_SELECTED is never performed in the delete_selected_nodule.
#       The readjusting of nodule indices also requires readjusting of self.nodule_dict_index.
#       update_nodule_index_list_and_nodule_shown also requires readjusting of self.nodule_dict_index.
#       The only extra thing that perform_nodule_selected requires is that it shows annotation window. this is not 
#       required when deletion is going on. hence current process of setting self.nodule_dict_index and readjusting 
#       nodule indices is fine.
#5: if nodule dict index being deleted lies in extra nodule shown then:
#6:     remove the nodule dict index being deleted from extra nodule shown
#
#pseudocode: update nodule index list and nodule shown(new):
#nodule dict index(for display) refers to self.nodule_dict_index
#1: add x to the list of free indices.
#2: remove x from the list of added indices.
#3: if nodule dict index(for display) is same as nodule dict index being deleted then:
#4:     set nodule dict index(for display) as -1.
#5: if nodule dict index being deleted lies in extra nodule shown then:
#6:     remove the nodule dict index being deleted from extra nodule shown
#7: readjust_nodule_indices
#8: chk_added_free_nodule_indices_correctness
#
#pseudocode: readjust_nodule_indices:
#1: if only one index in nodule_dict_indices_shown_extra and 
#   nodule_dict_index(display) is -1(i.e. no nodule there) then:
#2:     move that nodule index from nodule_dict_indices_shown_extra to nodule_dict_index(display).
#3: 
#
#pseudocode(update rest mapping)(based on data structure)
#This code also performs decrement the display index from y+1 to last by 1.
#This code also delete last entry from mapping display index to dict index, 
#i.e the entry for largest display index.
#1: for dict index(di) in the indices used:
#2:     Let mdi be the mapped display index.
#3:     chk that mdi is not y because that entry has been deleted.
#4:     if mdi > y:
#5:         decrement nodule display index and other things //%#update number display nodule dict mapping for delete
#6: chk both mapping equality
#
#pseudocode decrement nodule display index //%# update number display nodule dict mapping for delete:\
#1: let di be the dict index and mdi be the mapped display index.       
#2: new display index ndi = mdi-1.
#3: decrement mdi for di i.e. set mapping[di]=ndi
#4: set mapping ndi to di in mapping display index to dict index
#    mdi-1 may not be deleted earlier  because we donot know the order of display indices for traversal over indices.
#5: delete mapping for mdi from mapping display index to dict index
#6: update the text in the box for as ndi.
#7: set the nodule box coordiates as what should have been for ndi. (currently automatically computed at redraw.)
#
#pseudocode: delete edges for nodule(x)
#
#
#pseudocode: delete nodule from graph class
#1: delete all edges for that nodule.
#2: delete the nodule box.
#3: delete the nodule text.
#
#pseudocode: delete all edges incident at nodule x(Based on data structure)
#1: delete the entry for x from nodule to img
#2: for all entry e in img to nodule:
#3:     if x is in adjcaency list in the entry e.
#4:         delete x from that adjacency list.
#5: 
#
#pseudocode:update image display for delete
#1: get the number of image displayed currently
#2: If only one image displayed currently then:
#3:     Again display the image with nodule indices in nodule_dict_index or nodule_indices shown_extra.
#4: If multiple images shown:
#5:     Display those images without any nodule shown
#
#
#pseudocode:update image display for delete(new)
#1: get the number of image displayed currently
#2: Let all indices be result of collate all indices to display
#   (in SELF.nodule_dict_index and nodule_indices shown_extra)
#2: If only one image displayed currently then:
#3:     Again display the image with nodule indices in all indices.
#4: If multiple images shown:
#5:     Display those images without any nodule shown
#

#        keep in mind that image names currently displayed will be displayed again and no need to consult nodule 
#        indices being displayed.

#collate is erroneous it needs to corrected. update readjusting nodule indices in pseudocode.
#Actually the thing was that a single list of nodules was to be passed to add_given_list_of_nodules_to_image.
#Therefore the nodule index in self.nodule_dict_index was added to nodule_dict_indices_shown_extra. 
#But the index was not removed from self.nodule_dict_index. Having the same index at two places is not good.
#In fact, what I should have done is that I should have created a list of all indices from nodule dict index and the
#indices shown extra. that list should have been returned by collate indices.
#Also, after dlete operation, is it ok to have indices both in self.nodule_dict_indices_shown_extra and 
#self.nodule_dict_index. In fact, after delete operation(and just display is remaining), if multple nodules are shown
#then they will all be in self.nodule_dict_indices_shown_extra. And if only a single nodule has been left then that 
#will be in self.nodule_dict_index. This task is performed by readjust_nodule_indices. Therefore, do add the above 
#said condition as a check in the readjust_nodule_indices. In fact this checkshould have been done befor delete.
#But, during delete operation, self.nodule_dict_index was allowed to have a valid value as clear from certain 
#conditions. Also, if a person has added a nodule and the he is in the middle of marking or annotating that nodule 
#then the nodule can be deleted without even saving. but here again the same case is there that a single nodule is 
#being shown and that is deleted. 
#but the consideration was that, can self.nodule_dict_index can have a valid value when multiple nodules are shown 
#and one nodule is being deleted. By default, when multiple nodules are shown then self.nodule_dict_index is -1.
#But when after showing multiple nodules, if user starts changing one of the nodule then that nodule index will be 
#in self.nodule_dict_index. When multiple nodules are shown then changing the marking is not allowed, but the user
#can still show annotation window and do changes in annotation for that nodule.
#In this case, self.nodule_dict_index will be -1 for MULTIPLE NODULES SHOWN AND ONE nodule being deleted.
#Therefore, one simple solution is that just do concatenate the indices in self.nodule_dict_index and 
#self.nodule_dict_indices_shown_extra in the collate function. But one more observation says that, when initially 
#multiple nodules are shown and one nodule gets changed by the user and still the nodue has not been saved and the 
#nodule gets deleted.
#

#multiple nodule are shown, one nodulwe gets changed but the other nodule is asked by the user to delete. 

#If I can stop the annotation of a nodule when multiple nodules are shown.
#but the more advanced version will require even changing the boundary when multiple nodules are shown. 

#SELF.NODULE_DICT_INDEX AND NODULE SAVE status completelyt tells which nodule is under operation and whether 
#it is saved or not and what part is saved?
#when a nodule is changed and user tries to show annotation window or just hide the current annotation window when 
#the annotation is being changed then the warning can be raised that save current annotation before moving on. 
#this requires the show unsaved warning. After that a lot of issues will get solved.
#

#############@#####################  remove_nodule(graph) earlier comments #########################################
        #whenever a nodule gets deleted, if we add the feature of further nodules getting a number less then 
        #888888888888888888888888 compltete this function later.
        #we must move all the edges up, and also move the annotations saved. 
        #cURRENTLY, THE maintainance of index in nodule dict and nodule index displayed makes it easy to not to 
        #shift the annotations. 
        #The images has to be redrawn as some nodules will move up. The edges will be redrawn wrt their current 
        #number displayed.
        #A message should also be shown that the numbers below the deleted nodule are being moved up.
        #moving up of nodule boxes is important because it is convinient to the user.
        #we have saved the nodule index in the dict for the nodule. Also the edges has been saved as per 
        #the nodule index in dict. when a nodule gets deleted, there is also displayed index which got deleted. 
        #We have looked from that point of view. 
        #Whenever a displayed index(nodule) gets deleted, its associated edges will also get deleted.
        #correspondingly, we are deleting the edges for its nodule dict index.
        #the edges for the other boxes are not changed. 
        #hence, no need to reshift edges to another node. But nodule box renumbering and repositioning of 
        #nodule box is an issue that needs to be addressed. By just deleting the entry for the corresponding
        #nodule_dict_index, we don't need to renumber any other edges.
        #In fact even in the img to nodule mapping, we have nodule dict indices in the values 
        #for every image. this is a better option that does not require change to a lot of edges.
        #In this case, the graph class will also require reference to the mapping that has number displayed to 
        #index in nodule dict. that mapping is maintained by dicom annotator class. The graph class knows only 
        #the nodule indices in dict.
        #I still have to write the function that updates mapping number displayed to index in nodule dict.
        #Fot the case of nodule to box as well, we need to address how to update/view the key values of this dict,
        #i.e. the nodule indices. In this dict as well, we have nodule dict indices as the key values. 
        #Updating many keys of a dict is a hard task. Still, we have to update the numbers inside the nodule 
        #boxes and we have to save the displayed numbers inside the nodule boxes. This we can do because 
        #no dict needs to be updated and only a few numbers needs to be updated.
        #The boxes are anyways going to be redrawn. Hence updating their text is not a problem.
        #The pseudocode for redo mapping handles all this.
        #The mapping to axial and sagital also need to follow the mapping index displayed to nodule dict.
        #But that mapping to axial and sagital is for image, hence no need to follow the mapping index displayed 
        #to nodule dict. The position of the nodule boxes should also be determined by the index displayed.
        #chk what all other mappings needs to be displayed.

#######################################################################################################
# 8888888888888888888888888  show unsaved warning.  88888888888888888888
#######################################################################################################
#When multiple nodules are shown, one annotaion window gets updated and the user wants to move on to annotation
#window of another nodule then warning must be shown. when just the current annotation window is being closed then 
#also warning must be shown.
#How can 
#1: 
#dR DEVA CAN BE ASKED THAT not to change any nodule annotation when multiple nodules are shown. 
#Also, unsaved warning can be done later.  

#######################################################################################################
# 8888888888888888888888888   mouse Press  88888888888888888888888888888
#######################################################################################################
#when mouse press occurs over menu, does it update mouse constants? does it call mouse press event?
#If it does not call mouse press or mouse release event then everything is wrkingfine otherwise it may change the image name selected andthe mouse button pressed etc.
#Yes it it true that the click over right click menu does not generate any mouse event and it is handled by the 
#click menu sytem. hencethe system is working fine.


#chrome os installation
#*********************************************************************************
#!@#$%^&*()!@#$%^&*()!@#$%^&*()!@#$%^&*()

############################################################################################88888888888888888888888888888888888888888888888888
#A very good suggestion by Dinesh sir, multiple images on same screen. 
#This can be implemented in the following way.
#Initially, all images will be visible on the screen.
#When the user selects an image, then that image will be shown.
#The marking will be done on that image.
#When, from the bipartite graph, a user selects an image, then all the 
#nodules for that image will be shown.
#Or, when first a nodule is selected, then all the images in which that 
#nodule is marked, are shown.
#In futher continuation of this, whenever a user selects an image and 
#then a connected nodule, then the marked image for that nodule gets opened up and the corresponding annotation.
#When double click is done over an image, then the image will be 
#opened afresh for marking a new nodule.
#If an already marked nodule is to be added to an image, then 
#the user will drag a line from an image box to that nodule box.
#In this case, a line will be drawn from the image to that nodule.
#The annotation for that nodule will be loaded.
#The image will be loaded afresh for marking that nodule.
#The other images with that nodule marked will be shown in small at the 
#, overlapping the buttons.
#where these small images will be shown can be decided slightly later.

#there is more than one variable associated with the current 
#directory. Hence create a class current directory, with
#the required functions, inluding loading directory content
#and classifying them as image or video.
#The marked array i.e. which nodule has been marked to which image 
#should also be there in this class.
 
#whenever an image, is selected for marking an already marked nodule, 
#then, all the images with that nodule marked can be shown in small size 
#at the top of image label.  

#More thoughts about this can be there.

#Testing over chromeOS is remaining.
#Testing over images from Dinesh Sir is also remaining.

#extension for videos.
#The version can be exended for videos where on the left we can display the frame index and on the right will 
#be nodule as of now. The extension to the video can be done in a very straightforward manner.


#******************************************************
#               further extension fo image.
#We may allow any number of images in input folder. the set image will then become scrollable. The number of 
#nodules then will also have to be increased. Extra buttons have to be removed.
#Choice of color may be given to user.
#

###################################################################################################
#8888888 changes to improve code 88888888888888888888888888888888888888888888888888888888888888888888
####################################################################################################
#nodule_index_for_marking should be deleted. it is useless now.

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
import traceback
import math
import struct
import shutil
from PIL import Image



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
        #The pixmap refers to the pixelmap for the image. the
        #image size can be different from the label size.
        #hence, the offset gives the value for the offset
        #of image wrt label.
        #if image is small then the offset will be positive and if 
        #image is large then offset will be negative.
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

class Annotation_window(QtWidgets.QWidget):
    """
    This  is the annotation widget for every nodule.
    """
    def __init__(self, annotation_label_width, dropdown_width, info_height, 
        window_x, window_y, window_width, window_height, csv_file_handle, image_type_name, nodule_index):
        """
       
        Parameters
        ----------
        dicom_annotator_ref : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        super().__init__()    
        self._old_pos = None  # to track the mouse position 
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
        #This is the index in nodule dict
        self.nodule_index = nodule_index
        self.window_size_computed = False
        self.add_items_to_widget(annotation_label_width, dropdown_width, info_height)
        self.init_comboboxes()
        self.compute_sizes()    
        self.do_layout()
        #This is the dir path to save the annotation. The annotation will be saved in the patient directory.
        #Hence, the path cannot be saved initially. 
        self.dir_path = ""

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self._old_pos is not None:
            delta = event.globalPos() - self._old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self._old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = None

    def set_directory_path(self, dir_path):
        """
        This function will set the directory path required for saving the annotation.
        """
        self.dir_path = dir_path

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
        self.textbox1.textChanged.connect(self.update_save_status)
        self.textbox2.setText("Free text 2("+self.image_type_name+")")
        self.textbox2.textChanged.connect(self.update_save_status)
                
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
        self.update_save_status()

    def update_save_status(self):
        self.dicom_annotator_reference.reset_nodule_annotation_saved()
        self.dicom_annotator_reference.set_graph.highlight_nodules_consistently()
    
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
        self.combobox_bethesda_category.activated[str].connect(self.update_save_status)

        self.unset_all_echogenic_foci()
    
    def set_dicom_annotator_reference(self, dicom_annotator_reference):
        """
        The reference will be used to update variable that reflect that change has been done. 
        """
        self.dicom_annotator_reference = dicom_annotator_reference

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

        print("var of annotation window="+str(vars(self)))
        #str_to_write = self.input_filename+","+str(self.nodule_index)+","+composition_text+\
        #not writig input filename and nodule index as they are meaningless now.
        str_to_write = composition_text+\
                                       ","+echogenecity_text+","+shape_text+","+margin_text+","+\
                                       echogenic_foci_text+","+bethesda_text+","+textbox1_text+\
                                           ","+textbox2_text+"\n"
        file_name = "annotation_nodule_dict_index_"+str(self.nodule_index)+".csv" 
        file_path = PurePath(self.dir_path).joinpath(file_name)
        with open(file_path, "w") as annotation_file:
            annotation_file.write(str_to_write)
            annotation_file.flush()
        #self.csv_file_handle.write(str_to_write)        
        #self.csv_file_handle.flush()
        self.dicom_annotator_reference.set_nodule_annotation_saved()
        self.dicom_annotator_reference.set_graph.highlight_nodules_consistently()
        ##str_for_bin = "nodule_annotation\n"+str_to_write
        ##write_to_binary_file(binary_filehandle, convert_to_binary(str_for_bin))

    def del_annotation(self):
        file_name = "annotation_nodule_dict_index_"+str(self.nodule_index)+".csv" 
        file_path = PurePath(self.dir_path).joinpath(file_name)
        self.dicom_annotator_reference.directory_loaded.delete_file(str(file_path))
        self.reinitialize()
        
    def load_annotation(self):
        """
        The function loads the annotation from the df row loaded.
        """       
        file_name = "annotation_nodule_dict_index_"+str(self.nodule_index)+".csv" 
        file_path = PurePath(self.dir_path).joinpath(file_name)
        df = pd.read_csv(file_path, header=None)
        self.combobox_composition.setCurrentText(df[0][0])      
        self.combobox_echogenicity.setCurrentText(df[1][0])
        self.combobox_shape.setCurrentText(df[2][0])
        self.combobox_margin.setCurrentText(df[3][0])
        self.unset_all_echogenic_foci()
        self.set_all_echogenic_foci_checked_from_loaded(df[4][0])
        self.combobox_bethesda_category.setCurrentText(df[5][0])       
        self.textbox1.setText(df[6][0])
        self.textbox2.setText(df[7][0])
        self.update_tirad_single_combobox("updating at the time of reloading")
        self.dicom_annotator_reference.set_nodule_annotation_saved()

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
        self.dir_path = ""

class Nodule():
    """
    This class is used to represent a nodule.
    This class will have a menu for that nodule and a colour for that nodule.
    """
    def __init__(self, nodule_index, color, toolbarRef, dicom_annotator_ref):
        """
        The nodule index is the index of nodule added.        

        Parameters
        ----------
        nodule_index : TYPE
        dicom_annotator_ref is the reference of the class over which the action needs to be displayed.
            DESCRIPTION.

        Returns
        -------
        None.

        """
        # self.toolbar=QToolBar("Nodule "+str(nodule_index))
        #This is the index in nodule dict
        self.nodule_index = nodule_index
        self.color=color
        self.toolbarRef = toolbarRef
        self.dicom_annotator_ref = dicom_annotator_ref
        #The directory path will depend upon the directory opened. hence, it cannot be set initially.
        #When adding a nodule fresh, the directory path must be set.88888888888888888888888888888888888888888888
        self.dir_path = ""
        #The alpha dict is empty initially. Whenever an edge from an image to a nodule will be added, 
        #an entry will be added to the alpha_dict for that nodule. The key of the dict will be image_name
        #(same as that used in graph class). The corresponding value will the alpha channel of the required shape.
        #The deletion of a nodule will automatically remove the alpha for that nodule from further consideration.
        #Based on nodule dict index management the alpha will work in sync with the annotation marked by the user.
        self.alpha_dict = {}
        
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
    
    def del_annotation(self):
        self.annotation_window.del_annotation()

    def set_input_filename(self, input_filename):
        """
        The function will be called whenever add nodule is done so that the nodule and file specific parameters are set.
        This function has been designed wrt a single image or single video selected by the user.
        But, when a directory has been selected by the user then the annotation of a nodule does not depend on a 
        single image file. In fact, we should save the anotation nodule wise and not as done in earlier format
        having input and output filenames.
        """
        self.annotation_window.set_input_filename(input_filename)

    def set_directory_path(self, dir_path):
        """
        This function will set the directory path required for saving the annotation.
        """
        self.dir_path = dir_path
        self.annotation_window.set_directory_path(dir_path)

    def set_dicom_annotator_reference(self, dicom_annotator_reference):
        """
        The reference will be used to update variable that reflect that change has been done. 
        """
        self.annotation_window.dicom_annotator_reference = dicom_annotator_reference
        self.dicom_annotator_reference = dicom_annotator_reference

    def add_image_connection(self, image_name, alpha_shape):
        #This function adds an connection to an image. currently, self.alpha_dict needs to be updated for adding a 
        #connection.
        self.alpha_dict[image_name] = np.zeros(alpha_shape, dtype = np.uint8)

    def reinit_alpha(self, image_name):
        alpha_shape = self.alpha_dict[image_name].shape
        self.alpha_dict[image_name] = np.zeros(alpha_shape, dtype = np.uint8)

    def mark_polylines(self, line_list, image_name):
        cv2.polylines(self.alpha_dict[image_name], [np.array(line_list)], False, (1), thickness=2)        

    def draw_rect(self, tmp_rectangle_coordinates, image_name):
        cv2.rectangle(self.alpha_dict[image_name],\
                      (tmp_rectangle_coordinates[0],tmp_rectangle_coordinates[1]),\
                        (tmp_rectangle_coordinates[2], tmp_rectangle_coordinates[3]),\
                            (1), thickness=2)
        print("drawn rect to alpha")
        print("tmp_rectangle_coordinates="+str(tmp_rectangle_coordinates))
        print("image_name="+str(image_name))

    def remove_image_connection(self, image_name):
        #This function removes an connection to an image.
        assert image_name in self.alpha_dict, "image must already be connected to this nodule."
        del self.alpha_dict[image_name] 

    def get_alpha(self, image_name):
        return self.alpha_dict[image_name]

    def get_alpha_shape(self, image_name):
        return self.alpha_dict[image_name].shape

    def load_alpha(self, image_name, alpha):
        self.alpha_dict[image_name] = np.copy(alpha)

    def reinitialize(self):
        """
        This function is used to reinitialize all the values in the annotation window. 
        The function also sets the input filename to null. The input filename needs to be changed 
        when the annotation of a new file is done.
        The function will also hide the annotation window.
        """
        self.alpha_dict = {}
        self.dir_path = ""
        self.annotation_window.reinitialize()
        self.hide_annotation_window()

    def close_annotation_window(self):
        """
        This function closes the toolbar. This is required when the current video is over and the toolbar needs to be closed.
        """
        self.annotation_window.close_widget()
        self.showing_annotation_window = False
    
    def is_annotation_shown(self):
        return self.showing_annotation_window

    def show_annotation_window(self):
        """
        This function shows the toolbar when the action for that nodule takes place.
        """
        print("show window called for nodule "+str(self.nodule_index))
        if(self.showing_annotation_window):
            #The function did not show. it was already shown.            
            return False
        else:
            self.annotation_window.show()
            self.showing_annotation_window = True
            #returning true because the show has been done by this function call.
            return True

    def hide_annotation_window(self):
        """
        This function shows the toolbar when the action for that nodule takes place.
        """
        print("hide window called for nodule "+str(self.nodule_index))
        if(False == self.showing_annotation_window):
            #False is being returned because hide has not been done by this function. 
            #The window was already hidden.
            return False
        else:
            self.annotation_window.hide()
            self.showing_annotation_window = False
            #returning true because hide has been done by this function.
            return True

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
        global nodule_index_for_marking
        nodule_index_for_marking = self.nodule_index
    
    def load_annotation(self):
        self.annotation_window.load_annotation()

#Such class will be required to hold box data set
#A separate class for image names
#A separate class for nodules.

class My_Image():
    def __init__(self):
        self.x_start = 0
        self.y_start = 0
        self.width = 0
        self.height = 0
        self.qlabel_ref = None
        self.center_x = 0
        self.center_y = 0
        self.image = 0
        
    def fill(self, x_start, y_start, width, height, qlabel_ref):
        #These height and width and start and end correspond to the available space for displaying the image.
        #These are required when initializing the image with the given parameters. When setting the image 
        #directly, then these attributes have no sense initially. Hence, these were set to 0 at the time 
        #when images were loaded from the dicom objects.
        #we can later fill these values and decide whether to scale the image and how much to scale the image.
        #This may help in computing appropriate scaling for displaying multiple images.
        #Therefore, it seems better to have an alpha list over here. 
        #each element of the list will be an alpha channel.
        #since nodule addition and deletion is a process which is dependent upon the nodule dict and
        #deletion of a nodule will lead to deletion of all aplha channels for that nodule, hence it is better to 
        #have alpha dict(and not aplha array) in the nodule class.
        self.x_start = x_start
        self.y_start = y_start
        self.width = width
        self.height = height
        self.x_end = self.x_start + self.width
        self.y_end = self.y_start + self.height
        self.qlabel_ref = qlabel_ref
        self.center_x = (int)(self.x_start + (self.width)/2)
        self.center_y = (int)(self.y_start + (self.height)/2)
        print("fill called of my image")
        print("self.x_start="+str(self.x_start))
        print("self.y_start="+str(self.y_start))
        print("self.width="+str(self.width))
        print("self.height="+str(self.height))
        print("self.x_end="+str(self.x_end))
        print("self.y_end="+str(self.y_end))

    def init_image(self):
        """
        This function initializes the image for showing set for images and nodules that have been marked. 
        """ 
        self.b_r = 0
        self.b_g = 0
        self.b_b = 0
        self.image = np.zeros((self.height, self.width, 3),dtype=np.uint8)
        #self.image = np.ones((self.height, self.width, 3),dtype='uint8')
        print("Initialized the image for set")
        print("self.image.shape="+str(self.image.shape))
        #We are saving a copy so that at the time of reinitialize, we can get a fresh matrix from here so 
        #that we donot need to save the image again.
        self.image_saved = self.image.copy()

    def compute_scaling_factor(self):
        #If image height is more then the ratio will be less than one. If we multiply image height
        #by this ratio, then we get the desired height that is self.height.
        height_ratio = self.height/self.image.shape[0]
        #If image width is more then the ratio will be less than one. If we multiply image width
        #by this ratio, then we get the desired width that is self.width.        
        width_ratio = self.width/self.image.shape[1]
        #the above ratios can be treated as a scaling factor.
        #we will select the lesser ratio as a scaling factor.
        if ( width_ratio < height_ratio ):
            self.scaling_factor = width_ratio
        else:
            self.scaling_factor = height_ratio
        assert self.scaling_factor<1, "The scaling factor cannot be more than 1."

    def create_scaled_image(self):
        self.compute_scaling_factor()
        #Assume that fill has occurred already.
        #The scaling factor is not reqd when scaling up the alpha channel.
        self.image_scaled_shape = (int(self.image.shape[0]*self.scaling_factor),
                                           int(self.image.shape[1]*self.scaling_factor))            
        print("self.image_scaled_shape = "+str(self.image_scaled_shape))
        
        self.image_scaled_array = cv2.resize(self.image,
                                                   (self.image_scaled_shape[1],
                                                    self.image_scaled_shape[0]),
                                                     interpolation=cv2.INTER_AREA)            
        print("self.image_scaled_array.shape = " + str(self.image_scaled_array.shape))
        self.image_width_for_display = self.image_scaled_shape[1]
        self.image_height_for_display = self.image_scaled_shape[0]            

    def set_image(self, image, b_r, b_g, b_b):
        self.image = image
        self.image_saved = self.image.copy()
        self.b_r = b_r
        self.b_g = b_g
        self.b_b = b_b

    #def update_other_param(self):
    #    self.width = self.image.shape[1]
    #    self.height = self.image.shape[0]
    #    self.x_end = self.x_start + self.width
    #    self.y_end = self.y_start + self.height

    def get_saved_image(self):
        return self.image_saved

    def save_image(self, image_filename):
        """
        save the image
        888888888888888 TODO: call this save function after addition of an edge in the bipartite graph
        for the images and nodules.
        """
        cv2.imwrite(image_filename, self.image)    

    def reinit_image(self):
        #But anywat, we are copying again from image saved. Therefore, earlier np opes array 
        #is getting discarded. just leave the issue for now.
        self.image = self.image_saved.copy()

class Box():
    def __init__(self):
        self.x_left = 0
        self.y_top = 0
        self.width = 0
        self.height = 0
        self.text = ""
    
    def chk_if_point_in_range(self, x, y):
        if(x>=self.x_left_wrt_window and x<=self.x_right_wrt_window):
            if(y>=self.y_top_wrt_window and y<=self.y_bottom_wrt_window):
                return True
        return False

    def printBox(self):
        print("A box has been added with following details")
        # print(vars(self))

    def fill(self, img_x_left, img_y_top, x_left, y_top, width, height, text, b_r, b_g, b_b):
        self.img_x_left = img_x_left
        self.img_y_top = img_y_top
        self.x_left = x_left
        self.y_top = y_top
        self.width = width
        self.height = height
        self.text = text
        self.top_left = (self.x_left, self.y_top)
        self.x_right = self.x_left + self.width
        self.y_bottom = self.y_top + self.height
        self.x_left_wrt_window = self.img_x_left + self.x_left
        self.y_top_wrt_window = self.img_y_top + self.y_top
        self.x_right_wrt_window = self.img_x_left + self.x_right
        self.y_bottom_wrt_window = self.img_y_top + self.y_bottom
        self.bottom_right = (self.x_right, self.y_bottom)
        self.rectangle_color = (255, 255, 255) #white  #(255,0,0) #red
        self.thickness = 4
        self.edge_thickness = 1
        self.y_mid = (int)((self.y_top + self.y_bottom)/2)
        self.right_mid_point = (self.x_right, self.y_mid)
        self.left_mid_point = (self.x_left, self.y_mid)
        self.background_color =(b_r, b_g, b_b)
        self.x_left_outer_box = self.x_left - self.thickness
        self.x_right_outer_box = self.x_right + self.thickness
        self.y_top_outer_box = self.y_top - self.thickness
        self.y_bottom_outer_box = self.y_bottom + self.thickness
        self.top_left_outer = (self.x_left_outer_box, self.y_top_outer_box)
        self.bottom_right_outer = (self.x_right_outer_box, self.y_bottom_outer_box)
        self.outer_color = (255, 255, 255)
        self.second_outer_color_image = (255, 255, 0)
        self.outer_thickness = 4
        self.x_left_inner_box = self.x_left + self.thickness
        self.x_right_inner_box = self.x_right - self.thickness
        self.y_top_inner_box = self.y_top + self.thickness
        self.y_bottom_inner_box = self.y_bottom - self.thickness
        self.top_left_inner = (self.x_left_inner_box, self.y_top_inner_box)
        self.bottom_right_inner = (self.x_right_inner_box, self.y_bottom_inner_box)
        self.inner_color = self.background_color
        self.x_left_second_outer_box = self.x_left_outer_box - self.thickness
        self.x_right_second_outer_box = self.x_right_outer_box + self.thickness
        self.y_top_second_outer_box = self.y_top_outer_box - self.thickness
        self.y_bottom_second_outer_box = self.y_bottom_outer_box + self.thickness
        self.top_left_second_outer = (self.x_left_second_outer_box, self.y_top_second_outer_box)
        self.bottom_right_second_outer = (self.x_right_second_outer_box, self.y_bottom_second_outer_box)
        self.bottom_right_image_second_outer = (self.x_right_second_outer_box, self.y_bottom_outer_box)
        self.printBox()

    def set_rect_color(self,r,g,b):
        self.rectangle_color = (r, g, b)

    def clear_box(self, image_ref):
        cv2.rectangle(image_ref, self.top_left, self.bottom_right, \
            self.background_color, cv2.FILLED) # self.thickness)

    def draw(self, image_ref):
        cv2.rectangle(image_ref, self.top_left, self.bottom_right, \
            self.rectangle_color, self.thickness) #cv2.FILLED) # self.thickness)
        self.draw_text(image_ref)

    def clear_inner_portion(self, image_ref):
        cv2.rectangle(image_ref, self.top_left_inner, self.bottom_right_inner, \
            self.inner_color, cv2.FILLED) #cv2.FILLED) # self.thickness)

    def update_text(self, newText, image_ref):
        self.text = newText
        #before drawing text, the prev text must be undrawn. there is facility of undraw text in cv. Therefore, 
        #the best option is to draw a filled rectangle inside. It will be better if we maintain the state of the 
        #current box as highlighted or not highlighted. It will help in a lot of other tasks.
        #8888888888888888888888888888888888888888888888888
        self.clear_inner_portion(image_ref)
        self.draw_text(image_ref)

    def highlight(self, image_ref):
        cv2.rectangle(image_ref, self.top_left_outer, self.bottom_right_outer, \
            self.outer_color, self.outer_thickness) #cv2.FILLED) # self.thickness)

    def highlight_image_more(self, image_ref):
        cv2.rectangle(image_ref, self.top_left_outer,\
                self.bottom_right_image_second_outer, \
                self.second_outer_color_image, self.outer_thickness) #cv2.FILLED) # self.thickness)

    def highlight_second_outer(self, image_ref, color):
        #The color needs to be passed for the second outer box.
        cv2.rectangle(image_ref, self.top_left_second_outer, self.bottom_right_second_outer, \
            color, self.outer_thickness) #cv2.FILLED) # self.thickness)
    
    def undo_highlight_second_outer(self, image_ref):
        cv2.rectangle(image_ref, self.top_left_second_outer, self.bottom_right_second_outer, \
            self.background_color, self.outer_thickness) #cv2.FILLED) # self.thickness)
    
    def undo_highlight(self, image_ref):
        cv2.rectangle(image_ref, self.top_left_outer, self.bottom_right_outer, \
            self.background_color, self.outer_thickness) #cv2.FILLED) # self.thickness)

    def undo_highlight_image(self, image_ref):
        self.undo_highlight(image_ref)
        cv2.rectangle(image_ref, self.top_left_outer,\
                self.bottom_right_image_second_outer, \
            self.background_color, self.outer_thickness) #cv2.FILLED) # self.thickness)

    def draw_text(self, image_ref):
        # Define text content, font, font scale, and color
        font = cv2.FONT_HERSHEY_PLAIN #SIMPLEX
        font_scale = 1
        text_color = (255, 255, 255)  # White color in BGR format

        # Get text size to position it within the rectangle
        (text_width, text_height) = cv2.getTextSize(self.text, font, \
            font_scale, self.thickness)[0]

        # Calculate text placement coordinates (center of the rectangle)
        text_x = int(self.top_left[0] + \
            (self.bottom_right[0] - self.top_left[0] - text_width) / 2)
        text_y = int(self.top_left[1] + \
            (self.bottom_right[1] - self.top_left[1]) / 2 + text_height)
        text_thickness = 1
        # Add text to the image
        cv2.putText(image_ref, self.text, (text_x, text_y), font, \
            font_scale, text_color, text_thickness)

        #image_ref = cv2.rectangle(image_ref, (x1, y1 - 20), (x1 + w, y1), color, -1)
        #image_ref = cv2.putText(image_ref, label, (x1, y1 - 5),\
        #            cv2.FONT_HERSHEY_SIMPLEX, 0.6, text_color, 1)

    def draw_line_to_right_box(self, image_ref, right_box_ref, line_color):
        """
        This function will draw a line from the current box to right box.
        """
        cv2.line(image_ref, self.right_mid_point, \
            right_box_ref.left_mid_point, line_color, \
            self.edge_thickness) 

    def draw_line_to_given_point(self, image_ref, given_point):
        #A img box color line will be draw by default .
        cv2.line(image_ref, self.right_mid_point, \
            given_point, self.outer_color, \
            self.edge_thickness) 


class Graph():
    """
    In this case, the graph is a bipartite graph. 
    The graph object must also be initialized and reinit should be done 
    when reinitialize of dicom annotator is done.
    888888888888888888888 the axial/sagital drop down is necessary now.  
    For every node, I want to have, adjacent node index, box class,
    and the text written for that node. Hence, I can create a class for 
    that, instead of maintaing separate dictionaries.
    I need to make things simple. I seems a bit difficult to maintain it 
    that way. Hence, currently procedding with separate dictionaries.
    Whether an image has already a nodule added can bechecked through the 
    dict img_to_nodule 
    """
    def __init__(self, image_obj_ref):
        self.image_obj_ref = image_obj_ref
        self.image_ref = self.image_obj_ref.image 
        self.reinit()

    def reinit(self):
        self.numBoxesLeft = 0
        #I can maintain a birectional dict 
        #But that will complicate the process.
        #We can have multiple nodules for each image and multiple 
        #images for each nodule.
        #Hence, at first sight adjacency matrix seems appropriate.
        #But the matrix will be very sparse, hence again adjacency list 
        #approach seems more appropriate. 
        #We can maintain 2 array of lists.
        #one array is indexed by image index and the other array
        #is indexed by nodule index.
        #We need to maintain both the arrays simultaneously.
        #Currently, I have images in the order 1, 2, 3.
        #But that may not be the case in general.
        #Hence, for the image have a dict and for the nodules have an 
        #array.
        #the image to box has the box object for every image
        self.img_to_box = {}
        #This dict tells what text to be written for an image
        self.img_to_text = {}
        self.reinit_nodules()
        #I also need to keep a record of which marking belong to which 
        #nodule.
        #We have a separate folder for every image and every nodule.
        #We can can load alpha channels from each of these and display 
        #them simultaneously.
        #In any graph, we store the list of vertices and the adjacency 
        #list.
        #The adjacency list is maintained by the two dictionary above.
        #The node list for images is already there in directory.
        #hence keep a reference to directory in this class.
        #There no need to keep a separate node list for nodules.
        #The key list of nodule_to_img will give a list of nodules.
        #For every nodule added, there will be at least one image. 
        #Therefore, the key list of nodule_to_img is sufficient for 
        #keeping the list of nodules.
        self.dir_ref = None 
        #Here, I can keep a list for every image. The list will not be 
        #more than 4 in size, as it can be thought of.
        #Hence it is easier to have a list for every image.
        #There has to be an ordering of nodes in the graph. The imagelist
        #of the directory will provide the ordering.
        #For the case of nodules, the key will be an index value 0 to 
        #n, hence no need to keep an external ordering.
        #The num nodules itself is sufficient to iterate through
        #all nodules.
        #The dict itself will tell how many nodulles are present
        # Get the image ref to draw the required stuff
        self.info_width = 0
    
    def set_dicom_annotator_reference(self, dicom_annotator_reference):
        """
        Though, I will not be changing the dicts referred here, still I must check some time later that 
        whether changes done here get reflected to the original dict?
        """
        self.dicom_annotator_reference = dicom_annotator_reference
    
    def init_with_dir_ref(self, dir_ref, info_width, info_height):
        """
        Initialize the graph with the given directory.
        The dictionary img_to_nodule will be initialized with empty list 
        for every image. 
        """
        self.dir_ref = dir_ref
        self.info_width = info_width
        #Div by 3 is done to so as to have 3 column :
        
        #left box, gap, right box
        self.box_width = (int)(self.info_width/3)
        self.img_box_width = (int)(2*self.box_width)
        self.nodule_box_width = (int)(self.box_width*0.4)
        self.box_horizontal_gap =(int)(self.box_width*0.6)

        self.info_height = info_height
        self.box_height = self.info_height
        self.box_vertical_gap = (int)(self.box_height/2)
        self.box_height_with_gap = self.box_height + self.box_vertical_gap
        self.image_box_x_left = window_margin
        self.nodule_box_x_left = self.image_box_x_left + self.img_box_width\
            +self.box_horizontal_gap
        self.fill_img_to_nodule_txt_initially()
        self.fill_img_to_box_initially()
        self.draw_img_boxes_initially()
        self.selected_image_name = ""
        self.nodule_index_for_marking = -1
        ####################
        #Save the image after every addition of nodule.
        #Also have the flexibility to redraw the image after removal of a 
        #nodule.
        #888888888888888888
        #The saving of image with img boxes will be done later.

    def draw_nodule(self, nodule_index, nodule_display_index):
        #nodule_index is the index in dict.
        # newNumberToDisplay is the displayed index
        self.nodule_to_box[nodule_index] =  Box() 
        #The box position is obtained wrt the displayed index.
        box_y_pos = nodule_display_index*(self.box_height_with_gap)
        self.nodule_to_box[nodule_index].fill(self.image_obj_ref.x_start, \
                self.image_obj_ref.y_start, self.nodule_box_x_left, \
            box_y_pos, self.nodule_box_width, self.box_height, \
            self.nodule_to_text[nodule_index], self.image_obj_ref.b_r, self.image_obj_ref.b_g, \
                self.image_obj_ref.b_b)
        #We have to TAKE COLOR WRT THE DISPLAYED NODULE INDEX.  
        self.nodule_to_box[nodule_index].set_rect_color(\
                self.dicom_annotator_reference.color_dict[nodule_display_index][0],\
                self.dicom_annotator_reference.color_dict[nodule_display_index][1],\
                self.dicom_annotator_reference.color_dict[nodule_display_index][2])
        self.nodule_to_box[nodule_index].draw(self.image_ref)

    def special_highlight_image_boxes(self, image_name_highlight_more = ""):        
        """
        This is the function to hight images as per the requirement. 
        The pseudocode is special highlight image boxes.
        """
        self.undo_highlight_all_images()
        image_names_to_highlight = \
                self.dicom_annotator_reference.image_names_currently_displayed  
        for image_name in image_names_to_highlight:            
            self.img_to_box[image_name].highlight(self.image_ref)
        if(image_name_highlight_more!=""):
            self.img_to_box[image_name_highlight_more].\
                    highlight_image_more(self.image_ref)
        self.set_selected_image_name(image_names_to_highlight)
        self.draw_all_edges()

    def set_selected_image_name(self, image_names_to_highlight):
        """
        This function sets slected image name if only one image is displayed.
        """
        if(len(image_names_to_highlight)==1):
            self.selected_image_name = image_names_to_highlight[0]
        else:
            self.selected_image_name = ""

    def special_highlight_nodule(self):
        """
        This function will cover all cases of nodule highlighting.
        """
        self.undo_highlight_all_nodules()
        numNodulesToDisplay = self.dicom_annotator_reference.get_num_nodule_displayed()
        if(0 == numNodulesToDisplay):
            return
        dicom_annotator_nodule_dict_index = self.dicom_annotator_reference.nodule_dict_index
        self.highlight_all_nodule_shown_white_color(dicom_annotator_nodule_dict_index)
        self.handle_highlight_second_outer_case(dicom_annotator_nodule_dict_index, numNodulesToDisplay)

    def handle_highlight_second_outer_case(self, dicom_annotator_nodule_dict_index, numNodulesToDisplay):
        if(-1 != dicom_annotator_nodule_dict_index):
            self.highlight_second_outer_nodule_dict_index(dicom_annotator_nodule_dict_index)
        if(numNodulesToDisplay > 1):
            if(-1 == dicom_annotator_nodule_dict_index):
                #Any other nodule annotation window can be shown only if none of the nodule is being marked.
                #chk which nodule annotation window being shown.
                nodule_index_shown = self.dicom_annotator_reference.get_extra_nodule_index_window_shown()
                if(-1 != nodule_index_shown):
                    self.nodule_to_box[nodule_index_shown].highlight_second_outer(self.image_ref, (255, 255, 0))
       
    def highlight_all_nodule_shown_white_color(self, dicom_annotator_nodule_dict_index):
        if(-1 != dicom_annotator_nodule_dict_index):
            self.nodule_to_box[dicom_annotator_nodule_dict_index].highlight(self.image_ref)
        for nodule_index in self.dicom_annotator_reference.nodule_dict_indices_shown_extra:
            self.nodule_to_box[nodule_index].highlight(self.image_ref)

    def highlight_second_outer_nodule_dict_index(self, dicom_annotator_nodule_dict_index):
        """
        The index is in nodule dict
        """
        if(self.dicom_annotator_reference.is_nodule_saved()):
            self.nodule_to_box[dicom_annotator_nodule_dict_index].highlight_second_outer(self.image_ref, \
                    (255, 255, 0))
        else:
            self.nodule_to_box[dicom_annotator_nodule_dict_index].highlight_second_outer(self.image_ref, \
                    (255, 0, 0))
        
    def get_num_nodules_given_image(self, image_name):
        return len(self.img_to_nodule[image_name])

    def get_nodules_indices_in_dict_given_image(self, image_name):
        return self.img_to_nodule[image_name]

    def update_nodule_display_index(self, nodule_index, newNumberToDisplay):
        msg = "The nodule should be present already"
        if(not(nodule_index in self.nodule_to_img)):
            self.show_error(msg)
        if(not(nodule_index in self.nodule_to_box)):
            self.show_error(msg)
        if(not(nodule_index in self.nodule_to_text)):
            self.show_error(msg)
        self.nodule_to_text[nodule_index] = "n"+str(newNumberToDisplay) 
        self.draw_nodule(nodule_index, newNumberToDisplay)

    def add_nodule(self, nodule_index, newNumberToDisplay):
        """
        The function adds a nodule.
        All the dict for that nodule needs to be updated.
        #nodule_index will be provided by the nodule manager that is currently dicom annotator
        I should somehow decouple the number displayed on screen and what is being stored in the background.
        88888888888888888888888888888888888888888888888888888888888888
        This mapping is maintained by dicom annotator. chk whther everything working fine.
        In the function add nodule, the index passed is the displayed number. chk again.8888888888888
        It was planned to maintain the index in nodule dict for edges AS WELL keys for the nodule dicts.
        The same must be followed for the new addition and for case of update due to delete. Hence index passed
        to this function is nodule dict index.
        We are adding a nodule. Therefore, no mapping has this nodule index. Therefore, we obtain 
        newNumberToDisplay from the calling function.
        """ 
        assert not(nodule_index in self.nodule_to_img), "The nodule should not be present already"
        assert not(nodule_index in self.nodule_to_box), "The nodule should not be present already"
        assert not(nodule_index in self.nodule_to_text), "The nodule should not be present already"
        #initialize the list with this img_index
        #Further inspection is reqd for appending to list when more edges are added from other images aswell
        #here append should not have been called since we are adding a nodule and this is the first image
        #to which the nodule gets assigned. Later when we add edges to an existing nodule, at that time 
        #append will be called.
        #moved some statements to add_edge_img_nodule and called that function.
        #there shouldalso be a mapping image to nodule and that must alse be updated.
        #yes there is a mapping. do update that. done as follows.
        self.nodule_to_text[nodule_index] = "n"+str(newNumberToDisplay) 
        self.draw_nodule(nodule_index, newNumberToDisplay)
        #The add nodule should not add connection.
        #self.add_edge_img_nodule(image_name, nodule_index)

    def undo_highlight_nodule(self, nodule_index_undo_highlight):
        self.nodule_to_box[nodule_index_undo_highlight].undo_highlight(self.image_ref)
        self.nodule_to_box[nodule_index_undo_highlight].undo_highlight_second_outer(self.image_ref)

    def undo_highlight_all_nodules(self):
        #Now the nodule indices which have a meaningful reference may not be continuous. They are the indices in 
        #the nodule dict. Therefore, we now pick the keys from nodule_to_box itself.
        for index in self.nodule_to_box:
            self.undo_highlight_nodule(index)

    def highlight_again(self):
        self.special_highlight_image_boxes()
        self.highlight_nodules_consistently()

    def redraw_graph(self):
        self.image_obj_ref.reinit_image()
        self.image_ref = self.image_obj_ref.image 
        self.draw_img_boxes_initially()
        #print("drawn image boxes")
        for nodule_index in self.nodule_to_box:            
            nodule_display_index = \
                    self.dicom_annotator_reference.index_in_nodule_dict_to_number_displayed[nodule_index]
            self.draw_nodule(nodule_index, nodule_display_index)
        self.highlight_again()
        #Edges need to be drawn after highlighting the required. 
        #self.draw_all_edges()
        #redraw graph is called other situations when clearing of partial line draw is required. Hence it is 
        #better to retain the highlight info in the redraw itself.
        #88888888888888888888888888 complete highlight forthe nodule as well.
        #print("redraw complete")

    def remove_nodule(self, nodule_index):
        print("removing nodule "+str(nodule_index))
        #delete the edges drawn
        self.remove_edges_img_nodule(nodule_index)
        #clear the box drawn. 
        self.nodule_to_box[nodule_index].clear_box(self.image_ref)
        #delete the nodule box
        self.remove_key_from_dict(self.nodule_to_box, nodule_index)        
        self.remove_key_from_dict(self.nodule_to_text, nodule_index)
        
    def remove_nodule_from_img_to_nodule(self, nodule_index):
        for image_name in self.img_to_nodule:
            if(nodule_index in self.img_to_nodule[image_name]):
                prev_len = len(self.img_to_nodule[image_name])
                self.img_to_nodule[image_name].remove(nodule_index)
                new_len = len(self.img_to_nodule[image_name])
                if(new_len+1 != prev_len):
                    self.show_error("error in delete edge from img_to_nodule.")

    def remove_key_from_dict(self, mydict, mykey):
        if mykey in mydict:
            del mydict[mykey]
        else:
            msg = "key "+str(mykey) +" not found in "+str(mydict)
            self.show_error(msg)

    def remove_edges_img_nodule(self, nodule_index):
        print("remove all edges from images to the given nodule")
        self.remove_key_from_dict(self.nodule_to_img, nodule_index)
        self.remove_nodule_from_img_to_nodule(nodule_index)

    def addto_nodule_to_img(self, image_name, nodule_index):
        """
        The nodule index is the index in nodule dict.
        """
        if(nodule_index in self.nodule_to_img):
            self.nodule_to_img[nodule_index].append(image_name)
        else:
            self.nodule_to_img[nodule_index] = [image_name]

    def add_edge_img_nodule(self, image_name, nodule_index):
        """
        88888888888888888
        In this case, both the nodule and the img must be present already.
        directory for saving also needsto be created.
        """
        print("implement")
        self.chk_highlighted_image_same(image_name)
        #The img nodue dict needs to be updaed. done.
        self.img_to_nodule[image_name].append(nodule_index)
        #Adding the image name for that nodule. 
        self.addto_nodule_to_img(image_name, nodule_index)   
        #The edge needs to drawn. done.
        self.draw_edge(image_name, nodule_index)
        #if the noduke was not highlighted earlier, it should be highlighted now.8888888888888888888888888888888
        #In fact this nodule should not be highlighted earlier. I mean none of the nodule should be highlighted earlier. but what ifline is drawn when already a nodule is highlighted.88888888888888888888888888888888888888888888
        self.highlight_nodules_consistently()

    def highlight_nodules_consistently(self):
        self.special_highlight_nodule()
        #seems completed as per graph is concerned
        self.draw_all_edges()

    def isEdgeExistsAlready(self, image_name, nodule_index):
        #This is index in nodule dict.
        if(nodule_index in self.img_to_nodule[image_name]):
            return True
        else:
            return False

    def reinit_nodules(self):
        print("iterate and delete all nodules")
        self.numBoxesRight = 0
        #The nodules will be added dynamically. hence it is better
        #to have a dict for nodules as well.
        self.img_to_nodule = {}
        self.nodule_to_img = {}
        #The nodule to box has the box object for every nodule
        self.nodule_to_box = {}
        #This dict tells what text to be written for a nodule
        self.nodule_to_text = {}

    def remove_all_nodules(self):
        self.reinit_nodules()
        #The variables needs to be reinstantiated in the 
        #dicom annotator class. hence redraw should not be done now.
        #self.redraw_graph()

    def draw_edge(self, image_name, nodule_index):
        """
        Draw a line from img_index box to nodule_index box.
        This is the index in nodule dict
        """
        #get the box for img.
        #image_name = self.dir_ref.imageList[img_index][0]
        img_box_ref = self.img_to_box[image_name]
        nodule_box_ref = self.nodule_to_box[nodule_index]
        #get the index displayed.
        nodule_index_displayed = self.dicom_annotator_reference.get_displayed_nodule_index(nodule_index)
        #The color has to be taken wrt the index displayed.
        img_box_ref.draw_line_to_right_box(self.image_ref, nodule_box_ref, \
                self.dicom_annotator_reference.color_dict[nodule_index_displayed])

    def draw_all_edges(self):
        #draw lines for all edges
        for image_name in self.img_to_nodule:
            #In the following loop, we are correctly picking the nodule indices that corresponds to nodule dict.
            for nodule_index in self.img_to_nodule[image_name]:
                self.draw_edge(image_name, nodule_index)

    def fill_img_to_nodule_txt_initially(self):
        """
        The function fills empty adjacency list for images initially 
        when no nodule has been added.
        """
        for image_name in self.dir_ref.loadedImages:
            self.img_to_nodule[image_name] = []
            self.img_to_text[image_name] = str(image_name)

    def chk_img_to_nodule_empty(self):
        for image_name in self.dir_ref.loadedImages:
            if(len(self.img_to_nodule[image_name])>0):
                return False
        return True

    def update_image_txt(self, image_name, newText):
        self.img_to_text[image_name] = newText
        self.img_to_box[image_name].update_text(newText, self.image_ref)
        self.draw_all_edges()

    def fill_img_to_box_initially(self):
        """
        The function fills empty adjacency list for images initially 
        when no nodule has been added.
        """
        image_index = 0
        for image_name in self.dir_ref.loadedImages:
            self.img_to_box[image_name] = Box()
            box_y_pos = image_index*(self.box_height_with_gap)
            self.img_to_box[image_name].fill(self.image_obj_ref.x_start, \
                self.image_obj_ref.y_start, self.image_box_x_left, \
                box_y_pos, self.img_box_width, self.box_height, \
                self.img_to_text[image_name], self.image_obj_ref.b_r, self.image_obj_ref.b_g, \
                self.image_obj_ref.b_b)
            image_index = image_index + 1
    
    def draw_img_boxes_initially(self):
        image_index = 0
        if(self.dir_ref is not None):
            for image_name in self.dir_ref.loadedImages:
                self.img_to_box[image_name].draw(self.image_ref)
                image_index = image_index + 1
       
    def chk_highlighted_image_same(self, image_name):
        if self.selected_image_name != image_name:
            msg = "A line can be drawn from an already highlighted image only\n"
            msg = msg + " image_name selected currently for line draw = "+str(image_name)
            msg = msg + " image name highlighted already = "+str(self.selected_image_name)
            self.dicom_annotator_reference.show_error(msg)

    def draw_line_img_to_given_point(self, image_name, point):
        self.chk_highlighted_image_same(image_name)
        self.redraw_graph()
        #The earlier highlight image is taken care of redraw. #also needs to be highlighted. done
        #self.special_highlight_image_boxes()
        self.img_to_box[image_name].draw_line_to_given_point(self.image_ref, point)

    def get_image_name_for_mouse(self, x, y):
        """
        Chk if the mouse event for given x and y occurs over any image box. Also return the image  
        name in the image list for which this event has occurred.
        If the x and y are not within boundary of any image, then return empty string.
        """
        for image_name, image_box in self.img_to_box.items():
            if(image_box.chk_if_point_in_range(x, y)):
                #This is the name ofthe image and not image index
                #Will it be fine, if we use the name of the image and not the image index.
                #will further functions for adding edges etc work fine?
                #yes it is fine at this stage if we return the image name.
                #the function for adding edge will be even more convinient to use with image name
                #Also, currently, we were adding the image index to the adjacency list of nodule. 
                #But, at that time, we will be adding the image name to adjacency list of nodule. 
                #How will the records be added to csv then?88888888888888888888888888888888
                return image_name
        return "" 

    def get_nodule_index_in_dict_for_mouse(self, x, y):
        """
        Chk if the mouse event for given x and y occurs over any image box. Also return the image  
        name in the image list for which this event has occurred.
        If the x and y are not within boundary of any image, then return empty string.
        It should be checked which index dict or displayed should be returned.
        Even if we return nodule dict index, still it is not a problem because, we can anyways obtain the 
        nodule index displayed. 
        Therefore, we are returning index in nodule dict. Let the calling function decide how to handle it.
        """
        for nodule_index, nodule_box in self.nodule_to_box.items():
            if(nodule_box.chk_if_point_in_range(x, y)):
                return nodule_index
        return -1 

    def undo_highlight_all_images(self):
        for image_name, image_box in self.img_to_box.items():
            self.img_to_box[image_name].undo_highlight_image(self.image_ref)


class Directory():
    def __init__(self, dicom_annotator_reference):
        self.dicom_annotator_reference = dicom_annotator_reference
        self.reinit()

    def reinit(self):
        self.directoryPath=""
        self.numFiles=0
        self.fileList=[]
        #We can access the elements by index as well.
        #Also, python lists are internally arrays only.
        self.imageList=[]
        self.jpgImageList=[]
        #This is dict of dicom objects loaded for the files which were initially guessed
        #as images by the file size . index is image filename only
        self.image_dicom_obj_dict = {}
        #This is a dict of loaded images. key is image name and value is MyImage class.
        #888888888888888888888888888888888
        #update the graph code to do box creation based on this dict of loaded images.
        #anyways, index for image is not need any more and the image name will itself be used as the index. 
        self.loadedImages={}
        #8888888888888888888888888888
        #The list of output paths should also be here
        #should we leave the save paths as it is, or should we make a directory per nodule and 
        #have all marked images for that nodule in that folder.
        self.numVideos=0
        self.videoList=[]
        self.img_to_nodule={}
        self.video_threshold=10000000
        #This is a dict having the save paths foe every loaded image.
        #the dict will be having keys as the loaded image names and the value will be a list 
        #having the names corresponding to nodules 0 to 
        #This is a dict having the save paths foe every loaded image.
        #the dict will be having keys as the loaded image names and the value will be a list 
        #having the names corresponding to nodules 0 to 9.
        self.savePath_loadedImages = {}

    def load_dir(self, dir_path):
        #reinit before loading directory
        self.reinit()
        self.directoryPath = dir_path
        self.get_file_sizes()

        if(len(self.jpgImageList)):
            # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            for i in self.jpgImageList:
                print(i)
            # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            self.load_and_set_jpgImages()

        self.segregate_images_videos()
        #The images also need to be loaded in the memory. done
        self.load_all_image_dicom()
        self.load_all_images()
        #Do all the box creation here when the image dicom has been loaded.
        #888888888888888888888888888888888888888888888888888888
        #Also, if there is problem in loading a single image, just leave that image. it should not be like the 
        #complete directory does not get loaded due to that. And create a final list of images that actually 
        #got loaded. Do the box creation based on this final list.

    def get_file_sizes(self):
        files = sorted(os.listdir(self.directoryPath))
        print("files="+str(files))
        for file in files:
            path = os.path.join(self.directoryPath, file)
            if os.path.isfile(path):
                if path.lower().endswith(('.jpg', '.png','.jpeg')):
                    self.jpgImageList.append(path)
                else:
                    size = os.path.getsize(path)
                    print(f"{file}: {size} bytes")
                    self.fileList.append((file, size))
        self.numFiles = len(self.fileList)
        print("self.fileList="+str(self.fileList))
        print("self.numFiles="+str(self.numFiles))

    def segregate_images_videos(self):
        for fileWithSize in self.fileList:
            if( fileWithSize[1] > self.video_threshold ):
                self.videoList.append(fileWithSize)
            else:
                self.imageList.append(fileWithSize)
        self.numVideos = len(self.videoList) 
        print("self.imageList="+str(self.imageList))
        print("self.videoList="+str(self.videoList))
        print("self.numVideos="+str(self.numVideos))

    def load_all_image_dicom(self):  #load_all_images(self):
        for image_with_size in self.imageList:
            #This is the list of tuples to be removed from the image list
            #8888888888888888888888888888888888888888888
            #chk a case of monochromatic video where the file came to image list list due to small size and later
            #the file gets moved to video list. Chk both image list and video list in this case.
            image_name = image_with_size[0]
            #list_tuple_to_remove = []
            absolute_filename = PurePath(self.directoryPath).joinpath(image_name)            
            dicom_loaded_successfully = self.load_dicom_object(image_name, absolute_filename)
            if(dicom_loaded_successfully):
                #here do the guess and further segregation.
                dicom_type = self.guess_dicom_type(image_name)
                if(dicom_type[1]=="video"):
                    self.videoList.append(image_with_size)
                    #list_tuple_to_remove.append(image_with_size)
            #else:
                #the dicom was not loaded. hence the tuple needs to be removed.
                #the tuple needs to be removed
                #list_tuple_to_remove.append(image_with_size)
            #remove all such tuples at the end
        #not removing entries from image list. further, we will be working with image_dicom_obj_dict.
        assert(len(self.image_dicom_obj_dict)<=len(self.imageList)), \
                "number of loaded dicom can be at most the number of images guessed."

    def load_dicom_object(self, image_name, absolute_filename):
        """
        Loads dicom object. common to both image and video.

        Returns
        -------
        None.

        """

        print("filename to load = "+ str(absolute_filename))            
        try:
            dicom_obj = pydicom.dcmread(absolute_filename)
            dicom_pixel_array_shape = dicom_obj.pixel_array.shape
            print("dicom_pixel_array_shape = "+str(dicom_pixel_array_shape))
            #Also checking that whether photometric interpretation is present.
            photometricInterpretation = dicom_obj.PhotometricInterpretation.lower()
            print("photometricInterpretation = "+str(photometricInterpretation))
        except Exception as e :
            #returning false as there was a problem in loading the dicom object.
            #8888888888888888888888888888888888888888888888888888
            #do log in log file
            print("error in loading dicom for file "+str(absolute_filename))
            print("the exception is "+str(e))
            print("it may also be the case that pixel_array or photometricInterpretation is missing.")
            return False
        #setting the value in dict only after it is sure that the dicom object has been loaded 
        self.image_dicom_obj_dict[image_name] = dicom_obj
        print("self.image_dicom_obj_dict["+image_name+"]="+str(self.image_dicom_obj_dict[image_name]))

        try:
            print("self.image_dicom_obj_dict[image_name].is_implicit_VR before any changes= "+\
                  str(self.image_dicom_obj_dict[image_name].is_implicit_VR))
        except AttributeError as e:
            print("attribute not found "+str(e))
        #self.load_and_set_image(image_name)
        #returning true because the dicom object has been loaded successfully.
        return True
        # print("flush after frame shape print")
        # sys.stdout.flush()    

    def get_dicom_object(self, image_name):
        return self.image_dicom_obj_dict[image_name]

    def load_all_images(self):
        for image_name in self.image_dicom_obj_dict:
            dicom_type = self.guess_dicom_type(image_name)
            if(dicom_type[1]=="image"):
                self.load_and_set_image(image_name)
        assert len(self.loadedImages)<=len(self.image_dicom_obj_dict) + len(self.jpgImageList), "number of images loaded cannot be more than the number of dicom loaded."
    
    
    def load_and_set_jpgImages(self):
        '''
        this function is used to load 
        '''
        # print("****************************!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        for i in self.jpgImageList:
            print(i)
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        for image_path in self.jpgImageList:
            # print("image path inside function is !!!!!!!!!!!!!!!! : ", image_path)
            image_loaded= Image.open(image_path)
            image_loaded = np.array(image_loaded)
            imageName = os.path.basename(image_path)
            self.loadedImages[imageName] = My_Image()
            self.loadedImages[imageName].fill(0, 0, 0, 0, None)
            self.loadedImages[imageName].set_image(image_loaded, 0, 0, 0)
        return True
        
    def load_and_set_image(self, image_name):
        #Here I need to call image type and if the earlier guess of image type was incorrect 
        #Then the image should be moved to the set of videos.
        #But, then I must iterating directly over image list.
        try:
            image_loaded = self.get_image(image_name)
        except Exception as e:
            print("There was a problem in image format conversion for "+image_name)
            print("the exception is "+str(e))
            return False
        #creating dict entry only after the image has been loaded successfully.
        self.loadedImages[image_name] = My_Image()
        self.loadedImages[image_name].fill(0, 0, 0, 0, None)
        self.loadedImages[image_name].set_image(image_loaded, 0, 0, 0)
        return True

    def get_saved_image(self, image_name):
        return self.loadedImages[image_name].get_saved_image()

    def delete_file(self, filename):
        """
        Deletes a non-empty directory and all its contents.

        Args:
            file_path (str): The path of the file to be deleted.
        """
        file_path = PurePath(self.directoryPath).joinpath(filename)
        try:
            # Check if the provided directory exists
            if not os.path.exists(file_path):
                msg = "Error: The file "+file_path+" does not exist."
                self.dicom_annotator_reference.show_error(msg)

            # Check if the provided path is a directory
            if os.path.isdir(file_path):
                msg = "Error: The path "+file_path+" is a directory."
                self.dicom_annotator_reference.show_error(msg)

            # Use shutil.rmtree to delete the directory and all its contents
            os.remove(file_path)
            print(f"Directory '{file_path}' and all its contents have been deleted.")
        except PermissionError:
            msg = "Error: Permission denied to delete "+file_path+"."
            self.dicom_annotator_reference.show_error(msg)
        except OSError as e:
            msg = "Error: "+str(e.strerror)+" while trying to delete "+file_path
            self.dicom_annotator_reference.show_error(msg)
        except Exception as e:
            msg = "Unexpected error: "+str(e)
            self.dicom_annotator_reference.show_error(msg)

    def load_file(self, filename):
        file_path = PurePath(self.directoryPath).joinpath(filename)
        try:
            # Check if the provided directory exists
            if not os.path.exists(file_path):
                return []
            # Check if the provided path is a directory
            if os.path.isdir(file_path):
                msg = "Error: The path "+file_path+" is a directory."
                self.dicom_annotator_reference.show_error(msg)
            return self.read_table_from_file(file_path)
        except PermissionError:
            msg = "Error: Permission denied to delete "+file_path+"."
            self.dicom_annotator_reference.show_error(msg)
        except OSError as e:
            msg = "Error: "+str(e.strerror)+" while trying to delete "+file_path
            self.dicom_annotator_reference.show_error(msg)
        except Exception as e:
            msg = "Unexpected error: "+str(e)
            self.dicom_annotator_reference.show_error(msg)

    def read_table_from_file(self, file_path):
        """Reads a table from a file with a variable number of columns.

        Args:
            file_path: The path to the file.

        Returns:
            A list of lists, where each inner list represents a row of the table.
        """

        table = []
        with open(file_path, 'r') as f:
            for line in f:
                row = line.strip().split()  # Split line by whitespace
                table.append(row)
        return table

    def chk_if_nodule_image_alpha_written(self, image_name, nodule_dict_index):
        """
        This function checks if the nodule alpha for an image has been written
        """
        frame_dir_path = self.get_frame_file_path(image_name, nodule_dict_index)
        if (not( self.chk_directory_if_exists(frame_dir_path) )):
            return False
        frame_file_name = "frame_"+str(0)+"_marked.npy"
        frame_filepath = PurePath(frame_dir_path).joinpath(frame_file_name)
        print("frame_filepath="+str(frame_filepath))
        if(self.chk_file_if_exists(frame_filepath)):
            return True
        return False

    def chk_file_if_exists(self, directory_path):
        """
        checks if a file exists.

        Args:
            directory_path (str): The path of the directory to be checked.
        Return:
            True if the file exists, false otherwise.
        """
        try:
            # Check if the provided path is a directory
            if os.path.isdir(directory_path):
                msg = "The path "+str(directory_path)
                msg = msg +" exists but is a directory."
                self.dicom_annotator_reference.show_error(msg)
                return False
            else:
                if os.path.exists(directory_path):
                    return True
        except PermissionError:
            msg = "Error: Permission denied to read "+directory_path+"."
            self.dicom_annotator_reference.show_error(msg)
        except OSError as e:
            msg = "Error: "+str(e.strerror)+" while trying to read "+directory_path
            self.dicom_annotator_reference.show_error(msg)
        except Exception as e:
            msg = "Unexpected error: "+str(e)
            self.dicom_annotator_reference.show_error(msg)

    def chk_directory_if_exists(self, directory_path):
        """
        checks if a directory exists.

        Args:
            directory_path (str): The path of the directory to be checked.
        Return:
            True if the directory exists, false otherwise.
        """
        try:
            # Check if the provided path is a directory
            if os.path.isdir(directory_path):
                return True
            else:
                if os.path.exists(directory_path):
                    msg = "The path "+str(directory_path)
                    msg = msg +" exists but is not a directory."
                    self.dicom_annotator_reference.show_error(msg)
                return False
        except PermissionError:
            msg = "Error: Permission denied to read "+directory_path+"."
            self.dicom_annotator_reference.show_error(msg)
        except OSError as e:
            msg = "Error: "+str(e.strerror)+" while trying to read "+directory_path
            self.dicom_annotator_reference.show_error(msg)
        except Exception as e:
            msg = "Unexpected error: "+str(e)
            self.dicom_annotator_reference.show_error(msg)

    def delete_directory(self, directory_path):
        """
        Deletes a non-empty directory and all its contents.

        Args:
            directory_path (str): The path of the directory to be deleted.
        """
        try:
            # Check if the provided directory exists
            if not os.path.exists(directory_path):
                msg = "Error: The directory "+directory_path+" does not exist."
                self.dicom_annotator_reference.show_error(msg)

            # Check if the provided path is a directory
            if not os.path.isdir(directory_path):
                msg = "Error: The path "+directory_path+" is not a directory."
                self.dicom_annotator_reference.show_error(msg)

            # Use shutil.rmtree to delete the directory and all its contents
            shutil.rmtree(directory_path)
            print(f"Directory '{directory_path}' and all its contents have been deleted.")
        except PermissionError:
            msg = "Error: Permission denied to delete "+directory_path+"."
            self.dicom_annotator_reference.show_error(msg)
        except OSError as e:
            msg = "Error: "+str(e.strerror)+" while trying to delete "+directory_path
            self.dicom_annotator_reference.show_error(msg)
        except Exception as e:
            msg = "Unexpected error: "+str(e)
            self.dicom_annotator_reference.show_error(msg)

    def delete_dir(self, image_name, nodule_index):
        dir_path = str(self.savePath_loadedImages[image_name][nodule_index]) 
        self.delete_directory(dir_path)

    def create_dir(self, image_name, nodule_index):
        self.chk_dir_does_not_exist_already(image_name, nodule_index)
        self.savePath_loadedImages[image_name][nodule_index].mkdir()

    def define_save_path(self, max_num_nodules):
        for image_name in self.loadedImages:
            self.savePath_loadedImages[image_name] = []
            for nodule_index in range(max_num_nodules):
                foldername_extension = "_frames_nodule_"+str(nodule_index)
                #now the color is a tuple hence removing the color name from
                #directory name reated
                save_path = Path(PurePath(self.directoryPath).joinpath(\
                        image_name + foldername_extension))
                print("save_path = "+str(save_path))
                self.savePath_loadedImages[image_name].append(save_path)
            assert(len(self.savePath_loadedImages[image_name]) == max_num_nodules),\
                    " path for all nodules should have been created." 

    def get_folders_present_list(self, max_num_nodules):
        """
        This function returns a list of folders present in the directroy for 
        the saved iamges. 
        """
        result = []
        for image_name in self.loadedImages:
            for nodule_index in range(max_num_nodules):
                foldername_extension = "_frames_nodule_"+str(nodule_index)
                #now the color is a tuple hence removing the color name 
                #from directory name reated
                save_path = Path(PurePath(self.directoryPath).joinpath(\
                        image_name + foldername_extension))
                print("save_path = "+str(save_path))
                if(self.chk_directory_if_exists(save_path)):
                    result.append(save_path)
        return result

    def get_frame_file_path(self, image_name, nodule_index):
        """
        should nodule index be the name displayed or the nodule dict index.
        Actually, the displayed index is the ni on the image. 
        The annotation window has the nodule dict index.
        The displayed index can be different from the nodule dict index.
        The edges drawn are also wrt the displayed names. The edges drawn needs to be updated whenever a nodule 
        gets deleted. Also, the color will be picked wrt the number displayed on the screen.
        But, the annotation is wrt the index in the nodule dict. The user wants to save an image marking wrt the 
        nodule displayed.
        The directory path, as earlier will be wrt the index in the nodule dict. Therefore, the nodule index 
        passed to this function must be the index in the nodule dict. The reason is that the directory path 
        discussed in earlier discussion is same as the frame file path. I may think that it is possible to pass 
        displayed nodule number to this function.But, due to nodule deletion, it may happen that the displayed
        nodule index is different from the index written in directories saved earlier. Therefore, as discussed
        earlier the index written on the directory name can be different from the index displayed to the user 
        and we also save a mapping from the index displayed to the index written on the directory. 
        Hence, as per that discussion, nodule_dict_index which is equivalent to the directory index must be 
        passed to this function. 
        """
        return self.savePath_loadedImages[image_name][nodule_index]

    def chk_dir_does_not_exist_already(self, image_name, nodule_index):
        assert (False == self.savePath_loadedImages[image_name][nodule_index].is_dir()),\
                "The directory for "+image_name+" with nodule "+str(nodule_index)+" should not exist"
        assert (False == self.savePath_loadedImages[image_name][nodule_index].is_file()),\
                "The file for "+image_name+" with nodule "+str(nodule_index)+" should not exist"

    def whether_monochromatic_by_PhotometricInterpretation(self, dicom_obj):
        photometricInterpretation = dicom_obj.PhotometricInterpretation.lower()
        if(("monochrome" in photometricInterpretation) or ("gray" in photometricInterpretation)):
            return True
        else:
            return False

    def guess_dicom_type(self, image_name):
        """
        bits allocated and bits stored also have an important role in guessing image type.
        if the bits alocated and the bits stored have the same value, the we can apply the standard procedured 
        for extracting the image i the rgb format.
        If the bits stored is less than bits allocated, then we have to manually extract the sub pixel array
        or check if the standard procedure works forthem as well.
        bits allocated and bits stored is a little bit confusing.
        Even in an rgb image, the bits allocated and bits stored is 8. And the high bit is 7.
        This means that the setting has been left unchanged as for the case of monochrome.
        BitsAllocated may be per channel because even the google gemini allows 8 as valid value for 
        bits allocated for the case of rgb image.

        The sample per pixel seem to represent correct value for number of channels.
        It was 1 in an an monochrome image and it was 3 in an rgb image. the ybr has not been tested yet.
        This can also be looked at later on.

        Based on the official documentation of pydicom at:
        https://pydicom.github.io/pydicom/stable/guides/glossary.html
        The following quote: 
        Allowed values: 'MONOCHROME1', 'MONOCHROME2', 'PALETTE COLOR', 'RGB', 'YBR_FULL', 'YBR_FULL_422', 'YBR_PARTIAL_420', 'YBR_ICT', 'YBR_RCT', however restrictions apply based on the Transfer Syntax UID, and further constraints may be required by the IOD.

        (0028,0006) Planar Configuration
        Required when Samples per Pixel is greater than one, this indicates the order of the samples used by the pixel data, as either:

        As per the above quote, transfer sytax uid, iod and planar configuration is required to handle all possible cases. 88888888888888888888888888888888888888888888888888.  These will be looked at last.
        https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.3.html#sect_C.7.6.3.1.2
        The above is good link for a better understanding.
        https://www.medicalconnections.co.uk/kb/Photometric-Interpretations
        The above link is also useful.
        https://www.kaggle.com/code/dskagglemt/basic-understanding-on-dicom-convert-to-numpy


        Also, the conversion is working well for following transfer synatx:
        (0002, 0010) Transfer Syntax UID                 UI: JPEG Lossless, Non-Hierarchical, First-Order Prediction (Process 14 [Selection Value 1])

        But what if the transfer syntax happens to be jpeg compressed or any other type?
        can we still directly work with the pixel data?

        what is  VOI LUT Module? how much useful it is in guessing image type and performing the conversion?
        I am not able to understand this. this may be looked at later.
        #999999999999999999999999999999999999999999999999999

        Can the convert_color_space of pydicom util handle monochrome or pallete color? try`. 

        Now write the code considering in mind that the conversion possible from known cases can be done. 

        """
        dicom_obj = self.image_dicom_obj_dict[image_name]
        numFramePresent=False
        pixel_array_shape = dicom_obj.pixel_array.shape
        if ('NumberOfFrames' in dicom_obj):
            #This dicom_obj has multiple frames. hence it cannot be monochromatic
            numFramePresent = True
            #return False
        monochromatic = self.whether_monochromatic_by_PhotometricInterpretation(dicom_obj)
        
        if(monochromatic and (False == numFramePresent)):
            assert len(pixel_array_shape) == 2, "The pixel array shape has to be two in this case."
            return ["monochromatic", "image"]
        elif(monochromatic and numFramePresent):
            assert len(pixel_array_shape) == 3, "The pixel array shape has to be three in this case."
            return ["monochromatic", "video"]
            #There is a possibility of monochromatic video.
            #88888888888888888888888888888888888 consider all possible cases.
            assert False == numFramesPresent, "num frames cannot be present in monochromatic"
            assert len(pixel_array_shape) == 2, "The pixel array shape has  "
            return True
        elif((False == monochromatic ) and (False == numFramePresent)):
            assert len(pixel_array_shape) == 3, "The pixel array shape has to be three in this case."
            #9999999999999999999999999999999999999999999999999999999 
            #for pallate image we may have 2 channel as well. This will effect the guess for image 
            #as well guess for pallete video. 
            #complete this by checking a few cases of pallate images and video.
            return ["multicolor", "image"]
        elif((False == monochromatic ) and (numFramePresent)):
            assert len(pixel_array_shape) == 3, "The pixel array shape has to be three in this case."
            return ["multicolor", "video"]

    def get_image(self, image_name):      
        #cv2 provides only gray to rgb and vice versa. hence cv2 will not be of much help.
        #999999999999999999999999999999999999999999999
        #Look at how to do mono chrome 1 and 2 differently.
        #test the difference on garima dhupper itself.
        #today focus only on difference between monochrome1 and monochrome2 and implement those.
        #Look at all other formats later on.
        #try the implementation of both monochrome 1 and 2 for garima dhupper.
        #chk the difference in display.
        pixel_array = self.image_dicom_obj_dict[image_name].pixel_array 
        photometric_interpretation = self.image_dicom_obj_dict[image_name].PhotometricInterpretation
        if("rgb" in photometric_interpretation.lower()):
            image = pixel_array
        elif('YBR_FULL' == photometric_interpretation):
            image = util.convert_color_space(pixel_array,'YBR_FULL','RGB') 
        elif('YBR_FULL_422' == photometric_interpretation):
            image = util.convert_color_space(pixel_array,'YBR_FULL_422','RGB')
        #The pallate code is from gemini. must be tested
        #now the pallete code is from pydicom website. still, it must be tested.
        #8888888888888888888888888888888888888888888888888888888888
        # Handle Palette Color with pydicom's apply_color_lut (may not work for all)
        elif photometric_interpretation == "PALETTE COLOR":
            image = util.apply_color_lut(pixel_array, self.image_dicom_obj_dict[image_name]) 
        elif("monochrome2" == photometric_interpretation.lower()):
            #this is normal monochrome.
            image = cv2.cvtColor(pixel_array,cv2.COLOR_GRAY2RGB)
        elif("monochrome1" == photometric_interpretation.lower()):
            image = cv2.cvtColor(pixel_array,cv2.COLOR_GRAY2RGB)
            #subtracting from 255 because monochrome1 is reverse monochrome.
            image = 255 - image
            assert (image>=0).all(), " all values must still be positive"
        elif("gray" in photometric_interpretation.lower()):
            image = cv2.cvtColor(pixel_array,cv2.COLOR_GRAY2RGB)
        else:
            print("unknown file type")
            raise Exception("unknown file type")
            #sys.exit(0)
        return image


class ImagePaneManager():
    def __init__(self, totalWidth, totalHeight, img_x_left, img_y_top, dicom_annotator_reference):
        #The box matrix is the matrix of boxes. 
        # This is what was was required.
        # Having a separate class reduces load of functions from dicom annotator class.
        #coordinates are for total image.
        self.reinit()
        self.total_width = totalWidth
        self.total_height = totalHeight
        self.img_x_left = img_x_left
        self.img_y_top = img_y_top
        self.dicom_annotator_reference = dicom_annotator_reference

    def reinit(self):
        self.box_matrix = []
        self.image_names = []
        self.dict_image_index_box_matrix_index = {}
        self.dict_box_matrix_index_image_index = {}
        self.num_images = 0
        self.num_panes =0
        self.pane_width = 0
        self.pane_height = 0

    def init_image_names(self, image_names):
        self.image_names = image_names.copy()
        self.num_images = len(self.image_names)

    def get_next_even(self, n):
        if(0 == n%2):
            return n
        else:
            return n+1

    def compute_box_coordinates(self, row_index, col_index):
        pane_x = (col_index)*self.pane_width
        pane_y = (row_index)*self.pane_height
        return (pane_x, pane_y)

    def set_box_coordinates_all(self):
        for row_index in range(self.num_rows):
            for col_index in range(self.num_columns):
                (x_left, y_top) = self.compute_box_coordinates(row_index, col_index)
                self.box_matrix[row_index][col_index].fill(\
                        self.img_x_left, self.img_y_top,\
                        x_left, y_top, self.pane_width,\
                        self.pane_height, "", 0, 0, 0)

    def get_box_index_given_x_y(self, x, y):
        row_index = math.floor(y/self.pane_height)
        col_index = math.floor(x/self.pane_width)
        return row_index, col_index

    def get_image_name_given_x_y(self, x, y):
        row_index, col_index = self.get_box_index_given_x_y(x, y)
        image_index =\
                self.dict_box_matrix_index_image_index[(row_index, col_index)]
        image_name = self.image_names[image_index]
        return image_name

    def divide_into_panes(self):
        self.num_panes = self.get_next_even(self.num_images)
        self.num_rows = 2
        self.num_columns = (int)(self.num_panes/2)
        self.pane_width = (int)(self.total_width/self.num_columns)
        self.pane_height = (int)(self.total_height/self.num_rows)
        print("self.pane_width=")
        print(self.pane_width)
        print("self.pane_height=")
        print(self.pane_height)
        self.box_matrix = self.create_matrix(self.num_rows, self.num_columns)
        self.set_box_coordinates_all()
        self.assign_images_to_panes()

    def fill_panes(self, nodule_index):
        """
        This function creats resized images along with their alpha channels and sticthes them to create the image
        to be displayed. the stitched image is then returned.        
        """
        #merged_images = []
        #image_index = 0
        output_image = np.zeros((self.total_height, self.total_width, 3), dtype=np.uint8)  
        print("output_image.shape = ")
        print(output_image.shape)
        print("self.image_names=")
        print(self.image_names)
        print("nodule_index=")
        print(nodule_index)
        for image_index in range(len(self.image_names)):
            #for image_name in self.image_names:
            image_name = self.image_names[image_index]
            print("image_name=")
            print(image_name)
            orig_image = self.dicom_annotator_reference.directory_loaded.loadedImages[image_name].image.copy()
            if(-1 !=nodule_index):
                merged_image =\
                        self.dicom_annotator_reference.\
                        add_alpha_to_single_image(\
                        orig_image, image_name, nodule_index) 
                print("merging of image is done\n\n")
            else:
                merged_image = orig_image
                print("merging of image is not done\n\n")
            merged_image = merged_image.astype(np.uint8)
            print("merged_image.dtype = "+str(merged_image.dtype))
            print("merged_image.shape = "+str(merged_image.shape))
            scaled_image = cv2.resize(merged_image, (self.pane_width, self.pane_height))
            print("scaled_image.shape = "+str(scaled_image.shape))
            start_row, end_row, start_col, end_col = \
                    self.get_start_end_for_image(image_index)
            print(start_row)
            print(end_row)
            print(start_col)
            print(end_col)
            print("output_image[start_row:end_row, start_col:end_col].shape = ")
            print(output_image[start_row:end_row, start_col:end_col].shape)
            output_image[start_row:end_row, start_col:end_col] = \
                    scaled_image
            #image_index = image_index + 1
            ## Assuming 3 channels (RGB) 
            #output_image = np.zeros((self.total_width, self.total_height, 3), dtype=np.uint8)  
            #for image_index in range(self.num_images): 
            #    print("scaled_image.shape = "+str(scaled_image.shape))
        return output_image

    def get_start_end_for_image(self, image_index):        
        row_index, col_index = self.dict_image_index_box_matrix_index[image_index]
        print("self.box_matrix[row_index][col_index].img_x_left=")
        print(self.box_matrix[row_index][col_index].img_x_left)
        print("self.box_matrix[row_index][col_index].x_left=")
        #end is exclusive hence not doing -1
        print(self.box_matrix[row_index][col_index].x_left)
        start_col = self.box_matrix[row_index][col_index].x_left
        end_col = start_col + self.box_matrix[row_index][col_index].width 
        start_row = self.box_matrix[row_index][col_index].y_top
        end_row = start_row + self.box_matrix[row_index][col_index].height
        #start_col = self.box_matrix[row_index][col_index].img_x_left +\
        #        self.box_matrix[row_index][col_index].x_left
        #end_col = start_col + self.box_matrix[row_index][col_index].width - 1
        #start_row = self.box_matrix[row_index][col_index].img_y_top +\
        #        self.box_matrix[row_index][col_index].y_top
        #end_row = start_row + self.box_matrix[row_index][col_index].height - 1
        return start_row, end_row, start_col, end_col

    def chk_row_col_index_in_range(self, row_index, col_index):
        if((row_index< self.num_rows) and (col_index<self.num_columns)):
            return True
        else:
            return False

    def chk_row_col_index_validity(self, row_index, col_index):
        if((row_index<0) or (col_index<0)):
            self.dicom_annotator_reference.show_error("index cannot be negative")
        if(not self.chk_row_col_index_in_range(row_index, col_index)):
            self.dicom_annotator_reference.show_error("index must be in range")

    def assign_single_image(self, image_index, row_index, col_index):
        self.chk_row_col_index_validity(row_index, col_index)
        self.dict_image_index_box_matrix_index[image_index] = (row_index, col_index)
        self.dict_box_matrix_index_image_index[(row_index, col_index)] = image_index
        print("image_index =")
        print(image_index)
        print("self.dict_image_index_box_matrix_index[image_index]=")
        print(self.dict_image_index_box_matrix_index[image_index])
        print("row_index = ")
        print(row_index)
        print("col_index = ")
        print(col_index)

    def assign_images_to_panes(self):
        row_index = 0
        col_index = 0
        for image_index in range(self.num_images):            
            if(self.chk_row_col_index_in_range(row_index, col_index)):
                self.assign_single_image(image_index, row_index, col_index)
                col_index = col_index + 1
            elif(col_index>=self.num_columns):
                row_index = row_index + 1
                col_index = 0 
                self.assign_single_image(image_index, row_index, col_index)
                col_index = col_index + 1
            elif(row_index>=self.num_rows):
                self.dicom_annotator_reference.show_error("The row index cannot exceed.")

    def create_matrix(self, rows, cols, value_factory=lambda: Box()):
        """
        Creates a matrix of MyClass objects.
    
        Args:
            rows: Number of rows in the matrix.
            cols: Number of columns in the matrix.
            value_factory: A function that creates a new MyClass object.
    
        Returns:
            A list of lists representing the matrix.
        """
    
        matrix = []
        for _ in range(rows):
            row = [value_factory() for _ in range(cols)]
            matrix.append(row)
        return matrix

class DicomAnnotator(QtWidgets.QWidget):
#class DicomAnnotator(QtWidgets.QMainWindow):
    def __init__(self, window_x, window_y, window_width, window_height,\
                 image_name, csv_filename_video, csv_file_handle_video,\
                    csv_filename_video_marked_frames, csv_file_handle_video_marked_frames):
        super().__init__()

        # Variable to store the currently selected shape
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
        self.reinit_nodule_var_newer_implementation()
        #initialize color dict    
        self.init_color_dict()        
        #initialize user interface
        self.initUI()
        #self.init_action_dict()
        #self.add_action_to_toolbar_initially()
        #self.add_action_to_menubar_initially()
        self.add_nodule_instances_initially()
        self.directory_loaded = Directory(self)     
        #the following variiable is reqd hence initialized here.
        self.image_names_currently_displayed = []
        self.set_graph = Graph(self.set_image)
        self.set_graph.set_dicom_annotator_reference(self)
        self.reinitialize()
        self.add_image_box_menu()
        self.add_nodule_box_menu()

    def add_image_box_menu(self):
        "This menu will be shown when right click on an image box is performed."
        #8888888888888888888888888888888888888888888888888888888888
        #There shuld be some option to hide all annotation window.

        #self.setWindowTitle("Right-Click Menu Example")

        # Create the context menu
        self.image_context_menu = QMenu(self)

        # Create actions for the menu
        self.action_showImageOnly = QAction("Show Image Only", self, triggered=self.showImageOnly)
        self.action_showImageWithNodules = QAction("Show Image With Nodules", self, triggered=self.showImageWithNodules)
        self.action_markAxial = QAction("Mark image as Axial", self, triggered=self.markAxial)
        self.action_markSagtial = QAction("Mark image as Sagital", self, triggered=self.markSagital)

        #self.action_addNoduleWithPrevNodules = QAction("Add Nodule With Previously Marked Nodules", self, triggered=self.addNoduleWithPrevNodules)
        self.action_addNoduleFresh = QAction("Add Nodule Fresh", self, triggered=self.addNoduleFresh)
        #88888888888888888888888888888888888888888888
        #showing all marked nodules can be done on the image on screen. That will be done slightly later.
        #show image or add nodule should close all previousouly shown annotation windows .

        # Add actions to the menu
        self.image_context_menu.addAction(self.action_showImageOnly)
        self.image_context_menu.addAction(self.action_showImageWithNodules)
        self.image_context_menu.addAction(self.action_markAxial)
        self.image_context_menu.addAction(self.action_markSagtial)
        #self.image_context_menu.addAction(self.action_addNoduleWithPrevNodules)
        self.image_context_menu.addAction(self.action_addNoduleFresh)

        # Connect the right-click event to show the menu
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        #self.customContextMenuRequested.connect(self.show_context_menu)        

    def check_appropriate_shape_action(self):
        # Set the default checked state for the "Rectangle" action
        # This must be done *after* adding the action to the QActionGroup
        if self.current_nodule_shape == "PolyLine":
            self.action_circle.setChecked(True)
        else:
            self.action_rectangle.setChecked(True)


    def add_nodule_box_menu(self):
        "This menu will be shown when right click on an image box is performed."
        #8888888888888888888888888888888888888888888888888888888888
        #There shuld be some option to hide all annotation window.

        #self.setWindowTitle("Right-Click Menu Example")

        # Create the context menu
        self.nodule_context_menu = QMenu(self)

        # Create actions for the menu
        self.action_showAnnotationWindow = QAction("Show Annotation Window",\
                self, triggered=self.showAnnotationWindow)
        self.action_hideAnnotationWindow = QAction("Hide Annotation Window",\
                self, triggered=self.hideAnnotationWindow)
        self.action_showNoduleInAllImages = QAction("Show Nodule In All Images",\
                self, triggered=self.show_all_images_given_nodule)
        self.action_deleteNodule = QAction("Delete Nodule",\
                self, triggered=self.delete_nodule)


        self.shape_menu = QMenu("Select Nodule Bounday Shape",\
                self)
        
        # self.nodule_context_menu.addMenu(self.shape_menu)

        # #defining the shape actions of the shape menu
        # self.action_circle = QAction("Circle", self, triggered=self.delete_nodule)
        # self.action_rectangle = QAction("Rectangle", self, triggered=self.delete_nodule)
        # self.action_ellipse = QAction("Ellipse", self, triggered=self.delete_nodule)


        # #adding actions to the shape menu
        # self.shape_menu.addAction(self.action_circle)
        # self.shape_menu.addAction(self.action_rectangle)
        # self.shape_menu.addAction(self.action_ellipse)

        # --- Create a QActionGroup for the shape actions (radio button behavior) ---
        self.shape_action_group = QActionGroup(self)
        self.shape_action_group.setExclusive(True) # Ensure only one action can be checked at a time

        # Define the shape actions and add them to the action group and menu
        # It's good practice to list your options, then loop to create actions
        #shape_options = ["Circle", "Rectangle", "Ellipse"]

        self.action_circle = QAction("PolyLine", self)
        self.action_rectangle = QAction("Rectangle", self)
        # self.action_ellipse = QAction("Circle !UnderConstruction", self)

        # Make each action checkable and add to the group and menu
        # We can use a loop or add them individually. Here, for clarity, individually.
        for action in [self.action_circle, self.action_rectangle]:
            action.setCheckable(True)
            self.shape_action_group.addAction(action) # Add to the QActionGroup
            self.shape_menu.addAction(action)        # Add to the submenu


        # Connect the QActionGroup's triggered signal to a slot
        # This signal emits the QAction that was just selected
        self.shape_action_group.triggered.connect(self.handle_shape_selection)
        #self.action_circle.trigger()

        # Add actions to the menu
        self.nodule_context_menu.addAction(self.action_showAnnotationWindow)
        self.nodule_context_menu.addAction(self.action_hideAnnotationWindow)
        self.nodule_context_menu.addAction(self.action_showNoduleInAllImages)
        self.nodule_context_menu.addAction(self.action_deleteNodule)
        self.nodule_context_menu.addMenu(self.shape_menu)

        # Connect the right-click event to show the menu
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        #self.customContextMenuRequested.connect(self.show_context_menu)        

        self.reinit_boundary_shape()
    
    def handle_shape_selection(self, selected_action: QAction):
        """
        Slot to handle the selection of a shape from the radio button group.
        """
        new_shape = selected_action.text()
        if new_shape != self.current_nodule_shape:
            self.current_nodule_shape = new_shape
            print(f"Nodule boundary shape selected: {self.current_nodule_shape}")
            # Here you would update your application's state or UI
            # to reflect the newly chosen shape.
            # self.centralWidget().setText(f"Right-click here. Current shape: {self.current_nodule_shape}")
        self.check_appropriate_shape_action()

    def handle_general_case_show_multiple_images(self,\
            nodule_index_user, images_names_for_nodule):        
        """
        This is a function that handles general case for showing multiple images
        """
        #The displayed index for the index in dict asked by user.
        nodule_index_user_displayed = self.get_displayed_nodule_index(nodule_index_user)
        msg = "Do you want to move to nodule  "+ str(nodule_index_user_displayed)
        msg = msg + " and display all its images. "
        msg = msg + "\n\n\n Please don't change marking or annotation while multiple display."
        #msg = msg + "\n In that display the markings cannot be changed only annotation can be changed."
        window_title = "Show multiple images for the nodule "+str(nodule_index_user_displayed)+" ?"
        answer = self.show_question(msg, window_title)
        # Check which button was clicked
        if answer == QMessageBox.Yes:
            print("Yes button clicked")
            self.display_all_images_given_nodule(images_names_for_nodule, nodule_index_user)
            self.perform_nodule_selected(nodule_index_user)
            self.set_nodule_save()
            self.set_graph.redraw_graph()
        elif answer == QMessageBox.No:
            print("No button clicked")
            return

    def display_all_images_given_nodule(self, images_names_for_nodule, nodule_index_user):
        #images can be added in any order for a nodule. They need not correspond to the display order.
        #selected_image... array will be updated here
        sorted_image_name_list = \
                self.sort_the_image_names_in_the_order_in_which_images_are_displayed(images_names_for_nodule)
        #Here currently displayed is just another name given for the image names displayed in thatorder. 
        #A copy of the sorted list.
        self.image_names_currently_displayed = sorted_image_name_list.copy()
        print("self.image_names_currently_displayed = ")
        print(self.image_names_currently_displayed)
        self.imagePaneManager.init_image_names(self.image_names_currently_displayed)
        self.imagePaneManager.divide_into_panes()
        self.image = self.imagePaneManager.fill_panes(nodule_index_user)

    def sort_the_image_names_in_the_order_in_which_images_are_displayed(self, images_names_for_nodule):
        output_array = []
        for image_name in self.directory_loaded.loadedImages:            
            if image_name in images_names_for_nodule:
                output_array.append(image_name)
        return output_array

    def chk_at_least_one_image(self, nodule_index, images_names_for_nodule):
        """
        This function checks that at least one image should be there for a nodule.
        """
        if(len(images_names_for_nodule) <= 0):
            self.show_error("At least one image should be there for an image.")

    def handle_mul_nodule_or_mul_image_display_already_for_mul_image(self, \
            nodule_index_user, images_names_for_nodule):
        """
        This function handles the case when multiple images or nodules are displayed are already and 
        we need to display multiple images for a nodule.
        This is the nodule index for which the user wants to display the images. 

        Dne something is represented as true by this function and not done anything is represented by False
        """
        num_nodules_displayed = self.get_num_nodule_displayed()
        #The following line is mainly to get the number of images displayed.
        (isSameImageDisplayed, numImagesDisplayed, image_name_displayed) =\
                self.chkSameImageOpened("")
        if(num_nodules_displayed > 1):
            self.handle_general_case_show_multiple_images(nodule_index_user, images_names_for_nodule)
            return True
        if(numImagesDisplayed > 1):
            #multiple images can be diaplyed only for one nodule index
            nodule_index_for_images = self.nodule_dict_index
            if(nodule_index_for_images == nodule_index_user):
                if(numImagesDisplayed != len(images_names_for_nodule)):
                    msg = "The number of displayed images must be same as "
                    msg = msg + "the number of images for this nodule."
                    self.show_error(msg)
                else:
                    msg = "The nodule and all its images have already been displayed."
                    box_title = "Displayed Already"
                    self.show_information(self, msg, box_title)
                return True
            else:
                self.handle_general_case_show_multiple_images(nodule_index_user, images_names_for_nodule)
                return True
        return False

    def chk(self, cond_string, cond):
        if(not cond):
            self.show_error(cond_string+" should be satisfied.")

    def procced_as_in_the_case_of_single_nodule_display_and_switch_image(\
            self, image_name, nodule_index_user):
        #Setting the following variables because the image_name will be picked from them.
        self.selected_image_name_by_right_click = image_name
        self.selected_image_name_by_left_click = image_name
        #The foolowing function has the setting of save variables.
        #self.showImageWithNodules()
        self.showImageOnly()
        self.show_nodule_single_image(image_name, nodule_index_user)

    def handle_nodule_display_single_image(self, nodule_index_user,\
            nodule_index_user_displayed, image_name):
        """
        This code handles the case when all images of a nodule needs to be displayed and the nodule 
        has only one image connected to it and the nodule is not already displayed.
        """
        msg = "Do you want to open/move to nodule "
        msg = msg +str(nodule_index_user_displayed) + ".\n"
        msg = msg + "The change in marking and annotation will be possible."        
        answer = self.show_question(msg, "open/move to nodule")
        if answer == QMessageBox.Yes:
            print("Yes button clicked")
            #nodule selection has been done at time of NODULE DISPLAY FOR this image. no need to do that again.
            self.procced_as_in_the_case_of_single_nodule_display_and_switch_image\
                    (image_name, nodule_index_user)
            self.set_graph.redraw_graph()
        elif answer == QMessageBox.No:
            print("No button clicked")
            return

    def show_all_images_given_nodule(self):
        """
        This function shows all images given a nodule index.
        The index is the index in nodule dict.
        """
        #888888888888888888888888888888888888888complete this function.
        #We will get the image names for a nodule from the graph class.
        #The image can be displayed by the left and right click. Therefore, image name to display was to be 
        #obtained from both left and right click and appropriate selection was required. but a nodule can be 
        #displayed only by right click, hence we can take the nodule index directly for the right click.
        nodule_index_user = self.selected_nodule_index_in_dict_by_right_click
        nodule_index_user_displayed =\
                self.get_displayed_nodule_index(nodule_index_user)
        images_names_for_nodule = \
                self.set_graph.nodule_to_img[nodule_index_user]
        self.chk_at_least_one_image(nodule_index_user, images_names_for_nodule)
        (isSameImageDisplayed, numImagesDisplayed, image_name_displayed) =\
                self.chkSameImageOpened("")
        nodule_index_image = self.nodule_dict_index            
        num_nodules_displayed = self.get_num_nodule_displayed()
        if(len(images_names_for_nodule)==1):
            if(1 == num_nodules_displayed and\
                    1 == numImagesDisplayed and\
                    nodule_index_image == nodule_index_user):
                self.chk(\
                        "image_name_displayed == images_names_for_nodule[0]",\
                        image_name_displayed == images_names_for_nodule[0])
                self.show_information("image and nodule is displayed already.",\
                        "Displayed already")
            else:
                self.handle_nodule_display_single_image(nodule_index_user,\
                        nodule_index_user_displayed, images_names_for_nodule[0])
        elif(len(images_names_for_nodule)>1):
            if(1 == num_nodules_displayed and\
                    1 < numImagesDisplayed and\
                    nodule_index_image == nodule_index_user):
                self.chk(\
                        "numImagesDisplayed == len(images_names_for_nodule)",\
                        numImagesDisplayed == len(images_names_for_nodule)\
                        )

                msg = "The nodule and all its images have already been displayed."
                box_title = "Displayed Already"
                self.show_information(msg, box_title)
                #self.display_info_multiple_images_shown(\
                #        nodule_index_user_displayed)
                #self.display_all_images_given_nodule(\
                #        images_names_for_nodule, nodule_index_user)
            else:
                self.handle_general_case_show_multiple_images(nodule_index_user, images_names_for_nodule)
        #self.set_graph.special_highlight_image_boxes()

        #if(self.handle_mul_nodule_or_mul_image_display_already_for_mul_image(\
        #        nodule_index_user, images_names_for_nodule)):
        return

    def showAnnotationWindow_gateway(self, nodule_dict_index):
        #the passed nodule_dict_index will be shown. the other indices(in dict) will get hidden.
        #Later: if annotation window is already shon then an info msg may be ther that annotation window of 
        #       that nodule is being closed.
        self.hide_other_annotation_window(nodule_dict_index)
        if(-1 != nodule_dict_index):
            nodule_display_index =\
                    self.get_displayed_nodule_index(nodule_dict_index)        
            if(False == self.nodule_dict[nodule_dict_index].show_annotation_window()):
                msg = "Annotation Window is already shown for nodule "+str(nodule_display_index)+".\n"
                self.show_information(msg, "Wake Up")
            self.set_graph.highlight_nodules_consistently()

    def show_information_only_marking_display(self):
        nodule_dict_index_displayed = self.get_displayed_nodule_index(self.nodule_dict_index)
        msg = "The annotation of only the nodule being marked can be shown/hidden. Currently nodule "
        msg = msg + str(nodule_dict_index_displayed) + " is being marked."
        msg = msg + "\n\nUnder the multiple nodule display, the annotation of a nodule can also be "
        msg = msg + "shown/hidden if none of the nodule is being marked."
        msg_title = "Cannot be displayed!"
        self.show_information(msg, msg_title)

    def showAnnotationWindow(self):
        print("showAnnotationWindow")
        #The following is actually the index in dict.
        nodule_index_user = self.selected_nodule_index_in_dict_by_right_click
        # Look at showAnnotationWindow newer comments and nodule_dict_index comments for a more detailed
        #description and reasoning for the case what to do when multiple nodules are shown.
        #Briefly:
        #The show annotation window can display or hide the window in the following cases:
        #1: nodule_dict_index is having a valid value and the annotation window requested corresponds to this 
        #   index.
        #2: nodule_dict_index is -1 and the annotation window requested corresponds to one of the index in 
        #   nodule_dict_indices_shown_extra.
        #8888888888888888888888888888888888
        #complete
        #A case left for the case of multiple nodules only show and none being marked. When annotation window of 
        #nodule a is already shown and the user selects to show the annotation window of nodule b, then the 
        #annotation window of nodule b must be shown. Upto this point handled now. But the annotation window of 
        #nodule a must get closed. chk if this case is handled now. 
        #Later: Also, it seems too much to show an information message in this case.

        if( nodule_index_user == self.nodule_dict_index ):
            #directly call showing of annotation window. 
            if(-1 != self.nodule_dict_index):
                #tHIS IS JUST A SNITY CHECK. If the nodule_dict_index is -1, then array index error will be there.
                self.showAnnotationWindow_gateway(nodule_index_user)
            else:
                self.show_error("how can display of -1 nodule dict index be asked by the user?")
        elif(-1 == self.nodule_dict_index):
            #chk if the index is in nodule_dict_indices_shown_extra.
            if(nodule_index_user in self.nodule_dict_indices_shown_extra):
                #already show window(if any) gets hidden. 
                self.showAnnotationWindow_gateway(nodule_index_user)
            else:
                self.show_information('This nodule is not displayed.', 'Nodule not displayed.')
        else:
            #a message to be shown for the other case.
            #here the self.nodule_dict_index is != -1 and nodule_index_user != self.nodule_dict_index.
            #Here again there can be a case that multiple nodules are shown. show the error according to that.
            if(nodule_index_user in self.nodule_dict_indices_shown_extra):
                #many nodules are shown but a nodule is being marked. show this msg that annotation window 
                #of that nodule can be displayed. 
                #Later: And if that annotation windw is displayed then tell that also but later.
                self.show_information_only_marking_display()
            else:
                #There is only one nodule displayed.
                self.show_information('This nodule is not displayed.', 'Nodule not displayed.')

    def hideAnnotationWindow_gateway(self, nodule_dict_index):
        nodule_display_index = self.get_displayed_nodule_index(nodule_dict_index)
        if(False == self.nodule_dict[nodule_dict_index].hide_annotation_window()):
            msg = "Annotation Window is already hidden for nodule "+str(nodule_display_index)+".\n"
            self.show_information(msg, "Wake Up")
        self.set_graph.highlight_nodules_consistently()

    def hideAnnotationWindow(self):
        #when a nodule annotation window is asked to be hidden, then the image label may be cleared as well.
        #888888888888888888888888888888888888888888888888888888888888. chk if the above makes sense.
        print("hideAnnotationWindow")
        #The select nodule index is index in nodule dict.
        nodule_index_user = self.selected_nodule_index_in_dict_by_right_click
        if(nodule_index_user == self.nodule_dict_index):
            self.hideAnnotationWindow_gateway(self.nodule_dict_index)
        elif(0==len(self.nodule_dict_indices_shown_extra)):
            self.show_information('This nodule is not displayed.', 'Nodule not displayed.')
        elif(0<len(self.nodule_dict_indices_shown_extra)):
            if(nodule_index_user in self.nodule_dict_indices_shown_extra):
                self.hideAnnotationWindow_gateway(nodule_index_user)
            else:
                self.show_information('This nodule is not displayed.', 'Nodule not displayed.')
        else:
            #here nodule_index_user != self.nodule_dict_index and both condition for num nodule shown have been 
            #covered. Hence, this case cannot be reached.
            self.show_error("This case cannot be reached.")

    def hideAnnotationWindow_old(self):
        #when a nodule annotation window is asked to be hidden, then the image label may be cleared as well.
        #888888888888888888888888888888888888888888888888888888888888. chk if the above makes sense.
        print("hideAnnotationWindow")
        #The select nodule index is index in nodule dict. 
        nodule_display_index = self.get_displayed_nodule_index(self.nodule_dict_index)
        if(self.selected_nodule_index_in_dict_by_right_click == self.nodule_dict_index):
            if(False == self.nodule_dict[self.nodule_dict_index].hide_annotation_window()):
                msg = "Annotation Window is already hidden for nodule "+str(nodule_display_index)+".\n"
                self.show_information(msg, "Wake Up")
        else:
            nodule_display_index_selected_by_user = \
                    self.get_displayed_nodule_index(self.selected_nodule_index_in_dict_by_right_click)
            msg = "Window is not shown for nodule "+str(nodule_display_index_selected_by_user)+".\n"
            #It may happen that window for nodule dict index is also hidden.
            #Hence, no need to write, for which nodule the window is shown. 
            #msg = msg + "\nWindow is shown for nodule "+str(nodule_display_index)+"."
            self.show_information(msg, "Wake Up")

    def show_context_menu(self, event):
        print("event.globalPos()="+str(event.globalPos()))
        event_x_wrt_window = event.pos().x()
        event_y_wrt_window = event.pos().y()
        image_name = self.set_graph.get_image_name_for_mouse(event_x_wrt_window, event_y_wrt_window)
        if(image_name!=""):
            self.image_context_menu.popup(event.globalPos())
            print("selected image name = "+str(image_name))
            self.selected_image_name_by_right_click = image_name
        #T8888888888888888888888888888888888888888888888888888888888888
        #The returned index is the index in nodule dict. update the functions that use this index
        nodule_index = self.set_graph.get_nodule_index_in_dict_for_mouse(event_x_wrt_window, event_y_wrt_window)
        print("selected nodule index = "+str(nodule_index))
        if(nodule_index!=-1):
            self.nodule_context_menu.popup(event.globalPos())
            print("selected nodule index = "+str(nodule_index))
            self.selected_nodule_index_in_dict_by_right_click = nodule_index

    def write_list(self, my_list, f, sep): 
        for item in my_list:
            f.write(f"{item}{sep}")

    def write_dict(self, dictToWrite, header, is_val_standard, is_val_list, filename):
        """
        This function writes given dict to a file with filename in the user directory.
        The file is written in write mode where earlier contents of the file are removed. 
        The function requires the value to be a single value, and not a list or other thing.
        is_val_standard: This is true if the value is a standard type

        """
        save_path = Path(PurePath(self.directory_loaded.directoryPath).joinpath(filename))
        try:
            # Convert dictionary to JSON string in a human-readable format
            #json_string = json.dumps(data, indent=4)
            with open(save_path, 'w') as f:
                f.write(f"{header}\n")  # Write header with a newline character
                # Iterate through key-value pairs and write to file
                for key, value in dictToWrite.items():
                    f.write(f"{key}\t")
                    if(is_val_standard):
                        f.write(f"{value}\n")
                    elif(is_val_list):
                        self.write_list(value, f, '\t')
                        f.write(f"\n")
                    else:
                        msg = "Wrtiting this type of value(dict) has not been implemented yet."
                        self.show_warning(msg, "Ask Programmer")
                #f.write(json_string)  # Write the JSON-formatted dictionary
            print(f"Dictionary saved successfully to '{filename}'.")
        except FileNotFoundError:
            print(f"Error: File '{filename}' could not be created.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def write_list_dict(self, dictToWrite, header, filename):
        """
        This function writes given dict to a file with filename in the user directory.
        The file is written in write mode where earlier contents of the file are removed. 
        The function requires the value to be a single value, and not a list or other thing.
        Thespecialit here 
        """
        save_path = Path(PurePath(self.directory_loaded.directoryPath).joinpath(filename))
        try:
            # Convert dictionary to JSON string in a human-readable format
            #json_string = json.dumps(data, indent=4)
            with open(save_path, 'w') as f:
                f.write(f"{header}\n")  # Write header with a newline character
                # Iterate through key-value pairs and write to file
                for key, value in dictToWrite.items():
                    f.write(f"{key}\t{value}\n")
                #f.write(json_string)  # Write the JSON-formatted dictionary
            print(f"Dictionary saved successfully to '{filename}'.")
        except FileNotFoundError:
            print(f"Error: File '{filename}' could not be created.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def write_to_csv_per_patient(self, image_name, nodule_index):
        try:
            #This is the nodulde display index.
            with open(save_path, 'a') as f:
                f.write(f"{image_name}\t{nodule_index}\n")
            print(f"written image_display_mapping.")
            #We must be having image display mapping in memory. After each update to that mapping, we can write 
            #that mapping. This will remove the need of removing entries from the central file and updating the
            #central file when any changes in image nodule mapping is done.
            #Therefore, this mapping can be written at the time when the nodule is added/deleted or a mapping
            #from an image to an existing nodule is added.
            #88888888888888888888888888888888888888888888888888888888888888888888888888888888
        except FileNotFoundError:
            print(f"Error: File '{filename}' could not be created.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def updateOrientation(self, image_name, orientation):
        #store the orientation in mapping
        self.image_to_orientation[image_name] = orientation
        #display the orientation in image box
        newText = image_name+"("+orientation+")"
        self.set_graph.update_image_txt(image_name, newText)

    def markOrientationFunctionality(self, image_name, orientation):
        """
        This function proovides the actual functionality of marking.
        orientation is a string that can have the value either a for axial or s for sagital
        """
        self.updateOrientation(image_name, orientation)
        #save the updated mapping
        filename = "map_orientation.txt" 
        header = "image_name\torientation"
        self.write_dict(self.image_to_orientation, header, True, False, filename)
        self.show_splash_window("Orientation "+ orientation+" marked for image "+image_name)

    def get_pixmap_for_text(self, text):
        pixmap = QPixmap()  # Create an empty QPixmap
        pixmap.fill(Qt.white)  # Optionally set a background color (white in this case)
        # Set a larger font size for better visibility on splash screen
        font = QFont()
        font.setPointSize(16)
        pixmap.text(0, 20, splash_font, Qt.AlignHCenter | Qt.AlignTop, text)

    def text_to_pixmap(self, text, width, height, font_family="Arial", font_size=12):
        """
        Creates a pixmap from the given text.
        
        Args:
            text: The text to be drawn.
            width: The width of the pixmap.
            height: The height of the pixmap.
            font_family: The font family to use (default: Arial).
            font_size: The font size to use (default: 12).
        
        Returns:
            A QPixmap object containing the drawn text.
        """
        print("text="+str(text))
        print("width="+str(width))
        print("height="+str(height))
        # Create a blank image
        image = QImage(width, height, QImage.Format_ARGB32)
        image.fill(Qt.transparent)
        
        # Create a painter object
        painter = QPainter(image)
        
        # Set font properties
        font = QFont(font_family, font_size)
        painter.setFont(font)
        
        # Draw the text
        painter.drawText(0, height // 2, text)
        
        # Clean up and convert to pixmap
        painter.end()
        return QPixmap.fromImage(image)

    def show_splash_window(self, splash_text):
        # Create the splash screen with background color (optional)

        # Assuming splash_text is a string containing your message
        #splash_pixmap = self.get_pixmap_for_text(splash_text)
        #splash_pixmap = self.text_to_pixmap(splash_text, int(100), int(100))
        #splash = QSplashScreen(splash_pixmap, Qt.WindowStaysOnTopHint)
        IMG = '/home/ankitsinghal/Downloads/IMG_20240513_142739.jpg'
        pixmap = QPixmap(IMG)
        splash = QSplashScreen(pixmap, Qt.WindowStaysOnTopHint)
        #splash.setStyleSheet("background-color: lightblue")  # Uncomment for background color

        # Display the splash screen
        splash.show()
        #time.sleep(4)

        # Close the splash screen
        splash.close() 

    def switch_image(self, operation):
        """
        This function switches the image view when user performs a right click and asks for some operation on 
        the image other than the image being displayed.
        """
        # Set the splash screen text
        splash_text = "switching/opening image."
        #splash_pixmap = self.get_pixmap_for_text(splash_text)
        splash_pixmap = self.text_to_pixmap(splash_text, 100, 100)
        # Create the splash screen with background color (optional)
        #8888888888888888888888888888888888888888888888888888888888888888888888888
        #specify qt widget self, which window called this splash screen.
        splash = QSplashScreen(self, splash_pixmap, Qt.WindowStaysOnTopHint)
        #splash.setStyleSheet("background-color: lightblue")  # Uncomment for background color

        # Display the splash screen
        splash.show()
        #The switch image will show the image without any nodules.
        self.showImageOnly()
        # Close the splash screen
        splash.close() 
        msg = "Opened image "+str(self.selected_image_name_by_right_click)+"."
        msg = msg + "Now you can perform "+ operation
        self.show_splash_window(msg)

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

    def show_warning(self, warning_text, box_title):
        msg_box = QMessageBox() 
        msg_box.setIcon(QMessageBox.Warning) 
        msg_box.setText(warning_text) 
        # setting Message box window title 
        msg_box.setWindowTitle(box_title) 
        # Set the buttons based on your options (choose 2 or 3)
        buttons = QMessageBox.Ok
        msg_box.setStandardButtons(buttons)
         
        # Show the message box
        answer = msg_box.exec_()
        return answer

    def show_information(self, warning_text, box_title):
        msg_box = QMessageBox() 
        msg_box.setIcon(QMessageBox.Information) 
        msg_box.setText(warning_text) 
        # setting Message box window title 
        msg_box.setWindowTitle(box_title) 
        # Set the buttons based on your options (choose 2 or 3)
        buttons = QMessageBox.Ok
        msg_box.setStandardButtons(buttons)
         
        # Show the message box
        answer = msg_box.exec_()
        return answer

    def show_warning_num_images_displayed(self, operation):
        warning_text = "num Images Displayed is not 1.\nWhereas, the operation "+ operation + " is allowed only"+\
                " when num Images Displayed is exactly one.\nPlease check whether you are doing everything fine?"
        box_title = "Wake Up"
        self.show_warning(warning_text, box_title)

    def show_question(self, question_text, box_title):
        msg_box = QMessageBox() 
        msg_box.setIcon(QMessageBox.Question) 
  
        msg_box.setText(question_text) 
          
        # setting Message box window title 
        msg_box.setWindowTitle(box_title) 
    
        # Set the buttons based on your options (choose 2 or 3)
        buttons = QMessageBox.Yes | QMessageBox.No  # Choose 2 buttons (Yes/No)
        # buttons = QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel  # Choose 3 buttons (Yes/No/Cancel)
        ## declaring buttons on Message Box 
        #msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
        # Set the standard buttons
        msg_box.setStandardButtons(buttons)
         
        # Show the message box
        answer = msg_box.exec_()
        return answer

    def msg_switch_image(self, current_filename, required_filename, operation):
        # setting message for Message Box
        msg = "Currently image "+current_filename+" is being shown.\n"
        msg = msg + "But, operation "+ operation+" is required on image "+required_filename+".\n"
        msg = msg + "You can perform "+operation+" after switching to "+required_filename+".\n\n"
        msg = msg + "Do you want to switch to image "+required_filename+"."
        window_title = "Switch Image?"
        return (msg, window_title)

    def msg_multiplt_to_single_image(self, required_filename, operation):
        # setting message for Message Box
        msg = "Currently multiple images are shown.\n"
        msg = msg + "But, operation "+ operation+" is required on image "+required_filename+".\n"
        msg = msg + "You can perform "+operation+" after opening "+required_filename+".\n\n"
        msg = msg + "Do you want to open image "+required_filename+" and close all other images."
        window_title = "Close Multiple / Open Image?"
        return (msg, window_title)

    def msg_open_image(self, required_filename, operation):
        # setting message for Message Box
        msg = "Currently no image is being shown.\n But, operation "+ operation+" is required on "
        msg = msg + "image "+required_filename+".\n"
        msg = msg + "You first need to look at the image to perform the operation.\n"
        msg = msg + "You can perform "+operation+" after opening "+required_filename+".\n\n"
        msg = msg + "Do you want to open image "+required_filename+".\n"
        window_title = "Open Image?"
        return (msg, window_title)

    def ask_file_change(self, num_current_files, current_filename, required_filename, operation): 
        if( 0 == num_current_files ):
            (msg, window_title) = self.msg_open_image(required_filename, operation)
        elif ( 1 == num_current_files ):
            (msg, window_title) = self.msg_switch_image(current_filename, required_filename, operation)
        elif ( num_current_files > 1 ):
            (msg, window_title) = self.msg_multiplt_to_single_image(required_filename, operation)
        else:
            assert False, "num_current_files cannot be negative."
        answer = self.show_question(msg, window_title)
        # Check which button was clicked
        if answer == QMessageBox.Yes:
            #The following function has call to displaying of message that image has been switched.
            self.switch_image(operation)
            print("Yes button clicked")
        elif answer == QMessageBox.No:
            print("No button clicked")
        # Add another elif for the third option if using 3 buttons
        # elif answer == QMessageBox.Cancel:
        #     print("Cancel button clicked")

    def msg_orientation_change(self, current_orientation, required_orientation, image_name):
        # setting message for Message Box
        msg = "Currently orientation "+current_orientation +" has been marked over image "+image_name+".\n"
        msg = msg + "But, you have asked to change it to orientation "+required_orientation+".\n\n"
        msg = msg + "Do you want to change the orientation to "+required_orientation+".\n"
        window_title = "Change Orientation?"
        return (msg, window_title)

    def ask_perform_orientation_change(self, current_orientation, required_orientation, image_name): 
        (msg, window_title) = self.msg_orientation_change(current_orientation, required_orientation, image_name)
        answer = self.show_question(msg, window_title)
        # Check which button was clicked
        if answer == QMessageBox.Yes:
            #The following function has call to displaying of message that orientation has been marked.
            self.markOrientationFunctionality(image_name, required_orientation)
            print("Yes button clicked")
        elif answer == QMessageBox.No:
            print("No button clicked")

    def chkSameImageOpened(self, image_name):
        numImagesDisplayed = len(self.image_names_currently_displayed)
        if(numImagesDisplayed>1):
            #returning false because we want to check if the given image_name is the only image displayed.
            return (False, numImagesDisplayed, self.image_names_currently_displayed[0])
        elif(numImagesDisplayed==0):
            return (False, numImagesDisplayed, "")
            #show message that the image was not opened yet. currently opeing the image. and then reclick 
            #appropriate type.
        else:
            assert(numImagesDisplayed == 1), "there is one image displayed"
            if(self.image_names_currently_displayed[0] == image_name):
                return (True, numImagesDisplayed, self.image_names_currently_displayed[0])
            else:
                return (False, numImagesDisplayed, self.image_names_currently_displayed[0])

    def markOrientationVariousPossibilities(self, image_name, orientation):
        """
        Also check the case where different orientation has been marked earlier.
        8888888888888888888888888888888888888888888888888
        The change of image here does not require the display of nodules.
        This can be used for both axial as well as sagital.
        """
        print("markOrientationVariousPossibilities")
        operation = "mark orientaion " + orientation
        (isSameImageDisplayed, numImagesDisplayed, image_name_displayed) = self.chkSameImageOpened(image_name)
        if(isSameImageDisplayed):
            assert image_name == self.image_names_currently_displayed[0], "This must be same"
            #the image name clicked by the user is same as the image name currently being displayed.
            #now check if already marked or not
            print("do marking if not done already.")
            if (False == (image_name in self.image_to_orientation)):
                #The orientation of this image has not been stored already
                #create a separate function for marking because it will be reused manytimes.
                #88888888888888888888888888
                #get orientation
                self.markOrientationFunctionality(image_name, orientation)
            #There is marking of this image. chk whether it is same.
            elif(self.image_to_orientation[image_name] == orientation):
                print("orientation has already been marked")
                #showing info msg box is required.
                msg = image_name+" has already been marked with orientation "+ orientation + "."
                self.show_splash_window(msg)
            #chk if different marking has been already.
            elif(self.image_to_orientation[image_name] != orientation):
                #show appropriate message box and do the image shifting.
                earlier_orientation = self.image_to_orientation[image_name]
                print(earlier_orientation+"has been marked earlier and "+orientation+" is required now.")
                self.ask_perform_orientation_change(earlier_orientation, orientation, image_name)
                #show appropriate message box and do the image shifting.
            else:
                #show message box
                msg = "no other possibility exist."
                print(msg)
                self.show_splash_window(msg)
        else:
            self.ask_file_change(numImagesDisplayed, image_name_displayed, image_name, operation)

    def markAxial(self):
        """
        Handler for marking axial
        """
        image_name = self.selected_image_name_by_right_click
        self.markOrientationVariousPossibilities(image_name, 'Axial')

    def markSagital(self):
        """
        Handler for marking sagital
        """
        image_name = self.selected_image_name_by_right_click
        self.markOrientationVariousPossibilities(image_name, 'Sagital')

    def handle_left_button_press_over_image_box(self, image_name, event):
        """
        image_name : This is the name of the image box over which press has occurred.
        """
        operation = "Show Image"
        (isSameImageDisplayed, numImagesDisplayed, image_name_displayed) = self.chkSameImageOpened(image_name)
        if(isSameImageDisplayed):
            assert image_name == self.image_names_currently_displayed[0], "This must be same"
            #Whether setting self.selected_image_name_by_left_press is sufficient to keep track of line draw 
            #from img to nodule? 8888888888888888888888888888888888888
            #we need to set set_image_drag_started as true
            self.set_image_drag_started = True
        else:
            self.clear_set_image_drag()
            self.ask_file_change(numImagesDisplayed, image_name_displayed, image_name, operation)

    def clear_set_image_drag(self):
        # print("in clear_set_image_drag")
        if(self.partial_line_drawn):
            if(not self.set_image_drag_started):
                self.show_error("self.partial_line_drawn can be true only if self.set_image_drag_started is true")
            #highlight again will be taken care of by redraw graph.
            self.set_graph.redraw_graph()

        self.set_image_drag_started = False
        self.partial_line_drawn = False

    def left_button_pressed_set_image(self, event):
        #p888888888888888888888888888888888888888 complete this.
        print("in left button press event.globalPos()="+str(event.globalPos()))
        event_x_wrt_window = event.pos().x()
        event_y_wrt_window = event.pos().y()
        image_name = self.set_graph.get_image_name_for_mouse(event_x_wrt_window, event_y_wrt_window)
        self.selected_image_name_by_left_press = image_name
        if(image_name!=""):
            print("selected image name = "+str(image_name))
            #We can show the corresponding image here.
            self.handle_left_button_press_over_image_box(image_name, event)
        else:
            self.clear_set_image_drag()

        #Currently not implementing the function when the left click is outside any image box.
        #but if drag was released in between, the line will get hide but if then drag is started from empty space 
        #or from a nodule, still a line will get drawn due to the image name being selected by left click. 
        #Hence, do update the image name name selected by left press as null when the left press is over some 
        #other space. done.

        ##The returned index is the index in nodule dict. update the functions that use this index
        #nodule_index = self.set_graph.get_nodule_index_in_dict_for_mouse(event_x_wrt_window, event_y_wrt_window)
        #print("selected nodule index = "+str(nodule_index))
        #if(nodule_index!=-1):
        #    print("selected nodule index = "+str(nodule_index))
        #    self.selected_nodule_index_in_dict_by_left_click = nodule_index
        #    selected_nodule_index_current_click = nodule_index
        #    #It may be that this click is start of dragged line. Nothing more needs to be done.
        #    #If drag occurs, then we can draw a line from the corresponding image box to the current point of 
        #    #drag event. It may happen that user clicked over an image, then left the mouse key and pressed the 
        #    #mouse key over an empty space and start dragging. What will happen in that case?
        #    #Why the selected image by right click is not set here. 
        #    #self.image = 
        

    #888888888888888888888888888888888888888888888888888888888888
    #earlier the nodule instances were added initially so that the windows also gets added initially.
    #Also, adding nodule instances initially made it possible for me to show the user all the nodule action 
    #items, so that the user selects the appropriate nodule. But now, all the nodules(that are present) will be
    #shown to the user.
    #and the nodules can be added and deleted as well.
    #The idea of adding all the nodules intially was also to have the instances of annotation windows added 
    #initially and just reinitialize them and just show or hide them.
    #Now, the same thing can be done by a nodule pool, just like a thread pool.
    #We can get a nodule from nodule pool.
    #This can work very well by having an index to the nodule added till now.
    #If the nodule is to beleted from the end, even then it will be fine.
    #But what if we want to delete a nodule from in between.
    #To achieve such functionality, we can maintain a list of nodule that are present now.
    #Whenever a nodule has been added, its entry gets added to the csv file.
    #How will the entry be deleted from the csv file, when a nodule gets deleted?
    #The naive method is to open up the csv file in write mode, load the contents in dataframe, delete the 
    #required entry from the dataframe and then, overwrite the csv file.
    #Currently, we have thecsv file opened in write mode itself.    
    def add_nodule_instances_initially(self):
        """
        The function will add thee nodule instances initially.
        """
        self.nodule_dict={}
        for i in range(self.max_num_nodules):
            self.nodule_dict[i] = Nodule(i, self.color_dict[i], None, self) #self.toolBar, self)
            self.nodule_dict[i].add_annotation_window(self.window_x, self.y_pos_first_row - self.info_height,\
                self.annotation_label_width, self.dropdown_width, self.info_height, self.csv_file_handle_video, self.image_name)
            self.nodule_dict[i].set_dicom_annotator_reference(self)
        print("self.nodule_dict="+str(self.nodule_dict))

    def init_color_dict(self):
        """
        This function initializes the color dict
        Initially, keeping 5 entries in the color dict
        """
        self.color_dict = {}
        #Setting color as per rgb values
        #Just have tuples for every color in rgb format
        self.color_dict[0] = (255, 0, 0)  #QColor(255,0,0,255) #"Red"
        self.color_dict[1] = (0, 255, 0) #"Green"
        self.color_dict[5] = (0, 0, 255) #"Blue"
        self.color_dict[4] = (255, 255, 0) #"Yellow"
        self.color_dict[3] = (0, 255, 255) # "Cyan"
        self.color_dict[2] = (255, 0, 255) # fuchsia light saturated magenta 
        self.color_dict[6] = (127, 0, 255) # violet
        self.color_dict[7] = (255, 0, 127) # dark saturated rose
        self.color_dict[8] = (255, 127, 0) #  dark saturated orange
        self.color_dict[9] = (255, 255, 255) # have the white color at last.

    def perform_nodule_selected(self, nodule_index):
        """
        This function is called to perform some basic functions when a nodule is selected either by seleting 
        that nodule or by adding that nodule for the first time.
        basically now the nodule selected is doing only window show and hide. also setting of nodule_dict_index
        also highling of nodule.
        """
        self.nodule_dict_index = nodule_index
        self.nodule_dict_indices_shown_extra = []
        print("self.nodule_dict_index = "+str(self.nodule_dict_index))
        #other nodule windows must be hidden.
        #Show the annotation window.
        #the parameters of the annotation window must already be filled with the user filled data.
        #We can have self.nodule_dict_index as -1 when we want to unselect all the nodules.
        self.showAnnotationWindow_gateway(self.nodule_dict_index)
        #the redraw will clear any unnecessary prev highlight and do ne highlight
        self.set_graph.redraw_graph()

    #8888888888888888888888888888 is this fnction complete and how will this function be used
    def show_only_given_action(self, index):
        for i in range(self.max_num_nodules):
            if i == index:
                print("displaying only i")
            else:
                print('error')
                #self.nodule_dict[i].hide_annotation_window()

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

    def action_1_triggered(self):
        """
        This function will be filred when action0 gets triggered
        """
        print("in action 1 triggered")
        if(self.video_opened or self.image_opened):
            if(self.is_video_playing()):
                return                 
            self.perform_nodule_selected(1)

    def action_2_triggered(self):
        """
        This function will be filred when action0 gets triggered
        """
        print("in action 2 triggered")
        if(self.video_opened or self.image_opened):
            if(self.is_video_playing()):
                return                 
            self.perform_nodule_selected(2)

    def action_3_triggered(self):
        """
        This function will be filred when action0 gets triggered
        """
        print("in action 3 triggered")
        if(self.video_opened or self.image_opened):
            if(self.is_video_playing()):
                return                 
            self.perform_nodule_selected(3)

    def action_4_triggered(self):
        """
        This function will be filred when action0 gets triggered
        """
        print("in action 4 triggered")
        if(self.video_opened or self.image_opened):
            if(self.is_video_playing()):
                return                 
            self.perform_nodule_selected(4)

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

    def get_extra_nodule_index_window_shown(self):
        """
        This function is used to obtain the nodule index(out of extra nodule indices shown), for which the 
        annotation window is shown. A check may be added that multiple windows cannot be shown simultaneously. 
        There must be a function in the nodule class which tells the show status of annotation window.
        """
        shown_index = -1 
        for nodule_index in self.nodule_dict_indices_shown_extra:
            if(self.nodule_dict[nodule_index].is_annotation_shown()):
                if(-1 != shown_index):
                    self.show_error("Only one annotation window can be shown at a time.")
                shown_index = nodule_index
        return shown_index

    def hide_other_annotation_window(self, nodule_index):
        """
        The fucntion is used to hide annotation window other than the nodule index given in dict.
        Returns
        -------
        None.
        """
        #Hiding the windows for all prev nodules added.
        for other_nodule_index in self.added_nodule_indices:
        #By default, when the widow gets added, it will be shown by default.
            if (other_nodule_index!=nodule_index):
                #treating hide as idempotent. hence not using the return value.
                self.nodule_dict[other_nodule_index].hide_annotation_window() 

    def create_directory_for_nodule(self):
        """
        This function will 
        #1: update the color to be ploted
        #2: create the folder in which the marked images will be placed.
        #3: update this folder name to the class variable which will be used by the save function.
        """
        #The color to be plotted is selected by self.color_dict[self.nodule_dict_index].
        #Hence, this part requires change in show image, plot lines and save image function
        #create the folder to save that nodule
        #I think folder creation should be done in save_image.Chk when this was done earlier. 
        #Earlier the code to chk dir was  in save_frame. we should not waste time in save frame, hence creating the directory here.
        #It it happens that the directory gets deleted accidentally, then earlier annotations would alsohave gone. Therefore, binary file
        #to save the annotations is required.
        if(self.loading_partially_annotated_video):
            #When add nodule is called while the video is being loaded,then the directories for any nodules that were added earlier
            #should already exist.
            assert self.dicom_frames_path[self.nodule_dict_index].is_dir(), "The directory should exist already."
        else: #if(not self.loading_partially_annotated_video):
            #assert not self.dicom_frames_path[self.nodule_dict_index].is_dir(), "The directory should not exist already."
            #Now, if the directory does not exist already, then a new one will be created but no 
            if(not self.dicom_frames_path[self.nodule_dict_index].is_dir()):
                self.dicom_frames_path[self.nodule_dict_index].mkdir()
        #The folder name to be used for saving the frames will be automatically selected correctly using the variable 
        #self.dicom_frames_path[self.nodule_dict_index]

    def get_a_free_index_nodule_dict(self):
        """
        Returns a free index from nodule dict that has not been assigned yet.
        """
        if (len(self.free_nodule_indices)==0):            
            #no free index left
            return -1
        free_index = self.free_nodule_indices[0]
        #88888888888888888888888888888888888888888888888
        #check that the free indexdoes not exist in the added_nodule_indices
        #also check there does not exist a directory by name free index  
        assert(False == (free_index in self.added_nodule_indices)), "The index should not already be allocated."
        #path names have been initialized just after directory loading.
        #The path existence will be checked by the calling function.
        #remove the index from the list of free indices.
        self.free_nodule_indices.remove(free_index)
        return free_index

    def write_image_nodule_dict(self):
        """
        Creating a SEParate function because the same funtion will br reqd many times.
        """      
        if(self.set_graph.chk_img_to_nodule_empty()):
            #delete the file
            self.directory_loaded.delete_file("Image_to_nodule.txt")
        else:
            self.write_dict(self.set_graph.img_to_nodule\
                    ,"image_name\tnodule_dict_index", False, True,\
                    "Image_to_nodule.txt")

    def get_displayed_nodule_index(self, nodule_dict_index):
        if (nodule_dict_index in self.index_in_nodule_dict_to_number_displayed):
            return self.index_in_nodule_dict_to_number_displayed[nodule_dict_index]
        else:
            error_msg = "The nodule index should have been a there in the dict."
            error_msg = error_msg + "\n"+str(nodule_dict_index)+" is not available in index_in_nodule_dict_to_number_displayed."
            self.show_error(error_msg)

    def update_and_write_nodule_number_mapping(self, nodule_index_in_dict, newNumberToDisplay):
        self.update_number_display_nodule_dict_mapping(newNumberToDisplay, nodule_index_in_dict)
        self.save_mapping_number_display_nodule_dict()

    def compute_newNumberToDisplay(self):
        numNodules = len(self.added_nodule_indices)
        newNumberToDisplay = numNodules
        assert newNumberToDisplay < self.max_num_nodules,\
                "the number to display cannot be larger than the number of nodules allowed."
        return newNumberToDisplay

    def init_nodule_for_edges(self, nodule_dict_index):
        self.nodule_dict[nodule_dict_index].reinitialize()
        self.nodule_dict[nodule_dict_index].set_directory_path(\
                self.directory_loaded.directoryPath)

    def add_nodule_functionality(self, image_name):
        #get a free index from dict.
        free_index = self.get_a_free_index_nodule_dict()
        #The free index has now been removed from the list of free indices
        if(free_index>=0):
            #The directory should not exis already for the free index that will become the nodule_dict_index.
            self.directory_loaded.chk_dir_does_not_exist_already(image_name, free_index)
            newNumberToDisplay = self.compute_newNumberToDisplay()
            self.added_nodule_indices.append(free_index)
            self.chk_added_free_nodule_indices_correctness()
            #update the mapping for display number and index in dict.
            self.update_and_write_nodule_number_mapping(free_index, newNumberToDisplay)            
            self.set_graph.add_nodule(free_index, newNumberToDisplay)  
            self.init_nodule_for_edges(free_index)
            #The following function will update self.nodule_dict_index
            self.add_img_nodule_connection(image_name, free_index)
            self.reset_nodule_save()
        else:
            #A message box can also be shown.
            #888888888888888888888888888888888888888888888888
            msg = "only "+str(self.max_num_nodules)+" nodules at max are allowed."
            self.show_warning(msg, "Ask Programmer")
            print(msg)

    def addNoduleFresh(self):
        """
        Make sure that the add nodule is called for the image which is selected before.
        If not, then show an information message that adding nodule for which the right click is done now.
        This image is different from the image earlier displayed. This part is done.
        Also, tell that a nodule has been added. this may be done.
        88888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        The delete option will be provided later on.
        88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        """
        print("addNoduleFresh")
        self.reinit_boundary_shape()
        #88888888888888888888888888888888
        #highlight nodule also needs to be done.
        image_name = self.selected_image_name_by_right_click
        operation = "Add Nodule Fresh"
        (isSameImageDisplayed, numImagesDisplayed, image_name_displayed) = self.chkSameImageOpened(image_name)
        if(isSameImageDisplayed):
            assert image_name == self.image_names_currently_displayed[0], "This must be same"
            #again displaying fresh image because there might be marking over earlier shown image.
            self.showImageOnly()
            #Even after reshowing the image the image name mmust be the required name.
            assert image_name == self.image_names_currently_displayed[0], "This must be same"
            self.add_nodule_functionality(image_name)
        else:
            self.ask_file_change(numImagesDisplayed, image_name_displayed, image_name, operation)

    def addNoduleWithPrevNodules(self):
        """
        This function adds a nodule when a directory is opened by the user.
        """
        assert self.directory_opened, "This function can be called only when directory has already been opened."
        #We also need to need to know for which image the nodule is being added. 
        #The knowledge of image is not reqd by this function. 
        #This function will add a new nodule 
        #The knowledge of image is required by the function which will draw the line, open up the image for marking
        #and so on.
        #There may be multiple nodules within an image as well. Therefore, now the marking of the images will 
        #be nodule wise. 
        #We need to pick a nodule from the nodule pool created by the nodule dict.
        assert len(self.nodule_dict) >= self.numNodules, "The len of nodule dict cannot be less than num nodule"
        largest_nodule_index = -1 
        if (self.numNodules>0):
            #get the nodule indices to add
            largest_nodule_index = self.added_nodule_indices[-1]
        if (self.numNodules<self.max_num_nodules and largest_nodule_index < self.max_num_nodules-1):
            self.numNodules = self.numNodules+1
            #when a nodule is deleted, the futher nodules should get one number less
            #currently not doing this
            #hence whenever a nodule is added, it will get the index one larger than the current largest index.
            #Also, num nodules may be less than than the max nodules allowed but the last nodule index may 
            #reach its boundary.
            #Add that check as well. done
            nodule_index_to_add = largest_nodule_index + 1
            self.nodule_dict_index = nodule_index_to_add
            #
            self.added_nodule_indices.append(nodule_index_to_add)
            self.numNodules = self.numNodules + 1
            #add the nodulebox, edge(handled by graph class). show annotation window. 
            #the image with/without other nodules is displayed based on user input
            #The image that is displayed already has been done earlier.
            #The current function will not change the image display
            #img_name is required.
            #************************8888888888888888888888888888888888888
            self.set_graph.add_nodule(self.selected_image_name_by_right_click)
            #Todo: complete the following
            #seems completed
            #the annotation window will be shown by default.
            #whenever adding another action, remember to close any previous windows, if they are opened.
            #This will help, because the user mightnot close the previous windows. this is done.
            self.hide_other_annotation_window(self.nodule_dict_index)
            #Todo: complete the following:
            #I need to implement this function. This function will 
            #1: update the color to be ploted. self.nodule_dict_index will automatically
            # update the required color
            #2: create the folder in which the marked images will be placed.
            #3: update this folder name to the class variable which will be used by the save function.
            #done
            #The earlier markings, if any over the current image, should be cleared. 
            #Else, when moving back and forth, the frames will be loaded only wrt the current nodule.
            #Todo: have separate framed_marked_array for each nodule.
            #8888888888888888888888888 use of following function will be looked at later on.
            self.perform_nodule_selected(self.nodule_dict_index)
            assert len(self.nodule_dict) >= self.numNodules, "The len of nodule dict cannot be less than num nodule"
        else:
            #All the annotation windows will be hidden if the add nodule is called more.
            self.hide_all_annotation_window()
            print("only"+ self.max_num_nodules + "nodules at max are allowed.")
            #Todo: show error message here

    def add_nodule_clicked(self):
        """
        This function is used when add nodule is clicked for the case of individual image or video.

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
                self.nodule_dict_index = self.numNodules - 1
                #Todo: complete the following
                #seems completed
                #By default, when the action gets added to the toolbar, the annotation window will be shown by default.
                #whenever adding another action, remember to close any previous windows, if they are opened.
                #This will help, because the user mightnot close the previous windows. this is done.
                self.hide_other_annotation_window(self.nodule_dict_index)
                #Making the action as visible
                self.action[self.nodule_dict_index].setVisible(True)                
                #Todo: complete the following:
                #I need to implement this function. This function will 
                #1: update the color to be ploted
                #2: create the folder in which the marked images will be placed.
                #3: update this folder name to the class variable which will be used by the save function.
                #done
                #The earlier markings, if any over the current image, should be cleared. 
                #Else, when moving back and forth, the frames will be loaded only wrt the current nodule.
                #Todo: have separate framed_marked_array for each nodule.
                self.perform_nodule_selected(self.nodule_dict_index)
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
        print("len(self.added_nodule_indices) = "+str(len(self.added_nodule_indices)))
        numNodules = len(self.added_nodule_indices)
        #8888888888888888888888888888888888888888888888888888888
        #the loop needs to be updated. This needs to be exactly for the added nodules 
        for i in range(numNodules):
            #The nodule needs to be closed.
            self.nodule_dict[i].reinitialize()
            #Will check this later when the toolbar is there for marking individual images.
            #The action needs to removed from the toolbar.
            #self.action[i].setVisible(False)
        self.set_graph.remove_all_nodules()
        self.reinit_nodule_var_newer_implementation()
        #do call removal of edges
        #self.add_nodule_button.setText("Add Nodule")
   
    def is_nodule_displayed_same(self, nodule_index):
        if(nodule_index == self.nodule_dict_index or \
                nodule_index in self.nodule_dict_indices_shown_extra): 
            return True
        else:
            return False

    def chk_nodule_displayed_same(self, nodule_index, op):
        if(self.is_nodule_displayed_same(nodule_index)):
            return True
        else:
            msg = "Operation "+op+" can be be performed if the requested nodule "
            msg = msg + " is open in at least one image. Please open the nodule "
            msg = msg + "first."
            box_title = "Open nodule first."
            self.show_information(msg, box_title)
            return False

    def update_rest_mapping(self, nodule_display_index_deleted):
        for nodule_dict_index in self.added_nodule_indices:
            nodule_dict_index_displayed =\
                    self.get_displayed_nodule_index(nodule_dict_index)
            self.chk(\
                    nodule_dict_index_displayed != nodule_display_index_deleted\
                    ,"The entry for deleted index cannot appear again.")
            if(nodule_dict_index_displayed > nodule_display_index_deleted):                
                self.decrement_nodule_display_index(\
                        nodule_dict_index_displayed, nodule_dict_index)
        self.chk_bidict_equality(self.number_displayed_to_index_in_nodule_dict,\
                self.index_in_nodule_dict_to_number_displayed)

    def readjust_nodule_indices(self):
        """
        #if we have a single nodule left then place the index in self.nodule_dict_index.
        """
        if((len(self.nodule_dict_indices_shown_extra) == 1) and \
                (-1 == self.nodule_dict_index)):
            self.nodule_dict_index = self.nodule_dict_indices_shown_extra[0]
            self.nodule_dict_indices_shown_extra.remove(self.nodule_dict_index)
            if((len(self.nodule_dict_indices_shown_extra) > 0)):
                msg = "self.nodule_dict_indices_shown_extra "
                msg = msg + "should have been cleared by now."
                self.show_error(msg)
        #elif(len(self.nodule_dict_indices_shown_extra) > 1)):
        #    self.chk("self.nodule_dict_index should be -1 when multiple nodules remain after delete",\
        #            -1 == self.nodule_dict_index)
        #    if()
        #elif(len(self.nodule_dict_indices_shown_extra) == 0)):
        #    a

    def update_nodule_index_list_and_nodule_shown(self, nodule_dict_index):
        self.free_nodule_indices.append(nodule_dict_index)
        self.added_nodule_indices.remove(nodule_dict_index)
        if(nodule_dict_index == self.nodule_dict_index):
            self.nodule_dict_index = -1
        if(nodule_dict_index in self.nodule_dict_indices_shown_extra):
            self.nodule_dict_indices_shown_extra.remove(nodule_dict_index)
        #if we have a single nodule left then place the index in self.nodule_dict_index.
        self.readjust_nodule_indices()
        self.chk_added_free_nodule_indices_correctness()

    def redo_nodule_index_mapping(self, nodule_dict_index, nodule_display_index):
        self.nodule_dict[nodule_dict_index].hide_annotation_window()
        self.nodule_dict[nodule_dict_index].reinitialize()
        self.set_graph.remove_nodule(nodule_dict_index)
        self.write_image_nodule_dict()
        self.update_nodule_index_list_and_nodule_shown(nodule_dict_index)
        self.delete_entry_number_display_nodule_dict_mapping(\
                nodule_display_index, nodule_dict_index)
        self.update_rest_mapping(nodule_display_index)
        self.save_mapping_number_display_nodule_dict()
        self.set_graph.redraw_graph()


    def delete_yolo_boundary(self, image_name, nodule_id):
        """
        This function will delete the YOLO annotation with the given nodule_id from the respective file.
        """

        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!hn bhai nodule delete kar rahe ho kya baat!!!!!!!!!!! ",image_name)
        # Generate the file name from the image_name (e.g., image_name_yolo.txt)
        file_name = f"{os.path.splitext(image_name)[0]}.txt"
        file_name= Path(PurePath(self.directory_loaded.directoryPath)).joinpath(file_name)
        # Check if the file exists
        if not os.path.exists(file_name):
            print(f"File {file_name} not found.")
            return

        # Read the existing lines from the file
        with open(file_name, 'r') as file:
            lines = file.readlines()

        # Initialize a flag to check if the nodule_id was found and removed
        deleted = False
        
        # Filter out the lines where the class_id matches the given nodule_id
        updated_lines = []
        for line in lines:
            parts = line.strip().split()
            class_id = parts[0]
            
            # If the class_id matches the nodule_id, we skip that line
            if class_id != str(nodule_id):
                updated_lines.append(line)  # Keep the line in the updated list
            else:
                deleted = True  # Mark as deleted if we found and skipped the line

        if not deleted:
            print(f"Nodule ID {nodule_id} not found in the file.")
            return

        # Write the updated lines back to the file, effectively deleting the line with the nodule_id
        with open(file_name, 'w') as file:
            file.writelines(updated_lines)

        print(f"Nodule ID {nodule_id} successfully deleted from {file_name}.")


    def delete_the_folder_for_dict_index_x(self, nodule_dict_index):
        image_names = self.set_graph.nodule_to_img[nodule_dict_index]
        for image_name in image_names:
            self.directory_loaded.delete_dir(image_name, nodule_dict_index)
            #function to delete yolo boundary with respective nodule if from the same image
            self.delete_yolo_boundary(image_name, nodule_dict_index)

    def collate_nodule_indices_to_display(self):
        result = self.nodule_dict_indices_shown_extra
        if(-1 != self.nodule_dict_index):
            result.append(self.nodule_dict_index)
        return result

    def update_image_display_for_delete(self):
        if(1 == len(self.image_names_currently_displayed)):
            image_name = self.image_names_currently_displayed[0]
            self.selected_image_name_by_left_press = image_name 
            self.selected_image_name_by_right_click = image_name
            all_indices = self.collate_nodule_indices_to_display()
            if(len(all_indices)>0):
                self.add_given_list_of_nodules_to_image(image_name, all_indices)
            else:
                self.make_image_to_display(image_name)
        elif(1 < len(self.image_names_currently_displayed)):
            self.display_all_images_given_nodule(\
                    self.image_names_currently_displayed, -1)

    def delete_nodule(self):
        nodule_index_user = self.selected_nodule_index_in_dict_by_right_click
        self.delete_selected_nodule(nodule_index_user)

    def delete_selected_nodule(self, nodule_dict_index):
        """
        """
        if(not self.chk_nodule_displayed_same(nodule_dict_index,\
                "nodule delete")):
            return
        nodule_display_index = \
                self.get_displayed_nodule_index(nodule_dict_index)
        self.delete_the_folder_for_dict_index_x(nodule_dict_index)
        #call delete yolo bundary
        #(nodule_dict_index, )
        self.nodule_dict[nodule_dict_index].del_annotation()
        #del annotation will reset the save variable.
        #hence setting the save variable.
        self.set_nodule_save()
        self.redo_nodule_index_mapping(nodule_dict_index, nodule_display_index)
        self.set_nodule_save()
        self.update_image_display_for_delete()
        self.set_nodule_save()
    
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
      
        
        #use this button to close the window
        self.close_window_button = QtWidgets.QPushButton("Close Current Window")
        self.clear_marking_button = QtWidgets.QPushButton("Clear markings over Current Image")                
        
        self.close_image_button = QtWidgets.QPushButton("Close Current Video/Image")                
        self.set_image_label = UnscaledQLabel() 
        
        self.dicom_open_button = QtWidgets.QPushButton("Open Dicom Image or Video")
        self.dicom_dir_open_button = QtWidgets.QPushButton("Select Directory For Patient")
        self.image_label = UnscaledQLabel() # QtWidgets.QLabel()
        self.set_image = My_Image()
        # setHeight(28)
        self.qlabel_heading.setText(" ULTRASOUND GRAPH ANNOTATOR (UGA, v1.0) ")
        font = QFont()
        font.setBold(True)  # Set the font to bold
        self.qlabel_heading.setFont(font)    # Apply the font to the label
        self.qlabel_sub_heading.setText(" Annotate png/jpg/jpeg/RGB DICOM Images")
        
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
        #By this time, the width and height for the set image would have been set. Therefore, initializing
        #the image for set image 
        print("var of self.set_image="+str(vars(self.set_image)))
        self.set_image.init_image()
        
        # Add widgets to the layout with specified positions and sizes
        #self.layout.addWidget(self.image_search_button, 0, 0, 2, 1)  # 2 rows, 1 column
        self.layout.addWidget(self.qlabel_heading, 0, 0, 1, 1)
        self.layout.addWidget(self.qlabel_sub_heading, 1, 0, 1, 1)
        #Todo: removing the image search button. Check if it works correctly.
        # self.layout.addWidget(self.image_search_button, 2, 0, 1, 1)  #1 row, 1 column
        #self.layout.addWidget(self.dicom_open_button, 2, 0, 1, 1)  #1 row, 2 column
        
        self.layout.addWidget(self.dicom_dir_open_button, 2, 0, 1, 1)
        #self.layout.addWidget(self.play_forward_button, 4, 0, 1, 1)
        #self.layout.addWidget(self.play_backward_button, 4, 1, 1, 1)
        ## self.layout.addWidget(self.pause_button, 5, 0, 1, 2)
        #self.layout.addWidget(self.next_frame_button, 5, 0, 1, 2)
        #self.layout.addWidget(self.prev_frame_button, 6, 0, 1, 2)                
        ##//have addNodule button
        ##have a nodule toolbar
        ##n1, n2 ...
        ##self.layout.addWidget(self.add_nodule_button, 7, 0, 1, 2)
        #self.layout.addWidget(self.menuBar, 7, 0, 1, 2)

        #self.layout.addWidget(self.toolBar, 8, 0, 1, 2)
        #Todo: Also need to do set fixed size for menu bar since, the menu items will be added dynamically.
        
        #TODO: I need to have a toolbar here for nodules.
        #At first add all menus for n1 to n5 and and n1 to n10. Just for testing that does it display properly and does the menu for each nodule displays properly.
        
        
        #TODO: As asked by Dinesh sir, Later also try that the play , next/prev frame button should only be there only when  video is opened.
        #TODO: I am converting the paly button  to pause button. Hence there no  need for a separate pause button. Later remove this as well, when doing the above modification.
        
        self.layout.addWidget(self.clear_marking_button, 3,  0, 1, 2)
        #self.layout.addWidget(self.close_image_button,4, 0, 1,2)
        #self.layout.addWidget(self.save_button, 5, 0, 1,2)  # spans only 1 cell        
        self.layout.addWidget(self.close_window_button, 4, 0, 1,2)        
        self.layout.addWidget(self.set_image_label, 5, 0, 1,2)        
        
        self.layout.addWidget(self.image_label, 0, 1, 5, 1)
        
        
        #Todo: how to display complete string when drop down is called?
        #May be i need to subclass and and make custom combobox
        
        self.dicom_open_button.clicked.connect(self.getVideo)
        self.dicom_dir_open_button.clicked.connect(self.getDirectory)
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
        self.imagePaneManager=ImagePaneManager(self.width_for_image, self.height_for_image,\
                self.image_label_x_start, self.image_label_y_start, self)
                
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
            image = self.dicom_obj.pixel_array[self.frameIndex]
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
            self.image_alpha = np.zeros(self.image_scaled_shape)            
        else:
            self.image_alpha = np.zeros((self.image_shape[0], self.image_shape[1]))
        print("self.image_alpha.shape = "+str(self.image_alpha.shape))
                        
    def perform_image_scaling(self):
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

    def create_scaled_image_directory(self):
        if(len(self.image_names_currently_displayed[0])<=0):
            msg = "at least one image should be displayed for creating scaled image"
            self.show_warning(msg, "Ask Programmer")
        else:
            image_name = self.image_names_currently_displayed[0]
            image_ref = self.directory_loaded.loadedImages[image_name].image
            self.image_shape, self.image_scaled_bool = self.whether_rescaling_required(image_ref)
            if(self.image_scaled_bool):
                self.directory_loaded.loadedImages[image_name].fill(self.image_label_x_start, self.image_label_y_start,\
                        self.width_for_image, self.height_for_image, self.image_label)
                self.directory_loaded.loadedImages[image_name].create_scaled_image()
                self.image_width_for_display = self.directory_loaded\
                        .loadedImages[image_name].image_scaled_shape[1]
                self.image_height_for_display = self.directory_loaded\
                        .loadedImages[image_name].image_scaled_shape[0]
            else:
                self.image_width_for_display = self.image_shape[1]
                self.image_height_for_display = self.image_shape[0]            

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
            self.perform_image_scaling()
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
        #888888888888888888888888888888888 make this or create a separate 
        #function for images from same directory.
        self.image_selected = True
        #This is setting frame path, frame index, num frames.
        #This should not be required even for update for frame.
        #This will create confusion when handling multiple images.
        self.init_var_for_frame(1)
        #load for partial annotation should be stopped now because the 
        #load will be done wrt the partial directory annotation. 
        self.load_if_video_is_partially_annotated()      
        #a custom function for images from same directory.
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
            self.load_common_video_image(tmp_tuple)
            # self.thread_get_video.start()
            # self.show()
            # self.thread_get_video.join()
            self.video_loading_message_window.hide()
            #self.display_loading_window.hide()
            #self.video_loading_dialog.hide()

    def getDirectory(self):                
        self.reinitialize()
        #dir_ = QtGui.QFileDialog.getExistingDirectory(None, 'Choose '+self.image_name+' Video File', 'C:\\', QtGui.QFileDialog.ShowDirsOnly)
        dir_path = QFileDialog.getExistingDirectory(self,\
                                                caption='Choose Patient Directory',\
                                                    directory=self.dirpath)
        print(" dir_path = "+str(dir_path))
        if(dir_path!=''):
            #Load all the files in that folder
            self.directory_loaded.load_dir(dir_path)
            self.directory_loaded.define_save_path(self.max_num_nodules)
            self.set_graph.init_with_dir_ref(self.directory_loaded,\
                2*self.info_width, self.info_height)
            #self.set_graph.add_nodule(0)
            self.directory_opened = True 
            self.set_graph.redraw_graph()
            #files= os.listdir(dir_path)
            #print(files)
            self.reload_partially_annotated()

    def reload_partially_annotated(self):
        self.load_map_orientation()
        self.load_map_folder()
        #The alpha is always saved wrt original image size. therefore, while 
        #reloading directory set the image width and height for display same
        #as the original image size. While initial annotation it was not 
        #assumed that all images will be of the same size. Hence, follow that
        #here as well. set these values foe setting each image nodule connection.
        image_to_nodule_loaded = self.directory_loaded.load_file(\
                "Image_to_nodule.txt")
        folder_present_list = self.directory_loaded.get_folders_present_list(\
                self.max_num_nodules)
        self.chk_non_empty_conditions(folder_present_list, image_to_nodule_loaded)
        self.update_display_for_orientation()
        #The following conditions says that nodules are present.
        if(len(self.number_displayed_to_index_in_nodule_dict) >0 ):
            self.initialize_nodule_boxes_in_graph_class()
            self.initialize_nodules_for_edges()
            self.add_edges_nodule_graph_class(image_to_nodule_loaded)
            self.load_annotation()
            self.load_alpha(image_to_nodule_loaded)
            self.update_added_free_nodule_indices()
        self.set_nodule_save()
        self.set_graph.redraw_graph()
    
    def chk_non_empty_conditions(self, folder_present_list, image_to_nodule_loaded):
        if (len(self.number_displayed_to_index_in_nodule_dict) >0 ):
            self.chk("len(folder_present_list)>0", len(folder_present_list)>0)
        else:
            self.chk("len(folder_present_list)==0", len(folder_present_list)==0)
        if ( len(image_to_nodule_loaded)>0 ):
            self.chk("len(folder_present_list)>0", len(folder_present_list)>0)
        else:
            self.chk("len(folder_present_list)==0", len(folder_present_list)==0)

    def load_map_folder(self):
        filename = "map_folder.txt"
        folder_table = self.directory_loaded.load_file(filename)
        if( []!=folder_table ):
            for row_index in range(1,len(folder_table)):
                row = folder_table[row_index]
                self.chk_2_rows(row, filename)
                number_displayed = (int)(row[0])
                dict_index = (int)(row[1])
                self.update_number_display_nodule_dict_mapping(\
                        number_displayed, dict_index)

    def chk_2_rows(self, row, filename):
        if(len(row)!=2):
            msg = "every entry in "+filename+" must have 2 rows."
            self.show_error(msg)

    def load_map_orientation(self):
        filename = "map_orientation.txt"
        orientation_table = self.directory_loaded.load_file(filename)
        if( []!=orientation_table ):
            for row_index in range(1,len(orientation_table)):
                row = orientation_table[row_index]
                self.chk_2_rows(row, filename)
                image_name = row[0]
                orientation = row[1]
                self.image_to_orientation[image_name] = orientation

    def update_display_for_orientation(self):
        for imagename, orientation in self.image_to_orientation.items():
            self.updateOrientation(imagename, orientation)

    def initialize_nodule_boxes_in_graph_class(self):
        for nodule_dict_index, nodule_display_index in\
                self.index_in_nodule_dict_to_number_displayed.items():
                    self.set_graph.add_nodule(\
                            nodule_dict_index, nodule_display_index)  

    def initialize_nodules_for_edges(self):
        for nodule_dict_index in self.index_in_nodule_dict_to_number_displayed:
            self.init_nodule_for_edges(nodule_dict_index)

    def add_edges_nodule_graph_class(self, image_to_nodule_loaded):
        """
        This function initialize nodule classes for relaoding 
        partially annotated directory.
        """
        for row_index in range(1,len(image_to_nodule_loaded)):
            row = image_to_nodule_loaded[row_index]
            image_name = row[0]
            self.image_shape = \
                    self.directory_loaded.loadedImages[image_name].image.shape
            self.image_width_for_display = self.image_shape[1]
            self.image_height_for_display = self.image_shape[0]            
            #Setting selected image name so that adding edges does not raise error
            self.set_graph.set_selected_image_name([image_name])
            for col_index in range(1, len(row)):
                nodule_dict_index = (int)(row[col_index])
                self.add_img_nodule_connection_core(image_name, nodule_dict_index)
        self.set_graph.set_selected_image_name([])

    def load_annotation(self):
        for nodule_dict_index in self.index_in_nodule_dict_to_number_displayed:
            self.nodule_dict[nodule_dict_index].load_annotation()

    def load_alpha(self, image_to_nodule_loaded):
        for row_index in range(1,len(image_to_nodule_loaded)):
            row = image_to_nodule_loaded[row_index]
            image_name = row[0]
            for col_index in range(1, len(row)):
                nodule_dict_index = (int)(row[col_index])
                self.load_frame(image_name, nodule_dict_index)

    def update_added_free_nodule_indices(self):
        for nodule_dict_index in self.index_in_nodule_dict_to_number_displayed:
            self.free_nodule_indices.remove(nodule_dict_index)
            self.added_nodule_indices.append(nodule_dict_index)
        self.chk_added_free_nodule_indices_correctness()

    def chk_added_free_nodule_indices_correctness(self):
        #len sum must be max nodule. the list must be non intersecting and contain all number 0 to max -1.
        #just concate the lists, sort and uniq and chk 1 to 10.
        #Call this for add, delete nodule and reload directory.
        #Call done at required positions.
        msg = "The added and free indices must add to 0 to max nodules-1."
        if((len(self.free_nodule_indices)+len(self.added_nodule_indices))\
                !=self.max_num_nodules):
            self.show_error(msg)
        total_indices = self.free_nodule_indices + self.added_nodule_indices
        uniq_list = sorted(set(total_indices))
        if( len(uniq_list) != self.max_num_nodules ):
            self.show_error(msg)
        expected_list = list(range(len(uniq_list)))
        if (not(expected_list == uniq_list)):
            print("\nexpected_list="+str(expected_list))
            print("\nuniq_list="+str(uniq_list))
            self.show_error(msg)

    def get_image_name_to_display(self):
        """
        This function returns the image name to display based on 
        whether the last click was left or right.
        """
        if(self.mouse_action!=self.mouse_press):
            self.show_error("The image is displayed only on mouse press.")
        if(self.mouse_button == self.mouse_null):
            self.show_error("mouse button cannot be null when trying to display an image.")
        if(self.mouse_button == self.wheel_button):
            self.show_error("Display image on wheel button has not been implemented yet.")
        if(self.mouse_button == self.left_button):
            return self.selected_image_name_by_left_press
        elif(self.mouse_button == self.right_button):
            return self.selected_image_name_by_right_click

    def chk_image_name_is_loaded(self, image_name):
        if("" == image_name):
            self.show_error("Image name cannot be empty.")
        elif(not(image_name in self.directory_loaded.loadedImages)):
            self.show_error("Image "+image_name+" is not loaded.")

    #def show_image_functionality(self, image_name):
    #    """
    #    This function must be called only if all the essential checks have been done before.
    #    """
    #    self.make_image_to_display(image_name)
    #    #we are displaying an image which should be dfferent that the earlier displayed image, because only in 
    #    #such a condition, this function will be called. Therefore, make nodule_dict_index as -1 and hide any
    #    #annotation windows displayed so far. This function is only called by showImageOnly. The showImageOnly
    #    #implies that display of only image is required. But the function name suggests that the functionality 
    #    #of showing images. Hence, this function naturally seems to be an eligible candidate for showing image 
    #    #with multiple nodules. Hence, donot create a confusing function. 
    #    #The display of image without unselecting the nodule also seems incorrect. This all depends only on 
    #    #the place where the show image is called.
    #    #After visualizing the functions, the function show_image_functionality seems useless.
    #    #the functions make_image_to_display and showImageOnly seems to suffice all the conditions.
    #    self.perform_nodule_selected(-1)

    def showImageOnly(self):
        print("showing the image only")
        #We are getting the image name to display based on whether last click was left or right.
        self.reinit_boundary_shape()
        image_name = self.get_image_name_to_display()
        self.chk_image_name_is_loaded(image_name)
        self.make_image_to_display(image_name)
        self.perform_nodule_selected(-1)
        #self.show_image_functionality(image_name)

    def add_given_list_of_nodule_alpha(self, image_name, nodule_indices):
        self.image = self.directory_loaded.loadedImages[image_name].image.copy()
        for nodule_index in nodule_indices:
            self.image = self.add_alpha_to_single_image(self.image, image_name, nodule_index)
        self.set_nodule_save()

    def add_given_list_of_nodules_to_image(self, image_name, nodule_indices):
        num_nodules_to_display = len(nodule_indices)        
        if( 1==num_nodules_to_display ):            
            self.show_nodule_single_image(image_name, nodule_indices[0])
        elif( 0==num_nodules_to_display ):            
            self.show_information("no nodules have been added for this image.", "no nodules present")
        else:
            if(num_nodules_to_display<0):
                self.show_error("number of nodules cannot be negative.")
            self.nodule_dict_indices_shown_extra = nodule_indices.copy()
            #the other functionality of show_nodule_single_image is not required because that is implied by 
            #showImageOnly
            self.add_given_list_of_nodule_alpha(image_name, nodule_indices)
            self.set_graph.highlight_nodules_consistently()
            #the not show showing of annotaion window has already been doen by showImageOnly.

    def showImageWithNodules(self):
        print("Showing the image with previously marked nodules")
        image_name = self.get_image_name_to_display()
        self.showImageOnly()
        #when shown the image, there is no already displayed nodule.
        #
        #get nodule indices for this image
        nodule_indices = self.set_graph.get_nodules_indices_in_dict_given_image(image_name)
        self.add_given_list_of_nodules_to_image(image_name, nodule_indices)

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
                    print("self.nodule_dict_index="+str(self.nodule_dict_index))
                    print("tmp_nodule_index="+str(tmp_nodule_index))
                    assert self.nodule_dict_index == tmp_nodule_index, "The indices of the nodules must match."
                    nodule_df_chk = video_df_current_file.iloc[:,2] == self.nodule_dict_index
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
                    self.nodule_dict[self.nodule_dict_index].load_annotation(nodule_df.iloc[entry_index_to_load,:])
                    #Now load the frame annotated array for the last nodule
                    self.load_frame_annotated_array_from_video_filename(self.nodule_dict_index)
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
        if(1==self.frame_marked_array[self.nodule_dict_index][self.frameIndex]):
            #load the saved frame
            self.load_annotated_frame()
        else:
            if(self.video_selected):
                self.image = self.get_frame_at_frameIndex()
            elif(self.image_selected):
                self.image = self.get_image()
            else:
                assert False, "This condition cannot occur"
            self.dicom_obj_loaded_annotated = None
            self.saved_image = self.image.copy()
            self.create_scaled_image_and_alpha()
        print("showing frame "+str(self.frameIndex))
        self.next_frame_button.setText("Show Next frame, Current Frame Index = "+str(self.frameIndex))
        self.frame_updated = True        
        self.activateWindow()
        
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
            
            #self.dicom_open_button.setGeometry(window_margin\
            #                                     , self.y_pos_third_row,\
            #                               2*self.info_width, self.info_height)
                
            self.dicom_dir_open_button.setGeometry(window_margin, self.y_pos_third_row,\
                                           2*self.info_width, self.info_height) 
            #self.play_forward_button.setGeometry(window_margin, self.y_pos_fifth_row,\
            #                               self.info_width, self.info_height) 
            #self.play_forward_button.setFixedSize(self.info_width, self.info_height)
            #
            #self.play_backward_button.setGeometry(window_margin+self.info_width, self.y_pos_fifth_row,\
            #                               self.info_width, self.info_height)
            #self.play_backward_button.setFixedSize(self.info_width, self.info_height)
            #self.next_frame_button.setGeometry(window_margin, self.y_pos_sixth_row,\
            #                               2*self.info_width, self.info_height)
            #self.next_frame_button.setFixedSize(2*self.info_width, self.info_height)
            #self.prev_frame_button.setGeometry(window_margin, self.y_pos_seventh_row,\
            #                               2*self.info_width, self.info_height)
                
            #self.menuBar.setGeometry(window_margin, self.y_pos_eighth_row,\
            #                               2*self.info_width, self.info_height)
            #self.menuBar.setFixedSize(2*self.info_width, self.info_height)
            #
            #self.toolBar.setGeometry(window_margin, self.y_pos_nineth_row,\
            #                                2*self.info_width, self.info_height)
            #self.toolBar.setFixedSize(2*self.info_width, self.info_height)
                
            self.clear_marking_button.setGeometry(window_margin, self.y_pos_fourth_row,\
                             2*self.info_width, self.info_height)            
            #self.close_image_button.setGeometry(window_margin, self.y_pos_fifth_row,\
            #                             2*self.info_width, self.info_height)            
            #self.save_button.setGeometry(window_margin, self.y_pos_twelth_row,\
            #                             2*self.info_width, self.info_height)
            self.close_window_button.setGeometry(window_margin, self.y_pos_fifth_row,\
                                         2*self.info_width, self.info_height)           
            self.update_image_label_dim()
            self.update_set_image_label_dim()
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

    def update_set_image_label_dim(self):
        """
        This function updates the image label dimension.

        Returns
        -------
        None.

        """
        #initialize My_Image(): here
        #But the compute sizes will be called every time the reinitialize gets called. therefore the 
        #set_image must be initialized in initUI and the entries must be filled here.
        #The init image needs to be called on every reinitialize. Therefore, it seems appropriate to call the 
        #init_image_here.
        x_start = window_margin 
        y_start = self.y_pos_fourteenth_row #0 #self.y_pos_first_row
        
        width = 2*self.info_width     
        #subtract the fourteenth row from total height      
        height = self.height_for_image - y_start
        #Why this computation being done 2 times for axial
        #The code is running thisway.
        print("width = "+str(width)+" for "+self.image_name)
        print("height = "+str(height)+" for "+self.image_name)
        
        self.set_image.fill(x_start, y_start, width, height, self.set_image_label)
        self.set_image_label.setGeometry(x_start, y_start, width, height)
        self.set_image_label.setFixedSize(width, height)
        assert (y_start + height) <= self.height_for_image , "height should not exceed"            
    
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

    def show_set_image(self):
        #self.set_image.image[:,:,:]=0
        rgba_image = cv2.cvtColor(self.set_image.image, cv2.COLOR_RGB2RGBA)        
        #print("rgba_image="+str(rgba_image))
        #print("type(rgba_image=)"+str(type(rgba_image)))
        qimage = QtGui.QImage(rgba_image.data, rgba_image.shape[1],
            rgba_image.shape[0], QtGui.QImage.Format_RGBA8888)
        pixmap = QtGui.QPixmap(qimage)
        self.set_image_label.setPixmap(pixmap)

    def show_image_directory_earlier(self):
        #need to display the axial image
        image_name = self.image_names_currently_displayed[0]
        if(self.image_scaled_bool):
            self.rgba_image = cv2.cvtColor(self.directory_loaded.loadedImages[image_name].image_scaled_array,\
                    cv2.COLOR_RGB2RGBA)        
        else:
            self.rgba_image = cv2.cvtColor(self.directory_loaded.loadedImages[image_name].image,\
                    cv2.COLOR_RGB2RGBA)                        
        #print("self.rgba_image="+str(self.rgba_image))
        qimage = QtGui.QImage(self.rgba_image.data, self.rgba_image.shape[1],
                                    self.rgba_image.shape[0], QtGui.QImage.Format_RGBA8888)
        pixmap = QtGui.QPixmap(qimage)
        self.image_label.setPixmap(pixmap)

    def show_image_directory(self):
        #need to display the axial image
        image_name = self.image_names_currently_displayed[0]
        if(self.image_scaled_bool):
            self.rgba_image = cv2.cvtColor(\
                    self.directory_loaded.loadedImages[image_name]\
                    .image_scaled_array, cv2.COLOR_RGB2RGBA)        
        else:
            self.rgba_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2RGBA)                        
        #print("self.rgba_image="+str(self.rgba_image))
        qimage = QtGui.QImage(self.rgba_image.data, self.rgba_image.shape[1],
                                    self.rgba_image.shape[0], QtGui.QImage.Format_RGBA8888)
        pixmap = QtGui.QPixmap(qimage)
        self.image_label.setPixmap(pixmap)

    def show_image_single(self):
        #need to display the axial image
        if(self.image_scaled_bool):
            self.rgba_image = cv2.cvtColor(self.image_scaled_array, cv2.COLOR_RGB2RGBA)        
        else:
            self.rgba_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2RGBA)                        
        #print("self.rgba_image="+str(self.rgba_image))
        qimage = QtGui.QImage(self.rgba_image.data, self.rgba_image.shape[1],
                                    self.rgba_image.shape[0], QtGui.QImage.Format_RGBA8888)
        pixmap = QtGui.QPixmap(qimage)
        self.image_label.setPixmap(pixmap)
        #self.image_label.setText("saved")
        # print("updated pixmap")

    def show_image(self):
        #rgba_image = self.image #cv2.cvtColor(self.image, cv2.COLOR_BGR2RGBA)
        # self.rgba_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGBA)
        # Get the size of a QWidget
        # print("inside_show_image")
        #if(False == self.window_size_computed):
        self.compute_sizes()
        if(self.image_opened or self.video_opened):            
            self.show_image_single()
            self.show_set_image()
        elif(self.directory_opened):
            #Here a different function may be called for the case of directory when multiple images are to be 
            #shown.
            if(self.show_image_clicked):
                self.show_image_directory()
            self.show_set_image()
    
    def make_image_to_display(self, image_name):
        """
        This function fills important data structures so that image can be displayed afresh.
        """
        self.image = self.directory_loaded.loadedImages[image_name].image.copy()
        self.image_names_currently_displayed = [image_name]
        self.set_graph.special_highlight_image_boxes()
        self.show_image_clicked = True 
        #Other than creating the image for alpha and creating the scaled image required, the following function 
        #also, set the important variable wrt image displayed like image_width_for_display and 
        #image_height_for_display.
        self.create_scaled_image_directory()

    def clear_image_display(self):
        if( self.directory_opened ):
            (isSameImageDisplayed, numImagesDisplayed, image_name_displayed) = self.chkSameImageOpened("")
            #We want to get the name of the image displayed and the number of images displayed. Hence,
            #null string is passed and therefore, isSameImageDisplayed is not used.
            if(numImagesDisplayed!=1):
                self.show_warning_num_images_displayed("clear_image_display")
            else:
                self.make_image_to_display(image_name_displayed)

    def reinit_boundary_shape(self):
        self.current_nodule_shape = "PolyLine" # Set "Rectangle" as the default
        self.rectangle_coordinates=[]
        self.tmp_rectangle_coordinates=[0,0,0,0]
        self.first_rectangle_coordinate_flag= False
        self.action_circle.trigger()
        #self.shape_action_group.triggered.connect(self.handle_shape_selection)
    

    def clear_image_markings(self):
        if( self.directory_opened ):
            nodule_dict_index = self.nodule_dict_index
            if (-1 != nodule_dict_index):
                (isSameImageDisplayed, numImagesDisplayed,\
                        image_name_displayed) = self.chkSameImageOpened("")
                #We want to get the name of the image displayed and the 
                #number of images displayed. Hence,
                #null string is passed and therefore, isSameImageDisplayed
                #is not used.
                self.reinit_boundary_shape()
                if(numImagesDisplayed!=1):
                    self.show_warning_num_images_displayed(\
                            "clear_image_markings")
                else: #if(1==numImagesDisplayed):
                    self.nodule_dict[nodule_dict_index].reinit_alpha(\
                            image_name_displayed)
                    if(self.directory_loaded.chk_if_nodule_image_alpha_written(\
                            image_name_displayed, nodule_dict_index)):
                       #The following will save alpha.
                       self.save_image()
                    self.add_given_list_of_nodule_alpha(\
                            image_name_displayed, [nodule_dict_index])
        
    def delete_edge(self, image_name, nodule_dict_index):
        """
        The function removes a single edge 
        """
        self.nodule_dict[nodule_index].remove_image_connection(image_name)
        #s

    def clear_loaded_frame(self):
        """
        This function clears the loaded frame, if any frame was loaded earlier

        Returns
        -------
        None.

        """        
        self.dicom_obj_loaded_annotated = None
        self.image_loaded = None
        
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
        self.imagePaneManager.reinit()
        
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
        self.rgba_image = None
        self.rgba_image_to_save = None
        
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
     
    def print_2_dict(self, dict1, dict2):
        msg = "Both dict should have same number of elements, "
        msg = msg + "because they are emulating a bidict.\n"
        msg = msg + "len(dict1) = "+str(len(dict1))+".\n"
        msg = msg + "len(dict2) = "+str(len(dict2))+".\n"
        msg = msg + "(dict1) = "+str(dict1)+".\n"
        msg = msg + "(dict2) = "+str(dict2)+".\n"
        print(msg)

    def delete_entry_number_display_nodule_dict_mapping(self, newNumberToDisplay,\
            nodule_dict_index):
        msg = "The mapping to delete must be already present."
        if(False == (newNumberToDisplay in \
                self.number_displayed_to_index_in_nodule_dict)):
            self.show_error(msg)
        if(False == (nodule_dict_index in \
                self.index_in_nodule_dict_to_number_displayed)):
            self.show_error(msg)
        del self.number_displayed_to_index_in_nodule_dict[newNumberToDisplay]
        del self.index_in_nodule_dict_to_number_displayed[nodule_dict_index]
        self.chk_bidict_equality(self.number_displayed_to_index_in_nodule_dict,\
                self.index_in_nodule_dict_to_number_displayed)
        #self.print_2_dict(self.number_displayed_to_index_in_nodule_dict,\
        #        self.index_in_nodule_dict_to_number_displayed)

    def decrement_nodule_display_index(self,\
            mapped_display_index, nodule_dict_index):
        msg = "The mapping to update must exist already."
        if(self.index_in_nodule_dict_to_number_displayed[nodule_dict_index]\
                != mapped_display_index):
            self.show_error(msg)
        if(self.number_displayed_to_index_in_nodule_dict[mapped_display_index]\
                != nodule_dict_index):
            self.show_error(msg)
        new_display_index = mapped_display_index - 1
        print("new_display_index")
        print(new_display_index)
        print("nodule_dict_index")
        print(nodule_dict_index)
        print("mapped_display_index")
        print(mapped_display_index)
        self.index_in_nodule_dict_to_number_displayed[nodule_dict_index] =\
                new_display_index
        self.number_displayed_to_index_in_nodule_dict[new_display_index] =\
                nodule_dict_index
        #The following extra entry must be deleted now.
        del self.number_displayed_to_index_in_nodule_dict[mapped_display_index]
        self.chk_bidict_equality(self.number_displayed_to_index_in_nodule_dict,\
                self.index_in_nodule_dict_to_number_displayed)
        self.set_graph.update_nodule_display_index(\
                nodule_dict_index, new_display_index)

    def update_number_display_nodule_dict_mapping(self, newNumberToDisplay,\
            nodule_dict_index):
        assert (False == (newNumberToDisplay in self.number_displayed_to_index_in_nodule_dict)),\
                "The mapping cannot be already present for the new number to display."
        assert (False == (nodule_dict_index in self.index_in_nodule_dict_to_number_displayed)),\
                "The nodule index could not be already mapped to any displayed number."
        self.number_displayed_to_index_in_nodule_dict[newNumberToDisplay] = nodule_dict_index
        self.index_in_nodule_dict_to_number_displayed[nodule_dict_index] = newNumberToDisplay
        self.chk_bidict_equality(self.number_displayed_to_index_in_nodule_dict,\
                self.index_in_nodule_dict_to_number_displayed)

    def chk_bict_len_equality(self, dict1, dict2):
        if(len(dict1) != len(dict2)):
            msg = "Both dict should have same number of elements, "
            msg = msg + "because they are emulating a bidict.\n"
            msg = msg + "len(dict1) = "+str(len(dict1))+".\n"
            msg = msg + "len(dict2) = "+str(len(dict2))+".\n"
            msg = msg + "(dict1) = "+str(dict1)+".\n"
            msg = msg + "(dict2) = "+str(dict2)+".\n"
            self.show_error(msg)

    def chk_bidict_equality(self, dict1, dict2):
        """
        This function checks equality of two dicts where key, value in onedict are value, key in the other dict.
        """
        self.chk_bict_len_equality(dict1, dict2)
        for k1, v1 in dict1.items():
            assert (dict2[v1] == k1), "same mapping should be present in both dict."

    def save_mapping_number_display_nodule_dict(self):
        self.chk_bidict_equality(self.number_displayed_to_index_in_nodule_dict,\
                self.index_in_nodule_dict_to_number_displayed)
        filename = "map_folder.txt" #_number_displayed_to_index_in_nodule_dict
        header = "number_displayed\tdirectory_number(dict_index)"
        if(len(self.number_displayed_to_index_in_nodule_dict)>0):
            self.write_dict(self.number_displayed_to_index_in_nodule_dict,\
                    header, True, False, filename)
        else:
            #delete the file
            self.directory_loaded.delete_file(filename)

    def reset_nodule_save(self):
        #When a new nodule is added, by default the save is false
        self.nodule_annotation_saved = False
        self.nodule_marking_saved = False
    
    def set_nodule_save(self):
        #When a marked nodule is shown, by default the save is True
        self.nodule_annotation_saved = True
        self.nodule_marking_saved = True

    def is_nodule_saved(self):
        if(self.nodule_annotation_saved and self.nodule_marking_saved):
            return True
        else:
            return False

    def reset_nodule_annotation_saved(self):
        self.nodule_annotation_saved = False

    def set_nodule_annotation_saved(self):
        self.nodule_annotation_saved = True

    def set_nodule_marking_saved(self):
        self.nodule_marking_saved = True

    def reset_nodule_marking_saved(self):
        self.nodule_marking_saved = False

    def chk_single_nodule_validity(self):
        if((-1==self.nodule_dict_index) and (1==len(self.nodule_dict_indices_shown_extra))):
            self.show_error("A single nodule cannot be placed in extra nodules.")
        if( len(self.nodule_dict_indices_shown_extra) < 0 or \
                len(self.nodule_dict_indices_shown_extra) > self.max_num_nodules):
            self.show_error("The length of extra nodules must be within range.")

    def get_num_nodule_displayed(self):
        numNodulesDisplayed = 0
        if(self.nodule_dict_index!=-1):
            numNodulesDisplayed = 1
        numNodulesDisplayed = numNodulesDisplayed + len(self.nodule_dict_indices_shown_extra)
        self.chk_single_nodule_validity()
        return numNodulesDisplayed

    def reinit_nodule_var_newer_implementation(self):
        """
        This function initializes the variables required for nodules.

        Returns
        -------
        None.

        """
        self.max_num_nodules=10
        #not explicitly maintaining num nodules. It is unnecessary bookkeeping.
        self.nodule_dict_index = -1
        self.number_displayed_to_index_in_nodule_dict = {}
        self.index_in_nodule_dict_to_number_displayed = {}
        self.added_nodule_indices=[]
        self.free_nodule_indices=[]
        self.reset_nodule_save()
        for i in range(self.max_num_nodules):
            self.free_nodule_indices.append(i)
        #the list contain the set of nodules whose markings are being displayed currently.
        #There may be more than one nodule whose markings are displayed currently.
        #Hence, keeping a list.
        self.nodule_dict_indices_shown_extra = []

    def init_mouse_action_constants(self):
        self.mouse_press = -1 
        self.mouse_release = 1
        self.mouse_move = 0
        self.mouse_wheel_moved = 2

    def init_mouse_button_constants(self):
        self.left_button = -1 
        self.right_button = 1
        self.wheel_button = 0

    def init_mouse_image_constants(self):
        self.mouse_over_set_image = -1
        self.mouse_over_dicom_image = 1

    def chk_which_extra_button(self, event):
        # Get the pressed buttons
        pressed_buttons = event.buttons()

        # Define a dictionary for button names (includes all Qt.MouseButtons)
        button_names = {
            Qt.NoButton: "No Button",
            Qt.AllButtons: "All Buttons",
            Qt.LeftButton: "Left Button",
            Qt.RightButton: "Right Button",
            Qt.MiddleButton: "Middle Button",
            Qt.BackButton: "Back Button",
            Qt.ExtraButton1: "Extra Button 1",
            Qt.ExtraButton2: "Extra Button 2",
            Qt.ExtraButton3: "Extra Button 3",
            Qt.ExtraButton4: "Extra Button 4",
            Qt.ExtraButton5: "Extra Button 5",
            Qt.ExtraButton6: "Extra Button 6",
            Qt.ExtraButton7: "Extra Button 7",
            Qt.ExtraButton8: "Extra Button 8",
            Qt.ExtraButton9: "Extra Button 9",
            Qt.ExtraButton10: "Extra Button 10",
            Qt.ExtraButton11: "Extra Button 11",
            Qt.ExtraButton12: "Extra Button 12",
            Qt.ExtraButton13: "Extra Button 13",
            Qt.ExtraButton14: "Extra Button 14",
            Qt.ExtraButton15: "Extra Button 15",
            Qt.ExtraButton16: "Extra Button 16",
            Qt.ExtraButton17: "Extra Button 17",
            Qt.ExtraButton18: "Extra Button 18",
            Qt.ExtraButton19: "Extra Button 19",
            Qt.ExtraButton20: "Extra Button 20",
            Qt.ExtraButton21: "Extra Button 21",
            Qt.ExtraButton22: "Extra Button 22",
            Qt.ExtraButton23: "Extra Button 23",
            Qt.ExtraButton24: "Extra Button 24",
        }

        # Check for combinations using bitwise OR
        pressed_list = []
        for button in button_names:
            if pressed_buttons & button:
                pressed_list.append(button_names[button])

        # Print the pressed button combinations
        if pressed_list:
            combinations = ", ".join(pressed_list)
            print(f"Pressed buttons: {combinations}")
        else:
            print("No mouse button pressed")


    def update_mouse_action_variables(self, event, mouse_image, mouse_action):
        self.mouse_image = mouse_image
        self.mouse_action = mouse_action
        #The button thing will be updated(left right) only if wheel event is not there 
        if(self.mouse_action == self.mouse_wheel_moved):
            self.mouse_button = self.mouse_null #self.wheel_button
            #I donot need to look at event button for the case of wheel moved.
            #In fact event button may be absent in this case.
            #if(event.buttons() == Qt.MiddleButton):
            #    msg = "middle button pressed caught in WHEEL EVENT IS NOT THERE."
            #    print(msg)
            #In the release event the button info seems to be missing. The reason must be that the button which was 
            #pressed is the same as the release button.
        elif(self.mouse_action == self.mouse_release):
            #No need to update the mouse button. it must be same as that was set earlier.
            print("self.mouse_button = "+str(self.mouse_button))
        else:
            if event.buttons() == QtCore.Qt.LeftButton:                        
                self.mouse_button = self.left_button
            elif event.buttons() == QtCore.Qt.RightButton:
                self.mouse_button = self.right_button
            else:
                if(event.buttons() == Qt.MiddleButton):
                    self.mouse_button = self.wheel_button
                    #The wheel button press has not been implemented yet.
                    msg = "The wheel button press has no role on images."
                    self.show_warning(msg, "Invalid press.")
                    #"middle button prssed caught WHEEL EVENT IS NOT THERE. Please consult the programmer."
                    #self.show_error(msg)
                else:
                    self.chk_which_extra_button(event)
                    #msg = "This condition in mouse update cannot be reached. Please consult the programmer."
                    msg = "Invalid mouse button."
                    txt =  msg + "\n nothing lost. start from where you left off."
                    self.show_warning(txt, msg)
                    #msg = msg + str(event.buttons())
                    #msg = msg+"\n vars of dicom annotator are: "
                    #msg = msg+str(vars(self))
                    #self.show_error(msg)

    def clear_mouse_action_variables(self):
        self.mouse_null = 100
        #Later an array of these may be maintained. We can then keep track of previous clicks.
        #For all the one liner updates, we will can use a queue instead of a single variable and all the updates
        #will work fine.
        #888888888888888888888888888888888888888888888888888888
        #There is one concern here. These variables will get updated at different times and there will be 
        #inconsistency in these variables. Instead, we can create a function to update all these and get all the
        #required details.
        #THIS IS ALSO one liner to update by the handler fired. Hence, no need to create a separate function to 
        #update this(self.mouse_image).
        #The one liner update( that was thought ) will be used to pass appropriate mouse constant.
        self.mouse_image = self.mouse_null
        self.mouse_button = self.mouse_null
        #This is a one liner to update by the event handler. Hence, no need to create a separate function to 
        #update this(self.mouse_action).
        self.mouse_action = self.mouse_null
        self.init_mouse_action_constants()
        self.init_mouse_button_constants()
        self.init_mouse_image_constants()

    def clear_set_image_related_variables(self):
        self.clear_mouse_action_variables()
        self.directory_opened = False 
        self.set_image_drag_started = False
        self.partial_line_drawn = False
        #The set image needs to be reinitialized when reinitialize is done, i.e. we are moving to a new patient 
        #or an independent video or image.
        #The clearing of label is not required as the image is reinitialized with its original initial
        #pixel values.
        #self.set_image_label.clear()
        self.set_image.reinit_image()
        self.directory_loaded.reinit()
        self.set_graph.reinit()
        self.selected_image_name_by_right_click = ""
        self.selected_image_name_by_left_press = ""
        self.show_image_clicked = False
        self.reinit_nodule_var_newer_implementation()
        self.selected_nodule_index_in_dict_by_right_click = -1
        self.selected_nodule_index_in_dict_by_left_click = -1
        #the image to orientation is a dictionary that stores axial or sagital for every image.
        self.image_to_orientation = {}
        #This is the name of the image that is currently being displayed.
        #using a list for image name currently displayed. The reason is that, it may contain more than element 
        #when multiple images gets displayed simultaneously
        #When only a single image is being displayed, then the following list will have only one value.
        #remember to update this variable 
        self.image_names_currently_displayed = []
        #Earlier at some point by looking at the similarity wrt images shown array, I thought to put even the 
        #nodule dict index into this array. But, there is one special case in nodules that is other nodules 
        #being shown and one nodule being marked. But there is no such special case for images. It is not that 
        #other images being show and one is being marked. And even such thing happens this is just a matter of 
        #choice. I am having one common array for images and an array and a variable for the nodules.
        #The following is the nodule index for which the annotation window is being displayed currently.
        #At a time only one annotation window can be shown. Hence keeping an integer for that.
        #Can the nodule_dict_index and nodule_index_annotation_window_display have different values.
        #actually the nodule dict index is the index for the nodule which is selected by the user.
        #We cannot display an annotation window for any nodule which is not clicked by the user.
        #But for the case when images are shown simultaneously, it could have happened that we need to 
        #display nodule other than the clicked by the user. May be a user clicked on a small image and we tend 
        #to display all nodules or other nodules or their annotation window. Hence, currently comment the 
        #variable  self.nodule_index_annotation_window_display. We may take further decisions over this variable 
        #later on.
        #self.nodule_index_annotation_window_display = -1
        #currently focussing on the situation when multiple nodules are being shown simultaneously.

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
        #The following function itself is doing the reinitialization of all the variables for nodules.
        self.delete_all_nodules()
        self.clear_set_image_related_variables()
        
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
        #They are used to tell whether video has been selected or image has been selected.
        #They have been added to add extra feature in update for frame when loading annotated frame initially, without disrupting the 
        #rest of the functionality.
        self.image_selected = False
        self.video_selected = False
        self.show_saved_thread = None


    def update_loaded_image_for_loaded_markings(self):
        """
        This function will update the loaded image for loaded markings.
        """
        if(self.color_dict[self.nodule_dict_index] == "Red"):
            #now update the red channel wrt  marking in alpha channel        
            self.image[:,:,0] = (np.maximum(self.image_loaded[:, :, 3],self.image_loaded[:, :, 0])).copy()
        if(self.color_dict[self.nodule_dict_index] == "Green"):
            #now update the green channel wrt  marking in alpha channel        
            self.image[:,:,1] = (np.maximum(self.image_loaded[:, :, 3],self.image_loaded[:, :, 1])).copy()
        if(self.color_dict[self.nodule_dict_index] == "Blue"):
            #now update the blue channel wrt  marking in alpha channel        
            self.image[:,:,2] = (np.maximum(self.image_loaded[:, :, 3],self.image_loaded[:, :, 2])).copy()
        if(self.color_dict[self.nodule_dict_index] == "Yellow"):
            #now update the red and green channel wrt  marking in alpha channel        
            self.image[:,:,0] = (np.maximum(self.image_loaded[:, :, 3],self.image_loaded[:, :, 0])).copy()
            self.image[:,:,1] = (np.maximum(self.image_loaded[:, :, 3],self.image_loaded[:, :, 1])).copy()
        if(self.color_dict[self.nodule_dict_index] == "Cyan"):
            #now update the green and blue channel wrt  marking in alpha channel        
            self.image[:,:,1] = (np.maximum(self.image_loaded[:, :, 3],self.image_loaded[:, :, 1])).copy()
            self.image[:,:,2] = (np.maximum(self.image_loaded[:, :, 3],self.image_loaded[:, :, 2])).copy()

    def load_annotated_frame(self):
        """
        The function will be called when it is already checked that the current frame index has already been marked.

        Returns
        -------
        None.

        """
        print("load frame called.")
        frame_filepath = PurePath(self.dicom_frames_path[self.nodule_dict_index]).joinpath(\
                                       "frame_"+str(self.frameIndex)+"_marked.dcm")            
        self.dicom_obj_loaded_annotated = pydicom.dcmread(frame_filepath)
        #the image currently has 4 channels, whereas under normal working of code, the image has only 3 channels. done.
        #Now, I extract only first channels from the loaded image as original image.        
        self.image_loaded = self.dicom_obj_loaded_annotated.pixel_array
        print("type of image_loaded in video loaded modified")
        print("type(image_loaded)="+str(type(self.image_loaded)))
        
        #Perform the conversion from rgba to rgb
        #Dry run, what will happen at save time or what will happen at clear markings. done
        #first load the image without alpha channel, as in normal case
        self.image = self.image_loaded[:,:,:3].copy()
        print("type of image in video loaded modified")
        print("type(image)="+str(type(self.image)))
        
        #save a copy of image as in normal case
        print("self.image.shape = "+str(self.image.shape))
        self.saved_image = self.image.copy()
        #In current case, the alpha need not be created, just loaded.
        #The loaded alpha may be rescaled if required.
        #Todo: chk consistency with further markings, c;learing image and recreating alpha. done in theory.
        self.image_alpha = self.image_loaded[:, :, 3].copy()
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

    def load_frame(self, image_name, nodule_dict_index):
        frame_dir_path = self.directory_loaded.get_frame_file_path(\
                image_name, nodule_dict_index)
        frame_file_name = "frame_"+str(0)+"_marked.npy"
        frame_filepath = PurePath(frame_dir_path).joinpath(frame_file_name)
        print("frame_filepath="+str(frame_filepath))
        nrow, ncol = self.nodule_dict[nodule_dict_index].get_alpha_shape(\
                image_name)
        alpha = self.read_compressed_matrix(frame_filepath, nrow, ncol)
        self.nodule_dict[nodule_dict_index].load_alpha(image_name, alpha)

    def save_frame(self, image_name, alpha_to_save):
        """
        image_name is the name ofthe image to be saved. thisshould be absoulte for image or video opened.
        for the case of directory chk the entry being written.
        This function will save the frame from a video.
        Returns
        -------
        None.

        """
        #separate dicom annotator object will thee for images and videos.
        if(self.directory_opened):
            #get fre path from directory object.
            #For the case of directory with images we have just one frame, hence, it seems useless to 
            #save the frame index. but for the case of sync with the earlier approach(videos), currently keeping that.
            #Later, before submitting I can change dir path and filename. 
            frame_dir_path = self.directory_loaded.get_frame_file_path(image_name, self.nodule_dict_index)
            frame_file_name = "frame_"+str(0)+"_marked.npy"
            frame_filepath = PurePath(frame_dir_path).joinpath(frame_file_name)
            print("frame_filepath="+str(frame_filepath))
            self.write_compressed_matrix(alpha_to_save, frame_filepath)
            new_arr = self.read_compressed_matrix(frame_filepath, alpha_to_save.shape[0], alpha_to_save.shape[1])
            self.chk_matrix_equality(alpha_to_save, new_arr)

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

    def save_yolo_coordinates(self, nodule_id, image_name):
        """
        This function will save the YOLO coordinates in a file.
        """
        yolo_coordinates = self.rectangle_coordinates
        # The YOLO coordinates are in the format of x1, y1, x2, y2
        # The YOLO coordinates are in the format of x, y, width, height
        # length = len(self.rectangle_coordinates)
        # coordinate_array = self.rectangle_coordinates[length - 1]
        x_min = self.tmp_rectangle_coordinates[0]
        y_min = self.tmp_rectangle_coordinates[1]
        x_max = self.tmp_rectangle_coordinates[2]
        y_max = self.tmp_rectangle_coordinates[3]

        # The YOLO coordinates are in the format of x_center, y_center, width, height


        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
        self.image_width = self.image.shape[1]  # Replace with actual image width
        self.image_height = self.image.shape[0]  # Replace with actual image height
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




        x_center = ((x_min + x_max) / 2) / self.image_width
        y_center = ((y_min + y_max) / 2) / self.image_height
        width = (x_max - x_min) / self.image_width
        height = (y_max - y_min) / self.image_height

        # Prepare the YOLO formatted data
        yolo_data = f"{nodule_id} {x_center} {y_center} {width} {height}\n"

        # Generate the file name from image_name
        file_name = f"{os.path.splitext(image_name)[0]}.txt"
        
        # Check if the file already exists
        # file_exists = os.path.exists(file_name)
        final_path= Path(PurePath(self.directory_loaded.directoryPath)).joinpath(file_name)
        file_exists = os.path.exists(final_path)
        if file_exists:
            # If file exists, open it and update/overwrite the line with the same class_id
            with open(final_path, 'r+') as file:
                lines = file.readlines()
                file.seek(0)  # Go back to the beginning of the file
                updated = False

                # Check if the line with the same class_id exists
                for idx, line in __builtins__.enumerate(lines):
                    parts = line.strip().split()
                    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!sparts[0] = ", parts)
                    if parts[0] == str(nodule_id):  # If the same class_id exists
                        lines[idx] = yolo_data  # Overwrite the existing line
                        updated = True
                        break

                if not updated:
                    # If no matching class_id is found, append the new data
                    lines.append(yolo_data)

                # Write the updated lines back to the file
                file.truncate(0)  # Clear the file before writing
                file.writelines(lines)
        else:
            # If file does not exist, create a new file and write the YOLO data
            with open(final_path, 'w') as file:
                file.write(yolo_data)


    def save_image(self):
        #Appropriate wrapper should be written for save.
        #New dicom object needs to created for saving individual frames that have been annotated.
        #there will be separate dicom annotator object for images and videos. 
        if(self.is_image_displayed() and self.directory_opened):
            (isSameImageDisplayed, numImagesDisplayed, image_name)\
                    = self.chkSameImageOpened("")
            if( numImagesDisplayed != 1 ):
                self.show_warning_num_images_displayed("save_image")        
                return
            if(self.current_nodule_shape=="Rectangle"):
                #I needto draw alpha rect
                #save the coordinates in main list.
                #save the coordinates in yolo format.
                #currently we have many nodules, therefore, main list needs to be created 
                #separately for each nodule. Therefore, currently donot update the main list. 
                #just have the temorary list list. we need those coordinates while drawing only.
                #main list we will discuss later.
                #Yolo coordinates does not seem to be plain x,y. ask ashish to do this.
                self.nodule_dict[self.nodule_dict_index].reinit_alpha(image_name)
                self.nodule_dict[self.nodule_dict_index].draw_rect(\
                        self.tmp_rectangle_coordinates, image_name)
                #fucion call to ave coordinates in a file in yolo format.
                self.save_yolo_coordinates(self.nodule_dict_index, image_name)
            image_alpha = self.nodule_dict[self.nodule_dict_index].get_alpha(image_name)
            if(self.image_scaled_bool):
                #rescaling is required
                alpha_to_save = self.image_alpha_scaled_up = cv2.resize(image_alpha,
                                                       (saved_image.shape[1],
                                                        saved_image.shape[0]),
                                                         interpolation=cv2.INTER_LINEAR)            
            else:
                alpha_to_save = image_alpha
                #rescaling is not required.
            #We donot need to reinitialize even after saving image because the user can add more nodules
            self.save_frame(image_name, alpha_to_save)
            self.set_nodule_marking_saved()
            self.set_graph.highlight_nodules_consistently()
            self.activateWindow()

    def plotLine_in_image_wrt_current_nodule(self, image_ref):
        """
        The line will be plotted wrt the current selected nodule
        image_ref is the reference of the image in which the plotting needs to be done.
        color_to_display must be picked wrt number displayed.
        """       
        color_index = self.index_in_nodule_dict_to_number_displayed[self.nodule_dict_index]
        color = self.color_dict[color_index]
        cv2.polylines(image_ref, [np.array(self.current_line)],\
                        isClosed=False, color=color, thickness=2)
        

    def draw_rectangle_on_image(self,draw_tmp, image_ref):
        """
        The line will be plotted wrt the current selected nodule
        image_ref is the reference of the image in which the plotting needs to be done.
        color_to_display must be picked wrt number displayed.
        """       
        color_index = self.index_in_nodule_dict_to_number_displayed[self.nodule_dict_index]
        color = self.color_dict[color_index]
        # print("***************************8!!!!!!!!!!!!!!!!!!!!!!!!!!1 :  in draw rectanle" ,)
        if(draw_tmp):
            my_thickness = 1
        else:
            my_thickness = 2
        #prev rectancgle drawn must be cleared   
        (isSameImageDisplayed, numImagesDisplayed,\
                        image_name_displayed) = self.chkSameImageOpened("")
        if(numImagesDisplayed != 1):
            self.show_error_num_images_displayed("draw rectangle")
        self.image = self.directory_loaded.loadedImages[image_name_displayed].image.copy()

        cv2.rectangle(self.image,\
                      (self.tmp_rectangle_coordinates[0],self.tmp_rectangle_coordinates[1]),\
                        (self.tmp_rectangle_coordinates[2], self.tmp_rectangle_coordinates[3]),\
                            color, thickness=my_thickness)
        
        self.reset_nodule_marking_saved()
        self.set_graph.highlight_nodules_consistently()
    

    def plotLines(self):
        if(0==len(self.current_line)):
            #nothing will be done if there are no points to plot
            return
        (isSameImageDisplayed, numImagesDisplayed, image_name) = self.chkSameImageOpened("")
        if(numImagesDisplayed != 1):
            self.show_warning_num_images_displayed("plot lines.")
        else:
            if(self.directory_opened):
                self.nodule_dict[self.nodule_dict_index].mark_polylines(self.current_line, image_name)
            #888888888888888888888888888888888888888888888888888888888888888888888888
            if(self.image_scaled_bool):
                image_ref = self.image_scaled_array
                # print("Hello scaling is print @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            else:
                image_ref = self.image
                # print("image referenece is !!!!!!!!!!!!!!!!!!!!!!!!!1 : ", image_ref)
            #Following also needs to be done wrt image scaled for that image(i.e.) when directory is loaded.
            #if(self.image_scaled_bool):
            #    if(self.directory_opened):
            #        image_ref = self.directory_loaded.loadedImages[image_name].image_scaled_array
            #    else:
            #        image_ref = self.image_scaled_array
            #else:
            #    if(self.directory_opened):
            #        image_ref = self.directory_loaded.loadedImages[image_name].image
            #    else:
            #        image_ref = self.image

            self.plotLine_in_image_wrt_current_nodule(image_ref)     

            if(self.image_scaled_bool):
                self.image = self.image_scaled_array
            self.reset_nodule_marking_saved()
            self.set_graph.highlight_nodules_consistently()
    
    def get_x_y_wrt_image(self, event, image_offset_x_wrt_global, image_offset_y_wrt_global):
        """
        This function will get the x and y coordinates wrt image.
        This will work even when the image is small than qlabel holding the image or the image was
        larger and got cropped.
        """
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
   
    def is_image_displayed(self): 
        if( self.image_opened or self.video_opened or \
                ( self.directory_opened and len(self.image_names_currently_displayed)>0 ) ):
            return True
        else:
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
        if(False == self.is_image_displayed()):
            #if the axial image has not been opened, we do not need to do anything
            #neither image is opened and nor the video is opened.
            #neither any image from directory is shown.
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
        #which pos should be used here must be rechecked before release and also before switching to pyqt6.
        print("global_pos.x() = "+str(global_pos.x()))
        print("self.image_offset_x_wrt_global = "+str(self.image_offset_x_wrt_global))
        print("self.image_width_for_display = "+str(self.image_width_for_display))
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
 
    def whether_mouse_over_set_image(self, event):
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
        if(False == self.directory_opened):
            #if directory has not been opened then this is false
            return False
        #8888888888888888888888888888888888888888888888888 have the check of showing annotation window
        #after completing nodule manager.
        #if(self.showing_annotation_window):
        #    #if annotation window is being shown then the mouse press would not work over set image.
        #    return False
        # Get the global mouse position
        global_pos = event.pos()
        #x_start and y_start of the set_image are required.
        #How the x_start and y_start of the big image were acquired?
        #the x_start and y_start of the big image were basically the position of image label inside the 
        #window and the offset of image inside that label.
        #How did it work correctly when the window in second screen was used to draw the marking.
        #was not the absoulte x position required?
        #How did we get the mouse location wrt image?
        #88888888888888888888888888888888above
        #For the set_image, we just need the position of image label inside the window. The reason is that 
        #currently the image occupies the complete label.
        
        #chk if the x and y of image surround the mouse
        if ((global_pos.x() >= self.set_image.x_start) and\
            (global_pos.x() <= self.set_image.x_end)):
            #The x is inside the image
            if ((global_pos.y() >= self.set_image.y_start) and\
                (global_pos.y() <= self.set_image.y_end)):
                #The y is also in the range.
                return True
            else:
                #The y is outside range.
                return False
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
        if(self.nodule_dict_index>-1):
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
                                      
    def handle_mousePress_dicom_image_what_to_do(self, event, x, y):
        """
        This function decides what to do with the mouse press over dicom image 
        based on whether single image isshown or multiple images are shown. 
        """
        (isSameImageDisplayed, numImagesDisplayed, image_name_displayed) =\
                self.chkSameImageOpened("")
        if(1 == numImagesDisplayed):
            if(self.current_nodule_shape == "Rectangle"):
                self.handle_mousePress_rectangle(event,x, y)
            else:
                self.current_line.append((x, y))
                self.update()
        elif(1 < numImagesDisplayed):
            #get box coordinates
            image_name = self.imagePaneManager.get_image_name_given_x_y(x, y)
            self.set_graph.special_highlight_image_boxes(image_name)

    def handle_mousePress_rectangle(self,event, x, y):
        """
        """
        print("handle_mousePress_rectangle")
        if( not self.first_rectangle_coordinate_flag):

                #here will go the code to sav ethe first coordinate
                        
                #self.rectangle_coordinates
                # self.rectangle_coordinates.append([x, y])

                self.tmp_rectangle_coordinates=[0,0,0,0]
                self.tmp_rectangle_coordinates[0]=x
                self.tmp_rectangle_coordinates[1]=y
                
                self.first_rectangle_coordinate_flag= True
                print("Saving first coordinates")
                print("self.rectangle_coordinates = "+str(self.rectangle_coordinates))
                print("self.tmp_rectangle_coordinates = "+str(self.tmp_rectangle_coordinates))
                print("self.first_rectangle_coordinate_flag="+str(self.first_rectangle_coordinate_flag))

                self.first_rectangle_coordinate_flag= False
                        
        #else:
        #        if(event.buttons()==QtCore.Qt.LeftButton):
        #            #here will go the code to save the second coordinate
        #                # x, y = self.get_x_y_wrt_image(event, self.image_offset_x_wrt_global, 
        #                #                                 self.image_offset_y_wrt_global)
        #                # self.chk_x_y_constraint(x, y, self.image_width_for_display,
        #                #                             self.image_height_for_display)
        #                # lenoflist = len(self.rectangle_coordinates)
        #                # # self.rectangle_coordinates[lenoflist-1].append(x)
        #                # # self.rectangle_coordinates[lenoflist-1].append(y)
        #                # self.tmp_rectangle_coordinates[2]=x
        #                # self.tmp_rectangle_coordinates[3]=y
        #                # #self.rectangle_coordinates[lenoflist-1].append([x, y])
        #                # # here will o the function to print the rectangle coordinates on the image
        #                print("self.tmp_rectangle_coordinates = "+str(self.tmp_rectangle_coordinates))
        #                
        #                self.draw_rectangle_on_image(False, self.image)
        #                self.first_rectangle_coordinate_flag= False
        #                self.tmp_rectangle_coordinates=[0,0,0,0]
        #                print("Saving Second coordinates")
        #                print("self.rectangle_coordinates = "+str(self.rectangle_coordinates))
        #                print("self.tmp_rectangle_coordinates = "+str(self.tmp_rectangle_coordinates))
        #                print("self.first_rectangle_coordinate_flag="+str(self.first_rectangle_coordinate_flag))
        #                # here will also come the code to draw the rectangle on the image
                        

    def handle_mousePress_dicom_image(self, event):
        """
        This function handles the mouse press event for the case when mouse is pressed over big image over 
        which marking is to be done.
        """
        print("handle_mousePress_dicom_image")
        self.update_mouse_action_variables(event, self.mouse_over_dicom_image, self.mouse_press)
        #self.clear_set_image_drag()
        print("self.nodule_dict_index = "+str(self.nodule_dict_index))
        if(self.nodule_dict_index>-1):
        #any marking will happen only if at least one nodule has been added.
            if(self.is_video_playing()):
                #write the code to pause the video.
                self.pause_video()
            else:                
                #do the processing i.e. line draw over image.
                if event.buttons() == QtCore.Qt.LeftButton:        
                    print("in mouse press checking button")
                    #The following offsets are computed again when displaying 
                    #a new image. hence there seems no cause to worry.
                    x, y = self.get_x_y_wrt_image(event, self.image_offset_x_wrt_global, 
                                                  self.image_offset_y_wrt_global)
                    self.chk_x_y_constraint(x, y, self.image_width_for_display,
                                            self.image_height_for_display)
                    #chk how many images shown.
                    self.handle_mousePress_dicom_image_what_to_do(event,x, y)
                elif event.buttons() == QtCore.Qt.RightButton:
                    #I need to perform the save operation now.
                    print("right click for save marking done.")
                    self.save_image()

    def handle_mousePress_set_image(self, event):
        print("handle_mousePress_set_image")
        print("event="+str(event))
        self.update_mouse_action_variables(event, self.mouse_over_set_image, self.mouse_press)
        if event.button() == Qt.RightButton:
            self.show_context_menu(event)
            self.clear_set_image_drag()
        elif event.button() == Qt.LeftButton:
            self.left_button_pressed_set_image(event)
            #888888888888888888888888 mouse release of left mouse button is required for drawing the edge from 
            #image to nodule.
        else:
            print("the middle button press not implemented yet.")
            self.clear_set_image_drag()
        event.accept()  # Optional: Prevent default behavior
        sys.stdout.flush()
 
    def mousePressEvent(self, event):
        #The event handling should take place if the event is within a label.
        #Also preallocate the label width and height.        
        # print("mouse press")
        #Now the ouse press event is for two things.
        #One, whether it is done over the image region.
        #The mouse press event over small image region will be looked at later.
        #The other event is when mouse presedd over the set image.
        #In this case, it is required to be lokked at that if currently the annotation window is being displayed,
        #then the mouse press or release etc will not be working.
        #Therefore, have a variable that tells that whether any annotation window is being shown.
        #There are too many places where show and hide of annotation window is called. Updating the variable at 
        #all of these places is error prone.
        #The point is that we have a nodule dict and other nodule variables. Hence adding one more independent 
        #nodule variable seems a task that we may need more such variables in future and in effect, 
        #if we had a nodule manager class then it will be much more easier to have such variables and also 
        #delete nodules.
        #888888888888888888888888888888888888888888888888888888
        #Now when more functionality is required like deleting nodules, then it becomes necessary to
        #have a nodule manager class.
        #First check that whether mouse press is working properly for set_image.
        #yes, the mouse press is working fine for set_image. 
        #The mouse press does not seem working properly.
        #sometimes it gets fired and sometimes, it does not get fired.
        #write the location of event and flush the output of print. 
        #now the mouse press is working fine. Earlier, I was using width and height of the 
        #image to compare. now, i am correctly using the end points to compare.
        #Now implement nodule manager.
        #There must be some connection between nodule manager and the graph class just like the directory and 
        #the graph class.
        #The nodule dict, num nodules etc will reside in the nodule manager class.
        #Therefore have two global variables seems sufficient. 
        #These variables will be axial_annotation_shown and sagital_annotation_shown.
        #Having global variables at the first sight seems not appropriate.
        print("in mouse press")
        print("x="+str(event.pos().x())+" y="+str(event.pos().y()))

        if(self.whether_mouse_over_image(event) ):
            #do further if the mouse press is inside the dicom(big - bigger than set image) image.
            self.handle_mousePress_dicom_image(event)
        #8888888888888888888888888888888888888888888888
        #hERE i NEED TO CHECK THAT Whether showing annotation window is true for any nodule.
        #For a mouse event doing such large checks is time consuming and accumulating such checks may result in 
        #delayed mouse event response.
        elif(self.whether_mouse_over_set_image(event)):
            #if(False == self.showing_annotation_window):
            self.handle_mousePress_set_image(event)
        else:
            #The press occurred somewhere else
            self.clear_set_image_drag()
        #self.showing_annotation_window this variable can be used to decide whether the mouse event in the range of 
        #set_image needs to be processed.
        #button_clicked has this variable.

    def handle_wheelEvent_dicom_image(self, event):
        # print("wheel event start")
        #The following checks that the video is not in playing mode.
        self.update_mouse_action_variables(event, self.mouse_over_dicom_image, self.mouse_wheel_moved)
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

    def handle_wheelEvent_set_image(self, event):
        self.update_mouse_action_variables(event, self.mouse_over_set_image, self.mouse_wheel_moved)

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
        self.clear_set_image_drag()
        if(self.whether_mouse_over_image(event) ):
            self.handle_wheelEvent_dicom_image(event)
        if(self.whether_mouse_over_set_image(event)):
            self.handle_wheelEvent_set_image(event)


    # main kaam yaha par hai 
    def handle_mouseMoveEvent_dicom_image(self, event):
        print("in mouse move event dicom")

        print(self.current_nodule_shape)
        self.update_mouse_action_variables(event, self.mouse_over_dicom_image, self.mouse_move)
        #self.clear_set_image_drag()
        if(self.nodule_dict_index>-1):
            if event.buttons() == QtCore.Qt.LeftButton:
                if(self.current_nodule_shape=="Rectangle"):
                    # print("!!!!!!!!!!!!!!!!!!!!in mouse move event rectangle")        
                    x, y = self.get_x_y_wrt_image(event, self.image_offset_x_wrt_global, 
                                                    self.image_offset_y_wrt_global)
                    self.chk_x_y_constraint(x, y, self.image_width_for_display,
                                                self.image_height_for_display)
                    
                    #self.rectangle_coordinates
                    self.tmp_rectangle_coordinates[2] = x
                    self.tmp_rectangle_coordinates[3] = y

                    #function to print temporary rectangular box
                    self.draw_rectangle_on_image(True, self.tmp_rectangle_coordinates)

                    print("Rectangle")
                elif (self.current_nodule_shape=="Ellipse"):
                    print("Ellipse")
                else:
                        
                            #any marking will happen only if at least one nodule has been added.
                            #(isSameImageDisplayed, numImagesDisplayed, image_name_displayed) =\
                            #        self.chkSameImageOpened("")
                            #if(1 == numImagesDisplayed):
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

    def draw_line_img_to_given_point(self, event):
        #The drawing will occur only if the image name is not null.       
        if("" == self.selected_image_name_by_left_press):
            if(self.set_image_drag_started):
                self.show_error("How drag started without selecting an image?")
            self.clear_set_image_drag()
            return
        image_name = self.selected_image_name_by_left_press
        if(self.set_image_drag_started):
            if("" == self.selected_image_name_by_left_press):
                self.show_error("drag started but no image selected. How?")
            #It may happen that in drag, we move out of the set image and then remain in drag state and 
            #come back to set image. In that case, the drag started will not be set and we will not be 
            #drawing a line.
            #self.show_error("set_image_drag_started must have been set when the mouse press occurred.")
            self.chk_image_name_is_loaded(image_name)
            #get the point wrt the set image. chk the drawing of boxes or setting their coordinates. done
            point_x = event.pos().x() - self.set_image.x_start
            point_y = event.pos().y() - self.set_image.y_start
            self.set_graph.draw_line_img_to_given_point(image_name, (point_x, point_y))
            self.partial_line_drawn = True
            #ask graph to draw line to required point.

    def handle_mouseMoveEvent_set_image(self, event):
        print("handle_mouseMoveEvent_set_image")
        self.update_mouse_action_variables(event, self.mouse_over_set_image, self.mouse_move)
        if event.buttons() == QtCore.Qt.LeftButton:
            #If the mouse move is occurring with the left button then it must be that earlier left button pressed
            #occurred. Hence, at this stage it does not seem necessary to keep track of previous different mouse 
            #action performed and the related variables. Though, when we will be keeping track of a different 
            #previous different mouse action, then we may assert that previous different mouse action must be 
            #left button press.
            #We may have a drag event for a line. 
            self.draw_line_img_to_given_point(event)
        else:
            self.clear_set_image_drag()

    def mouseMoveEvent(self, event):
        # print("mouseMoveEvent")
        if(self.whether_mouse_over_image(event) ):
            self.handle_mouseMoveEvent_dicom_image(event)
        elif(self.whether_mouse_over_set_image(event)):
            self.handle_mouseMoveEvent_set_image(event)
        else:
            #the move occurred some where else.
            self.clear_set_image_drag()

    def handle_mouseRelease_rectangle(self, event):
        print("in handle_mouseRelease_rectangle")
        x, y = self.get_x_y_wrt_image(event, self.image_offset_x_wrt_global,\
                self.image_offset_y_wrt_global)
        self.chk_x_y_constraint(x, y, self.image_width_for_display,\
                self.image_height_for_display)
        self.tmp_rectangle_coordinates[2]=x
        self.tmp_rectangle_coordinates[3]=y
        print("self.tmp_rectangle_coordinates = "+str(self.tmp_rectangle_coordinates))
        
        self.draw_rectangle_on_image(False, self.image)
        print("self.rectangle_coordinates = "+str(self.rectangle_coordinates))
        print("self.tmp_rectangle_coordinates = "+str(self.tmp_rectangle_coordinates))
        print("self.first_rectangle_coordinate_flag="+str(self.first_rectangle_coordinate_flag))

    def handle_mouseReleaseEvent_dicom_image(self, event):
        print("in handle_mouseReleaseEvent_dicom_image")
        self.update_mouse_action_variables(event, self.mouse_over_dicom_image, self.mouse_release)
        #self.clear_set_image_drag()
        if event.button() == QtCore.Qt.LeftButton:
            if(self.nodule_dict_index>-1):
                #any marking will happen only if at least one nodule has been added.
                #(isSameImageDisplayed, numImagesDisplayed, image_name_displayed) =\
                #        self.chkSameImageOpened("")
                #if(1 == numImagesDisplayed):
                if(self.current_nodule_shape == "Rectangle"):
                    self.handle_mouseRelease_rectangle(event)
                else:
                    if(self.whether_mouse_over_image(event) and not self.is_video_playing()):            
                        self.plotLines()
                        self.current_line = []
        self.set_graph.redraw_graph()

    def confirm_nodule_index_displayed_is_same(self, nodule_index_displayed_currently, \
            nodule_index_to_be_displayed):
        if(nodule_index_displayed_currently != nodule_index_to_be_displayed):
            msg = "the nodule displayed index must have mathed.\n"
            msg = msg + "nodule_index_displayed_currently = " +str(nodule_index_displayed_currently)
            msg = msg +"\nnodule_index_to_be_displayed = "+str(nodule_index_to_be_displayed)
            self.show_error(msg)

    def show_information_edge_exists(self, image_name, nodule_index):
        #This is the nodule_index(in nodule_dict) at which the mouse has been released.
        nodule_index_displayed = self.get_displayed_nodule_index(nodule_index)
        msg = "There already exists an edge from image "+str(image_name) +" to nodule "+ \
                str(nodule_index_displayed)+"."
        nodule_displayed_already = False
        if(self.nodule_dict_index == nodule_index):
            msg = msg + "\n\nThe same nodule is displayed currently."
            window_title = "Same nodule displayed"
            nodule_displayed_already = True
        else:
            #the nodule_dict_index needs to be updated for this case after display if appropriate msg.
            msg = msg + "\n\nNow the nodule "+str(nodule_index_displayed)+" will be displayed." 
            nodule_displayed_already = False
            if(self.nodule_dict_index != -1):
                #Whether any nodule displayed currently
                nodule_index_displayed_currently = self.get_displayed_nodule_index(self.nodule_dict_index)
                if(nodule_index_displayed_currently == nodule_index_displayed):
                    msg = msg + "\n\n The nodule "+str(nodule_index_displayed_currently)+\
                            " will be removed from display." 
            window_title = "Showing nodule "+str(nodule_index_displayed)
        msg = msg + "\n\nAny change in marking/annotation that you do now has to be saved explicitly." 
        msg = msg +"\n\nAlso, this change in annotation will get reflected to other images in which "
        msg = msg +"the same nodule has been marked."
        self.show_information(msg, window_title)
        return nodule_displayed_already

    def show_information_edge_exists_and_display_image(self, image_name, nodule_index):
        #This is the nodule_index(in nodule_dict) at which the mouse has been released.
        #we must get the index displayed.
        #whether the nodule is already displayed?
        nodule_displayed_already = self.show_information_edge_exists(image_name, nodule_index)
        if(not nodule_displayed_already):            
            #show_nodule_single_image calls perform_nodule_selected and updates self.nodule_dict_index. 
            #calling following function to show the nodule marking and also show the corresponding annotation 
            #window.  
            self.show_nodule_single_image(image_name, nodule_index)

    def get_channel_matrix_to_set(self, required_channel_val, channel_pos_matrix):
        """
        The channel_pos_matrix is expected to have 255 at place where it is required to have the 
        required_channel_val at that position.
        """
        matrix_to_apply =  required_channel_val * channel_pos_matrix
        print("maximum val in matrix to apply = "+str(np.max(matrix_to_apply)))
        return matrix_to_apply

    def get_r_g_b_arrays_for_alpha(self, nodule_index, alpha):
        #actually the following is the color that needs to BE DISPLAYED IN RED CHANNEL, I.E. FOR ALL THE PLACES
        #where 255 is present in the alpha channel, we have to place the following value in red channel try min.
        #The color from the color dict needs to be picked wrt the displayed index.
        nodule_index_displayed = self.get_displayed_nodule_index(nodule_index)
        r_val = self.color_dict[nodule_index_displayed][0]
        #broadcast r_val to alpha_shape and then take minimum of the broadcasted matrix and the alpha matrix.
        #The following function does that.
        #get alpha dict from nodule
        r_to_apply = self.get_channel_matrix_to_set(r_val, alpha)
        g_val = self.color_dict[nodule_index_displayed][1]
        g_to_apply = self.get_channel_matrix_to_set(g_val, alpha)
        b_val = self.color_dict[nodule_index_displayed][2]
        b_to_apply = self.get_channel_matrix_to_set(b_val, alpha)
        print(" (r_to_apply>0).any() ="+str((r_to_apply>0).any()))
        print(" (g_to_apply>0).any() ="+str((g_to_apply>0).any()))
        print(" (b_to_apply>0).any( ="+str((b_to_apply>0).any()))
        return (r_to_apply, g_to_apply, b_to_apply) 

    def add_to_channel_index(self, channel_index, channel_to_apply):
        #In some cases, at some pixels the image itself might have value greater than 127 but the channel has 
        #value 127. then taking the max will give the earlier value and not the required value. this must be corrected.
        #Also, when adding the color initially, the other channels were made zero or so. now that may be taken 
        #care of so that reloading retains the color used for marking.
        #We can get a mask of alpha channel as zero and non zero. that is already there.
        tmp = np.maximum(self.image[:,:,channel_index], channel_to_apply) 
        self.image[:,:,channel_index] = tmp

    def add_alpha_to_single_image_old(self, image_name, nodule_index):
        """#This is the index in nodule dict.
        We are currently showing the nodule over a single image. 
        """
        #And that is also an issue that in which color we need to add the alpha channel.
        #Here we add the computed matrixto the appropriate channel by max operation.
        alpha = self.nodule_dict[nodule_index].alpha_dict[image_name]
        (r_to_apply, g_to_apply, b_to_apply) = self.get_r_g_b_arrays_for_alpha(nodule_index, alpha)
        self.add_to_channel_index(0, r_to_apply)
        self.add_to_channel_index(1, g_to_apply)
        self.add_to_channel_index(2, b_to_apply)

    def get_masked_image_rgb(self, given_image, mask):
        """
        This function returns the masked image
        assuming that the mask is 1 dimensional. Hence conversion of mask to 3d is required and done here.
        we need 
        """
        #print(mask>1)
        if((mask>1).any()):
            self.show_error("mask is greater than 1")
        mask = mask*255
        mask_3channel = cv2.merge([mask] * 3)
        reqd_mask_3channel = mask_3channel.astype(given_image.dtype)
        print("given_image.shape="+str(given_image.shape))
        print("reqd_mask_3channel.shape="+str(reqd_mask_3channel.shape))
        print("given_image.dtype="+str(given_image.dtype))
        print("reqd_mask_3channel.dtype="+str(reqd_mask_3channel.dtype))
        masked_image = cv2.bitwise_and(given_image, reqd_mask_3channel)
        return masked_image

    def get_surroundings_image(self, orig_image, inverse_alpha):
        """
        This function returns an image where the surroundigs of the alpha is returned as it is from the original 
        image and the alpha region is returned as zero.
        """
        return self.get_masked_image_rgb(orig_image, inverse_alpha)

    def get_coloured_image_for_alpha(self, nodule_index, alpha):
        #get the broadcasted arrays for alpha
        (r_to_apply, g_to_apply, b_to_apply) = self.get_r_g_b_arrays_for_alpha(nodule_index, alpha)
        channels = [r_to_apply, g_to_apply, b_to_apply] 
        rgb_broadcasted = np.stack(channels, axis=-1)
        print("rgb_broadcasted.shape= " +str(rgb_broadcasted.shape))
        C = self.get_masked_image_rgb(rgb_broadcasted, alpha)
        return C

    def add_alpha_to_single_image(self, orig_image, image_name, nodule_index):
        """#This is the index in nodule dict.
        We are currently showing the nodule over a single image. 
        """
        alpha = self.nodule_dict[nodule_index].alpha_dict[image_name]
        inverse_alpha = 1 - alpha
        S = self.get_surroundings_image(orig_image, inverse_alpha)
        C = self.get_coloured_image_for_alpha(nodule_index, alpha)
        added_image = np.add(S,C)
        print("nodule_index = "+str(nodule_index))
        print("image_name=")
        print(image_name)
        #print("added_image = "+str(added_image))
        print("added_image.shape = "+str(added_image.shape))
        print("added_image.dtype = "+str(added_image.dtype))
        added_image_int = added_image.astype(np.uint8)
        return added_image_int

    def chk_nodule_index_correct(self, nodule_index):
        msg = "The nodule dict index must have been updated before calling the function to show the nodule. "
        if(self.nodule_dict_index != nodule_index):
            self.show_error(msg)

    def show_nodule_single_image(self, image_name, nodule_index):
        """#This is the index in nodule dict.
        We are currently showing the nodule over a single image. 
        """
        #888888888888888888888888 complete this.
        #If the image is already displayed then the displayed dimension must be same as used for marking. 
        #add the scalig to alpha if required.8888888888888888888888888888888888888888888888888888888
        #I think that for the initial display as well, the alpha scaling is not done.
        #Hence the alpha shape must match with the shape of the displayed image.
        #Also, we must hide the previously displayed nodule.
        #WheneVER AN IMAGE IS DIsPLAYED in showimageonly an copy of the image is made. We must follow the same 
        #method even here as well. 
        #Since we are showingthe nodule over a single image, we must clear the image first if any markings are 
        #present over the image. This function will also hide all annotation window.  
        #Is the ordering below correct? I think the perform nodule selected should be called after 
        #clear image markings so that the marking remains.  
        #The perform_nodule_selected handles only the display and hide of annotation window. The image and 
        #display of markings is not affected by this function. Hence, the order of perform_nodule_selected and
        #clear_image_markings is immaterial.
        self.perform_nodule_selected(nodule_index)
        self.chk_nodule_index_correct(nodule_index)
        self.clear_image_display()
        #self.show_image_functionality(image_name)
        #*88888888888888888888888888888888888888888888888888
        #instead of show image functionality, we need to just clear the markings over the image. Also, 
        #we donot need to perform any change to nodule thing over here. That has been handled by 
        #perform_nodule_selected.
        #The shape equivalence was required because the alpha must be added to the image displayed.
        #The following function does that.
        orig_image = self.directory_loaded.loadedImages[image_name].image.copy()
        self.image = self.add_alpha_to_single_image(orig_image, image_name, nodule_index)
        self.set_nodule_save()

    def add_img_nodule_connection_core(self, image_name, nodule_index):
        """
        This function is used by add_img_nodule_connection 
        and add_edges_nodule_graph_class
        """
        alpha_shape = (self.image_height_for_display, self.image_width_for_display)
        self.nodule_dict[nodule_index].add_image_connection(image_name, alpha_shape)
        self.set_graph.add_edge_img_nodule(image_name, nodule_index)

    def add_img_nodule_connection(self, image_name, nodule_index):
        self.perform_nodule_selected(nodule_index)
        #Also save the mapping image to nodule.
        self.add_img_nodule_connection_core(image_name, nodule_index)
        self.write_image_nodule_dict()
        #now mappings have been written. The directory can be created now.
        #The directory will be created for the nodule dict index and not for the number displayed.
        self.directory_loaded.create_dir(image_name, self.nodule_dict_index)
        self.reset_nodule_marking_saved()

    def ask_nodule_close(self, image_name, nodule_index):
        nodule_index_display_required = self.get_displayed_nodule_index(nodule_index)
        nodule_index_displayed_currently = self.get_displayed_nodule_index(self.nodule_dict_index)
        msg = "\nCurrently nodule "+str(nodule_index_displayed_currently)+" is being shown."
        msg = msg + "\n The current line drag will add an edge from image "+ image_name+" to nodule "
        msg = msg + str(nodule_index_display_required)+"."
        msg = msg + "\n\nDo you wish to close nodule "+str(nodule_index_displayed_currently)
        msg = msg + " \n and add edge from image "+image_name+" to nodule "+ \
                str(nodule_index_display_required)+"?"
        msg = msg + "\n\n If nodule "+str(nodule_index_displayed_currently)+" gets closed then its annotation"+\
                " window will be removed from display and the annotation window of nodule "+\
                str(nodule_index_display_required)+" will be shown."
        window_title = "Switch Nodule, add connection?"
        answer = self.show_question(msg, window_title)
        # Check which button was clicked
        if answer == QMessageBox.Yes:
            #only the image markings needs to be cleared.
            print("Yes button clicked")
            return True
        elif answer == QMessageBox.No:
            print("No button clicked")
            return False

    def perform_add_edge_requested_by_line_drag(self, image_name, nodule_index):
        #This function has been called when the edge between image and nodule passed does not exist.
        #Also, if a mouse left button gets released with partial line drawn then it must be that the image 
        #passed has been shown. Hence, it is not possible the nodule passed is shown already. if some nodule 
        #is shown already then it must be a different nodule for the shown image(i.e. passed image.)
        #The following condition has been added to check if a previously marked nodule has already been shown.
        if(-1!=self.nodule_dict_index):
            #Some nodule is shown already.
            #show information that we will be swithcing nodules to add connection from image img to nodule n.
            #do you wish to add the connection from img to n?
            #We also need to tell that the annotation window for already shown nodule(if annotation window is 
            #visible) will be closed.
            #The adding of img nodule connection itself closes any previous annotation window shown and 
            #displays the annotation window for the nodule to be added.
            #Actually, tHE CLosing of earlier annotation window and opening of newer annotation window and 
            #updation to nodule_dict_index is handled by add_img_nodule_connection.
            #WE JUST NEED TO ASK PERMISSION AND CLEAR THE IMAGE MARKINGS.
            #888888888888888888888888 test this.
            if(self.ask_nodule_close(image_name, nodule_index)):
                self.clear_image_display()
            else:
                #The user does not want to add the edge
                return
        #whether or not a prev nodule was shown, we need to add edge if not declined by user.
        self.add_img_nodule_connection(image_name, nodule_index)

    def mouse_left_button_released_at_nodule_with_partial_line_drawn(self, nodule_index):
        #The prev annotation window if shown, must be hidden.
        #If a nodule is already shown then it must be asked from the user that whether the user wants 
        #marking with the already shown nodule.
        #currently the mechanishm of adding nodules with prev nodules is not working. the user may also 
        #get confused with the annotation window show. Hence, we must do add nodule fresh where the 
        #annotation window already shown must be shown here. Also, some msg can be shown to user that 
        #adding connection to already added nodule. showing the annotation window for the already added 
        #nodule. Hence, no need to save annotation window now. But, if you perform changes to annotations 
        #then the annotation window must be saved and the annotations will apply equally well to other 
        #images in which this nodule has been marked.
        #Dragging the line to a nodule such that img-nodule connection already exists, then info must be 
        #shown that connection already exists and show info that earlir annotation window and marking is 
        #being shown. Also show the earlier annotation window and marking.
        #Changing of save to saved may also be done.
        #888888888888888888888888888888888888888888888888888888888888888
        image_name = self.selected_image_name_by_left_press
        self.reinit_boundary_shape()
        if self.set_graph.isEdgeExistsAlready(image_name, nodule_index):
            #show info 88888888888888888888888888888
            #I think this condition is complete now. This should be checked by running.
            self.show_information_edge_exists_and_display_image(image_name, nodule_index)
            #show earlier
        else:
            self.perform_add_edge_requested_by_line_drag(image_name, nodule_index)

    def handle_mouseReleaseEvent_set_image(self, event):
        #here we need to check if the release is for the right click. but the release event did not had a button
        #info
        #hence, prior to updating the mouse action variables, we can check the button info as well as the mouse 
        #action. That is the previous mouse action. 
        #It may happen that the drag started some where else and mouse release occurs in the set image. 
        #Hence, in that case the prev mouse button will be left only and prev mouse image will be set image only.
        #Hence, whether darg started and whether partial line drawn are the two things to check.
        self.update_mouse_action_variables(event, self.mouse_over_set_image, self.mouse_release)
        if(self.partial_line_drawn):
            #We need to take some action only if partial line is drawn. 
            if(not self.set_image_drag_started):
                self.show_error("self.partial_line_drawn can be true only if self.set_image_drag_started is true")
            #chk if the release is over some nodule box.
            print("event.globalPos()="+str(event.globalPos()))
            event_x_wrt_window = event.pos().x()
            event_y_wrt_window = event.pos().y()
            nodule_index = \
                    self.set_graph.get_nodule_index_in_dict_for_mouse(event_x_wrt_window, event_y_wrt_window)
            print("mouse released at nodule index = "+str(nodule_index))
            if(nodule_index!=-1):
                #We are calling a function that is based on mouse left button released, but during the recursive 
                #call, we have still not checked that whether actually the left button is released. based on the 
                #partial line drawn and set image drag started, we are inferring that the left button must have 
                #been released, because for the case of right button press, these variables must have been 
                #cleared. We cannot check which button has been released, because I could not find the mouse 
                #button information in the mouse release event.  
                self.mouse_left_button_released_at_nodule_with_partial_line_drawn(nodule_index)
        #In any case, the drag must be cleared whether or not prcocessing that drag.
        self.clear_set_image_drag()
            
    def mouseReleaseEvent(self, event):
        #If the line drag started in set image and line drag continues to outside this then the clear drag will 
        #be occurred because drag started in set image.
        #Also, if the drag accidentally to dicom image then the marking should not be done. 
        #Drag started can and should be implemented for dicom image as well.
        if(self.whether_mouse_over_image(event) ):
            self.handle_mouseReleaseEvent_dicom_image(event)
        elif(self.whether_mouse_over_set_image(event)):
            self.handle_mouseReleaseEvent_set_image(event)
        else:
            self.clear_set_image_drag()
        
    def event_beg(self, event):
        if event.type() == QtCore.QEvent.Paint:
            self.show_image()
        elif event.type() == 77:
            #print("at 77")
            a=1 #break        
            #QEvent::UpdateRequest	
        elif event.type() == 11:
            #QEvent::Leave
            a=1 #break
        elif event.type() == 25:
            #QEvent::WindowDeactivate	
            a=1 #break
        elif event.type() == 99:
            #QEvent::ActivationChange            
            a=1 #break
        #    24
        #    QEvent::WindowActivate
        #    110
        #    QEvent::ToolTip
        #    10
        #    QEvent::Enter	
        #    6
        #    QEvent::KeyPress
        #51
        #QEvent::ShortcutOverride
        #5
        #QEvent::MouseMove
        else:
            #print("type(event.type()) = "+str(type(event.type())))
            #print("event.type() = "+str(event.type()))
            #print("event = "+str(event))
            #print("(type(event)) = "+str(type(event)))
            #print("event.type().name() = "+event.type().name())
            if isinstance(event, QtCore.QEvent):
                ## Print the event type name
                #print("event is QtCore.QEvent")
                ##print("Event Type:", event.type().name())
                #print("Event Type:", event.type())
                num = event.type()
                #print("QEvent.registerEventType(num) = "+str(QEvent.registerEventType(num)))
                #event_type_name = QEvent.Type(num).name()
                event_type_value = QEvent.Type(num)
                ## Print the information
                ##print(f"Event Type: {event_type_name} (Value: {event_type_value})")
                #print(f"(Value: {event_type_value})")
            else:
                zzzzzzz = 0
                #print("event is not  QtCore.QEvent")
                #print("Non-Qt Event:", type(event))

            #print("(vars(event)) = "+str(vars(event)))
            #print("obj = "+str(obj))
            #print("(vars(obj)) = "+str(vars(obj)))

    #def event(self, event):
    #    print("event called")
    #    self.event_beg(event)
    #    return False

    def eventFilter(self, obj, event):
        #https://doc.qt.io/qt-5/qevent.html
        #print("eventFilter called")
        self.event_beg(event)
        return False

    def list_all_events(self): 
        for i in range(QEvent.Type.registerEventType(0)):
            # Get the event type name and value
            event_type_name = QEvent.Type(i).name()
            event_type_value = QEvent.Type(i)

            # Print the information
            print(f"Event Type: {event_type_name} (Value: {event_type_value})")

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
    
    ##time.sleep(10)
    #if(len(available_screen_list)>1):
    #    screen_1 = available_screen_list[1] #app.screens()[1] 
    #    print('Screen: %s' % screen_1.name())
    #    size_1 = screen_1.size()
    #    print('Size_1: %d x %d' % (size_1.width(), size_1.height()))
    #    rect_1 = screen_1.availableGeometry()
    #    print("available_geometry_1 = "+str(rect_1))
    #    global screen_1_availableWidth, screen_1_availableHeight
    #    screen_1_availableWidth = rect_1.width()
    #    screen_1_availableHeight = rect_1.height()
    #    print('Available_1: %d x %d' % (screen_1_availableWidth, screen_1_availableHeight))
    #    screen_1_top = rect_1.top()
    #    screen_1_left = rect_1.left()
    #    print("screen_1_top = "+str(screen_1_top))
    #    print("screen_1_left = "+str(screen_1_left))
    #    
    #    window_x_sagital = screen_1_left + screen_margin_left
    #    window_y_sagital = screen_1_top + screen_margin_top
    #    window_width_sagital = screen_1_availableWidth - (screen_margin_left+screen_margin_right)
    #    window_height_sagital = screen_1_availableHeight - (screen_margin_top+screen_margin_bottom)
    #    print("window_width_sagital = "+str(window_width_sagital))
    #    print("window_height_sagital = "+str(window_height_sagital))
    #else:
    #    window_x_sagital = screen_0_left + screen_margin_left
    #    window_y_sagital = screen_0_top + screen_margin_top
    #    window_width_sagital = screen_0_availableWidth - (screen_margin_left+screen_margin_right)
    #    window_height_sagital = screen_0_availableHeight - (screen_margin_top+screen_margin_bottom)
    #    print("window_width_sagital = "+str(window_width_sagital))
    #    print("window_height_sagital = "+str(window_height_sagital))
    #
    #window_sagital = DicomAnnotator(window_x_sagital, window_y_sagital, window_width_sagital,\
    #                              window_height_sagital, "Sagital",\
    #                                  csv_filename_video, csv_file_handle_video,\
    #                                    csv_filename_video_marked_frames, csv_file_handle_video_marked_frames)
    #window_sagital.setWindowFlags(Qt.FramelessWindowHint)  # Set the flag for a frameless window
    #window_sagital.setGeometry(window_x_sagital, window_y_sagital, window_width_sagital,\
    #                            window_height_sagital)    
    #window_sagital.show()
    #Todo: update this variable whenever a nodule gets selected.
    #Also, in the annotation window, have a variable that specifies the current window index.
    #Whenever an update to this variable is done, an action must be fired in the dicom annotator window which 
    #does all the changes when add nodule is done. Therefore, leave this at the moment. Currently add nodule 
    #is the only thing that changes the nodule.
    #Actually, this is required to be updated from the nodule class because the nodule class has actions.
    #The class ref in the nodule class may be used to call the function that updates all the variables in the main class 
    #including the color etc that correspond to updating a nodule.
    #But still,this task will be done at last.
    global nodule_index_for_marking
    nodule_index_for_marking = -1
    #global global_thread_and_window_collector
    #global_thread_and_window_collector = Global_thread_and_window_collector()
    #global global_hide
    #global_hide =  Global_hide()
    #global_hide.start_regular_chk_windows()
    sys.exit(app.exec_())
