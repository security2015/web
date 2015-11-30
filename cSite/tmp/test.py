#!/usr/bin/python

def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

import os
import sys

if len(sys.argv) == 1:
  print "In num"
  exit(1)
elif not isNumber(sys.argv[1]):
  print "error"
  exit(2)

sum = float(sys.argv[1]) + 1
print sum
