#!/usr/bin/env python

with open('error.log','r') as f:
    for i in f:
        max(i.strip())
    print(i)

