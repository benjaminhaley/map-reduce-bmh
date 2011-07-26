#!/usr/bin/python

import sys
import re

def main(argv):
  line = sys.stdin.readline()
  pattern = re.compile("A*")
  try:
    while line:
      for word in pattern.findall(line):
        print "LongValueSum:" + word.lower() + "\t" + "1"
      line = sys.stdin.readline()
  except "end of file":
    return None
if __name__ == "__main__":
  main(sys.argv)

