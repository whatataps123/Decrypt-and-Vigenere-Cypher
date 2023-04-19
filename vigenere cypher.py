#Joshua Lemuel Z. Centina BS CPE 1-4 Vigenere Cypher
# store the 26 letters of the alphabet in uppercase
eng_alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# ask for the user to input a message to be encrypted and save it
message_input = input("Enter a message: ")
index_message = []

# check message and convert to uppercase
for letter in message_input.upper():
    if letter.isalpha():
        index_m = eng_alphabets.index(letter)
        index_message.append(index_m)

# ask for the user to input a key for encryption and save it
key_input = input("Enter a key: ")
index_key = []

# check the key and convert to uppercase
for letter in key_input.upper():
        index_k = eng_alphabets.index(letter)
        index_key.append(index_k)

# convert letters to numbers
# initialize an empty list to store encrypted indices
# check the index
# convert numbers back to letters
# convert the list of encrypted back to letters
# print output 
