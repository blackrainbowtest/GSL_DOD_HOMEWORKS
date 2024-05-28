Task1:
Your challenge is to enable "gambling for the elderly" (aka Bingo), and you'll achieve it like this:
1. Randomly generate a series of number between 0 and 90.
2. Allocate each number to a place in a 2D list.
3. The numbers should be in numerical order, left to right.
4. Numbers should not be repeated.
5. The center square should not contain a number. It should contain the word 'BINGO!'.
6. When the program is run, the bingo card should be displayed on screen.
Hints:
 Try using a 2D list with each sublist as a row.
 Randomly generate the numbers and append each to a list as you do.
 Use .sort() to put the list of numbers in order before adding to the card.


Your video game inventory system should:
1. Have a menu that allows the user to:
i. Add
ii. View
iii. Remove
2. Adding an item saves it to a file using captalize mode. Duplicates are allowed.
3. Removing an item deletes it from the file.
4. View is trickier. It should output the name of the item and tell you how many of those items you have.
Hint:
 Use the count() function when viewing an item.