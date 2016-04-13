#!/usr/bin/python

print("https://projecteuler.net/problem=1")

answer = sum([x for x in range(3,1000) if x % 3 == 0 or x % 5 == 0])

print("Answer:", answer)
