from collections import Counter

str1 = " python"
str2 = " phtony"
str3 = " Java"
str4 = " apaJ"
str5 = " 1234"
str6 = " 2341"


def is_anagram(word1, word2):
    letters_count_1 = Counter(word1)
    letters_count_2 = Counter(word2)
    return letters_count_1 == letters_count_2


print(is_anagram(str1, str2))
print(is_anagram(str3, str4))
print(is_anagram(str5, str6))
