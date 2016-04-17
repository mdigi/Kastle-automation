# This scrilocation is for Krieger's telnet Kastle game at figgis.agency and will
# automate the game to location 25 on the map and hold the device with wheel to
# open the door at location 26
#
# map link:
# https://docs.google.com/spreadsheets/d/1TuqVXwYYit-Qv8WSQls64TOblJMtHQWOyFp-t5aMVMw/edit#gid=0

import telnetlib
import time

def do(actions, t=.4, disp_txt=1):
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
do('take stick')

# move east, north, north to location 3, get diskette and chainsaw
do(['e', 'n', 'n', 'take diskette', 'take chainsaw'], disp_txt=0)

# go north to location 4, get gas & key, move south back to location 3
do(['n', 'take gas', 'take key', 's'], disp_txt=0)

# go east 4x then north to location 6, get briefcase & muffin
do(list('eeeen') + ['take briefcase', 'open briefcase'], disp_txt=0)

# move south then east to location 5 & use key on padlock
# wait 2 seconds for text to load
do(['s', 'e'], disp_txt=0)
do('use key on padlock', 2, disp_txt=0)

# move east 5x to location 34 & get robot arm
do(['e']*5 + ['take arm'], disp_txt=0)

# go south 2x, west 2x, south 2x, east 4x, south 2x, east 2x, north 2x, east 2x,
# north 2x, east 2x, south 2x, east 2x, south 6x
do(list('sswwsseeeesseenneenneessee' + 's'*6), disp_txt=0)

print 'kriger is at the wooden device, type "use device" when other krieger' + \
      ' is ready to go through the door'

tn.interact()
# tn.close()
