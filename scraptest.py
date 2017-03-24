#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request, parse
import json
from bs4 import BeautifulSoup
import sqlite3
import mysql.connector

def scrap(page=0):
	with request.urlopen('https://movie.douban.com/j/search_subjects?type=movie&tag=%%E7%%83%%AD%%E9%%97%%A8&sort=rank&page_limit=20&page_start=%s' % page) as f:
	    data = f.read()
	    #print('Status:', f.status, f.reason)
	    # for k, v in f.getheaders():
	    #     print('%s: %s' % (k, v))
	    obj = json.loads(data.decode('utf-8'))
	    for x in obj['subjects']:
	    	print(x['title'] + x['rate'])

def lianjia(page,region,cursor):
	url_page="http://bj.lianjia.com/xiaoqu/pg%srs%s/" % (page,region)
	with request.urlopen(url_page) as f:
		data = f.read()
		soup = BeautifulSoup(data,"html.parser")
		xiaoqu_list=soup.findAll('li',{'class':'xiaoquListItem'})
		for xq in xiaoqu_list:
			name = xq.find('div','totalPrice').find('span').text
			price = xq.find('div','title').find('a').text
			print('小区均价：',name,'\t',price)
			cursor.execute("insert into xiaoqu (name,price) values (\'%s\', \'%s\')" % (name,price))
			print('rowcount =', cursor.rowcount)

# region = parse.quote('昌平')
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# cursor.execute('create table if not exists xiaoqu (id varchar(20) primary key, name varchar(20),price int)')

# for x in range(20):
# 	lianjia(x,region,cursor)	
# cursor.close()
# conn.commit()
# conn.close()

def search():
	# 查询记录：
	conn = sqlite3.connect('test.db')
	cursor = conn.cursor()
	# 执行查询语句:
	cursor.execute('select * from xiaoqu')
	# 获得查询结果集:
	values = cursor.fetchall()
	#print(values)
	global datas
	datas = values
	cursor.close()
	conn.close()
search()

print(len(datas))


# # change root password to yours:
# conn = mysql.connector.connect(user='root', password='Pass2016word', database='awesome')

# cursor = conn.cursor()
# # 创建user表:
# cursor.execute('create table if not exists xiaoqu (id int not null AUTO_INCREMENT primary key, name varchar(20),price varchar(20))')
# # 插入一行记录，注意MySQL的占位符是%s:
# for data in datas:
# 	cursor.execute('insert into xiaoqu (name, price) values (%s, %s)', (data[2], data[1]))
# # 提交事务:
# conn.commit()
# cursor.close()

# n=0
# while True:
# 	scrap(n)
# 	n=n+20