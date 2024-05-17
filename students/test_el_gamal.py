

from elgamal import *

if __name__ == "__main__":

    p,g=gen_elgamal_pg(20)
    print(p)
    bob_sk,bob_pk=gen_elgamal_sk_Ephemeral(p, g)
    al_sk,al_pk=gen_elgamal_sk_Ephemeral(p, g)
    al_secret=caluclate_secret_alice(bob_pk, al_sk, p)
    bob_secret=caluclate_secret_bob(al_pk, bob_sk, p)
    c1=enc_secret("co", al_secret, p)
    c2=enc_secret("pl", al_secret, p)
    m1=dec_secret(c1,bob_secret,p)
    m2=dec_secret(c2,bob_secret,p)
    print(m1,m2)
    print(al_secret,bob_secret)






