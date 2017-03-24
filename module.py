#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'RobertChan'

import sys

def test():
	print(sys.argv) #sys模块有一个argv变量，用list存储了命令行的所有参数

if __name__ == '__main__':
	test()

