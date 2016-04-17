# This sript is for Krieger's telnet Kastle game at figgis.agency and will
# automate the game to location 25 on the map and hold the device with wheel to
# open the door at location 26
#
# map link:
# https://docs.google.com/spreadsheets/d/1TuqVXwYYit-Qv8WSQls64TOblJMtHQWOyFp-t5aMVMw/edit#gid=0

import telnetlib
import time

def do(actions, t=.3, disp_txt=0):
    if type(actions) == str:
        actions = [actions]
    for action in actions:
        tn.write(action + '\n')
        time.sleep(t)
        if disp_txt:
            print tn.read_very_eager()

tn = telnetlib.Telnet('figgis.agency')
time.sleep(.5)

tn.write('\n')
print tn.read_very_eager()
time.sleep(8)

# take stick
do(['take stick', 'e'])

# go north to location 4, get key, move south back to location 3
do(list('nnn') + ['take key', 's'])

# go east 5x, open door
do(list('eeeee'))
do('use key on padlock', t=2, disp_txt=1)

# go east 5x, south 2x, west 2x, south 2x, east 4x, south 2x, east 2x, north 2x,
# east 2x, north 2x, east 2x, south 2x, east 2x, south 6x
do(list('eeeeesswwsseeeesseenneenneessee' + 's'*6))

print 'kriger is at the wooden device, type "use device" when other krieger' + \
      ' is ready to go through the door'

tn.interact()
# tn.close()
