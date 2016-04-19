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

    def go_to_button(self, location):
        'Go to button location'
        # take stick go east, go north 3x to location 4, get key, move south back to
        # location 3, go east 5x
        self.command(['take stick'] + list('ennn') + ['take key', 's'] + ['e']*5)

        # open door
        time.sleep(.3)
        self.command(['use key on padlock'], t=2, disp_txt=1)

        # go east 5x, south 2x, west 2x, south 2x, east 4x, south 2x, east 2x, north 2x,
        # east 2x, north 2x, east 2x, south 2x, east 2x, south 6x
        self.command(list('eeeeesswwsseeeesseenneenneessee' + 's'*7), t=.3, disp_txt=1)

        # go into cave
        print 'At wooden door'
        self.krieger_wood.open_door()
        time.sleep(3)

        # go south, west 2x, north 2x, west 2x, north 2x, west 2x, south 2x, west 2x,
        # south 2x, west 2x, south to location 43 & get keycard
        self.command(list('swwnnwwnnwwsswwsswws'), t=.3)
        self.command(['take card'], t=.3, disp_txt=1)

        # go north, east 2x, north 2x, east 2x, north 2x, east 2x, south 2x, east 2x,
        # south 2x, east 2x to door under 26
        self.command(list('neenneenneesseessee'), t=.3, disp_txt=1)

        # leave cave, don't need to ask other krieger to open door as commands
        # should be fast enough that the door should still be open
        print 'At wooden door'

        # go north 8x, west 2x, north 2x, west 2x, south 2x, west 2x, south 2x, west 2x,
        # north 2x, west 2x, south 2x, west 2x, south 6x to location 12
        self.command(list('n'*8 + 'wwnnwwsswwsswwnnwwssww' + 's'*6), t=.3)

        # open lab door
        self.command('use card on door', t=1, disp_txt=1)

        # go west 5x, north 10x, east 2x, south 2x
        self.command(list('w'*5 + 'n'*10 + 'eess'), t=.3, disp_txt=1)

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


