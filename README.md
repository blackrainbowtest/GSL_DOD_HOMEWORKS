The first task:
Magic Dates
A magic date is a date where the day multiplied by the month equals the number formed by the last two digits of the
year.
Write a function is_magic(date) that takes a string representation of a valid date as an argument and returns True if the
date is magic, and False otherwise.
The following code:
print(is_magic('10.06.1960'))
print(is_magic('11.06.1960'))
Should output:
True
False

The second task:
Pangrams
A pangram is a sentence that contains every letter of the alphabet. Pangrams are typically used to display fonts, so that
all glyphs can be viewed in a single phrase.
Write a function is_pangram(text) that takes a string of English text as an argument and returns True if the text is a
pangram and False otherwise.
Note 1: It is guaranteed that the input string contains only English letters and spaces.
Note 2: The following code:
print(is_pangram('Jackdaws love my big sphinx of quartz'))
print(is_pangram('The jay pig fox zebra and my wolves quack'))
print(is_pangram('Hello world'))
Should output:
True
True
False