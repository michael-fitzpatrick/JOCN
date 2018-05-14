from psychopy import visual, event, core, os
import glob

directory = os.getcwd()

# Initialization
imageList = [os.path.join(directory, image) for image in
                 glob.glob('images/*.jpg')]
timer = core.Clock()
win = visual.Window(fullscr=True, size=[1100, 800], units='pix', monitor='testMonitor')
mouse = event.Mouse()
d = 20 
rt = 0 
resp1 = ''


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
myItem = visual.ImageStim(win=win, image=imageList[1], units='pix', pos=[0, 0], size = [156,156])

# target boxes:
option1MoneyShape = visual.ShapeStim(win, fillColor=[1,1,1],
    vertices=[(-(d/2 + 156), -156/2), (-(d/2 + 156), 156/2), (-d/2, 156/2), (-d/2, -156/2)], opacity = 0)
option1ItemsShape = visual.ShapeStim(win, fillColor=[1,1,1],
    vertices=[((d/2 + 156), -156/2), ((d/2 + 156), 156/2), (d/2, 156/2), (d/2, -156/2)], opacity = 0)

# Choice 1 Loop
timer.reset()
while timer.getTime() < 4:
    print (timer.getTime())
    # Monetary Option Chosen
    if mouse.isPressedIn(option1MoneyShape):
        rt1 = timer.getTime()
        option1Money.setBorderColor('red')
        option1Money.draw()
        option1Items.draw()
        win.flip()
        core.wait(1)
        resp1 = option1Money.getDisplayedText()
        print('money')
        print(rt)
        break
    # Choice option Chosen
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
    try_faster_screen = visual.TextStim(win, text="""Please make a faster decision next round!""")
    # Show 'try faster' screen
    event.clearEvents()
    try_faster_screen.draw()
    win.flip()
    core.wait(3)

# Delay 1. Select 5 or 6 second delay
while timer.getTime() < 6:
    print(timer.getTime())
    win.flip()

# Choice 2



win.close()
core.quit()