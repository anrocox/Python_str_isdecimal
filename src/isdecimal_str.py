#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 10, 2014

@author: anroco

In python how to know if the characters of a string are decimal?

En python ¿como saber si los caracteres de un string son decimales?
'''

#create a str
s = '123'
print(s)

#verify if all characters in the string are decimal characters. Return True or
#False. Include all characters are those from general category 'Nd' of the
#system Unicode.
print(s.isdecimal())

#create a str
s = '172¾'
print(s)

#return False because the ¾ character is of type numeric.
print(s.isdecimal())
