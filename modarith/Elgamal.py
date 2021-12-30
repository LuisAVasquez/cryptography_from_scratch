###########################################
# Elgamal encryption with modular arithmetic
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



###########################################
#Encrypt and Decrypt
###########################################


def elgamal_encrpyt_single_number(integer, masking):
    """send a single number, encrypting with modarith"""
    masking_key, prime = masking
    encrypted = (integer*masking_key)%prime
    print(">>>Message", integer, "encrypted as", encrypted, sep="\t")
    return encrypted


def elgamal_encrpyt_number_list(integer_list, masking):
    """send a list of numbers, encrypting with modarith"""
    
    return [elgamal_encrpyt_single_number(integer, masking) 
            for integer in integer_list 
            ]


def elgamal_decrypt_single_number(integer, masking):
    """decrypt a single number with a RSA private key"""
    masking_key, prime = masking

    decrypted = (integer * modarith.inverse(masking_key, prime))%prime
    print(">>>Message", integer, "decrypted as", decrypted, sep="\t")
    return decrypted

def elgamal_decrypt_number_list(integer_list, masking):
    """decrypt a list of numbers with a RSA private key"""
    return [elgamal_decrypt_single_number(integer, masking)
            for integer in integer_list
            ]




if __name__ == "__main__":


    print("Bob will send an encrpyted message to Alice.")
    print("Alice publishes a prime number and a mod base...")
    
    prime = random.choice( utilities.primes['50'])
    base = random.choice(range(10**4)) #small base

    print("Public prime number:","\t", prime)
    print("Public mod base:","\t", base)

    #generate key pair for alice
    alice_private_key = random.choice(range(prime-1))
    alice_public_key = modarith.power_mod(base, alice_private_key, prime)
    
    print("\n")
    print("Alice private key:","\t", alice_private_key)
    print("Alice public key:", "\t", alice_public_key)

    # generate ephemeral key and masking key
    print("\n")
    print(">>> Bob generates an ephemeral key and a masking key:")

    bob_ephemeral_exponent = random.choice(range(prime-1))
    bob_ephemeral_key = modarith.power_mod(base, bob_ephemeral_exponent, prime)
    bob_masking_key = modarith.power_mod(alice_public_key, bob_ephemeral_exponent, prime)

    print("exponent for key generation:","\t", bob_ephemeral_exponent)
    print("ephemeral key:","\t", bob_ephemeral_key)
    print("masking key:", "\t", bob_masking_key)


    #get the message
    print("What message is Bob sending? (ASCII-only):")
    bob_message = input(">>> ")
    print("\n")
    #bob_message = "Hello There!"

    #encode
    encoding = utilities.string_to_integers(bob_message)
    print("The message whas encoded in", len(encoding), "integers")

    #sending the message
    print("Bob sends the message in batches:")
    encrypted_list = elgamal_encrpyt_number_list(encoding, (bob_masking_key, prime))

    #sending the ephemeral key
    print("\n")
    print("Bob sends the ephemeral key", "\t", bob_ephemeral_key)
    
    #alice obtains the masking key
    alice_masking_key = modarith.power_mod(bob_ephemeral_key, alice_private_key, prime)
    alice_masking = (alice_masking_key, prime)
    print("Alice calculates the masking key","\t", alice_masking_key)

    #checking integrity
    check = (bob_masking_key == alice_masking_key)
    print("Checking integrity:","\t", check)

    #decripting the message
    print("\n")
    print("Alice decrypts the batches")
    decrypted_list = elgamal_decrypt_number_list(encrypted_list, alice_masking)

    #decoding the message
    print("Alice decodes the message")
    alice_decoded_message = utilities.digits_to_string(decrypted_list)
