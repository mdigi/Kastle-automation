# This srcipt will put krieger at location 38 to push button

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
# east 2x, north 2x, east 2x, south 2x, east 2x, south 7x
do(list('eeeeesswwsseeeesseenneenneessee' + 's'*7))

print tn.read_very_eager()
print 'At wooden door'
x = raw_input('press enter when other krieger clone opens up door')

# go south, west 2x, north 2x, west 2x, north 2x, west 2x, south 2x, west 2x,
# south 2x, west 2x, south to location 43 & get keycard
do(list('swwnnwwnnwwsswwsswws'))
do(['take card'])

# go north, east 2x, north 2x, east 2x, north 2x, east 2x, south 2x, east 2x,
# south 2x, east 2x to door under 26
do(list('neenneenneesseessee'))

print tn.read_very_eager()
print 'At wooden door'
x = raw_input('press enter when other krieger clone opens up door')

# go north 8x, west 2x, north 2x, west 2x, south 2x, west 2x, south 2x, west 2x,
# north 2x, west 2x, south 2x, west 2x, south 6x to location 12
do(list('n'*8 + 'wwnnwwsswwsswwnnwwssww' + 's'*6))

# open lab door
do('use card on door', 1)

# go west 5x, north 10x, east 2x, south 2x
do(list('w'*5 + 'n'*10 + 'eess'))

print tn.read_very_eager()
print 'at location 38'
tn.interact()
