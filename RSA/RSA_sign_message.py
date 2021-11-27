###########################################
# Send a message, signing with RSA
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
    print("Bob will send a signed message to Alice.")
    print("Bob starts a RSA session...")

    rsa_session = RSA_utilities.RSASession()

    print(rsa_session)

    #generate key pair
    print("Generating keys for Bob...")
    (bob_public_key, bob_private_key) = RSA_utilities.get_key_pair(rsa_session)
    print( ">>> Public key =\t", bob_public_key)
    print(">>> Private key =\t", bob_private_key)

    #get the message

    print("What message is Bob sending? (ASCII-only): \n")
    bob_message = input(">>> ")
    print("\n")
    #bob_message = "Hello There!"

    #encode
    encoding = utilities.string_to_integers(bob_message)
    print("The message whas encoded in", len(encoding), "integers")

    #sending the message
    print("Bob signs with his private key and sends the signed message in batches:")
    N, e = bob_public_key
    d = bob_private_key
    encrypted_list = RSA_utilities.encrpyt_number_list(encoding, (N, d) )

    #decripting the message
    print("Alice decrypts the batches using Bob's public key")
    decrypted_list = RSA_utilities.encrpyt_number_list(encrypted_list, (N, e) )
    #decrypted_list = RSA_utilities.decrypt_number_list(encrypted_list, alice_public_key, alice_private_key)

    #decoding the message
    print("Alice decodes the signed message")
    alice_decoded_message = utilities.digits_to_string(decrypted_list)

    #checking for integrity

    print("Alice got as a message:")
    print(">>> ", bob_message)
    print("Alice decrypted the signature as:")
    print(">>> ", alice_decoded_message)
    print("Integrity check:", bob_message == alice_decoded_message)



