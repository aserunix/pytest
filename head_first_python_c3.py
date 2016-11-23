#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
# try:
#     data=open('missing.txt','w')
#     # print(data.readline(),end='')
#     print("It's...",file=data)
# except IOError as err:
#     print('File error: ' + str(err) )
# finally:
#     if 'data' in locals():
#         data.close()

# print("Current Dir: " + os.getcwd())
# try:
#     with open('test.txt','w') as data:
#         print("It's...",file=data)
# except  IOError as err:
#     print('File error:',+str(err))

def print_lol(the_list,indent=False,level=0):
    for each_item in the_list:
        if  isinstance(each_item,list):
            print_lol(each_item,indent,level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end='')
            print(each_item)
