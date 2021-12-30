###########################################
# Key exchange with modular arithmetic
###########################################






###########################################
# putting the parent folder in syspath 
# to be able to import all the modules in the package
import os, sys

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), '..'
        )
    )
)
###########################################

from utilities import utilities
from modarith import modarith
import random 


if __name__ == "__main__":
    #randomly choose one primes
    prime = random.choice( utilities.primes['50'])
    base = random.choice(range(10**4)) #small base

    print("Public prime number: ", prime)
    print("Public mod base: ", base)

    alice_private = random.choice(range(prime-1))
    alice_public = modarith.power_mod(base, alice_private, prime)

    print("\n")

    print("Alice private key:","\t", alice_private)
    print("Alice public key:", "\t", alice_public)


    bob_private = random.choice(range(prime-1))
    bob_public = modarith.power_mod(base, bob_private, prime)
    print("Bob private key:", "\t", bob_private)
    print("Bob public key:","\t", bob_public)

    
    print("\n>>>> Exchanging keys")

    alice_encryption_key = modarith.power_mod(bob_public, alice_private, prime)
    print("Alice calculates:","\t", alice_encryption_key)
    
    bob_encryption_key  = modarith.power_mod(alice_public, bob_private, prime)
    print("Bob calculates:","\t", bob_encryption_key)

    print("\n>>>> Checking keys")
    
    check = (alice_encryption_key == bob_encryption_key)
    print("Are the keys equal?", check)

    if check:
        print("DH Key exchange successful")
    else:
        print("DH Key exchange unsuccessful")



        