

from elgamal import *

    #bob ou alice
p,g=gen_elgamal_pg(40,True)
    #bob    
bob_sk,bob_pk=gen_elgamal_sk_Ephemeral(p, g)
    #alice
al_sk,al_pk=gen_elgamal_sk_Ephemeral(p, g)
    #alice
al_secret=caluclate_secret_alice(bob_pk, al_sk, p)
    #bob
bob_secret=caluclate_secret_bob(al_pk, bob_sk, p)
    #alice
c1=enc_secret("test1", al_secret, p)
    #alice
c2=enc_secret("test2", al_secret, p)
    #bob
m1=dec_secret(c1,bob_secret,p)
    #bob
m2=dec_secret(c2,bob_secret,p)
print(m1,m2)

r,s=elgamalsignature(g,p,al_sk,"test1")
print(elgamalverification(g,p,r,s,"test1",al_pk))






