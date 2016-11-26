#!/bin/python3

# This little module just reads current data.
# Values are consumed by main.

import os
import datetime

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

def collecttime():
    # Arbitrarily get time based on SMN, apply to all later.
    val = os.path.getmtime('/tmp/smn')
    a = datetime.datetime.fromtimestamp(val)
    return a.strftime('%H:%M:%S')
