#!/usr/bin/env python

from sig import var_sig

def test_range(n):
    if n in range(31,98):
        print("var_bars = 5")
    elif n in range(26,30):
        print("var_bars = 4")
    elif n in range(20,25):
        print("var_bars = 3")
    elif n in range(11,19):
        print("var_bars = 2")
    elif n in range(0,10):
        print("var_bars = 1")
    elif n == 99:
        print("var_bars = 0")
    else:
        print("var_bars = 9")

test_range(var_sig)


