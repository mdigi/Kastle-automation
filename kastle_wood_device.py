# This script is for Krieger's telnet Kastle game at figgis.agency and will
# automate the game to location 25 on the map and hold the device with wheel to
# open the door at location 26
#
# map link:
# https://docs.google.com/spreadsheets/d/1TuqVXwYYit-Qv8WSQls64TOblJMtHQWOyFp-t5aMVMw/edit#gid=0

import telnetlib
import time

def do(actions, t=.4):
    if type(actions) == str:
        actions = [actions]
    for action in actions:
        tn.write(action + '\n')
        time.sleep(t)
        print tn.read_very_eager()

tn = telnetlib.Telnet('figgis.agency')
time.sleep(.5)

tn.write('\n')
print tn.read_very_eager()
time.sleep(8)

# pick up stick
do('pick up stick')

# move east, north, north to pt 3, get diskette and chainsaw
do(['e', 'n', 'n', 'pick up diskette', 'pick up chainsaw'])

# go north to pt 4, get gas & key, move south back to pt 3
do(['n', 'pick up gas', 'pick up key', 's'])

# go east 4x then north to pt 6, get briefcase & muffin
do(['e']*4 + ['n', 'pick up briefcase', 'open briefcase'])

# move south then east to pt 5 & use key on padlock
# wait 2 seconds for text to load
do(['s', 'e'])
do('use key on padlock', 2)

# move east 5x to pt 34 & get robot arm
do(['e']*5 + ['pick up arm'])

# go south 2x, west 2x, south 2x, east 4x, south 2x, east 2x, north 2x, east 2x,
# north 2x, east 2x, south 2x, east 2x, south 4x
do(['s']*2 + ['w']*2 + ['s']*2 + ['e']*4 + ['s']*2 + ['e']*2 + ['n']*2 +
   ['e']*2 + ['n']*2 + ['e']*2 + ['s']*2 + ['e']*2 + ['s']*6)

# use the wooden device
do('use device', 2)

tn.interact()
# tn.close()
