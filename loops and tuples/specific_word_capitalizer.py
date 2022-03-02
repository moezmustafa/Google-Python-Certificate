# def highlight_word(sentence, word):
#     new_string = ""
#     new_string = sentence.split()
#     final= ""
#     for index in new_string:
#         if index == word:
#             word = word.upper()
#             final = sentence.replace(index, word)
#     return(final)

# print(highlight_word("Have a nice day", "nice"))
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# print(highlight_word("Automating with Python is fun", "fun"))



def highlight_word(sentence, word):
    new_string = ""
    new_string = sentence.replace("!", "")
    new_string = new_string.split()
    final= ""
    for index in new_string:
        if index == word:
            print(index)
            word = word.upper()
            final = sentence.replace(index, word)
    return(final)


print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


#there is an error in the code below
#  the output works when the input word only has letters in it it stops and posts a null outpput if the desired
#  word has any symbols in it

