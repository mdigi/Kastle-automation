import time

def do(tn, actions, t=0, disp_txt=0):
    if type(actions) == str:
        actions = [actions]
    actions = ''.join(i + '\n' for i in actions)
    tn.write(actions)
    time.sleep(t)
    if disp_txt:
        print tn.read_very_eager()