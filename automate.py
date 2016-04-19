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
    # create krieger to go to location 38
    k38 = Krieger_Button(38, kwood)

    # krieger for 40
    k40 = Krieger_Button(40, kwood)

    # krieger for 42
    k42 = Krieger_Button(42, kwood)

    k = [k1, k38, k40, k42, kwood]

    k1.command(list('nne'), t=.3, disp_txt=1)

    k38.push_button()
    k40.push_button()
    k42.push_button()

    print 'waiting for octopus'
    time.sleep(192)

    k1.command(list('wss'), t=1, disp_txt=1)
    k1.command(list('w' + 's'*4 + 'ww') + ['take album'], t=.3, disp_txt=1)
    k1.command(list('ee' + 'n'*6 + 'e'), t=.3, disp_txt=1)

