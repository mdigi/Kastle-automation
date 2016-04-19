# this script automates kriegers
from krieger_wood_device import Krieger_Wood_Device
from krieger_button import Krieger_Button
from krieger_1 import Krieger_1
import time

# create krieger to turn wheel
kwood = Krieger_Wood_Device()

# create krieger to get all the stuff
k1 = Krieger_1(kwood)

if 1:
    # create krieger to push buttons
    kb = Krieger_Button(kwood)

    k = [k1, kb, kwood]

    k1.command(list('nne'), t=.3, disp_txt=1)
    
    kb.push_button()

    print 'waiting for octopus'
    time.sleep(192)

    # get vinyl record
    k1.get_record()
    
    # tell button krieger to make a bomb & plant it
    time.sleep(30)
    kb.bomb()
    
    # wait for bomb then go to cave door
    time.sleep(4)
    k1.command(list('nnnneenneenneesseessee'), t=.3)
    
    # go through door and go to location 17
    kwood.open_door()
    time.sleep(3)
    
    k1.command(list('n'*8 + 'wwnnwwsswwsswwnnwwssww' + 's'*8 + 'wwsswws'), t=.3, 
               disp_txt=1)
               
    k1.command('use record on shelf', t=2, disp_txt=1)
    k1.command('s')
