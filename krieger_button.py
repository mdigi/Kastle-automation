# This sript is for Krieger's telnet Kastle game at figgis.agency and will
# automate the game to location 25 on the map and hold the device with wheel to
# open the door at location 26
#
# map link:
# https://docs.google.com/spreadsheets/d/1TuqVXwYYit-Qv8WSQls64TOblJMtHQWOyFp-t5aMVMw/edit#gid=0

import telnetlib
import time
from do import do
from create_krieger import Krieger

class Krieger_Button(Krieger):
    '''
    Create a Krieger that will be at location 38, 40, or 42 to push button
    krieger_wood is the krieger object used to turn the wheel at location 25
    '''
    def __init__(self, krieger_wood):
        Krieger.__init__(self)
        self.krieger_wood = krieger_wood
        self.go_to_button()

    def go_to_button(self):
        'Go to button'
        # take stick go east, go north 3x to location 4, get key, move south back to
        # location 3, go east 5x
        self.command(['take stick'] + list('ennn') + ['take key', 's'] + ['e']*5)

        # open door
        time.sleep(.3)
        self.command(['use key on padlock'], t=2, disp_txt=1)
        
        # get dry ice for bomb later on
        self.command(list('eeeeesseenn' + 'e'*6 + 'n') + ['take ice'], t=.3)
        
        # go to door
        self.command(list('s' + 'w'*6 + 'sswwwwsseeeesseenneenneessee' + 's'*7),
                     t=.3, disp_txt=1)

        # go into cave
        print 'At wooden door'
        self.krieger_wood.open_door()
        time.sleep(3)

        # go south, west 2x, north 2x, west 2x, north 2x, west 2x, south 2x, west 2x,
        # south 2x, west 2x, south to location 43 & get keycard
        #self.command(list('swwn'), t=5, disp_txt=1) # fight barry
        self.command(list('swwnnwwnnwwsswwsswws'), t=.3)
        self.command(['take card'], t=.3, disp_txt=1)

        # go north, east 2x, north 2x, east 2x, north 2x, east 2x, south 2x, east 2x,
        # south 2x, east 2x to door under 26
        self.command(list('neenneenneesseessee'), t=1, disp_txt=1)

        # leave cave, don't need to ask other krieger to open door as commands
        # should be fast enough that the door should still be open
        #self.krieger_wood.open_door()
        #time.sleep(3)
        print 'At wooden door'

        # go north 8x, west 2x, north 2x, west 2x, south 2x, west 2x, south 2x
        # to locatoin 20 and get bottle cap
        self.command(list('n'*8 + 'wwnnwwsswwss') + ['take cap'], t=.3)
        
        # go west 2x, north 2x, west 2x, south 2x, west 2x, south 6x to location 12
        self.command(list('wwnnwwssww' + 's'*6), t=.3)

        # open lab door
        self.command('use card on door', t=1, disp_txt=1)

        # go west 5x, north 10x, east 2x, south 2x
        self.command(list('w'*5 + 'n'*10 + 'eess'), t=.3, disp_txt=1)
        
        # pick up beer bottle for later
        self.command('take beer bottle', t=.3, disp_txt=1)

        print 'at location 38'

    def push_button(self):
        'Tell Krieger to push the button on the console'
        self.command('push button', t=1)
        
        # go to location 40
        self.command(list('nnwwsswwss'), t=.3, disp_txt=1)
        print 'at location 40'
        self.command('push button', t=1)

        # go to location 42
        self.command(list('nnee' + 's'*10 + 'ee'), t=.3, disp_txt=1)
        print 'at location 42'
        self.command('push button', t=1)
        
    def bomb(self):
        'Do this after pushing button, should be at location 42'
        
        # krieger at the door is probably dead, make him go to the door again
        self.krieger_wood.go_to_device()
        
        # go to location 16 to get water for the dry ice bomb
        self.command(list('wwnn' + 'e'*6 + 'nneennee') + ['use beer bottle on water'], 
                     t=3., disp_txt=1)        
                     
        # go west 2x, south 2x, west 2x, north 4x, east 2x, north 2x, east 2x, south 2x,
        # east 2x, north 2x, east 2x, north 2x, east 2x, south 2x, east 2x, south 7x
        # to location 26 the wooden door
        self.command(list('wwsswwnnnneenneesseenneenneessee' + 's'*7), disp_txt=1)

        # enter cave #2 with bomb
        print 'At wooden door'
        self.krieger_wood.open_door()
        time.sleep(3)

        # go south, west 2x, north 2x, west 2x, north 2x, west 2x, south 2x, west 2x,
        # south 2x, west 2x, south to location 43 & make dry ice bomb
        self.command(list('swwnnwwnnwwsswwsswws') + ['use dry ice on beer bottle'], t=.3)

        # plant the bomb
        self.command('use dry ice on beer bottle', t=.3, disp_txt=1)
        self.command('use bottle cap on dry ice bomb', t=.3, disp_txt=1)
        time.sleep(2)
        
    def avoid_bomb(self):

        # go north, east & wait to avoid bomb, then west & south 4x to location 46
        self.command('n', t=1)
        self.command('e', t=4)


