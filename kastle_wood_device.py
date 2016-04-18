# This sript is for Krieger's telnet Kastle game at figgis.agency and will
# automate the game to location 25 on the map and hold the device with wheel to
# open the door at location 26
#
# map link:
# https://docs.google.com/spreadsheets/d/1TuqVXwYYit-Qv8WSQls64TOblJMtHQWOyFp-t5aMVMw/edit#gid=0

import telnetlib
import time

def do(actions, t=0, disp_txt=0):
    if type(actions) == str:
        actions = [actions]
    actions = ''.join(i + '\n' for i in actions)
    tn.write(actions)
    time.sleep(t)
    if disp_txt:
        print tn.read_very_eager()

tn = telnetlib.Telnet('figgis.agency')
time.sleep(.5)

tn.write('\n')
print tn.read_very_eager()
time.sleep(8)

# take stick go east, go north 3x to location 4, get key, move south back to
# location 3, go east 5x
do(['take stick'] + list('ennn') + ['take key', 's'] + ['e']*5)

# open door
time.sleep(.3)
do(['use key on padlock'], t=2, disp_txt=1)

# go east 5x, south 2x, west 2x, south 2x, east 4x, south 2x, east 2x, north 2x,
# east 2x, north 2x, east 2x, south 2x, east 2x, south 6x
do(list('eeeeesswwsseeeesseenneenneessee' + 's'*6))

print 'kriger is at the wooden device, type "use device" when other krieger' + \
      ' is ready to go through the door'

tn.interact()
# tn.close()
