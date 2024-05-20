from collections import Counter


# Pangram words does not contain symbols
def is_pangram(word):
    text = word.lower().replace(' ', '')  # remove all spaces
    letters_counts = Counter(text)  # count each letter
    return len(letters_counts) == 26


print(is_pangram('Jackdaws love my big sphinx of quartz'))
print(is_pangram('The jay pig fox zebra and my wolves quack'))
print(is_pangram('Hello world'))
