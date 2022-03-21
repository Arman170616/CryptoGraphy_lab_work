import math


p = int(input("large prime number(p): "))
q = int(input('q: '))

n = p*q 
phi_of_n = (p - 1)*(q-1)

print("possible values of e: ")

for e in range(2, phi_of_n):
    if math.gcd(e, phi_of_n) == 1:
        print(e, end=' ')
print(" ")
e = int(input("select a value for e: "))

for d in range(2, phi_of_n):
    if (d * e) % phi_of_n == 1:
        break

print(f"Public key {e, n}")
print(f"Private key {d, n}")

m = int(input('message bit: '))

#In Python, the assert statement is used to continue the execute if the given condition evaluates to True

assert m<n, "RSA Error"

encrypt = pow(m,e) % n
print(f"Message Encrypted as: {encrypt}")


decrypt = pow(encrypt, d) % n
print(f"Message Decrypted as: {decrypt}")
