#Joshua Lemuel Z. Centina BS CPE 1-4 Vigenere Cypher
# store the 26 letters of the alphabet in uppercase
eng_alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# ask for the user to input a message to be encrypted and save it
message_input = input("Enter a message: ")
index_message = []

# check message and convert to uppercase
for letter in message_input.upper():
    # check if letter is alphabet
    if letter.isalpha():
        # get index of the message in eng_alphabets
        index_m = eng_alphabets.index(letter)
        # add the index to the index_message
        index_message.append(index_m)

# ask for the user to input a key for encryption and save it
key_input = input("Enter a key: ")
index_key = []

# check the key and convert to uppercase
for letter in key_input.upper():
        # get the index of the key in eng_alphabets
        index_k = eng_alphabets.index(letter)
        # add the index to the index_key
        index_key.append(index_k)

# convert letters to numbers
# initialize an empty list to store encrypted indices
index_mod = []

# check the index
for i in range(len(index_message)):
     # calculate the index of corresponding letter in the key
     index = i % len(index_key)
     # add the index_message and index_key
     add = (index_message[i] + index_key[index])
     # take mod of 26 of add
     mod = add % 26
     # add the mod to index_mod
     index_mod.append(mod)

# convert numbers back to letters
# convert the list of encrypted back to letters
index_message = ""

# check the number in index_mod
for number in index_mod:
     # convert the number back into alphabets
     letter = eng_alphabets[number]
     # append the letter to index_message
     index_message += letter

# print output 
print(index_message)

# try 
# message: LETSGOTOTHESHOW
# key: TICKET
# cipher text should be E M V C K H M W V R I L A W Y

# message: THISISTHELASTTASKHOORDAY
# key: KNIGHTS