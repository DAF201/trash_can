import numpy
# a = numpy.array([[1, 2, 3],
#                 [2, 3, 4],
#                 [4, 5, 6]])
# b = numpy.array([[0, 2, 4],
#                  [4, 6, 8],
#                  [8, 10, 12]])
# c = a*b

import base64
with open('1.py', 'rb')as file:
    data = base64.b64encode(file.read())
fin = []
data = str(data).split('b\'')[1]
data = data.split('\'')[0]
save = data
data = list(data)
temp = []
for x in data:
    temp.append(ord(x))
fin = []
for x in range(len(temp)):
    if x % 4 == 0:
        set = [[temp[x], temp[x+1]], [temp[x+2], temp[x+3]]]
        fin.append(set)
fin = numpy.array(fin)