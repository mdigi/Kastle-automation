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
do(list('enn') + ['take diskette', 'take chainsaw'])

# go north to location 4, get gas & key, move south back to location 3
do(['n', 'take gas', 'take key', 's'])

# put gas in the chainsaw
do('use gas on chainsaw')

# go east 4x then north to location 6, get briefcase & muffin
do(['e']*4 + ['n', 'take briefcase', 'open briefcase'])

# move south then east to location 5 & use key on padlock
# wait 2 seconds for text to load
do(['s', 'e'])
do('use key on padlock', 2)

# move east 5x to location 34 & get robot arm
do(list('e'*5) + ['take arm'])

# go south 2x, east 2x, north 2x, east 2x, north to location 29 & get bowling ball
do(list('sseenneen') + ['take ball'])

# go south, east 4x, north to location 31 & get mare's leg, dry ice
do(list('s' + 'e'*4) + ['n', 'take leg', 'take ice'])

# go south, east 2x to location 32, & take poster
do(list('see') + ['take poster'])

# go south to location 33 & take rocks
do(['s', 'take rocks'])

# go north, west 8x, south 2x, west 4x to location 28, get gator tooth
do(list('n' + 'w'*8 + 'sswwww') + ['take tooth'])

# go south 2x, east 2x, south to 18, get crumbs
do(list('ssees') + ['take crumbs'])

# go south to location 13 get crumpled paper
do(['s', 'take paper'])

# go west 2x to location 11, get thermos
do(list('ww') + ['take thermos'])

# go south 4x, east 2x, north 2x, east to location 15 & get weekly spyglass
do(list('s'*4 + 'eenne') + ['take spyglass'])

# go east to location 16 & get fish
do(['e', 'take fish'])

# go west 2x, south 2x, west 2x, south 4x, west 2x, & get archer paperback
do(list('wwssww' + 's'*4 + 'ww') + ['take paperback'])

# go east 2x, north 4x, west 2x, north to location 10 & get garrote
do(list('eennnnwwn') + ['take garrote'])

# go north to location 9 & get glue bottle
do(['n', 'take bottle'])

# go west 2x to location 8 & get torch
do(['w', 'w', 'take torch'])

# go east 2x, south 2x, east 2x, north 4x, east 2x, north 2x, east 2x, south 2x,
# east to location 19 & get hamburger
do(list('eesseennnneenneesse') +  ['take hamburger'])

# go east to location 20, open glove compartment & get manual, & bottle cap
do(['e', 'open glove compartment', 'pickup manual', 'take cap'])

# go north 2x, east 2x, north 2x to location 23 & get cesta
do(list('nneenn') + ['take cesta'])

# go east 2x, south 2x, east 2x, south 4x to location 24 & get stack of flyers
do(list('eesseessss') + ['take flyers'])

# go south 3x to location 26 where the door is located
do(list('sss'))

print 'At wooden door'
x = raw_input('press enter when other krieger clone opens up door')

# go south, west 2x, north 2x, west 2x, north 2x, west 2x, south 2x, west 2x,
# south 2x, west 2x, south to location 43 & get keycard
do(list('swwnnwwnnwwsswwsswws') + ['take card'])

# go north, east 2x, north 2x, east 2x, north 2x, east 2x, south 2x, east 2x,
# south 2x, east 2x to door under 26
do(list('neenneenneesseessee'))

print 'At wooden door'
x = raw_input('press enter when other krieger clone opens up door')

# go north 8x, west 2x, north 2x, west 2x, south 2x, west 2x, south 2x, west 2x,
# north 2x, west 2x, south 2x, west 2x, south 6x to location 12
do(list('n'*8 + 'wwnnwwsswwsswwnnwwssww' + 's'*6))

# open lab door
do('use card on door', 1)

# go west 5x, south 2x, east 2x to location 42 & get hand truck
do(list('w'*5 + 'ssee') + ['take hand truck'])

# go west 2x, north 10x, west to location 39 & get slingshot
do(list('ww' + 'n'*10 + 'w') + ['take slingshot'])

# go west, south 2x to location 40 & get crock pot
do(list('wss') + ['take pot'])

# go north 2x, east 2x, north to location 44 & get robot leg
do(list('nneen') + ['take leg'])

# go north, east, & get pinata
do(['n', 'e', 'take pinata'])

# go east to location 45 & get punched card
do(['e', 'take vials', 'take punched card'])

# go south 2x to location 38 & take beer bottle
do(['s', 's', 'take beer bottle'])

# go north 2x, west 2x, south 10x, east 6x, north 2x, east 2x, north 2x, east 2x
# to location 16
do(list('nnww' + 's'*10 + 'e'*6 + 'nneennee'))

# fill up beer bottle with water
do('use beer bottle on water')

# go west 2x, south 2x, west 2x, north 4x, east 2x, north 2x, east 2x, south 2x,
# east 2x, north 2x, east 2x, north 2x, east 2x, south 2x, east 2x, south 7x
# to location 26 the wooden door
do(list('wwsswwnnnneenneesseenneenneessee' + 's'*7))

print 'At wooden door'
x = raw_input('press enter when other krieger clone opens up door')

# go south, west 2x, north 2x, west 2x, north 2x, west 2x, south 2x, west 2x,
# south 2x, west 2x, south to location 43
do(list('swwnnwwnnwwsswwsswws'))

# make dry ice bomb
do(['use dry ice on beer bottle', 'use bottle cap on dry ice bomb'])
time.sleep(2)

# go north, east & wait to avoid bomb, then west & south 4x to location 46
do('n', 1)
do('e', 4)
do(list('w' + 's'*4))

# take pen at location 46
do('take pen')

# go west 2x, south 2x, west 2x to location 47 & get whiskey stones
do(list('wwssww') + ['take whiskey stones'])

# go south 2x & get hole
do(list('ss') + ['take hole'])

# go east 4x, north 2x, east 4x, north to location 49 & get candy wrapper
do(list('eeeenneeeen') + ['take wrapper'])

# go north to location 50 & get foil swan
do(['n', 'pick swan'])

# go south 2x, west 2x, north 2x to location 48 & get knife
do(list('sswwnn') + ['take knife'])

# go north 2x, east 4x, south 2x to location 53 & get knitting needle
do(list('nneeeess') + ['take needle'])

# go north 2x, east 4x, south 2x to location 54 & get spatula, hat
do(list('nneeeess') + ['take spatula', 'take hat'])

# go north 2x, west 2x, south 6x, east 2x to location 55 & get bratwurst
do(list('nnww' + 's'*6 + 'ee') + ['take bratwurst'])

# go west 2x & take window
do(list('ww') + ['take window'])

# go north 6x, west 6x, south 4x, west 2x, souith 2x, west 4x, north 2x,
# east 2x, north 2x,  east 2x, north 4x
do(list('n'*6 + 'w'*6 + 'sssswwsswwwwnneenneennnn'))

tn.interact()
# # tn.close()
