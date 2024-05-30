The first task �

Write an algorithm that takes an array and moves all of
the zeros to the end, preserving the order of the other
elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0,
0]

The second task �

Create a func;on that takes positive integers diff, low,
high, and returns a list of all Pythagorean triples whose
smallest side a lies between low and high inclusive
(assume low <= high) and whose other sides sa;sfy c-b =
diff. The list should be in ascending order by a.

(1, 2, 10) -> [(3,4,5), (5,12,13), (7,24,25), (9,40,41)]
(3, 10, 25) -> [(15,36,39), (21,72,75)]
(4, 100, 100) -> [(100,1248,1252)]
(10, 91, 99) -> []

The random tests have diff <= 9,999 and low <= high <=
9,999,999.