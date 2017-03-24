#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#装饰器
import functools
def log(func):
	@functools.wraps(func) #functools.wraps 把原始函数的__name__等属性复制到wrapper()函数中
	def wrapper(*args,**kw): #在wrapper()函数内，首先打印日志，再紧接着调用原始函数
		print('call %s()' % func.__name__)
		return func(*args,**kw)
	return wrapper
@log
def now(*args,**kw):
	print(args)
now(1,2,3)
print(now.__name__) #wrapper


#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数  
#相当于 testlog = log2('excute')(testlog)
def log2(text):
	def decorator(func): 
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s %s()' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
@log2('excute')
def testlog():
	print('123')
testlog()
print(testlog.__name__)

print('----------------以下是既支持传参又支持不传参的装饰器------------------')

from functools import wraps
def log3(str_or_func):
	def decorator(func):
		@wraps(func)
		def wrapper(*args,**kw):
			print('%s call %s()' % (text,func.__name__))
			func(*args,**kw)
			print('end call %s()' % func.__name__)
		return wrapper
	if isinstance(str_or_func,str):
		text = str_or_func
		return decorator
	else:
		text = 'start'
		return decorator(str_or_func)
@log3('start')
def testlog3():
	print('I\'m testlog3')
testlog3()

print('----------------------------')
#偏函数
#简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
int2 = functools.partial(int,base=2)
print(int2('1000000'))
max2 = functools.partial(max,10)
print(max2(3,5,6))