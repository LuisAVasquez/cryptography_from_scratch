###########################################
# Utilities for RSA
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



from modarith import modarith
from utilities import utilities
import random




###########################################
#RSASession
###########################################
#contains all the parameters from a rsa session

class RSASession():
    """
    This class contains all the environment information for
    using RSA
    """
    def __init__(self, *primes):
        if primes is None or len(primes) != 2: 
            #randomly choose two different primes
            primes = random.sample( utilities.primes['50'] , 2)
        
        self.p = primes[0]
        self.q = primes[1]

        self.N = self.p*self.q
        self.euler_phi = (self.p-1)*(self.q-1)


    def __repr__(self) -> str:
        return ("RSA session parameters:"
        + "\n"
        + "\n".join(
            map(str, [
                ">>> p =\t" + str(self.p),
                ">>> q =\t" + str(self.q),
                ">>> N =\t" + str(self.N),
                ">>> euler_phi =\t" + str(self.euler_phi)
                ])
            )
        )

#session = RSASession(3,5)
#print(session)

#common public keys for encryption: 
# they are expected to be coprime to euler_phi(N) for many N's
common_pub_keys = [3, 5, 7, 13, 17, 19, 37]

from modarith import modarith

def get_key_pair(rsa_session):
    """
    Use the parameters of a RSA session to choose a 
    key pair (public_key, private_key)
    where public_key = (N, e)), privake_key = d
    such that d = inverse(e, euler_phi(N) )
    """

    euler_phi = rsa_session.euler_phi

    e = None
    for option in common_pub_keys:
        if modarith.gcd(option, euler_phi) == 1:
            e = option
            break
    
    #handling the case where the common public keys for encryption cannot be used

    if e is None:
        gcd = None
        while gcd != 1:
            e = random.choice(range(euler_phi))
            gcd = modarith.gcd(e, euler_phi)
        
    # now we are sure that e is invertible mod euler_phi
    d = modarith.inverse(e, euler_phi)

    return ( (rsa_session.N, e) , d)


###########################################
#Encrypt and Decrypt
###########################################


def encrpyt_single_number(integer, public_key):
    "send a single number, encrypting with RSA"
    N,e = public_key

    encrypted = modarith.power_mod(integer, e, N)
    print(">>>Message", integer, "encrypted as", encrypted, sep="\t")
    return encrypted


def encrpyt_number_list(integer_list, public_key):
    """send a list of numbers, encrpting with RSA"""
    
    return [encrpyt_single_number(integer, public_key) 
            for integer in integer_list 
            ]


def decrypt_single_number(integer, public_key, private_key):
    """decrypt a single number with a RSA private key"""
    N = public_key[0]

    decrypted = modarith.power_mod(integer, private_key, N)
    print(">>>Message", integer, "decrypted as", decrypted, sep="\t")
    return decrypted

def decrypt_number_list(integer_list, public_key, private_key):
    """decrypt a list of numbers with a RSA private key"""
    return [decrypt_single_number(integer, public_key, private_key)
            for integer in integer_list
            ]




###########################################
#Basic tests
###########################################


if __name__=="__main__":
    
    random.seed(10)
    
    rsa_session = RSASession()
    k_pub, k_priv = get_key_pair(rsa_session)
    N, e = k_pub
    euler_phi = rsa_session.euler_phi
    
    assert( (k_priv * e) % euler_phi == 1)

    assert(modarith.power_mod(5,3,13)==8)

    inter = 17
    
    print(N)
    #print(rsa_session.p * rsa_session.q)
    #print(rsa_session.N)
    print(euler_phi)
    print(modarith.power_mod(inter, euler_phi, N) )
    assert(modarith.power_mod(inter, euler_phi, N) == 1 )
    encrypted = modarith.power_mod(inter, e, N)
    decrypted = modarith.power_mod(encrypted, k_priv, N)

    assert(inter == decrypted)
