#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
'''
class X(object):
	a=1
print(X)
'''
#type可以接受一个类的描述作为参数，然后返回一个类。
#type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)

X = type('X',(object,),{'a':1})
print(X)


#metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
	def  __new__(cls,name,bases,attrs): #cls:当前准备创建的类的对象（ListMetaclass） name：类的名字 bases：类继承的父类集合 attrs：类的方法集合
		attrs["add"] = lambda self,value:self.append(value)
		return type.__new__(cls,name,bases,attrs)
class MyList(list,metaclass=ListMetaclass):
	pass
#Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建
L = MyList()
L.add(1)
print(L)