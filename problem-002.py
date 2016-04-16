#!/usr/bin/python

print("https://projecteuler.net/problem=2")

memorized_terms = dict()

def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    if n in memorized_terms:
        return memorized_terms[n]

    f1 = 1
    f2 = 2

    for i in range(3, n+1):
        f1, f2 = f2, f1+f2

    memorized_terms[n] = f2

    return f2

answer = 0
term = 0
n = 1

while term <= 4e6:
    term = fib(n)
    if term % 2 == 0:
        answer += term
    n += 1
        
print("Answer:", answer)

