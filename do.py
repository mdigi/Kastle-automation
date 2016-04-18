# This function is for the krieger objects and sends commands to the telnet
# session

import time

def do(tn, actions, t=0, disp_txt=0):
    '''
    tn = telnet object
    actions = list of actions example: ['s', 'n', 'take poop']
    t = is a time delay
    disp_txt = print stuff to console
    '''
    if type(actions) == str:
        actions = [actions]
    actions = ''.join(i + '\n' for i in actions)
    tn.write(actions)
    time.sleep(t)
    if disp_txt:
        print tn.read_very_eager()