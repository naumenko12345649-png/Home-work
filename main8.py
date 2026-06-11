import string
a = input('text:')
punctuation_to_spaces = str.maketrans(string.punctuation, " " * len(string.punctuation))
clean_text = a.translate(punctuation_to_spaces)
hashtag = "#" + "".join(word.capitalize() for word in clean_text.split())
print(hashtag[:140])
