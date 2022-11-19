#!/usr/bin/env python3
import math
c =  964354128913912393938480857590969826308054462950561875638492039363373779803642185
n = 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
e = 65537

# n = p * q -> public

# lambda(n) = lcm(p-1, q-1) -> secret

# e such that 1 < e < lambda(n)
#          &  e and lambda(n) are coprimes
# ->  public key exponent

# d such that d ≡ e^-1  (mod lamda(n) )
# d * e ≡ 1  (mod lamda(n) )
# -> private key exponent

# encryption of a message m to a cypher c
# for m < n
# c ≡ m^e (mod n)

# decryption
# m ≡ c^d ≡ (m^e)^d (mod n)



# factor n using http://factordb.com/index.php
# n =  2434792384523484381583634042478415057961 *
#      650809615742055581459820253356987396346063

p = 2434792384523484381583634042478415057961
q = 650809615742055581459820253356987396346063

lambda_n = math.lcm(p-1, q-1)
print(f'{lambda_n=}')
# 792293148091706053734237211764996137969721454833335979425547602818247371973876760

# https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
# https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
# a * x === 1 (mod m)
def mod_multiplicative_inverse(a, n):
    t, new_t = 0, 1
    r, new_r = n, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        return None
    if t < 0:
        return t + n
    return t

d = mod_multiplicative_inverse(e, lambda_n)
print(f'{d=}')
# 143269696477330491826059251974105760579202114244317937839268880800144187333298953

# m = (c ** d) % n
m = pow(c, d, n)    # pow icludes modulo!
print(f'{m=}')
# 13016382529449106065927291425342535437996222135352905256639684640304028661985917

decoded_message = list()

while m>0:
    decoded_message.append(chr(m & 0xff))
    m >>= 8
print(*reversed(decoded_message), sep='')
# picoCTF{sma11_N_n0_g0od_73918962}
