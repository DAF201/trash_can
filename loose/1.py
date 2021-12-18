import subprocess
import sys
import random
name = str(random.random())
this_file=__file__
with open(name+'.py', 'w')as file1:
    with open(__file__,'r')as file2:
        file1.write(file2.read())
# # Start the external program
# subprocess.Popen(program)
# # We have started the program, and can suspend this interpreter
# sys.exit(exit_code)
