#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

print(Student('Michael'))

print('------------------------------------')
class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

for n in Fib():
    print(n)
print(list(Fib()))
print(list(Fib())[:10:2])

print('------------------------------------')
class FibItem(object):

    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):# n是切片
            start = n.start
            stop = n.stop
            step = n.step
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            if step is not None:
            	return L[::step]
            return L

f = FibItem()
print(f[0])
print(f[5])
print(f[100])
print(f[0:5])
print(f[:10])
print(f[:10:2])


print('------------------------------------')
class StudentAttr(object):

    def __init__(self):
        self.name = 'Robert'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'StudentAttr\' object has no attribute \'%s\'' % attr)
    def __call__(self): #定义一个__call__()方法，就可以直接对实例进行调用
        print('My name is %s.' % self.name)

s = StudentAttr()
print(s.name)
print(s.score)
print(s.age())
# AttributeError: 'StudentAttr' object has no attribute 'grade'
#print(s.grade)

s()
#你完全可以把对象看成函数，把函数看成对象
#如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限
#那么，怎么判断一个变量是对象还是函数呢？ 我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
print('callable(StudentAttr())?',callable(StudentAttr()))
print('callable(max)?',callable(max))
print('callable([1,2,3])?',callable([1,2,3]))

print('------------------------------------')
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __call__(self,param):
    	return Chain('%s/%s' % (self._path, param))

    def __str__(self):
        return self._path

    __repr__ = __str__
#动态创建restful api的url http://api.server/user/timeline/list
print(Chain().status.user.timeline.list)
#GET /users/:user/repos
print(Chain().users('michael').repos)

#For More：https://docs.python.org/3/reference/datamodel.html#special-method-names