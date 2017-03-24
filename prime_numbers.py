#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#获取素数-只能被1和自己整除的数
def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

def _odd_iter():
    n = 1
    while True:
        n = n + 2 
        yield n #从3开始生成

def _not_divisible(n):
    return lambda x: x % n > 0 #返回的是一个方法

#_not_divisible 相当于以下方法   而且这是一个闭包（closure）哦
def _not_divisible_1(n):
    def f(x):
        return x % n > 0
    return f

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible_1(n), it) #过滤掉能被n整除的数

if __name__ == '__main__':
    main()