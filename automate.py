# this script automates kriegers
import create_krieger
import time

# create krieger to turn wheel
kwood = create_krieger.Krieger_Wood_Device()

if 0:
    # code to get all the items and go to mitsuko

    # create krieger to get all the stuff
    k1 = create_krieger.Krieger_1(kwood)

    # create krieger to push buttons
    kb = create_krieger.Krieger_Button(kwood)

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

if 1:
    # code to get computer
    kcomp = create_krieger.Krieger_Computer(kwood)

    k = [kwood, kcomp]
