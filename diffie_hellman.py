import random
import hashlib
import sys

g = 23
p = 9

a = random.randint(5,10)
b = random.randint(10, 20)

A = (g**a) % p 
B = (g**b) % p

print('g: ', g,'(a shared value), p: ', p, '(a prime number)')

print('\n person1 calculates: ')
print('a (person1 random): ', a)
print('person1 value(A): ', A, '(g^a) mod p')


print('\n person2 calculates: ')
print('a (person2 random): ', a)
print('person2 value(B): ', B, '(g^b) mod p')

print('\n person1 calculates: ')
keyA = (B**a) % p
print('key:', keyA, '(B^a) mod p')
print('key: ', hashlib.sha256(str(keyA).encode()).hexdigest())

print('\n person2 calculates: ')
keyB = (A**b) % p
print('key:', keyB, '(A^b) mod p')
print('key: ', hashlib.sha256(str(keyB).encode()).hexdigest())