# This sript is for Krieger's telnet Kastle game at figgis.agency and will
# automate the game to location 25 on the map and hold the device with wheel to
# open the door at location 26
#
# map link:
# https://docs.google.com/spreadsheets/d/1TuqVXwYYit-Qv8WSQls64TOblJMtHQWOyFp-t5aMVMw/edit#gid=0

import telnetlib
import time
from do import do

class Krieger:
    'Create a Krieger'
    def __init__(self, krieger_type=''):
        self.type = krieger_type
        self.tn = telnetlib.Telnet('figgis.agency')
        time.sleep(.5)

        self.tn.write('\n')
        print self.tn.read_very_eager()
        time.sleep(8)

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
        if self.type == 'door':
            'Tell Krieger to use the wooden device and open the cave door'
            self.command('use device\n', t=.3, disp_txt=1)
        else:
            print "I'm not at the wooden device"

    def quit(self):
        self.tn.write('quit\n')
        time.sleep(.3)
        self.tn.write('exit\n')
