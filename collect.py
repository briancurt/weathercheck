#!/bin/python3

# This little module just reads current data.
# Values are consumed by main.

def collectsmn():
    with open('/tmp/smn', 'r') as f:
        r = f.read()
    return r

def collectaccu():
    with open('/tmp/accu', 'r') as f:
        r = f.read()
    return r

def collectwc():
    with open('/tmp/wc', 'r') as f:
        r = f.read()
    return r
