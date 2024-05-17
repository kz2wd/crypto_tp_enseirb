from common import expo_modulaire,expo_modulaire_fast,test_fermat,gen_prime,test_rabin

if __name__ == "__main__":
    print(expo_modulaire(176,511, 13))
    print("ok si c'est 5")
    print(expo_modulaire_fast(176,511,13))
"""     p=gen_prime(8)
    print(p)
    print(test_fermat(p,10000))
    print(test_rabin(p,10000)) """