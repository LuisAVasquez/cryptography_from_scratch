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
        + "\t".join(
            map(str, [
                "p=", self.p,
                "q=", self.q,
                "N=", self.N,
                "euler_phi=", self.euler_phi
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

print( 
    get_key_pair(RSASession())
)