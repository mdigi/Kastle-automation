# This sript is for Krieger's telnet Kastle game at figgis.agency and will
# automate the game to location 25 on the map and hold the device with wheel to
# open the door at location 26
#
# map link:
# https://docs.google.com/spreadsheets/d/1TuqVXwYYit-Qv8WSQls64TOblJMtHQWOyFp-t5aMVMw/edit#gid=0

import telnetlib
import time
from do import do
       
class krieger_button:        
    '''
    Create a Krieger that will be at location 38, 40, or 42 to push button
    type is 38, 40, or 42
    krieger_wood is the krieger object used to turn the wheel at location 25
    '''
    def __init__(self, type, krieger_wood):
        self.type = str(type)
        
        self.tn = telnetlib.Telnet('figgis.agency')
        time.sleep(.5)

        self.tn.write('\n')
        print self.tn.read_very_eager()
        time.sleep(8)
        
        # take stick go east, go north 3x to location 4, get key, move south back to
        # location 3, go east 5x
        do(self.tn, ['take stick'] + list('ennn') + ['take key', 's'] + ['e']*5)

        # open door
        time.sleep(.3)
        do(self.tn, ['use key on padlock'], t=2, disp_txt=1)

        # go east 5x, south 2x, west 2x, south 2x, east 4x, south 2x, east 2x, north 2x,
        # east 2x, north 2x, east 2x, south 2x, east 2x, south 6x
        do(self.tn, list('eeeeesswwsseeeesseenneenneessee' + 's'*7), t=.3, disp_txt=1)

        print 'At wooden door'
        krieger_wood.open_door()
        time.sleep(3)

        # go south, west 2x, north 2x, west 2x, north 2x, west 2x, south 2x, west 2x,
        # south 2x, west 2x, south to location 43 & get keycard
        do(self.tn, list('swwnnwwnnwwsswwsswws'), t=.3)
        do(self.tn, ['take card'], t=.3, disp_txt=1)

        # go north, east 2x, north 2x, east 2x, north 2x, east 2x, south 2x, east 2x,
        # south 2x, east 2x to door under 26
        do(self.tn, list('neenneenneesseessee'), t=.3, disp_txt=1)

        print 'At wooden door'

        # go north 8x, west 2x, north 2x, west 2x, south 2x, west 2x, south 2x, west 2x,
        # north 2x, west 2x, south 2x, west 2x, south 6x to location 12
        do(self.tn, list('n'*8 + 'wwnnwwsswwsswwnnwwssww' + 's'*6), t=.3)

        # open lab door
        do(self.tn, 'use card on door', t=1, disp_txt=1)
                          
        if self.type == '38':
            # go west 5x, north 10x, east 2x, south 2x
            do(self.tn, list('w'*5 + 'n'*10 + 'eess'), disp_txt=1)

            print 'at location 38'
            
        if self.type == '40':
            # go west 5x, north 8x, west 2x, south 2x
            do(self.tn, list('w'*5 + 'n'*8 + 'wwss'), disp_txt=1)

            print 'at location 40'
            
        if self.type == '42':
            # go west 5x, south 2x, east 2x
            do(self.tn, list('w'*5 + 'ssee'), disp_txt=1)

            print 'at location 42'
              
    def check(self):
        'Press return and print out to console to check game stats'
        do(self.tn, '', t=.3, disp_txt=1)
        
    def interact(self):
        'Enter the telnet session'
        self.tn.interact()
    
    def push_button(self):
        'Tell Krieger to push the button on the console'
        do(self.tn, 'push button', t=.3)
        
    def quit(self):
        self.tn.write('quit\n')
        time.sleep(.3)
        self.tn.write('exit\n')
    
# tn.close()
