i = 1

class Chain(object):
    
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        global i
        print("step "+ str(i))
        i=i+1
        print("current: "+ path)
        print("previous:" + self._path)


        # print(Chain('%s/%s' % (self._path, path)))
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
    
Chain().status.user.timeline.list
