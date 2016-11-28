#!/usr/bin/env python3
#-*- coding:utf-8 -*-

class Athlete:
    def __int__(self,value=0):
        ##the code to initialize a "Athlete" object
        self.thing=value
    def how_big(self):
        return(len(self.thing))

d=Athlete("Holy Grail")
