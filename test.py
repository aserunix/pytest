#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
try:
    data=open('missing.txt','w')
    # print(data.readline(),end='')
    print("It's...",file=data)
except IOError as err:
    print('File error: ' + str(err) )
finally:
    if 'data' in locals():
        data.close()
