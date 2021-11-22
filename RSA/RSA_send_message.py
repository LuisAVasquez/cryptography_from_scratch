###########################################
# Send a message, encrypthing with RSA
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

from RSA import RSA_utilities

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


def decrypt_number(integer, public_key, private_key):
    """decrypt a single number with a RSA private key"""
    N = public_key[0]

    decrypted = modarith.power_mod(integer, private_key, N)
    print(">>>Message", integer, "decrypted as", decrypted, sep="\t")
    return decrypted

def decrypt_number_list(integer_list, public_key, private_key):
    """decrypt a list of numbers with a RSA private key"""
    return [decrypt_number(integer, public_key, private_key)
            for integer in integer_list
            ]


if __name__ == "__main__":
    print("Alice starts a RSA session...")
    rsa_session = RSA_utilities.RSASession()

    print(rsa_session)
    
    #generate key pair
    (alice_public_key, alice_private_key) = RSA_utilities.get_key_pair(rsa_session)
    print("Public key", alice_public_key, "Private key", alice_private_key)

    #get the message
    #bob_message = input("What message is Bob sending? (ASCII-only)")
    bob_message = "Hello There!"

    #encode
    encoding = utilities.string_to_integers(bob_message)
    print("The message whas encoded in", len(encoding), "integers")

    #sending the message
    print("Bob sends the message substrings:")
    encrypted_list = encrpyt_number_list(encoding, alice_public_key)

    #decripting the message
    print("Alice decrypts the message")
    decrypted_list = decrypt_number_list(encrypted_list, alice_public_key, alice_private_key)

    print(decrypted_list)
    #decoding the message
    print("Alice decodes the message")
    alice_decoded_message = utilities.digits_to_string(decrypted_list)


