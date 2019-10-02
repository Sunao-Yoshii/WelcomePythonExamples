#!/usr/bin/python
import os
import sys

value = sys.stdin.read()
value = value.replace('//', '/')

splitted = value.split("\n")
for line in splitted:
    if os.path.isfile(line):
        filename, ext = os.path.splitext(line)
        if '.txt' == ext:
            with open(line, mode='r') as rf:
                print(''.join(rf.readlines()))
