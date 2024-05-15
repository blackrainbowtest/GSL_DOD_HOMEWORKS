nums = [0, 1, 3, 0, 2]
nums.sort(key=lambda num: num == 0)
print('day 1 task #1: ')
print(nums)


def findLargestSequence(strArray):
    if not isinstance(strArray, str):
        raise TypeError("Input must be a string")
    strArray = list(strArray)

    largestSequence = []  # Initialize the list to store the longest sequence of unique characters
    currentSequence = [strArray[0]]  # Start with the first letter of the string

    for i in range(1, len(strArray)):
        if not strArray[i] in currentSequence:
            # If the symbol is unique to the current sequence, add it
            currentSequence.append(strArray[i])
        else:
            # If the symbol is not unique, update largestSequence if currentSequence is longer
            if len(currentSequence) > len(largestSequence):
                largestSequence = currentSequence
            # Start a new sequence from the current character
            currentSequence = [strArray[i]]

    # Last check to update largestSequence if current sequence is longest
    if len(currentSequence) > len(largestSequence):
        largestSequence = currentSequence

    return largestSequence


s = "abcabcbb"
print('day 1 task #2: ')
print(findLargestSequence(s))