#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# class Person(object):

#     def __init__(self):
#         print('1')
#     def __new__(cls, *args, **kwargs):
#         print("2")
#         return object.__new__(cls, *args, **kwargs)
#
# p = Person()

# def testE(p):
#     if p<1:
#         raise(Exception,"err")
# try:
#     testE(0)
# except(Exception, err):
#     print(1,err)

a = [1, 2 , 3, 4]
a.sort(key=lambda a:len(str(a)), reverse=True)
print(a)



