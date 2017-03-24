import json

d = {'name':'james','age':'28','score':'1P00'}
print(type(d))
print(json.dumps(d))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
dic = json.loads(json_str)
print(dic['age'])



class Student(object):
	"""docstring for Student"""
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score
s = Student("james",28,100)
print(json.dumps(s,default=lambda obj:obj.__dict__))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
s1 = json.loads(json_str,object_hook=dict2student)
print(s1.name)
