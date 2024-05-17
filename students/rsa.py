import math
import random
import sys
from math import sqrt
from common import *

####################
# Q9
####################

# input: n
# output: e,d,N

def gen_rsa(n):
    p = gen_prime(n, True)
    q = gen_prime(n, True)

    n = p * q

    psy_n = (p - 1) * (q - 1)

    e = random.randint(1, psy_n)
    while pgcd(psy_n, e) != 1:
        e = random.randint(1, psy_n)
    d = inverse_modulaire(psy_n, e)
    return e, d, n

####################
# Q10
####################

# e exponent
# N modulo
# m message
# output: c
# message/cipher sous forme de nombre


def enc_rsa(m, e, N):
    m = str_to_int(m)
    c = expo_modulaire_fast(e, m, N)
    return c

# d exponent
# N modulo
# c cipher
# output m
# message/cipher sous forme de nombre


def dec_rsa(c, d, N):
    m = expo_modulaire_fast(d, c, N)
    return int_to_str(m)

####################
# Q11
####################

# e exponent
# N modulo
# m message sous forme de texte
# output: c sous forme de nombre


def RSAcipher(e, N, m):
    return 0
    # utilisez str_to_int

# d exponent
# N modulo
# c cipher sous forme de nombre
# output: m message sous forme de texte


def RSAdecipher(d, N, c):
    return 0
    # utilisez int_to_str


####################
# Q13
####################

# d exponent
# N modulo
# m message sous forme de texte
# output: sig
def RSAsignature(d, N, m):
    return 0

# e exponent
# N modulo
# m message sous forme de texte
# sig signature
# output: bool verifie si signature valide
# true = valid


def RSAverification(e, N, m, sig):
    return 0
