1. Create a string made of the first, middle and last character

Write a program to create a new string made of an input string’s first, middle, and last
character with upper letters
Hints of steps:
➢ String index always starts with 0
➢ Use string indexing to get the character present at the given index.
➢ Get the index of the middle character by dividing string length by 2
➢ Use upper method for characters
➢ Print new string

Given:
str1 = &quot;Euphoria&quot;
Expected Output:
EOA


2. Calculate number of days between two given dates

Write a program that compares the dates, computes the difference in days, and handle any
formatting errors.

Hints for steps.
➢ Prompt the user to enter two dates and times
➢ Define the date format ( date_format = &quot;%Y-%m-%d %H:%M:%S&quot;)
➢ Convert the input strings to datetime objects
➢ Compare the datetime objects and calculate the difference
➢ Print the difference in days
For try, except block
1. Pars Input Strings: (The datetime.strptime() function to convert the input strings to
datetime objects.)
2. The subtraction of two datetime objects yields a timedelta object.
3. Error Handling: Use try block to catch ValueError exceptions if the input strings are
not in the correct format.
Given:
&gt; Enter the first date and time (YYYY-MM-DD HH:MM:SS): 2021-05-05 22:10:22
&gt; Enter the second date and time (YYYY-MM-DD HH:MM:SS): 2024-01-03 23:01:01

Expected Output:
&gt; Difference is 973 days