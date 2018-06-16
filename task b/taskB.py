from psychopy import visual, event, core, os
import random
import glob, util



# Initialization #
directory = os.getcwd()
imageList = util.imageSorter('fgdf task a results.csv')
timer = core.Clock()
win = visual.Window(fullscr=True, units='pix', monitor='testMonitor',
        color = [-.9,-.9,-.9])
mouse = event.Mouse()
d = 20;

## Trials. 45 presenting high pref images, and 45 presenting low pref images.
## 1 = high pref, 2 = low pref, trial order is randomized.
highPrefTrials = [1] * 45
lowPrefTrials = [2] * 45
trials = highPrefTrials + lowPrefTrials
random.shuffle(trials)

choice1Responses = '' * len(trials)
choice1ReactionTimes = '' * len(trials)
choice2Responses = '' * len(trials)
choice2ReactionTimes = '' * len(trials)
postChoiceResponses = '' * len(trials)
postChoiceReactionTimes = '' * len(trials)

## Textboxes
option1Money=visual.TextBox(window=win,
                         text='$',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=(-(d/2 + 156/2),0),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option1Items=visual.TextBox(window=win,
                         text='2',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=((d/2 + 156/2),0),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )

# Target Boxes #
## First choice
option1MoneyShape = visual.ShapeStim(win, fillColor=[1,1,1],
    vertices=[(-(d/2 + 156), -156/2), (-(d/2 + 156), 156/2), (-d/2, 156/2), (-d/2, -156/2)], opacity = 0)
option1ItemsShape = visual.ShapeStim(win, fillColor=[1,1,1],
    vertices=[((d/2 + 156), -156/2), ((d/2 + 156), 156/2), (d/2, 156/2), (d/2, -156/2)], opacity = 0)
## Second choice
option1MoneyShape = visual.ShapeStim(win, fillColor=[1,1,1],
    vertices=[((-(d/2 + 156+d+156), d+156/2), ((-(d/2 + 156+d+156), d+156/2+156), (-(d/2 + 156+d), d+156/2+156), (-(d/2 + 156+d), d+156/2)], opacity = 0)
option2MoneyShape = visual.ShapeStim(win, fillColor=[1,1,1],
    vertices=[((-(d/2 + 156), d+156/2), ((-(d/2 + 156), d+156/2+156), (-(d/2), d+156/2+156), (-(d/2), d+156/2)], opacity = 0)
option2MoneyShape = visual.ShapeStim(win, fillColor=[1,1,1],
    vertices=[((-(d/2 + 156), d+156/2), ((-(d/2 + 156), d+156/2+156), (-(d/2), d+156/2+156), (-(d/2), d+156/2)], opacity = 0)

## Coordinates for ImageStims, origin = (0,0)
xInner = (d/2 + 160/2)
xOuter = (d/2 + 160 + d + 160/2)
y = (160/2 + d + 160/2)

# ImageStim - initialized with placeholder images
## Top - left to right
option2Item1 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[-(xOuter), (y)], size = [156,156])
option2Item2 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[-(xInner), (y)], size = [156,156])
option2Item3 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[(xInner), (y)], size = [156,156])
option2Item4 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[(xOuter), (y)], size = [156,156])
## Middle
option2Item5 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[-(xOuter), 0], size = [156,156])
option2Item6 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[-(xInner), 0], size = [156,156])
option2Item7 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[(xInner), 0], size = [156,156])
option2Item8 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[(xOuter), 0], size = [156,156])
## Bottom
option2Item9 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[-(xOuter), -(y)], size = [156,156])
option2Item10 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[-(xInner), -(y)], size = [156,156])
option2Item11 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[(xInner), -(y)], size = [156,156])
option2Item12 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[(xOuter), -(y)], size = [156,156])
## Subejct's selected image
postChoiceItem = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[0,0], size = [156,156])


option2Item1Border = visual.ShapeStim(win, fillColor=[1,1,1],
    vertices=[((d/2 + 156), -156/2), ((d/2 + 156), 156/2), (d/2, 156/2), (d/2, -156/2)], opacity = 0)

# Choice 1 Loop
timer.reset()
while timer.getTime() < 4:
    print (timer.getTime())
    ## Monetary Option Chosen
    if mouse.isPressedIn(option1MoneyShape):
        rt1 = timer.getTime()
        option1Money.setBorderColor('red')
        option1Money.draw()
        option1Items.draw()
        win.flip()
        core.wait(1)
        resp1 = option1Money.getDisplayedText()
        print('money')
        print(rt1)
        break
    ## Choice option Chosen
    elif mouse.isPressedIn(option1ItemsShape):
        rt1 = timer.getTime()
        option1Items.setBorderColor('red')
        option1Items.draw()
        option1Money.draw()
        win.flip()
        core.wait(1)
        resp1 = option1Items.getDisplayedText()
        print('items')
        print(rt1)
        break
    option1Money.draw()
    option1MoneyShape.draw()
    option1Items.draw()
    option1ItemsShape.draw()
    win.flip()

# Exit current trial and begin new one if did not answer in time
if resp1 == '':
    resp1 = 'None'
    rt1 = 'None'
    resp2 = 'None'
    rt2 = 'None'
    try_faster_screen = visual.TextStim(win, text='Please make a faster decision next round!')
    ## Show 'try faster' screen
    event.clearEvents()
    try_faster_screen.draw()
    win.flip()
    core.wait(3)

# Delay 1. Select 5 or 6 second delay
while timer.getTime() < 6:
    #print(timer.getTime())
    win.flip()

# Setup random images to be used based on amount unique images to be shown
imageType = random.randint(0, 1)
numberUniquePics = int(option1Items.getDisplayedText())
timesImageRepeated = 12 / numberUniquePics

if trials[0] == 1: # Check if want high preference images
    uniquePics = random.sample(imageList[imageType], numberUniquePics)
else: # Select low preference images
    uniquePics = random.sample(imageList[imageType + 2], numberUniquePics)

trialPics = uniquePics * timesImageRepeated
random.shuffle(trialPics)

option2Item1.setImage(trialPics[0])
option2Item2.setImage(trialPics[1])
option2Item3.setImage(trialPics[2])
option2Item4.setImage(trialPics[3])
option2Item5.setImage(trialPics[4])
option2Item6.setImage(trialPics[5])
option2Item7.setImage(trialPics[6])
option2Item8.setImage(trialPics[7])
option2Item9.setImage(trialPics[8])
option2Item10.setImage(trialPics[9])
option2Item11.setImage(trialPics[10])
option2Item12.setImage(trialPics[11])

# Choice 2
if resp1 == option1Money.getDisplayedText():
    timer.reset()
    #while timer.getTime() < 5:
    print(option1Money.getDisplayedText())
elif resp1 == option1Items.getDisplayedText(): # use int("String") to use the number of items as int
    timer.reset()
    while timer.getTime() < 5:
        ## item1 Chosen
        if mouse.isPressedIn(option2Item1):
            choice2ReactionTimes = timer.getTime() ## record reaction time
            option2Item1Shape.setBorderColor('red')
            option2Item1.draw()
            option2Item2.draw()
            option2Item3.draw()
            option2Item4.draw()
            option2Item5.draw()
            option2Item6.draw()
            option2Item7.draw()
            option2Item8.draw()
            option2Item9.draw()
            option2Item10.draw()
            option2Item11.draw()
            option2Item12.draw()
            win.flip()
            core.wait(1)
            choice2Responses = trialPics[0]
            print(trialPics[0])
            print(rt2)
            break
        elif mouse.isPressedIn(option2Item2):
            choice2ReactionTimes = timer.getTime() ## record reaction time
            option2Item2Shape.setBorderColor('red')
            option2Item1.draw()
            option2Item2.draw()
            option2Item3.draw()
            option2Item4.draw()
            option2Item5.draw()
            option2Item6.draw()
            option2Item7.draw()
            option2Item8.draw()
            option2Item9.draw()
            option2Item10.draw()
            option2Item11.draw()
            option2Item12.draw()
            win.flip()
            core.wait(1)
            choice2Responses = trialPics[1]
            print(trialPics[1])
            print(rt2)
            break
        elif mouse.isPressedIn(option2Item3):
            choice2ReactionTimes = timer.getTime() ## record reaction time
            option2Item3Shape.setBorderColor('red')
            option2Item1.draw()
            option2Item2.draw()
            option2Item3.draw()
            option2Item4.draw()
            option2Item5.draw()
            option2Item6.draw()
            option2Item7.draw()
            option2Item8.draw()
            option2Item9.draw()
            option2Item10.draw()
            option2Item11.draw()
            option2Item12.draw()
            win.flip()
            core.wait(1)
            choice2Responses = trialPics[2]
            print(trialPics[2])
            print(rt2)
            break
        elif mouse.isPressedIn(option2Item4):
            choice2ReactionTimes = timer.getTime() ## record reaction time
            option2Item4Shape.setBorderColor('red')
            option2Item1.draw()
            option2Item2.draw()
            option2Item3.draw()
            option2Item4.draw()
            option2Item5.draw()
            option2Item6.draw()
            option2Item7.draw()
            option2Item8.draw()
            option2Item9.draw()
            option2Item10.draw()
            option2Item11.draw()
            option2Item12.draw()
            win.flip()
            core.wait(1)
            choice2Responses = trialPics[3]
            print(trialPics[3])
            print(rt2)
            break
        elif mouse.isPressedIn(option2Item5):
            choice2ReactionTimes = timer.getTime() ## record reaction time
            option2Item5Shape.setBorderColor('red')
            option2Item1.draw()
            option2Item2.draw()
            option2Item3.draw()
            option2Item4.draw()
            option2Item5.draw()
            option2Item6.draw()
            option2Item7.draw()
            option2Item8.draw()
            option2Item9.draw()
            option2Item10.draw()
            option2Item11.draw()
            option2Item12.draw()
            win.flip()
            core.wait(1)
            choice2Responses = trialPics[4]
            print(trialPics[4])
            print(rt2)
            break
        elif mouse.isPressedIn(option2Item6):
            choice2ReactionTimes = timer.getTime() ## record reaction time
            option2Item6Shape.setBorderColor('red')
            option2Item1.draw()
            option2Item2.draw()
            option2Item3.draw()
            option2Item4.draw()
            option2Item5.draw()
            option2Item6.draw()
            option2Item7.draw()
            option2Item8.draw()
            option2Item9.draw()
            option2Item10.draw()
            option2Item11.draw()
            option2Item12.draw()
            win.flip()
            core.wait(1)
            choice2Responses = trialPics[5]
            print(trialPics[5])
            print(rt2)
            break
        elif mouse.isPressedIn(option2Item7):
            rt2 = timer.getTime() ## record reaction time
            option2Item7Shape.setBorderColor('red')
            option2Item1.draw()
            option2Item2.draw()
            option2Item3.draw()
            option2Item4.draw()
            option2Item5.draw()
            option2Item6.draw()
            option2Item7.draw()
            option2Item8.draw()
            option2Item9.draw()
            option2Item10.draw()
            option2Item11.draw()
            option2Item12.draw()
            win.flip()
            core.wait(1)
            resp2 = trialPics[6]
            print(trialPics[6])
            print(rt2)
            break
        elif mouse.isPressedIn(option2Item8):
            rt2 = timer.getTime() ## record reaction time
            option2Item8Shape.setBorderColor('red')
            option2Item1.draw()
            option2Item2.draw()
            option2Item3.draw()
            option2Item4.draw()
            option2Item5.draw()
            option2Item6.draw()
            option2Item7.draw()
            option2Item8.draw()
            option2Item9.draw()
            option2Item10.draw()
            option2Item11.draw()
            option2Item12.draw()
            win.flip()
            core.wait(1)
            resp2 = trialPics[7]
            print(trialPics[7])
            print(rt2)
            break
        elif mouse.isPressedIn(option2Item9):
            rt2 = timer.getTime() ## record reaction time
            option2Item9Shape.setBorderColor('red')
            option2Item1.draw()
            option2Item2.draw()
            option2Item3.draw()
            option2Item4.draw()
            option2Item5.draw()
            option2Item6.draw()
            option2Item7.draw()
            option2Item8.draw()
            option2Item9.draw()
            option2Item10.draw()
            option2Item11.draw()
            option2Item12.draw()
            win.flip()
            core.wait(1)
            resp2 = trialPics[8]
            print(trialPics[8])
            print(rt2)
            break
        elif mouse.isPressedIn(option2Item10):
            rt2 = timer.getTime() ## record reaction time
            option2Item10Shape.setBorderColor('red')
            option2Item1.draw()
            option2Item2.draw()
            option2Item3.draw()
            option2Item4.draw()
            option2Item5.draw()
            option2Item6.draw()
            option2Item7.draw()
            option2Item8.draw()
            option2Item9.draw()
            option2Item10.draw()
            option2Item11.draw()
            option2Item12.draw()
            win.flip()
            core.wait(1)
            resp2 = trialPics[9]
            print(trialPics[9])
            print(rt2)
            break
        elif mouse.isPressedIn(option2Item11):
            rt2 = timer.getTime() ## record reaction time
            option2Item11Shape.setBorderColor('red')
            option2Item1.draw()
            option2Item2.draw()
            option2Item3.draw()
            option2Item4.draw()
            option2Item5.draw()
            option2Item6.draw()
            option2Item7.draw()
            option2Item8.draw()
            option2Item9.draw()
            option2Item10.draw()
            option2Item11.draw()
            option2Item12.draw()
            win.flip()
            core.wait(1)
            resp2 = trialPics[10]
            print(trialPics[10])
            print(rt2)
            break
        elif mouse.isPressedIn(option2Item12):
            rt2 = timer.getTime() ## record reaction time
            option2Item12Shape.setBorderColor('red')
            option2Item1.draw()
            option2Item2.draw()
            option2Item3.draw()
            option2Item4.draw()
            option2Item5.draw()
            option2Item6.draw()
            option2Item7.draw()
            option2Item8.draw()
            option2Item9.draw()
            option2Item10.draw()
            option2Item11.draw()
            option2Item12.draw()
            win.flip()
            core.wait(1)
            resp2 = trialPics[11]
            print(trialPics[11])
            print(rt2)
            break
        #draw boxes behind
        option2Item1.draw()
        option2Item2.draw()
        option2Item3.draw()
        option2Item4.draw()
        option2Item5.draw()
        option2Item6.draw()
        option2Item7.draw()
        option2Item8.draw()
        option2Item9.draw()
        option2Item10.draw()
        option2Item11.draw()
        option2Item12.draw()
        win.flip()
    print(resp2)

# Exit current trial and begin new one if did not answer in time
if resp2 == '':
    resp2 = 'None'
    rt2 = 'None'
    resp2 = 'None'
    rt2 = 'None'
    try_faster_screen = visual.TextStim(win, text='Please make a faster decision next round!')
    ## Show 'try faster' screen
    event.clearEvents()
    try_faster_screen.draw()
    win.flip()
    core.wait(3)

# Delay 2. Select 2 or 3 second delay
while timer.getTime() < 3:
    #print(timer.getTime())
    win.flip()

while timer.getTime() < 2:
    postChoiceItem.setImage(resp2)
    win.flip()

# Display rating scale and store result as resp3.
# Put this in a for trial in trials loop.


win.close()
core.quit()
