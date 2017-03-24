#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
txt = ''
with open('test.txt','r') as f:
	txt = f.read()
	print(txt)

with open('test.txt','w') as f:
	f.write(txt+datetime.now().strftime('%a, %b %d %H:%M:%S')+'\n')