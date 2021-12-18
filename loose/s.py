import os
def isWritable(path):
    try:
        with open('test', 'wb')as file:
            file.write('a')
        os.remove('test')
    except Exception:
        return False
    return True
print(isWritable('C:\Windows\System\Speech'))
