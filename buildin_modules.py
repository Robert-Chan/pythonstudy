#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
phonenumber=input('please input phone number:')
if re.match(r'^\d{3,4}\-\d{5,8}$',phonenumber):
	print('OK!')
else:
	print('failed.')

#切分字符串
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))

#分组(提取)
m=re.match(r'^(\d{3,4})\-(\d{5,8})$',phonenumber)
if m:
	print(m.group(0))
	print(m.group(1))
	print(m.group(2))
	print(m.groups())
