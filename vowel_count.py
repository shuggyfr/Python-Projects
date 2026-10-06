def vowel_check():
    sentence = input("write a random sentence ").lower()
    number_of_vowels = 0
    for letters in sentence:
        if letters in "aeiou":
           number_of_vowels += 1
    print(number_of_vowels)

vowel_check()