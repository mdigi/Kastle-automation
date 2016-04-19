# this script automates kriegers
from krieger_wood_device import Krieger_Wood_Device
from krieger_button import Krieger_Button
from krieger_1 import Krieger_1
import time

# create krieger to turn wheel
kwood = Krieger_Wood_Device()

# create krieger to get all the stuff
k1 = Krieger_1(kwood)

if 0:
    # create krieger to go to location 38
    kb = Krieger_Button(kwood)

    k = [k1, kb, kwood]

    k1.command(list('nne'), t=.3, disp_txt=1)
    
    kb.push_button()

    print 'waiting for octopus'
    time.sleep(192)

    k1.command(list('wss'), t=1, disp_txt=1)
    k1.command(list('w' + 's'*4 + 'ww') + ['take vinyl record'], t=.3, disp_txt=1)
    k1.command(list('ee' + 'n'*6 + 'e'), t=.3, disp_txt=1)

