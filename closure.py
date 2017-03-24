#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calc_sum(*args):
	res = 0
	for x in args:
		res += x
	return res
print(calc_sum(1,2,3,4,5,6))

#使用闭包
def lazy_sum(*args):
	def sum():
		res = 0
		for x in args:
			res += x
		return res
	return sum
f = lazy_sum(1,2,3,4)
print(f)
print(f())

#使用闭包注意点
#返回的函数并没有立刻执行，而是直到调用了f()才执行
#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量
def count():
	fs = []
	for x in range(1,4):
		def f():
			return x*x
		fs.append(f)
	return fs
f1,f2,f3 = count()
print(f1(),f2(),f3())

#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count_1():
	fs = []
	def f(i):
		def g():
			return i*i
		return g
	for x in range(1,4):
		fs.append(f(x))
	return fs
f1,f2,f3 = count_1()
print(f1(),f2(),f3())
#lambda简化
def count_2():
	fs = []
	def f(i):
		return lambda :i*i
	for x in range(1,4):
		fs.append(f(x))
	return fs
f1,f2,f3 = count_2()
print(f1(),f2(),f3())



