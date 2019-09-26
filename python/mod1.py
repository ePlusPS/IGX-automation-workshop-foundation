#!/usr/bin/env python

name = 'dave'

def printhello():
    print('hello George')

def printname(name):
    print(name)

print(f'Name from mod1 is{__name__}')

def printthis():
    print('mod1 says print this')

if __name__ == "__main__":
    printthis()
    print('You ran this module directly as the main script')
