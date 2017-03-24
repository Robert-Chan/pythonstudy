#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object): #继承object
	"""docstring for Student"""
	def __init__(self, name, score):
		#super(Student, self).__init__()
		self.name = name
		self.__score = score #私有变量
	def get_score(self):
		return self.__score
	def set_score(self,score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')
	def printscore(self):
		print("%s ：%s" % (self.name,self.__score))

james = Student('James',99)
curry = Student('Curry',100)
james.printscore()
curry.printscore()

james.set_score(88)
print(james.get_score())

print(james._Student__score) #可以通过这种方式访问私有属性，但是强烈不建议，不同的解释器可能会是不同的变量名


def set_age(self,age):
	self.age = age
from types import MethodType
curry.set_age = MethodType(set_age,curry)# 给实例绑定一个方法
curry.set_age(25)
print(curry.age)

