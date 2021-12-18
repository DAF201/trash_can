import numpy
from numba import jit
a = numpy.array([[1, 2], [3, 4]])
b = numpy.array([[1, 1], [2, 3]])
c = a/b
numpy.save('test', c)
d = numpy.load('test.npy')
print(d)
