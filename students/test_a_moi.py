from common import expo_modulaire,expo_modulaire_fast,test_fermat,gen_prime,test_rabin

if __name__ == "__main__":

    expo_modulaire_fast(10, 3, 20)

    for i in range(10, 100):
        for j in range(10, 100):
            for k in range(10, 100):
                assert (expo_modulaire(i, j, k) == expo_modulaire_fast(i, j, k))

    print(expo_modulaire(176,511, 13))
    print("ok si c'est 5")
    print(expo_modulaire_fast(176,511,13))
"""     p=gen_prime(8)
    print(p)
    print(test_fermat(p,10000))
    print(test_rabin(p,10000)) """