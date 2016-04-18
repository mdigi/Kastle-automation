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
do(list('eeeeesswwsseeeesseenneenneessee' + 's'*7), t=.3, disp_txt=1)

print 'At wooden door'
x = raw_input('press enter when other krieger clone opens up door')

# go south, west 2x, north 2x, west 2x, north 2x, west 2x, south 2x, west 2x,
# south 2x, west 2x, south to location 43 & get keycard
do(list('swwnnwwnnwwsswwsswws'), t=.3)
do(['take card'], t=.3, disp_txt=1)

# go north, east 2x, north 2x, east 2x, north 2x, east 2x, south 2x, east 2x,
# south 2x, east 2x to door under 26
do(list('neenneenneesseessee'), t=.3, disp_txt=1)

print 'At wooden door'
x = raw_input('press enter when other krieger clone opens up door')

# go north 8x, west 2x, north 2x, west 2x, south 2x, west 2x, south 2x, west 2x,
# north 2x, west 2x, south 2x, west 2x, south 6x to location 12
do(list('n'*8 + 'wwnnwwsswwsswwnnwwssww' + 's'*6), t=.3)

# open lab door
do('use card on door', t=1, disp_txt=1)

# go west 5x, north 8x, west 2x, south 2x
do(list('w'*5 + 'n'*8 + 'wwss'), disp_txt=1)

print 'at location 40'
tn.interact()
