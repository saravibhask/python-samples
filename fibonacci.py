'''
Created on Dec 9, 2016

@author: saravibhask
'''

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
    
fib(10)
