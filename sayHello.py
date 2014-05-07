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
def multiplication(num1,num2):
    try :
        num1=int(num1)
	num2=int(num2)
    except Exception :
        return False
    return num1*num2
if __name__ == "__main__":
    sayHello('wenjie')

