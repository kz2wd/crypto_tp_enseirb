import random
import sys
from math import sqrt
from common import *

####################
# Q14
####################

# retourne p g
# g generateur sur le groupe Z*p => on utilise 3
# p premier sur n bits.


def gen_elgamal_pg(n):
    return 1

####################
# Q15
####################

# retourne couple cle prive/publique [sk,pk]
# definit tel que sk compris entre (3,p-2)
# pk =  g^sk [p]
# output: [sk,pk]


def gen_elgamal_sk_pk(p, g):
    return 0

####################
# Q15 - bis
####################

# retourne couple cle prive/cle ephemeral [sk,ke]
# definit tel que sk compris entre (3,p-2)
# ke =  g^sk [p]
# output: [sk,ke]


def gen_elgamal_sk_Ephemeral(p, g):
    return 0

####################
# Q16
####################

# execute par alice
# retourne le secret partage par Alice et Bob
# en utilisant la cle prive ephemeral et la cle publique de Bob


def caluclate_secret_alice(pk_b, sk, p):
    return 0

# execute par bob
# retourne le secret partage par Alice et Bob
# en utilisant la cle ephemeral et la cle prive de Bob


def caluclate_secret_bob(ke, sk_b, p):
    return 0

####################
# Q17
####################

# chiffrement du message m avec le secret
# output: chaine de charactere c en binaire  represantant c
# contrainte: secret plus grand que message


def enc_secret(m, secret, p):
    # indice transformez le message (et le secret) en binaire:
    # bin_m = bin(str_to_int(m))[2:]
    return 0

# dechiffrement du message c avec le secret
# output: chaine de charactere m
# contrainte: secret plus grand que message


def dec_secret(c, secret, p):
    return 0

# [une suggestion]
# vous pouvez ajouter 2 fonctions:


####################
# Q19
####################

# retourne la signatue [r, s]
# sk cle secrete utilise pour signer message m
# m sous forme de texte
def elgamalsignature(g, p, sk, m):
    return 0

# r,s signature
# pk cle publique utilise pour signer message m
# m sous forme de texte
# output: bool verifie si signature valide
# true = valid


def elgamalverification(g, p, r, s, m, pk):
    return 0
