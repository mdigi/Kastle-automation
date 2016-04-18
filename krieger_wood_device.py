# This sript is for Krieger's telnet Kastle game at figgis.agency and will
# automate the game to location 25 on the map and hold the device with wheel to
# open the door at location 26
#
# map link:
# https://docs.google.com/spreadsheets/d/1TuqVXwYYit-Qv8WSQls64TOblJMtHQWOyFp-t5aMVMw/edit#gid=0

import telnetlib
import time
from do import do

class Krieger_Wood_Device:
    'Create a Krieger that goes to location 25 on the map and is ready to use device'
    def __init__(self):
        self.tn = telnetlib.Telnet('figgis.agency')
        time.sleep(.5)

        self.tn.write('\n')
        print self.tn.read_very_eager()
        time.sleep(8)

        # take stick go east, go north 3x to location 4, get key, move south back to
        # location 3, go east 5x
        self.command(['take stick'] + list('ennn') + ['take key', 's'] + ['e']*5)

        # open door
        time.sleep(.3)
        self.command(['use key on padlock'], t=2, disp_txt=1)

        # go east 5x, south 2x, west 2x, south 2x, east 4x, south 2x, east 2x, north 2x,
        # east 2x, north 2x, east 2x, south 2x, east 2x, south 6x
        self.command(list('eeeeesswwsseeeesseenneenneessee' + 's'*6))

        print 'kriger is at the wooden device, ready to turn the damn wheel'

    def check(self):
        'Press return and print out to console to check game stats'
        self.command('', t=.3, disp_txt=1)

    def command(self, actions, t=0, disp_txt=0):
        'Use do function'
        do(self.tn, actions, t, disp_txt)

    def interact(self):
        'Enter the telnet session'
        self.tn.interact()

    def open_door(self):
        'Tell Krieger to use the wooden device and open the cave door'
        self.command('use device\n', t=.3, disp_txt=1)

    def quit(self):
        self.tn.write('quit\n')
        time.sleep(.3)
        self.tn.write('exit\n')

# tn.close()
