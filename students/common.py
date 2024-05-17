import random
import sys
from math import sqrt


####################
# Q1
####################

# retourne le pgcd de deux entiers naturels
# assurez vous que a > b
def pgcd(a, b):
    assert (a > b)
    while b != 0:
        a, b = b, a % b
    return a

# algo euclide etendu
# retourne d,u,v avec pgcd(a,b)=d=ua+vb


def euclide_ext(a, b):
    if 0 == a:
        return b, 0, 1
    gcd, _u, v = euclide_ext(b % a, a)
    u = v - (b // a) * _u
    v = _u
    return gcd, u, v

####################
# Q2
####################

# retourne un entier b dans [1,N-1] avec ab=1 modulo N


def inverse_modulaire(N, a):
    gcd, u, _ = euclide_ext(a, N)
    if 1 != gcd:
        return Exception
    return u % N

####################
# Q3
####################

# retourne (b**e) % n
# calcule le modulo apres chaque multiplication


def expo_modulaire(e, b, n):
    if (e==0):
        return 1
    ret,xcpt,mcpt=1,0,0
    for i in range (e):
        ret*=b
        xcpt+=1
        ret=ret%n
        mcpt+=1
    print("le nombre de multiplication est",xcpt)
    print("le nombre de modulo est",mcpt)
    return ret

####################
# Q4
####################

# retourne (b**e) % n
# calcule le modulo apres chaque multiplication
# O(log(e)) operations


def expo_modulaire_fast(e, b, n):
    # help:

    # representer e en binaire
    # bin_e = bin(e)[2:]

    # utile pour iterer sur chaque element de e
    # for x in range(len(bin_e)):
    #   int(bin_e[x])
    if (e == 0):
        return 1
    b_or=b
    xcpt,mcpt=0,0
    bin_e = bin(e)[2:]
    for i in range(len(bin_e)):
        if (int(bin_e[i]) == 0):
            b=expo_modulaire(2,b,n)
        else:
            b=b*b_or
            b=b%n
            xcpt+=1
            mcpt+=1
            
    print("le nombre de multiplication est",xcpt)
    print("le nombre de multiplication est",mcpt)
    return b

####################
# Q5
####################

# retourne la liste des nombres premiers <= n
# methode du crible d Eratosthene


def crible_eras(n):
    """

    Time complexity : O(n * sqrt(n))
    Space complexity : O(n) (current version) could be improved to O(sqrt(n)) by building the list little by little.

    """
    if n < 2:
        return []
    crible = list(range(2, n + 1))
    cur_min = crible[0]
    i = 1
    while cur_min * cur_min < n:
        crible = list(filter(lambda x: x % cur_min != 0 or x == cur_min, crible))
        cur_min = crible[i]
        i += 1

    return crible

####################
# Q6
####################

# input: n
# input: t number of tests
# test if prime according to fermat
# output: bool if prime


def test_fermat(n, t):
    # random number generator between a and b
    # x = random.randint(a,b)
    for i in range(t):
        x=random.randint(1,n)
        if (expo_modulaire_fast(n-1, x, n) != 1):
            print(x,expo_modulaire_fast(n-1, x, n))
            return False
    return True

####################
# Q7
####################

# input: n
# output: r and u coefficient
# for rabin test
# returns r,u such that 2^r * u = n and u is odd


def find_ru(n):
    #n-=1
    r,u=0,0
    while (n%2 == 0):
        r+=1
        n=n//2
    u=n
    return r,u

####################
# Q8
####################

# n entier
# a entier dans [1,n-2]
# pgcd(a,n)=1
# retourne True , si a est un temoin de Rabin de non-primalite de n


def temoin_rabin(a, n):
    # utilisez expo_modulaire_fast !
    r,u=find_ru(n)
    if (expo_modulaire_fast(u,a,n) == 1):
        return False
    for i in range(r):
        if (expo_modulaire_fast(u*2**i,a,n) == n-1):
            return False
    return True


# n entier a tester, t nombre de tests
# retourne True , si n est premier
# retourne False , avec proba > 1-(1/4)**t, si n est compose
def test_rabin(n, t):
    if (n%2 == 0):
        return False
    for i in range(t):
        a=random.randint(1,n-1)
        if (pgcd(n,a) != 1 or temoin_rabin(a,n) == True):
            return False
    return True

# prime generator
# output: n range for prime number
# utilise votre implementation de rabin (ou la plus effice si rabin non dispo)
# pour generer un nombre premier sur n bits.
# range de n: p = random.randint(pow(2,n-1),pow(2,n)-1)


def gen_prime(n):
    p = random.randint(pow(2,n-1),pow(2,n)-1)
    while (test_rabin(p, 10000) == False):
        p = random.randint(pow(2,n-1),pow(2,n)-1)
    return p

####################
# Helper functions for rsa/elgamal
####################

# Helper function
# convert str to int


def str_to_int(m):
    s = 0
    b = 1
    for i in range(len(m)):
        s = s + ord(m[i])*b
        b = b * 256
    return s

# Helper function
# convert int to str


def int_to_str(c):
    s = ""
    q, r = divmod(c, 256)
    s = s+str(chr(r))
    while q != 0:
        q, r = divmod(q, 256)
        s = s+str(chr(r))
    return s


