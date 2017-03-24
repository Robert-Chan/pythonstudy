#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
def quadratic(a,b,c):
	x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
	x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
	return x1,x2
print('求解一元二次方程')
a = float(input('please input a:'))
if a==0:
	print('a should not be 0!')
else:
	b = float(input('please input b:'))
	c = float(input('please input c:'))
if b**2-4*a*c<0:
	print('there is no real solution of this quadratic!')
else:
	print('solutions of equations:x1=%.1f,x2=%.1f' % quadratic(a,b,c))

exit()

#汉诺塔
# def move(n,a,b,c):
#     if n == 1:
#         print('move', a, '-->', c)
#         return
#     move(n-1, a, c, b)##将前n-1个盘子看成一个整体（一个盘子），从a搬到b
#     print('move', a, '-->', c)##将最后一个盘子从a搬到c
#     move(n-1, b, a, c)##将n-1个盘子从b搬到c，同样看做一个盘子，细节由递归处理
# move(10,"A","B","C")

#Iteration
l=['aa','bb','c']
for i,v in enumerate(l):#带上索引，用enumerate转换
	print(i,v)
dic = {'a':11,'b':123,'c':14}
for k,v in dic.items():
	print(k,v)
for x,y,z in [(1,1,1),(2,2,3),(3,3,'k')]:
	print(x,y,z)
    
#List Comprehensions
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)

#Generator
#斐波那契数列
def fib(max):
	n,a,b = 0,0,1
	while (n<max):
		yield(b)#print(b)
		(a,b) = (b,a+b)
		n=n+1
	return 'done'
print(fib(10))
print([x for x in fib(10)])
#杨辉三角
def triangles():
	L1 = [1]
	i = 1
	yield(L1)
	L1 = [0,1,0]
	while True:
		L2 = [L1[i]+L1[i+1] for i in range(len(L1)-1)]
		yield(L2)
		L2.insert(0,0)
		L2.append(0)
		L1=L2
		i=i+1	
n=0
t=triangles()
while n<10:
	print(next(t))
	n=n+1

#map/reduce
def normalize(name):
	return name.title() #name[0].upper()+name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce
def prod(L):
	def mutiply(x,y):
		return x*y
	return reduce(mutiply,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

def str2float(s):
	L = s.split('.')
	def f1(x,y):
		return x*10+y
	def f2(x,y):
		return x*0.1+y
	def char2num(i):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[i]
	a = reduce(f1,map(char2num, L[0]))
	b = reduce(f2,map(char2num, L[1][::-1] + '0'))
	return a+b
print('str2float(\'123.456\') =', str2float('123.456'))

#回数
def is_palindrome(n):
	return str(n) == str(n)[::-1]
output = filter(is_palindrome, range(1, 1000))
print(list(output))

#sorted
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]
def by_score(t):
	return t[1]
L1 = sorted(L)
print(L1)
L2 = sorted(L, key=by_score)
print(L2)



