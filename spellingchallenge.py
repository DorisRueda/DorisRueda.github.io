#store the data
words = ["color", "color", "colour", "amok", "amok", "amuck", "adviser", "adviser", "advisor", "adviser", "pepper"]

canonical_spellings = ["color", "amuck", "adviser", "pepper"]

mappings = {"colour": "color", "amok": "amuck", "advisor": "adviser"}

#make an empty list

new_list = []

#loop over the list of words

for word in words:
    if word is mappings:
        #if a word is mispelled do something
        #correct the canonical_spellings using the mappings dictionary
        correct_word = mappings[word]
        #add the correct word
        new_list.append(corrected_word)

    else:
        #if a a word is correct do something else
        new_list.append(word)
print(new_list)
