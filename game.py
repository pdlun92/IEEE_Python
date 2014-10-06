#!/usr/bin/python2.7.5 -tt

import sys
import random

def main():
  print 'Welcome to the game!'
  max = input("Enter the Max: ")
  print "Max = " + str(max)
  prev = 0
  guess = -1
  target = random.randint(0, max)
  print target
  guess = input('Guess: ')
  if guess != target:
    prev = guess
    guess = input('Guess: ')
  while guess != target:
    if abs(guess - target) < abs(prev - target):
      print 'warmer...'
    elif abs(guess - target) > abs(prev - target):
      print 'colder...'
    prev = guess
    guess = input('Guess: ')
  print 'CORRECT!'  

if __name__ == '__main__':
  main()
