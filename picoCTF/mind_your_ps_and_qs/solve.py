#!/usr/bin/env python3

c =  964354128913912393938480857590969826308054462950561875638492039363373779803642185
n = 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
e = 65537

# n = p * q -> public

# lambda(n) = lcm(p-1, q-1) -> secret

# e such that 1 < e < lambda(n)
#          &  e and lambda(n) are coprimes
# ->  public key exponent

# d such that d ≡ e^-1  (mod lamda(n) )
# -> private key exponent

# encryption of a message m to a cypher c
# for m < n
# c ≡ m^e (mod n)

# decryption
# m ≡ c^d ≡ (m^e)^d (mod n)

def primes():
    n = 3
    yield 2
    yield n
    while True:
        if n % 10000 == 1: print(n)
        n += 2
        for m in range(2, int(n ** 0.5) +1):
            if n % m == 0:
                found = False
                break
        else:
            yield n

for d in primes():
    m = (c ** d) % n
    last = m & 0xff
    if last == 175: # "}"
        print(f'*********** {d=} ***********')
        hex_m = (hex(m)[2:])
        for i in range(10):
            print(chr(int(hex_m[i:i+2], 16)), end='')
        print('\n')
    continue

    hex_m = (hex(m)[2:])

    for i in range(10):
        print(chr(int(hex_m[i:i+2], 16)), end='')
    print('\n')

