Task 1: Thousands separators

Given a list with duplicate elements in it. Remove all duplicate elements from the
list.

Note:
• The order of remaining elements in the output should be the same as in the original list.

Example:
Input : [57, 94, 4, 4, 4, 41, 65, 94, 4, 99, 9, 9, 94]
Output : [57, 94, 4, 41, 65, 99, 9]
Տրվում է ցուցակ, որտեղ կան կրկնօրինակ տարրեր: Հեռացրեք բոլոր
կրկնօրինակ տարրերը ցանկից:

Նշում.
Արդյունքում մնացած տարրերի հերթականությունը պետք է լինի նույնը, ինչ սկզբնական
ցուցակում:
Օրինակ:
Input : [1, 2, 3, 20, 5, 3, 2]
Output : [1, 2, 3, 5, 20]

Task 2: Find Anagram

Write a function that takes two strings as its parameters. Your function should
return True if the strings are anagrams, and False otherwise.

Hint:
Two strings are anagrams if the second is a simple rearrangement of the first string
(containing the same characters: letters or numbers).

Note:
• Use the sort() method to sort both the strings.
• Check both strings to see if they form an anagram or not.
• If sorted arrays are equal, then the strings are anagram.

Example 1:
Input : str1 = " python"
str2 = " phtony"
Output : True
Example 2:
Input : str1 = " Java"
str2 = " apaJ"
Output : False
Example 3:
Input : str1 = " 1234"
str2 = " 2341"
Output : True
Գրեք ֆունկցիա, որը որպես պարամետր վերցնում է երկու տող: Ձեր ֆունկցիան
պետք է վերադարձնի True, եթե տողերը անագրամներ են, իսկ հակառակ
դեպքում՝ False:

Հուշում.
Երկու տողերը անագրամներ են, եթե երկրորդը առաջին տողի պարզ վերադասավորումն
է (պարունակում է նույն նիշերը՝ տառեր կամ թվեր)։

Նշում:
• Երկու տողերը տեսակավորելու համար օգտագործեք sort() մեթոդը
• Ստուգեք երկու տողերն էլ, թե արդյոք դրանք կազմում են անագրամ, թե ոչ:
• Եթե տեսակավորված զանգվածները հավասար են, ապա տողերը անագրամ են.
Օրինակ 1:
Input : str1 = " python"
str2 = " phtony"
Output : True
Օրինակ 2:
Input : str1 = " Java"
str2 = " apaJ"
Output : False
Օրինակ 3:
Input : str1 = " 1234"
str2 = " 2341"
Output : True