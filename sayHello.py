#!/usr/bin/env python
# -*- coding: utf-8 -*-
def sayHello(name):
    print 'Welcome '+name+' come to python world!'

def Sum(num):
    i=0
    sum=0
    for i in range(num):
        sum +=i
    return sum
if __name__ == "__main__":
    sayHello('wenjie')

