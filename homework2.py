import re


def counter(text):

    vowelsPattern = r'[aeiou]'
    consonantsPattern = r'[bcdfghjklmnpqrstvwxyz]'

    vowelCount = len(re.findall(vowelsPattern, text.lower()))
    consonantCount = len(re.findall(consonantsPattern, text.lower()))

    return vowelCount, consonantCount


user_input = input("Enter your string: ")
vowel, consonant = counter(user_input)

print(f"Vowels: {vowel}")
print(f"Consonant: {consonant}")