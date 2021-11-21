#UTF-8

# utilities for crpytography




###########################################
#String encoding and decoding
###########################################

def string_to_integers(message, sub_character_length =3 ,dummy = '}', 
    sub_string_grouping = 5):
    """
    Encode a message to a tuple of strings of digits.
    
    """
    print(">>>Encoding: ", message)
    #get the ascii values
    ascii_vals = map(ord, message)

    #convert to strings of length three
    ascii_vals = map(str, ascii_vals)
    ascii_vals = map(lambda st: st.zfill( sub_character_length  ), ascii_vals ) #pad 0's to the left
    ascii_vals = list(ascii_vals)


    #group into strings of length sub_string_grouping * sub_character_length
    missing_to_pad = len(ascii_vals) % sub_string_grouping

    #pad the message to the right with substrings of a dummy character
    ascii_vals += [str(ord(dummy)).zfill(sub_character_length)] * ( 
        sub_string_grouping - missing_to_pad
    )
    #now the length of the ascii values is a multiple of sub_string_grouping

    #split the list into sublist of length sub_string_grouping

    ascii_vals = [ascii_vals[i:i+sub_string_grouping] for i in range(0, len(ascii_vals), sub_string_grouping)]    
    ascii_vals = tuple(map(lambda lst: "".join(lst), ascii_vals))
    ascii_vals = tuple(map(int, ascii_vals))

    print(">>>>>>result", *ascii_vals, sep="\t|\t")
    return ascii_vals


#test = string_to_integers("hello There!!")
#print(
#    string_to_integers("hello There!!")
#)


def digits_to_sub_string(digits, sub_character_length =3 ,dummy = '}', 
    sub_string_grouping = 5):
    """
    Decode a digit string into the submessage that it represents
    """

    #convert to string and pad to the desired length
    chr_vals = str(digits).zfill(sub_character_length * sub_string_grouping)

    #split into substrings of length sub_character_length
    chr_vals = [chr_vals[i:i+sub_character_length] for i in range(0, len(chr_vals), sub_character_length)]
    
    #get the string characters and join them
    chr_vals = list(map(int, chr_vals))
    chr_vals = list(map(chr, chr_vals))
    chr_vals = "".join(chr_vals).rstrip(dummy)
    return chr_vals


def digits_to_string(digits_list, sub_character_length =3 ,dummy = '}', 
    sub_string_grouping = 5):
    """
    Decode a digit string list into the message that it represents
    """
    #just decode each substring and then join them.
    print(">>> Decoding ", *digits_list, sep="\t|\t" )
    decoded = [
        digits_to_sub_string(
            digits,
            sub_character_length =sub_character_length ,
            dummy = dummy, 
            sub_string_grouping = sub_string_grouping
        )
    
        for digits in digits_list]
    
    decoded = "".join(decoded)
    
    print(">>>>>>result:", decoded)
    return decoded


#print(
#    digits_to_string(test)
#)

###########################################

###########################################