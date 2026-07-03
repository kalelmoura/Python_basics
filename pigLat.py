text = "My name is AL SWEIGART and I am 4,000 years old."

alt_text = text.split(' ')

consonants = "bcdfghjklmnpqrstvwxyz"

for i in range(len(alt_text)):
    word = alt_text[i]
    new_word = ""
    if word[0] in "1234567890":
        continue
    if word[0] in "aeiouy" or word[0] in "AEIOUY":
        alt_text[i] = alt_text[i] + "yay"
    elif len(word) >= 2 and word[0].lower() in consonants and word[1].lower() in consonants:
       for y in range(0, len(alt_text[i]) - 2):
           new_word = new_word + word[y+2]
       new_word = new_word + word[0] + word[1] + "ay"
       alt_text[i] = new_word
    elif word[0] in "qwrtpsdfghjklzxcvbnm" or word[0] in "QWRTPSDFGHJKLZXCVBNM":
        for x in range(0, len(alt_text[i]) - 1):
            new_word = new_word + word[x+1] 
        new_word = new_word + word[0] + "ay"
        alt_text[i] = new_word

text = ' '.join(alt_text)
print(text)
