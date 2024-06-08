Write a function that masks the input numbers with asterisks (*) and displays only
the last 4 digits.

Note:
• Find the last four digits and place them in result as they are.
• For the rest of the numbers, you can put * or X.

Example 1:
Input : 1234 5678 1234 5678
Output : **** **** **** 5678

Example 2:
Input : 52310259
Output : XXXX0259

Առաջադրանք 1: Թվերի քողարկում

Գրեք ֆունկցիա, որը քողարկում է մուտքագրված թվերը աստղանիշներով (*) եւ
ցուցադրում է միայն վերջին 4 նիշերը:

Նշում.
• Գտեք վերջին չորս թվերը եւ տեղադրեք դրանք արդյունքի մեջ այնպես, ինչպես կան:
• Մնացած թվերի համար կարող եք դնել * կամ X նշանը։

Օրինակ 1:
Մուտքագրում: 1234 5678 1234 5678
Արդյունքը: **** **** **** 5678
Օրինակ 2:
Մուտքագրում: 52310259
Արդյունքը: XXXX0259

Task 2: Password Generator

Write a function to generate random passwords of a specified length (set to 6 by
default).

Hint:
• If no length is specified by the user, the password will have 8 characters.
• The password must contain uppercase and lowercase letters, numbers and symbols
(!@#$%^&*()_+=-).

Note
• Use the string() and random() methods to generate the password.

Example 1:
# password length 6 (default)
Input : Enter the password length:
Output : The password is: IaT-h1
Example 2:
# password length 12
Input Enter the password length: 12
Output : The password is: 98hK;'|^Q91U

Առաջադրանք 2: Գաղտնաբառի գեներատոր

Գրեք ֆունկցիա, որը ստեղծում է որոշակի երկարության (լռելյայն սահմանված
լինի 6) պատահական գաղտնաբառեր:

Հուշում.
• Եթե օգտագործողի կողմից երկարություն նշված չէ, գաղտնաբառը պետք է ունենա 6
նիշ:
• Գաղտնաբառը պետք է պարունակի մեծատառեր, փոքրատառեր, թվեր եւ սիմվոլներ
(!@#$%^&*()_+=-)։

Նշում.
• Գաղտնաբառը ստեղծելու համար օգտագործեք string() եւ random() մեթոդները

Օրինակ 1:
# password length 6 (default)
Մուտքագրում: Enter the password length:
Արդյունքը: The password is: IaT-h1
Օրինակ 2:
# password length 12
Մուտքագրում: Enter the password length: 12
Արդյունքը: The password is: 98hK;'|^Q91U