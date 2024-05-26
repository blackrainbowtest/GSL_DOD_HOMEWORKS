The First Task:

The program receives a string of natural numbers as input. From the
elements of the string, a list of numbers is formed. Write a program to
perform a cyclic shi; of the elements of the list to the right, where the
last element becomes the first, and the rest are shi;ed one posi>on
forward, increasing their indices.
Input Format:
A string of space-separated natural numbers is provided as input to the
program.
Output Format:
The program should output the elements of the modified list with a
cyclic shi;, separa>ng its elements with a single space.
Sample Input 1:
1 2 3 4 5

Sample Output 1:
5 1 2 3 4

Sample Input 2:
6 6 6 6 6 6 6

Sample Output 2:
6 6 6 6 6 6 6

Sample Input 3:
5 4 3 2 1

Sample Output 3:
1 5 4 3 2


The Second Task:

Write a program to determine if a number is the product of two
numbers from a given set. The program should output the result as
"YES" or "NO".

Input Format:
The first line contains a natural number n (0 < n < 1000) – the number
of numbers in the set. The next n lines contain integers that make up
the set (they can be repeated). Then an integer follows, which either is
or is not the product of two dis>nct numbers from the set.
Output Format:
The program should output "YES" or "NO" according to the problem's
condi>on.

Note 1: A number from the set cannot be mul>plied by itself. In other
words, the two factors must have different indices in the set.
Note 2: To solve the problem, use nested loops.

Sample Input 1:
3
33
17
35
999

Sample Output 1:

NO

Sample Input 2:
4
89
4
77
4
16

Sample Output 2:
YES

Sample Input 3:
5
1
999
87
33
325
999

Sample Output 3:
YES
