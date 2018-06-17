from psychopy import visual, event, core, os
import random
import glob, util

# Initialization # taskB(subj_id, confed_id,
subj_id = 't5'
confed_id = 'Bob'
directory = os.getcwd()
imageList = util.imageSorter('Matt2 task a results.csv')
timer = core.Clock()
win = visual.Window(fullscr=True, units='pix', monitor='testMonitor',
        color = [-.9,-.9,-.9])
mouse = event.Mouse()
d = 20;

## Trials. 45 presenting high pref images, and 45 presenting low pref images.
## 1 = high pref, 2 = low pref, trial order is randomized.
itemChoiceAmounts = [2,3,4,6,12]
monetaryChoiceAmounts = [0.50, 0.75, 1.00, 1.25, 1.50]
highPrefTrials = [1] * 45
lowPrefTrials = [2] * 45
trials = highPrefTrials + lowPrefTrials
random.shuffle(trials)

# Lists holding responses and reaction times for each trial
monetaryOptions = [''] * len(trials)
itemNumberOptions = [''] * len(trials)
choice1Responses = [''] * len(trials)
choice1ReactionTimes = [''] * len(trials)
choice2Responses = [''] * len(trials)
choice2ReactionTimes = [''] * len(trials)
postChoiceResponses = [''] * len(trials)
postChoiceReactionTimes = [''] * len(trials)
trialImages = [''] * len(trials)

# Rating Scale
satisfactionScale = visual.RatingScale(win, name='satisfaction',
        choices=['1', '2', '3', '4', '5', '6', '7'], pos=[0,0])

monetaryAmount = 0
choiceAmount = 0
## Textboxes
option1Money=visual.TextBox(window=win,
                         text=' ',
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
                         text=' ',
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

# Target Boxes 
##  Overlaying these on the textbox stim because visual textboxs do not
##  have the .isPressedIn() method.

## First choice
option1MoneyShape = visual.ShapeStim(win, fillColor=[1,1,1], 
    vertices=[(-(d/2 + 156), -156/2), (-(d/2 + 156), 156/2), (-d/2, 156/2), (-d/2, -156/2)], opacity = 0)
option1ItemsShape = visual.ShapeStim(win, fillColor=[1,1,1],
    vertices=[((d/2 + 156), -156/2), ((d/2 + 156), 156/2), (d/2, 156/2), (d/2, -156/2)], opacity = 0)

## Second choice
## Top - left to right
option2Pos1Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb', 
    vertices=[(-(d/2 + 160+d+160), d+160/2), (-(d/2 + 160+d+160), d+160/2+160), (-(d/2 + 160+d), d+160/2+160), (-(d/2 + 160+d), d+160/2)])
option2Pos2Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb', 
    vertices=[(-(d/2 + 160), d+160/2), (-(d/2 + 160), d+160/2+160), (-(d/2), d+160/2+160), (-(d/2), d+160/2)])
option2Pos3Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb', 
    vertices=[((d/2), d+160/2), ((d/2), d+160/2+160), ((d/2 + 160), d+160/2+160), ((d/2 + 160), d+160/2)])
option2Pos4Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb', 
    vertices=[((d/2 + 160+d), d+160/2), ((d/2 + 160+d), d+160/2+160), ((d/2 + 160+d+160), d+160/2+160), ((d/2 + 160+d+160), d+160/2)])
## Middle
option2Pos5Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb', 
    vertices=[(-(d/2 + 160+d+160), -160/2), (-(d/2 + 160+d+160), 160/2), (-(d/2 + 160+d), 160/2), (-(d/2 + 160+d), -160/2)])
option2Pos6Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb', 
    vertices=[(-(d/2 + 160), -160/2), (-(d/2 + 160), 160/2), (-(d/2), 160/2), (-(d/2), -160/2)])
option2Pos7Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb', 
    vertices=[((d/2), -160/2), ((d/2), 160/2), ((d/2 + 160), 160/2), ((d/2 + 160), -160/2)])
option2Pos8Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb', 
    vertices=[((d/2 + 160+d), -160/2), ((d/2 + 160+d), 160/2), ((d/2 + 160+d+160), 160/2), ((d/2 + 160+d+160), -160/2)])
## Bottom
option2Pos9Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb', 
    vertices=[(-(d/2 + 160+d+160), -(d+160/2+160)), (-(d/2 + 160+d+160), -(d+160/2)), (-(d/2 + 160+d), -(d+160/2)), (-(d/2 + 160+d), -(d + 160/2 + 160))])
option2Pos10Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb', 
    vertices=[(-(d/2 + 160), -(d+160/2+160)), ((-(d/2 + 160)), -(d+160/2)), (-(d/2), -(d+160/2)), (-(d/2), -(d+160/2+160))])
option2Pos11Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb', 
    vertices=[((d/2), -(d+160/2+160)), ((d/2), -(d+160/2)), ((d/2 + 160), -(d+160/2)), ((d/2 + 160), -(d+160/2+160))])
option2Pos12Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb', 
    vertices=[((d/2 + 160+d), -(d+160/2+160)), ((d/2 + 160+d), -(d+160/2)), ((d/2 + 160+d+160), -(d+160/2)), ((d/2 + 160+d+160), -(d+160/2+160))])

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

option2Money1=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=(-(xOuter), (y)),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money2=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=(-(xInner), (y)),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money3=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=((xInner), (y)),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money4=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=((xOuter), (y)),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money5=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=(-(xOuter), 0),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money6=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=(-(xInner), 0),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money7=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=((xInner), 0),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money8=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=((xOuter), 0),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money9=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=(-(xOuter), -(y)),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money10=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=(-(xInner), -(y)),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money11=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=((xInner), -(y)),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money12=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=((xOuter), -(y)),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )

for i in range(1):
    if event.getKeys(['escape']):
                core.quit()
    # Set option offered in trial randomly from lists
    monetaryAmount = monetaryChoiceAmounts[random.randint(0, len(monetaryChoiceAmounts) - 1)]
    choiceAmount = itemChoiceAmounts[random.randint(0, len(itemChoiceAmounts) - 1)]
    option1Money.setText('$' + str(monetaryAmount))
    option1Items.setText(str(choiceAmount))
    monetaryOptions[i] = monetaryAmount
    itemNumberOptions[i] = choiceAmount
    # Choice 1 Loop
    timer.reset()
    while timer.getTime() < 4:
        print (timer.getTime())
        ## Monetary Option Chosen
        if mouse.isPressedIn(option1MoneyShape):
            choice1ReactionTimes[i] = timer.getTime()
            option1Money.setBorderColor('red')
            option1Money.draw()
            option1Items.draw()
            win.flip()
            core.wait(1)
            choice1Responses[i] = monetaryAmount
            break
        ## Choice option Chosen
        elif mouse.isPressedIn(option1ItemsShape):
            choice1ReactionTimes[i] = timer.getTime()
            option1Items.setBorderColor('red')
            option1Items.draw()
            option1Money.draw()
            win.flip()
            core.wait(1)
            choice1Responses[i] = choiceAmount
            break
        option1Money.draw()
        option1MoneyShape.draw()
        option1Items.draw()
        option1ItemsShape.draw()
        win.flip()
    
    # Check for response
    ## Exit current trial and begin new one if subject did not answer in time
    if choice1Responses[i] == '':
        choice1Responses[i] = 'None'
        choice1ReactionTimes[i] ='None'
        choice2Responses[i] = 'None'
        choice2ReactionTimes[i] = 'None'
        postChoiceResponses[i] = 'None'
        postChoiceReactionTimes[i] = 'None'
        try_faster_screen = visual.TextStim(win, text='Please make a faster decision next round!')
        ## Show 'try faster' screen
        event.clearEvents()
        try_faster_screen.draw()
        win.flip()
        core.wait(3)
        continue # Jumps to start of for loop, begins a new trial

    # Delay 1. Select 5 or 6 second delay
    while timer.getTime() < 5:
        win.flip()

    # Choice 2
    if choice1Responses[i] == monetaryAmount:
        option2Money1.setText('$' + str(monetaryAmount))
        option2Money2.setText('$' + str(monetaryAmount))
        option2Money3.setText('$' + str(monetaryAmount))
        option2Money4.setText('$' + str(monetaryAmount))
        option2Money5.setText('$' + str(monetaryAmount))
        option2Money6.setText('$' + str(monetaryAmount))
        option2Money7.setText('$' + str(monetaryAmount))
        option2Money8.setText('$' + str(monetaryAmount))
        option2Money9.setText('$' + str(monetaryAmount))
        option2Money10.setText('$' + str(monetaryAmount))
        option2Money11.setText('$' + str(monetaryAmount))
        option2Money12.setText('$' + str(monetaryAmount))
        timer.reset()
        print(option1Money.getDisplayedText())
    # Subject chose item option
    else:  
        # Setup random images to be used based on amount unique images to be shown
        imageType = random.randint(0, 1)
        numberUniquePics = choiceAmount
        timesImageRepeated = 12 / numberUniquePics

        if trials[i] == 1 and numberUniquePics < imageList[imageType]: # Check if trial requires high preference images
            uniquePics = random.sample(imageList[imageType], numberUniquePics) 
        else: # Select low preference images
            uniquePics = random.sample(imageList[imageType + 2], numberUniquePics) 
        
        trialImages[i] = uniquePics
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
        
        timer.reset()
        while timer.getTime() < 5:
            ## item1 Chosen
            if mouse.isPressedIn(option2Item1):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos1Shape.draw()
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
                choice2Responses[i] = trialPics[0]
                break
            elif mouse.isPressedIn(option2Item2):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos2Shape.draw()
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
                choice2Responses[i] = trialPics[1]
                break
            elif mouse.isPressedIn(option2Item3):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos3Shape.draw()
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
                choice2Responses[i] = trialPics[2]
                break
            elif mouse.isPressedIn(option2Item4):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos4Shape.draw()
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
                choice2Responses[i] = trialPics[3]
                break
            elif mouse.isPressedIn(option2Item5):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos5Shape.draw()
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
                choice2Responses[i] = trialPics[4]
                break
            elif mouse.isPressedIn(option2Item6):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos6Shape.draw()
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
                choice2Responses[i] = trialPics[5]
                break
            elif mouse.isPressedIn(option2Item7):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos7Shape.draw()
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
                choice2Responses[i] = trialPics[6]
                break
            elif mouse.isPressedIn(option2Item8):
                choice2ReactionTimes[i] =  timer.getTime() ## record reaction time
                option2Pos8Shape.draw()
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
                choice2Responses[i] = trialPics[7]
                break
            elif mouse.isPressedIn(option2Item9):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos9Shape.draw()
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
                choice2Responses[i] = trialPics[8]
                break
            elif mouse.isPressedIn(option2Item10):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos10Shape.draw()
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
                choice2Responses[i] = trialPics[9]
                break
            elif mouse.isPressedIn(option2Item11):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time 
                option2Pos11Shape.draw()
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
                choice2Responses[i] = trialPics[10]
                break
            elif mouse.isPressedIn(option2Item12):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos12Shape.draw()
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
                choice2Responses[i] = trialPics[11]
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
            
    # Exit current trial and begin new one if did not answer in time
    if choice2Responses[i] == '':
        choice2Responses[i] = 'None'
        choice2ReactionTimes[i] = 'None'
        postChoiceResponses[i] = 'None'
        postChoiceReactionTimes[i] = 'None'
        try_faster_screen = visual.TextStim(win, text='Please make a faster decision next round!')
        ## Show 'try faster' screen
        event.clearEvents()
        try_faster_screen.draw()
        win.flip()
        core.wait(3)
        continue

    # Delay 2. Select 2 or 3 second delay
    timer.reset()
    while timer.getTime() < 3:
        # print(timer.getTime())
        win.flip()

    # Show Subject's choice
    timer.reset()
    while timer.getTime() < 2:
        postChoiceItem.setImage(choice2Responses[i])
        postChoiceItem.draw()
        win.flip()
        core.wait(3)
    
    satisfactionScale.reset(); 
    event.clearEvents()
    timer.reset()
    while timer.getTime() < 5:
        if not preferenceScale.noResponse:
            postChoiceReactionTimes[i] = timer.getTime()
            postChoiceResponses[i] = satisfactionScale.getRating()
            satisfactionScale.draw()
            win.flip()
            core.wait(1)
            break
        # assigns response to corresponding image
        preferenceScale.draw()
        win.flip()
    
    if postChoiceResponses[i] == '':
        postChoiceResponses[i] = 'None'
        postChoiceReactionTimes[i] = 'None'
        try_faster_screen = visual.TextStim(win, text='Please make a faster decision next round!')
        ## Show 'try faster' screen
        event.clearEvents()
        try_faster_screen.draw()
        win.flip()
        core.wait(3)

# Display rating scale and store result as resp3.
# Put this in a for trial in trials loop.

# Write to .csv file with participants name, subj_id, in file name
f=open( subj_id + ' task b results.csv','w')
f.write('Confederate: ' + confed_id + '\n')
for i in range(1):
    # Remove filepath from imageList[i] string
    f.write('Trial Type, Money Option, Item Option, Trial Images, Choice 1, Choice 1 RT, Choice 2, Choice 2 RT, PostChoice, PostChoiceRT\n')
    print(trials[i])
    print(monetaryOptions[i])
    print(itemNumberOptions[i])
    print(trialImages[i])
    print(choice1Responses[i])
    print(choice1ReactionTimes[i])
    print(choice2Responses[i])
    print(choice2ReactionTimes[i])
    print(postChoiceResponses[i])
    print(postChoiceReactionTimes[i])
    f.write(str(trials[i]) + ',' + str(monetaryOptions[i]) + ',' + str(itemNumberOptions[i]) + ',' + " ".join(map(str,trialImages[i])) 
        + ',' + str(choice1Responses[i]) +','+ str(choice1ReactionTimes[i]) + ',' + str(choice2Responses[i]) + ',' + str(choice2ReactionTimes[i]) 
        + ',' + str(postChoiceResponses[i]) +','+ str(postChoiceReactionTimes[i]) + "\n")
f.close()

win.close()
core.quit()
