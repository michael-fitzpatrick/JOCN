from psychopy import visual, core, event, gui, data, sound, logging
import sys
import os
import glob
import csv
import datetime
import random

# Path to working directory
directory = os.getcwd()

# Get subjID
subjDlg=gui.Dlg(title="JOCN paper- rate items")
subjDlg.addField('Enter Subject ID: ')
subjDlg.show()
subj_id=subjDlg.data[0]

if len(subj_id)<1: # Make sure participant entered name
    core.quit()

# Initialzing Window, insruction, and thank you screens
win = visual.Window(fullscr=True, size=[1100, 800], units='pix', monitor='testMonitor')
instruction_screen = visual.TextStim(win, text="""Rate how much you prefer the items by clicking on the rating line.
                                     \nPress \'Enter\' or click the button below the line to move on to the next item.
                                     \nThe rating is from: \n  1 (little to no preference)\n  to 7 (very high preference). 
                                      \n Press any key to start""")
thank_you_screen = visual.TextStim(win, text="""Thank you for choosing!""")

# Show instruction screen
event.clearEvents()
instruction_screen.draw()
win.flip()

# Lets participant quit at any time by pressing escape button
if 'escape' in event.waitKeys():
    core.quit()



# Initialize image list
imageList = [os.path.join(directory, image) for image in 
                 glob.glob('images/*.jpg')]
# Randomize order of images
random.shuffle(imageList)

# Initializing response list same size as imageList
responses = [""] * len(imageList)

# Initializing rating scale
myRatingScale = visual.RatingScale(win, choices=['1', '2', '3', '4', '5', '6', '7'])

# Main Loop
for image in imageList:
    x, y = myRatingScale.win.size 
    # The size parameter rescales images.
    # Stretch can be mitigated by cropping images to a resolution that would scale to the specified one bellow.
    myItem = visual.ImageStim(win=win, image=image, units='pix', pos=[0, y//7], size = [500,450])
    myRatingScale.reset()  # reset between repeated uses of the same scale
    event.clearEvents()
    while myRatingScale.noResponse:
        myItem.draw()
        myRatingScale.draw()
        win.flip()
        if event.getKeys(['escape']): 
            core.quit()
    # assigns response to corresponding image
    responses[imageList.index(image)] = myRatingScale.getRating() 

    # clear the screen & pause between ratings
    win.flip()
    core.wait(0.35)  # brief pause, slightly smoother for the subject

# Write to .csv file with participants name, subj_id, in file name
f=open( subj_id + ' task a results.csv','w')
for i in range(0,len(imageList)):
    f.write(imageList[i]+","+responses[i]+"\n")
f.close()

# Thank participant
thank_you_screen.draw()
win.flip()
core.wait(1.5)