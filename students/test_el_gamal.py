

from elgamal import *

if __name__ == "__main__":
    #bob ou alice
    p,g=gen_elgamal_pg(20)
    #bob
    bob_sk,bob_pk=gen_elgamal_sk_Ephemeral(p, g)
    #alice
    al_sk,al_pk=gen_elgamal_sk_Ephemeral(p, g)
    #alice
    al_secret=caluclate_secret_alice(bob_pk, al_sk, p)
    #bob
    bob_secret=caluclate_secret_bob(al_pk, bob_sk, p)
    #alice
    c1=enc_secret("co", al_secret, p)
    #alice
    c2=enc_secret("pl", al_secret, p)
    #bob
    m1=dec_secret(c1,bob_secret,p)
    #bob
    m2=dec_secret(c2,bob_secret,p)
    print(m1,m2)






