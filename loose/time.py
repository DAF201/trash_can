import time
import os


def fileTime(file):
    return [time.ctime(os.path.getatime(file)),
            time.ctime(os.path.getctime(file)),
            time.ctime(os.path.getmtime(file))]
times = fileTime("C:\\Users\\16418\\Desktop\\something\\something.py")
#times = fileTime("ccc")
print(times)
# ['Mon Nov 15 12:13:17 2021', 'Mon Nov 15 12:13:16 2021', 'Mon Nov 15 12:13:16 2021']

# with open("C:\\Users\\16418\\Desktop\\something\\something.jpg",'rb')as file:
#     file.read()
