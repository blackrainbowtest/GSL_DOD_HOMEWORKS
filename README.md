With a tuple that user input, write a program to print the first half values in one line and the
last half values in one line.
Hints:
Use [n1:n2] notation to get a slice from a tuple.
Examples:
1.Input:
(10, 20, 30, 40, 50, 60)
Output:
First half values: (10, 20, 30)
Last half values: (40, 50, 60)
2.Input:
(1, 3, 5, 7, 9)
Output:
First half values: (1, 3)
Last half values: (5, 7, 9)

Given a non-negative integer num, implement a function that returns True if num is a Curzon
number, or False otherwise. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2
multiplied by num, then num is a Curzon number.
Examples։
Input: 5
Output: is_curzon(5) ➞ True
Explanation.
# 2 ** 5 + 1 = 33
# 2 * 5 + 1 = 11
# 33 is a multiple of 11
Input: 10
Output: is_curzon(10) ➞ False
Explanation.
# 2 ** 10 + 1 = 1025
# 2 * 10 + 1 = 21
# 1025 is not a multiple of 21
Input: 14
Output: is_curzon(14) ➞ True
Explanation.
# 2 ** 14 + 1 = 16385
# 2 * 14 + 1 = 29
# 16385 is a multiple of 29