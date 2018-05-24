from psychopy import visual, event, core, os
import glob



# Initialization
directory = os.getcwd()
imageList = [os.path.join(directory, image) for image in glob.glob('images/*.jpg')]
timer = core.Clock()
win = visual.Window(fullscr=True, size=[1100, 800], units='pix', monitor='testMonitor', color = [-.9,-.9,-.9])
mouse = event.Mouse()
d = 20; rt1 = 0; resp1 = ''; rt2 = 0; resp2 = ''

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

## Coordinates for ImageStims
xInner = (d/2 + 160/2)
xOuter = (d/2 + 160 + d + 160/2)
y = (160/2 + d + 160/2)
## ImageStim - Top - left to right
option2Item1 = visual.ImageStim(win=win, image=imageList[1], units='pix', pos=[-(xOuter), (y)], size = [156,156])
option2Item2 = visual.ImageStim(win=win, image=imageList[1], units='pix', pos=[-(xInner), (y)], size = [156,156])
option2Item3 = visual.ImageStim(win=win, image=imageList[1], units='pix', pos=[(xInner), (y)], size = [156,156])
option2Item4 = visual.ImageStim(win=win, image=imageList[1], units='pix', pos=[(xOuter), (y)], size = [156,156])
## Middle
option2Item5 = visual.ImageStim(win=win, image=imageList[1], units='pix', pos=[-(xOuter), 0], size = [156,156])
option2Item6 = visual.ImageStim(win=win, image=imageList[1], units='pix', pos=[-(xInner), 0], size = [156,156])
option2Item7 = visual.ImageStim(win=win, image=imageList[1], units='pix', pos=[(xInner), 0], size = [156,156])
option2Item8 = visual.ImageStim(win=win, image=imageList[1], units='pix', pos=[(xOuter), 0], size = [156,156])
## Bottom
option2Item9 = visual.ImageStim(win=win, image=imageList[1], units='pix', pos=[-(xOuter), -(y)], size = [156,156])
option2Item10 = visual.ImageStim(win=win, image=imageList[1], units='pix', pos=[-(xInner), -(y)], size = [156,156])
option2Item11 = visual.ImageStim(win=win, image=imageList[1], units='pix', pos=[(xInner), -(y)], size = [156,156])
option2Item12 = visual.ImageStim(win=win, image=imageList[1], units='pix', pos=[(xOuter), -(y)], size = [156,156])

## target boxes:
option1MoneyShape = visual.ShapeStim(win, fillColor=[1,1,1],
    vertices=[(-(d/2 + 156), -156/2), (-(d/2 + 156), 156/2), (-d/2, 156/2), (-d/2, -156/2)], opacity = 0)
option1ItemsShape = visual.ShapeStim(win, fillColor=[1,1,1],
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
trialPics = [''] * 12
uniquePics = random.sample(imageList, int(option1Items.getDisplayedText)
timesRepeated = 12/ int(option1Items.getDisplayedText)
for x in timesRepeated:
    trialPics.append(uniquePics)
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
            rt2 = timer.getTime()
            #option1Money.setBorderColor('red') change the box behind it to red
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
            resp2 = trialPics[0]
            print(trialPics[0])
            print(rt2)
            break
        ## Choice option Chosen NOT UPDATED
        elif mouse.isPressedIn(option1ItemsShape):
            rt1 = timer.getTime()
            option1Items.setBorderColor('red')
            option1Items.draw()
            option1Money.draw()
            win.flip()
            core.wait(1)
            resp1 = option1Items.getDisplayedText()
            print('items')
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
    print(option1Items.getDisplayedText())

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



win.close()
core.quit()