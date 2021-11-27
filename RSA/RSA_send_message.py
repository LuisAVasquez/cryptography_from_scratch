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


if __name__ == "__main__":
    print("Alice starts a RSA session...")
    rsa_session = RSA_utilities.RSASession()

    print(rsa_session)
    
    #generate key pair
    print("Generating keys for Alice...")
    (alice_public_key, alice_private_key) = RSA_utilities.get_key_pair(rsa_session)
    print( ">>> Public key =\t", alice_public_key)
    print(">>> Private key =\t", alice_private_key)

    #get the message
    print("What message is Bob sending? (ASCII-only): \n")
    bob_message = input(">>> ")
    print("\n")
    #bob_message = "Hello There!"

    #encode
    encoding = utilities.string_to_integers(bob_message)
    print("The message whas encoded in", len(encoding), "integers")

    #sending the message
    print("Bob sends the message in batches:")
    encrypted_list = RSA_utilities.encrpyt_number_list(encoding, alice_public_key)

    #decripting the message
    print("Alice decrypts the batches")
    decrypted_list = RSA_utilities.decrypt_number_list(encrypted_list, alice_public_key, alice_private_key)

    #decoding the message
    print("Alice decodes the message")
    alice_decoded_message = utilities.digits_to_string(decrypted_list)



############
"""
print("#"*20 )
rsa_session = RSA_utilities.RSASession()
print(rsa_session)
    
#generate key pair
(alice_public_key, alice_private_key) = RSA_utilities.get_key_pair(rsa_session)
print((alice_public_key, alice_private_key))

#encrypt and decrypt
number = 10
encrypted = encrpyt_single_number(10, alice_public_key)
decrypted = decrypt_single_number(encrypted, alice_public_key, alice_private_key)

print(

    modarith.power_mod(
        2,
        rsa_session.euler_phi,
        rsa_session.N
    )% rsa_session.N
)

print(

    modarith.power_mod(
        9,4000,100
    )
)
"""