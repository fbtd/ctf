#!/usr/bin/env python3

flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽'

for char in flag:
    print(chr(ord(char) >> 8), chr(ord(char) & 0x00ff), sep='', end='')
print()
