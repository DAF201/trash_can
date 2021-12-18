from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
def split(x):
    list = x.split('.')
    return list
def str2float(x):
    a = split(x)[0]
    b = split(x)[1]
    a = str2int(a)
    b = str2int(b)
    c = (pow(10, -1*len(split(x)[1])))
    return a+b*c
result = str2float('123.456')
print(result, type(result))
