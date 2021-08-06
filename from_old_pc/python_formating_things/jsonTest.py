import json
class student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def toDict(self):
        return{
            'name':self.name,
            'age':self.age,
            'score':self.score
        }
s=student('Bob',20,88)
js=json.dumps(s.toDict())
def dict2obj(d):
    return student(d['name'],d['age'],d['score'])
print(json.loads(js,object_hook=dict2obj))