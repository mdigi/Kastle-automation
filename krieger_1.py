# This sript is for Krieger's telnet Kastle game at figgis.agency and will
# automate the game to location 25 on the map and hold the device with wheel to
# open the door at location 26
#
# map link:
# https://docs.google.com/spreadsheets/d/1TuqVXwYYit-Qv8WSQls64TOblJMtHQWOyFp-t5aMVMw/edit#gid=0

import telnetlib
import time
from do import do
from create_krieger import Krieger

class Krieger_1(Krieger):
    '''
    Create a Krieger that gets all the items
    '''
    def __init__(self, krieger_wood):
        Krieger.__init__(self, krieger_type='')
        self.krieger_wood = krieger_wood
        self.go()

    def go(self):

        # take stick, go east, north 2x to location 3 take diskette & chainsaw
        self.command(['take stick'] + list('enn') + ['take diskette', 'take chainsaw'], t=.3)

        # go north to location 4, get gas & key, move south back to location 3
        self.command(['n', 'take gas', 'take key', 's'])

        # put gas in the chainsaw
        self.command('use gas on chainsaw', t=.3)

        # go east 4x then north to location 6, get briefcase & muffin
        self.command(['e']*4)
        self.command(['n', 'take briefcase', 'open briefcase'], t=.3)

        # move south then east to location 5 & use key on padlock
        # wait 2 seconds for text to load
        self.command(['s', 'e'], t=.3)
        self.command('use key on padlock', t=2, disp_txt=1)

        # move east 5x to location 34 & get robot arm
        self.command(list('e'*5) + ['take arm'], t=.3)

        # go south 2x, east 2x, north 2x, east 2x, north to location 29 & get bowling ball
        self.command(list('sseenneen') + ['take ball'], t=.3)

        # go south, east 4x, north to location 31 & get mare's leg, dry ice
        self.command(list('s' + 'e'*4 + 'n') + ['take leg', 'take ice'], t=.3)

        # go south, east 2x to location 32, & take poster
        self.command(list('see') + ['take poster'], t=.3)

        # go south to location 33 & take rocks
        self.command(['s', 'take rocks'], t=.3)

        # go north, west 8x, south 2x, west 4x to location 28, get gator tooth
        self.command(list('n' + 'w'*8 + 'sswwww') + ['take tooth'], t=.3)

        # go south 2x, east 2x, south to 18, get crumbs
        self.command(list('ssees') + ['take crumbs'], t=.3)

        # go south to location 13 get crumpled paper
        self.command(['s', 'take paper'], t=.3)

        # go west 2x to location 11, get thermos
        self.command(list('ww') + ['take thermos'], t=.3)

        # go south 4x, east 2x, north 2x, east to location 15 & get weekly spyglass
        self.command(list('s'*4 + 'eenne') + ['take spyglass'], t=.3)

        # go east to location 16 & get fish
        self.command(['e', 'take fish'], t=.3)

        # go west 2x, south 2x, west 2x, south 4x, west 2x, & get archer paperback
        self.command(list('wwssww' + 's'*4 + 'ww') + ['take paperback'], t=.3)

        # go east 2x, north 4x, west 2x, north to location 10 & get garrote
        self.command(list('eennnnwwn') + ['take garrote'], t=.3)

        # go north to location 9 & get glue bottle
        self.command(['n', 'take bottle'], t=.3)

        # go west 2x to location 8 & get torch
        self.command(['w', 'w', 'take torch'], t=.3)

        # go east 2x, south 2x, east 2x, north 4x, east 2x, north 2x, east 2x, south 2x,
        # east to location 19 & get hamburger
        self.command(list('eesseennnneenneesse') + ['take hamburger'], t=.3)

        # go east to location 20, open glove compartment & get manual, & bottle cap
        self.command(['e', 'take cap'], t=.3)
        self.command('open glove compartment', t=.3)
        self.command('pickup manual', t=.3)

        # go north 2x, east 2x, north 2x to location 23 & get cesta
        self.command(list('nneenn') + ['take cesta'], t=.3)

        # go east 2x, south 2x, east 2x, south 4x to location 24 & get stack of flyers
        self.command(list('eesseessss') + ['take flyers'], t=.3)

        # go south 3x to location 26 where the door is located
        self.command(list('sss'), disp_txt=1)

        # go into cave
        print 'At wooden door'
        self.krieger_wood.open_door()
        time.sleep(3)

        # go south, west 2x, north 2x, west 2x, north 2x, west 2x, south 2x, west 2x,
        # south 2x, west 2x, south to location 43 & get keycard
        self.command(list('swwnnwwnnwwsswwsswws'), t=.3)
        self.command(['take card'], t=.3, disp_txt=1)

        # go north, east 2x, north 2x, east 2x, north 2x, east 2x, south 2x, east 2x,
        # south 2x, east 2x to door under 26
        self.command(list('neenneenneesseessee'), disp_txt=1)

        # leave cave, don't need to ask other krieger to open door as commands
        # should be fast enough that the door should still be open
        print 'At wooden door'
        self.krieger_wood.open_door()
        time.sleep(3)

        # go north 8x, west 2x, north 2x, west 2x, south 2x, west 2x, south 2x, west 2x,
        # north 2x, west 2x, south 2x, west 2x, south 6x to location 12
        self.command(list('n'*8 + 'wwnnwwsswwsswwnnwwssww' + 's'*6), t=.3)

        # open lab door
        self.command('use card on door', t=1, disp_txt=1)

        # go west 5x, south 2x, east 2x to location 42 & get hand truck
        self.command(list('w'*5 + 'ssee') + ['take hand truck'], t=.3)
        self.command('take data tape', t=.3)

        if 0:
            # this code is for using getting the computer back to location 42 to use
            # the data tape
            # go to location 21 & haul the computer back to 42
            self.command(list('wwnn' + 'e'*6 + 'n'*6 + 'eenneess' + 'e'*6 + 'ss'))
            self.command('take computer')

            # go back to location 42
            self.command(list('nn' + 'w'*6 + 'nnwwssww' + 's'*6))
            self.command('use card on door', 1)
            self.command(list('w'*5 + 'ssee'))

            # get data tape
            self.command(['use data tape on computer'])

            tn.interact()

        # go west 2x, north 10x, west to location 39 & get slingshot
        self.command(list('ww' + 'n'*10 + 'w') + ['take slingshot'], t=.3)

        # go west, south 2x to location 40 & get crock pot
        self.command(list('wss') + ['take pot'], t=.3)

        # go north 2x, east 2x, north to location 44 & get robot leg
        self.command(list('nneen') + ['take leg'], t=.3)

        # go north, east, & get pinata
        self.command(['n', 'e', 'take pinata'], t=.3)

        # go east to location 45 & get punched card
        self.command(['e', 'take vials'], t=.3)
        self.command('take punched card', t=.3)

        # go south 2x to location 38 & take beer bottle
        self.command(['s', 's', 'take beer bottle'], t=.3)

        # go north 2x, west 2x, south 10x, east 6x, north 2x, east 2x, north 2x, east 2x
        # to location 16 & fill beer bottle with water
        self.command(list('nnww' + 's'*10 + 'e'*6 + 'nneennee') + ['use beer bottle on water'], t=.3)

        # go west 2x, south 2x, west 2x, north 4x, east 2x, north 2x, east 2x, south 2x,
        # east 2x, north 2x, east 2x, north 2x, east 2x, south 2x, east 2x, south 7x
        # to location 26 the wooden door
        self.command(list('wwsswwnnnneenneesseenneenneessee' + 's'*7), disp_txt=1)

        # enter cave #2 with bomb
        print 'At wooden door'
        self.krieger_wood.open_door()
        time.sleep(3)

        # go south, west 2x, north 2x, west 2x, north 2x, west 2x, south 2x, west 2x,
        # south 2x, west 2x, south to location 43 & make dry ice bomb
        self.command(list('swwnnwwnnwwsswwsswws') + ['use dry ice on beer bottle'], t=.3)

        # plant the bomb
        self.command('use bottle cap on dry ice bomb', t=.3, disp_txt=1)
        time.sleep(2)

        # go north, east & wait to avoid bomb, then west & south 4x to location 46
        self.command('n', t=1)
        self.command('e', t=4)
        self.command(list('w' + 's'*4))

        # take pen at location 46
        self.command('take pen', t=.3)

        # go west 2x, south 2x, west 2x to location 47 & get whiskey stones
        self.command(list('wwssww') + ['take whiskey stones'], t=.3)

        # go south 2x & get hole
        self.command(list('ss') + ['take hole'], t=.3)

        # go east 4x, north 2x, east 4x, north to location 49 & get candy wrapper
        self.command(list('eeeenneeeen') + ['take wrapper'], t=.3)

        # go north to location 50 & get foil swan
        self.command(['n', 'pick swan'], t=.3)

        # go south 2x, west 2x, north 2x to location 48 & get knife
        self.command(list('sswwnn') + ['take knife'], t=.3)

        # go north 2x, east 4x, south 2x to location 53 & get knitting needle
        self.command(list('nneeeess') + ['take needle'], t=.3)

        # go north 2x, east 4x, south 2x to location 54 & get spatula, hat
        self.command(list('nneeeess') + ['take spatula'], t=.3)
        self.command('take hat', t=.3)

        # go north 2x, west 2x, south 6x, east 2x to location 55 & get bratwurst
        self.command(list('nnww' + 's'*6 + 'ee') + ['take bratwurst'], t=.3)

        # go west 2x & take window
        self.command(list('ww') + ['take window'], t=.3)

        # # go north 6x, west 6x, south 4x, west 2x, souith 2x, west 4x, north 2x,
        # # east 2x, north 2x,  east 2x, north 4x
        # self.command(list('n'*6 + 'w'*6 + 'sssswwsswwwwnneenneennnn'))

        # go near robot
        self.command(list('n'*6 + 'wwss'), t=.3)

        print self.tn.read_very_eager()
        print 'near robot'

