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
    elif text_input[i] == "&":
        text_output += "e"
# if # then change i
    elif text_input[i] == "#":
        text_output += "i"
# if + then change o
    elif text_input[i] == "+":
        text_output += "o"
# if ! then change u
    elif text_input[i] == "!":
        text_output += "u"
    else:
        text_output += text_input[i]
# print output
print(text_output)
# try
#th& q!#ck br+wn f+x j!mps +v&r th& l*zy d+g.