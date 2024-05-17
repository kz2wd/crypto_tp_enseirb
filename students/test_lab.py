import random

from common import pgcd, euclide_ext, inverse_modulaire

from common import crible_eras

from rsa import gen_rsa

if __name__ == "__main__":
    # print(pgcd(7398, 2877))
    # print(euclide_ext(30, 20))
    # print(inverse_modulaire(11, 3))

    # print(crible_eras(50))

    random.seed(0)
    gen_rsa(10)







