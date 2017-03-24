#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
try:
	r=10/0
	print('result:',r)
except Exception as e:
	logging.exception(e)
else: #当没有错误发生时，会自动执行else语句
	print('else')
finally:
	print('finally')
print('END')

#常见错误类型和继承关系  https://docs.python.org/3/library/exceptions.html#exception-hierarchy