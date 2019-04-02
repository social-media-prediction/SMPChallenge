#-*-coding:utf-8-*-

import sqlite3


conn = sqlite3.connect('smp.db')
cursor = conn.cursor()

cursor.execute('create table user (uid integer primary key autoincrement, username varchar(20), password varchar(20), email varchar(20))')
cursor.execute('create table team (uid integer, teamname varchar(50), members varchar(500))')
# cursor.execute('insert into user values (NULL, "zengzhaoyang", "123123123", "root@zengzhaoyang.com")')

conn.commit()
# a = cursor.execute('select * from team').fetchall()
# print a