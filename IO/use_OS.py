#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import os

pwd = os.path.abspath('.')

#os.mkdir(os.path.join(pwd,'testdir'))

#[x for x in os.listdir('.') if os.path.isdir(x)]
#[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))