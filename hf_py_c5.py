#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return(time_string)
    (mins,secs)=time_string.split(splitter)
    return(mins+'.'+secs)

with open('julie.txt') as juf:
    data=juf.readline()
julie=data.strip().split(',')

clean_julie=[]
for each_time in julie:
    clean_julie=clean_julie.append(sanitize(each_time))
# print(sorted(clean_julie))
# print(clean_julie)

# a=[6,3,2,5,4]
# a=sorted(a)
# print(a)
