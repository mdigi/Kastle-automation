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

# take stick, go east, north 2x to location 3 take diskette & chainsaw
do(['take stick'] + list('enn') + ['take diskette', 'take chainsaw'], t=.3)

# go north to location 4, get gas & key, move south back to location 3
do(['n', 'take gas', 'take key', 's'])

# put gas in the chainsaw
do('use gas on chainsaw', t=.3)

# go east 4x then north to location 6, get briefcase & muffin
do(['e']*4)
do(['n', 'take briefcase', 'open briefcase'], t=.3)

# move south then east to location 5 & use key on padlock
# wait 2 seconds for text to load
do(['s', 'e'], t=.3)
do('use key on padlock', t=2, disp_txt=1)

# move east 5x to location 34 & get robot arm
do(list('e'*5) + ['take arm'], t=.3)

# go south 2x, east 2x, north 2x, east 2x, north to location 29 & get bowling ball
do(list('sseenneen') + ['take ball'], t=.3)

# go south, east 4x, north to location 31 & get mare's leg, dry ice
do(list('s' + 'e'*4 + 'n') + ['take leg', 'take ice'], t=.3)

# go south, east 2x to location 32, & take poster
do(list('see') + ['take poster'], t=.3)

# go south to location 33 & take rocks
do(['s', 'take rocks'], t=.3)

# go north, west 8x, south 2x, west 4x to location 28, get gator tooth
do(list('n' + 'w'*8 + 'sswwww') + ['take tooth'], t=.3)

# go south 2x, east 2x, south to 18, get crumbs
do(list('ssees') + ['take crumbs'], t=.3)

# go south to location 13 get crumpled paper
do(['s', 'take paper'], t=.3)

# go west 2x to location 11, get thermos
do(list('ww') + ['take thermos'], t=.3)

# go south 4x, east 2x, north 2x, east to location 15 & get weekly spyglass
do(list('s'*4 + 'eenne') + ['take spyglass'], t=.3)

# go east to location 16 & get fish
do(['e', 'take fish'], t=.3)

# go west 2x, south 2x, west 2x, south 4x, west 2x, & get archer paperback
do(list('wwssww' + 's'*4 + 'ww') + ['take paperback'], t=.3)

# go east 2x, north 4x, west 2x, north to location 10 & get garrote
do(list('eennnnwwn') + ['take garrote'], t=.3)

# go north to location 9 & get glue bottle
do(['n', 'take bottle'], t=.3)

# go west 2x to location 8 & get torch
do(['w', 'w', 'take torch'], t=.3)

# go east 2x, south 2x, east 2x, north 4x, east 2x, north 2x, east 2x, south 2x,
# east to location 19 & get hamburger
do(list('eesseennnneenneesse') + ['take hamburger'], t=.3)

# go east to location 20, open glove compartment & get manual, & bottle cap
do(['e', 'take cap'], t=.3)
do('open glove compartment', t=.3)
do('pickup manual', t=.3)

# go north 2x, east 2x, north 2x to location 23 & get cesta
do(list('nneenn') + ['take cesta'], t=.3)

# go east 2x, south 2x, east 2x, south 4x to location 24 & get stack of flyers
do(list('eesseessss') + ['take flyers'], t=.3)

# go south 3x to location 26 where the door is located
do(list('sss'), disp_txt=1)

print 'At wooden door'
x = raw_input('press enter when other krieger clone opens up door')

# go south, west 2x, north 2x, west 2x, north 2x, west 2x, south 2x, west 2x,
# south 2x, west 2x, south to location 43 & get keycard
do(list('swwnnwwnnwwsswwsswws'), t=.3)
do(['take card'], t=.3, disp_txt=1)

# go north, east 2x, north 2x, east 2x, north 2x, east 2x, south 2x, east 2x,
# south 2x, east 2x to door under 26
do(list('neenneenneesseessee'), disp_txt=1)

print 'At wooden door'
x = raw_input('press enter when other krieger clone opens up door')

# go north 8x, west 2x, north 2x, west 2x, south 2x, west 2x, south 2x, west 2x,
# north 2x, west 2x, south 2x, west 2x, south 6x to location 12
do(list('n'*8 + 'wwnnwwsswwsswwnnwwssww' + 's'*6), t=.3)

# open lab door
do('use card on door', t=1, disp_txt=1)

# go west 5x, south 2x, east 2x to location 42 & get hand truck
do(list('w'*5 + 'ssee') + ['take hand truck'], t=.3)
do('take data tape', t=.3)

if 0:
    # this code is for using getting the computer back to location 42 to use
    # the data tape
    # go to location 21 & haul the computer back to 42
    do(list('wwnn' + 'e'*6 + 'n'*6 + 'eenneess' + 'e'*6 + 'ss'))
    do('take computer')

    # go back to location 42
    do(list('nn' + 'w'*6 + 'nnwwssww' + 's'*6))
    do('use card on door', 1)
    do(list('w'*5 + 'ssee'))

    # get data tape
    do(['use data tape on computer'])

    tn.interact()

# go west 2x, north 10x, west to location 39 & get slingshot
do(list('ww' + 'n'*10 + 'w') + ['take slingshot'], t=.3)

# go west, south 2x to location 40 & get crock pot
do(list('wss') + ['take pot'], t=.3)

# go north 2x, east 2x, north to location 44 & get robot leg
do(list('nneen') + ['take leg'], t=.3)

# go north, east, & get pinata
do(['n', 'e', 'take pinata'], t=.3)

# go east to location 45 & get punched card
do(['e', 'take vials'], t=.3)
do('take punched card', t=.3)

# go south 2x to location 38 & take beer bottle
do(['s', 's', 'take beer bottle'], t=.3)

# go north 2x, west 2x, south 10x, east 6x, north 2x, east 2x, north 2x, east 2x
# to location 16 & fill beer bottle with water
do(list('nnww' + 's'*10 + 'e'*6 + 'nneennee') + ['use beer bottle on water'], t=.3)

# go west 2x, south 2x, west 2x, north 4x, east 2x, north 2x, east 2x, south 2x,
# east 2x, north 2x, east 2x, north 2x, east 2x, south 2x, east 2x, south 7x
# to location 26 the wooden door
do(list('wwsswwnnnneenneesseenneenneessee' + 's'*7), disp_txt=1)

print 'At wooden door'
x = raw_input('press enter when other krieger clone opens up door')

# go south, west 2x, north 2x, west 2x, north 2x, west 2x, south 2x, west 2x,
# south 2x, west 2x, south to location 43 & make dry ice bomb
do(list('swwnnwwnnwwsswwsswws') + ['use dry ice on beer bottle'], t=.3)

# plant the bomb
do('use bottle cap on dry ice bomb', t=.3, disp_txt=1)
time.sleep(2)

# go north, east & wait to avoid bomb, then west & south 4x to location 46
do('n', t=1)
do('e', t=4)
do(list('w' + 's'*4))

# take pen at location 46
do('take pen', t=.3)

# go west 2x, south 2x, west 2x to location 47 & get whiskey stones
do(list('wwssww') + ['take whiskey stones'], t=.3)

# go south 2x & get hole
do(list('ss') + ['take hole'], t=.3)

# go east 4x, north 2x, east 4x, north to location 49 & get candy wrapper
do(list('eeeenneeeen') + ['take wrapper'], t=.3)

# go north to location 50 & get foil swan
do(['n', 'pick swan'], t=.3)

# go south 2x, west 2x, north 2x to location 48 & get knife
do(list('sswwnn') + ['take knife'], t=.3)

# go north 2x, east 4x, south 2x to location 53 & get knitting needle
do(list('nneeeess') + ['take needle'], t=.3)

# go north 2x, east 4x, south 2x to location 54 & get spatula, hat
do(list('nneeeess') + ['take spatula'], t=.3)
do('take hat', t=.3)

# go north 2x, west 2x, south 6x, east 2x to location 55 & get bratwurst
do(list('nnww' + 's'*6 + 'ee') + ['take bratwurst'], t=.3)

# go west 2x & take window
do(list('ww') + ['take window'], t=.3)

# # go north 6x, west 6x, south 4x, west 2x, souith 2x, west 4x, north 2x,
# # east 2x, north 2x,  east 2x, north 4x
# do(list('n'*6 + 'w'*6 + 'sssswwsswwwwnneenneennnn'))

# go near robot
do(list('n'*6 + 'wwss'), t=.3)

print tn.read_very_eager()
tn.interact()
# # tn.close()
