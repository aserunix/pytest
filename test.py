#/usr/bin/env python
#-*- coding:utf-8 -*-

import os
os.chdir('/home/jiangshijian/PycharmProjects/pytest')

with open('julie.txt') as  juf:
    data=juf.readline()
    julie=data.strip().split(',')
    print(juf)
