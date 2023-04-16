# Joshua Lemuel Z. Centina BS CpE 1-4
# ask user to input encrypted text and save it
text_input = input("Enter a string to decrypt: ")
text_output = ""
# check every character
for i in range(len(text_input)):
# if * then change a
    if text_input[i] == "*":
        text_output += "a"
# if & then change e
# if # then change i
# if + then change o
# if ! then change u

    else:
        text_output += text_input[i]
# print output
print(text_output)