# Cryptography from scratch

My implementation of some cryptographic algorithms, from scratch.

To be able to send strings, I implemented my own string to integer enconder with its respective decorder.

Strings are decoded into batches of integers, and these integers are then fed to the cryptographic algorithms. After a successful process, they are decoded into the original strings.


# Methods based on modular arithmetic


## Diffie–Hellman key exchange
Run
```
python3 modarith/DHKey_exchange.py
```

The process is described step-by-step
```
Public prime number:  1125899906842511
Public mod base:  7815


Alice private key: 	 253908363983023
Alice public key: 	 172870429994238
Bob private key: 	 938295762504057
Bob public key: 	 732628139550321

>>>> Exchanging keys
Alice calculates: 	 4734224873141
Bob calculates: 	 4734224873141

>>>> Checking keys
Are the keys equal? True
DH Key exchange successful

```


## Elgamal encryption

Run 
```
python3 modarith/Elgamal.py 
```
The process is described step by step
```
Bob will send an encrpyted message to Alice.
Alice publishes a prime number and a mod base...
Public prime number: 	 1125899906842429
Public mod base: 	 6539


Alice private key: 	 736948346207418
Alice public key: 	 433734413277313


>>> Bob generates an ephemeral key and a masking key:
exponent for key generation: 	 969929725239989
ephemeral key: 	 102325605126408
masking key: 	 291740505016748
What message is Bob sending? (ASCII-only):
>>> hi!


>>>Encoding:  hi!
>>>>>>result  |  104105033125125
The message whas encoded in 1 integers
Bob sends the message in batches:
>>>Message	104105033125125	encrypted as	1074880864360724


Bob sends the ephemeral key 	 102325605126408
Alice calculates the masking key 	 291740505016748
Checking integrity: 	 True


Alice decrypts the batches
>>>Message	1074880864360724	decrypted as	104105033125125
Alice decodes the message
>>> Decoding 	|	104105033125125
>>>>>>result: hi!
```


## RSA

### Sending an ecrypted message

Run 
```
python3 RSA/RSA_send_message.py
```
The process is described step by step

```
Bob will send an encrpyted message to Alice.
Alice starts a RSA session...
RSA session parameters:
>>> p =	1125899906842429
>>> q =	1125899906842597
>>> N =	1267650600227979451717384148113
>>> euler_phi =	1267650600227977199917570463088
Generating keys for Alice...
>>> Public key =	 (1267650600227979451717384148113, 5)
>>> Private key =	 760590360136786319950542277853
What message is Bob sending? (ASCII-only): 

>>> hello here!


>>>Encoding:  hello here!
>>>>>>result  |  104101108108111  |  32104101114101  |  33125125125125
The message whas encoded in 3 integers
Bob sends the message in batches:
>>>Message	104101108108111	encrypted as	146092281434392436187061379941
>>>Message	32104101114101	encrypted as	414149083502017860101125117629
>>>Message	33125125125125	encrypted as	1016699765471562140736895216854
Alice decrypts the batches
>>>Message	146092281434392436187061379941	decrypted as	104101108108111
>>>Message	414149083502017860101125117629	decrypted as	32104101114101
>>>Message	1016699765471562140736895216854	decrypted as	33125125125125
Alice decodes the message
>>> Decoding 	|	104101108108111	|	32104101114101	|	33125125125125
>>>>>>result: hello here!
```

### Signing a message

Run
```
python3 RSA/RSA_sign_message.py
```

```
Bob will send a signed message to Alice.
Bob starts a RSA session...
RSA session parameters:
>>> p =	1125899906842511
>>> q =	1125899906842553
>>> N =	1267650600228022235913844170583
>>> euler_phi =	1267650600228019984114030485520
Generating keys for Bob...
>>> Public key =	 (1267650600228022235913844170583, 3)
>>> Private key =	 845100400152013322742686990347
What message is Bob sending? (ASCII-only): 

>>> Hello there!    


>>>Encoding:  Hello there!
>>>>>>result  |  72101108108111  |  32116104101114  |  101033125125125
The message whas encoded in 3 integers
Bob signs with his private key and sends the signed message in batches:
>>>Message	72101108108111	encrypted as	1014640438524198703982200062687
>>>Message	32116104101114	encrypted as	178450223502823609901338720490
>>>Message	101033125125125	encrypted as	340657869404703214649919972073
Alice decrypts the batches using Bob's public key
>>>Message	1014640438524198703982200062687	encrypted as	72101108108111
>>>Message	178450223502823609901338720490	encrypted as	32116104101114
>>>Message	340657869404703214649919972073	encrypted as	101033125125125
Alice decodes the signed message
>>> Decoding 	|	72101108108111	|	32116104101114	|	101033125125125
>>>>>>result: Hello there!
Alice got as a message:
>>>  Hello there!
Alice decrypted the signature as:
>>>  Hello there!
Integrity check: True
```

# Methods based on elliptic curves

Coming soon...
