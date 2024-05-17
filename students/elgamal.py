import random
import sys
from math import *
from common import *
from sympy import *

####################
# Q14
####################

# retourne p g
# g generateur sur le groupe Z*p => on utilise 3
# p premier sur n bits.


def gen_elgamal_pg(n,use_is_prime=True):
    p=gen_prime(n,use_is_prime)
    g=3
    return p,g

####################
# Q15
####################

# retourne couple cle prive/publique [sk,pk]
# definit tel que sk compris entre (3,p-2)
# pk =  g^sk [p]
# output: [sk,pk]


def gen_elgamal_sk_pk(p, g):
    sk=random.randint(3,p-1)
    pk=expo_modulaire_fast(sk,g,p)
    return sk,pk

####################
# Q15 - bis
####################

# retourne couple cle prive/cle ephemeral [sk,ke]
# definit tel que sk compris entre (3,p-2)
# ke =  g^sk [p]
# output: [sk,ke]


def gen_elgamal_sk_Ephemeral(p, g):
    sk=random.randint(3,p-1)
    ke=expo_modulaire_fast(sk,g,p)
    return sk,ke

####################
# Q16
####################

# execute par alice
# retourne le secret partage par Alice et Bob
# en utilisant la cle prive ephemeral et la cle publique de Bob


def caluclate_secret_alice(pk_b, sk, p):
    return expo_modulaire_fast(sk,pk_b,p)

# execute par bob
# retourne le secret partage par Alice et Bob
# en utilisant la cle ephemeral et la cle prive de Bob


def caluclate_secret_bob(ke, sk_b, p):
    return expo_modulaire_fast(sk_b,ke,p)

####################
# Q17
####################

# chiffrement du message m avec le secret
# output: chaine de charactere c en binaire  represantant c
# contrainte: secret plus grand que message


def enc_secret(m, secret, p):
    # indice transformez le message (et le secret) en binaire:
    # bin_m = bin(str_to_int(m))[2:]
    bin_m = str_to_int(m)
    print(bin_m)
    bin_m=bin_m*secret
    bin_m=bin_m%p
    return int_to_str(bin_m)

# dechiffrement du message c avec le secret
# output: chaine de charactere m
# contrainte: secret plus grand que message


def dec_secret(c, secret, p):
    bin_m = str_to_int(c)
    secr=inverse_modulaire(p,secret)
    bin_m=bin_m*secr
    bin_m=bin_m%p
    print(bin_m)
    return int_to_str(bin_m)

# [une suggestion]
# vous pouvez ajouter 2 fonctions:


####################
# Q19
####################

# retourne la signatue [r, s]
# sk cle secrete utilise pour signer message m
# m sous forme de texte
def elgamalsignature(g, p, sk, m):

    k=gen_prime(p,True)
    r= expo_modulaire_fast(k,g,p)
    l=inverse_modulaire(p-1,k)
    print(l)
    s=(str_to_int(m)-sk*r)
    s=s*l
    s=s%(p-1)
    return r,s

# r,s signature
# pk cle publique utilise pour signer message m
# m sous forme de texte
# output: bool verifie si signature valide
# true = valid


def elgamalverification(g, p, r, s, m, pk):
    v1=expo_modulaire_fast(r,pk,p)*expo_modulaire_fast(s,r,p)
    v1=v1%p
    v2=expo_modulaire_fast(str_to_int(m),g,p)
    #print(v1,v2)
    return v1==v2
