#!/usr/bin/python2.7.5 -tt

import sys

# Define a main() function that demonstrates loops
def main():
  print '---FOR LOOP---'
  for x in range(0, 3):
    print "x = %d" % (x)
  
  print '---WHILE LOOP---'
  x = 0
  while x < 3:
    print "x = %d" % (x)
    x+=1

  print '---XRANGE---'
  x = 0
  for x in xrange(3):
    print "x = %d" % (x)
  
  print '---STRING---'
  string = 'STRING'
  for x in string:
    print x

  print '---LIST---'
  list = [1, 2, 3]
  for x in list:
    print x 

if __name__ == '__main__':
  main()

