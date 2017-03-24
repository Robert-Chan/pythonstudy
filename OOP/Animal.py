#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
	def run(self):
		print('Animal is running')
class Dog(Animal):
	def run(self):
		print('Dog is running')
class Cat(Animal):
	def run(self):
		print('Cat is running')
a = Animal()
b = Dog()
c = Cat()

print('a is Animal?',isinstance(a,Animal))
print('b is Dog?',isinstance(b,Dog))
print('b is Animal?',isinstance(b,Animal))

def run_twice(animal):
	animal.run()
	animal.run()
#新增一个Animal的子类，不必对run_twice()做任何修改，实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态
run_twice(a)
run_twice(c)
#调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
#对扩展开放：允许新增Animal子类；
#对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

class Duck(object):
	def run(self):
		print('duck is running')
d = Duck()
run_twice(d)#动态语言的“鸭子类型”。不一定需要传入Animal类型，我们只需要保证传入的对象有一个run()方法就可以了

print('---获取对象信息---')
# type()
print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))
print('type(abs) =', type(abs))
print('type(\'abc\')==str?', type('abc')==str)

class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print('hasattr(obj, \'x\') =', hasattr(obj, 'x')) # 有属性'x'吗？
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
print('getattr(obj, \'y\') =', getattr(obj, 'y')) # 获取属性'y'
print('obj.y =', obj.y) # 获取属性'y'

print('getattr(obj, \'z\') =',getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404

f = getattr(obj, 'power') # 获取属性'power'并赋值到变量f
print(f) #f指向obj.power
print(f()) #与调用obj.power()一样

print('---实例属性和类属性---')
class Student(object):
	def __init__(self, name):
		self.name = name #实例属性
	score = 99 #类属性
print(Student.score)
print(Student('james').name)

