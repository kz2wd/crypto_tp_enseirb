import random

from common import pgcd, euclide_ext, inverse_modulaire, str_to_int, int_to_str

from common import crible_eras

import rsa

if __name__ == "__main__":
    # print(pgcd(7398, 2877))
    # print(euclide_ext(30, 20))
    # print(inverse_modulaire(11, 3))

    # print(crible_eras(50))

    random.seed(0)
    e, d, n = rsa.gen_rsa(512)
    m = "ceci est le message de la question"
    c = rsa.enc_rsa(m, e, n)
    print(e)
    print(d)
    print(n)

    print("Public channel [", c, "]")

    decrypted = rsa.dec_rsa(c, d, n)
    print("Private channel [", decrypted, "]")











