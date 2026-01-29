words=["data","science"]
def new_dictionaries(list_of_words):
    new_dictionary={} #creating the empty dictionary
    for item in list_of_words:
        length_of_item = len(item) #length of word
        if length_of_item % 2 == 0: # checking for even/odd
            parity_of_item = "even"
        else:
            parity_of_item = "odd"
        new_dictionary[item]={"length":length_of_item,"parity":parity_of_item} #adds word and properties to dictionary

    print (new_dictionary)

new_dictionaries(words)