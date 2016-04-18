# this script automates kriegers
from krieger_wood_device import Krieger_Wood_Device
from krieger_button import Krieger_Button
from krieger_1 import Krieger_1

# create krieger to turn wheel
kwood = Krieger_Wood_Device()

if 0:
    # create krieger to go to location 38
    k38 = Krieger_Button(38, kwood)
    
    # krieger for 40
    k40 = Krieger_Button(40, kwood)
    
    # krieger for 42
    k42 = Krieger_Button(42, kwood)
    
# create krieger to get all the stuff
k1 = Krieger_1(kwood)
 
