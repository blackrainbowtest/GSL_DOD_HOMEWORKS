# vahram
def right_rotate(lst, n):
    if n == 0:
        return lst
    else:
        # lst[n:] return from n to end when we send -1 its return from last variable to end => just return last variable
        # lst[:n] return from start to n element (not contains n = -1 last element)
        return lst[n:] + lst[:n]


def create():
    lst = [int(item) for item in input("Enter the list items : ").split()]

    print(right_rotate(lst, -1))
    # print(right_rotate(lst1, 1))
    # print(right_rotate(lst1, 2))
    # print(right_rotate(lst1, 0))


create()

# ====================================================================================
# derenik

nums = "1 2 3 4 5 5"

# version 1
def move_nums1(numstr):
    num_list = numstr.split(" ")
    last = num_list[-1]
    for i in range(len(num_list)-1, 0, -1):
        num_list[i] = num_list[i-1]
    num_list[0] = last
    return num_list


# version 2
def move_nums2(numstr):
    num_list = numstr.split(" ")
    first = num_list[0]
    last = num_list[-1]
    for i in range(len(num_list)-1):
        num_list[i] = num_list[i+1]
    num_list.remove(num_list[-1])
    num_list.remove(num_list[-1])
    num_list.insert(0, first)
    num_list.insert(0, last)
    return num_list

# version 3 (without loop)
def move_nums3(numstr):
    num_list = numstr.split(" ")
    last = num_list[-1]
    num_list.remove(num_list[-1])
    num_list.insert(0, last)
    return num_list

print(move_nums1(nums))
print(move_nums2(nums))
print(move_nums3(nums))

# ===============================================================
# roza


def cyclic_right(numbers):
    # Convert the input string to a list of integers
    num_list = [int(num) for num in numbers.split()]

    # Perform the cyclic shift
    if num_list:
        last_element = num_list.pop()
        num_list.insert(0, last_element)

    # Convert the list back to a string of space separated numbers
    shifted_numbers = ' '.join(map(str, num_list))

    return shifted_numbers


# Ask user
input_string = input("Enter a string of space separated natural numbers: ")

# Perform the cyclic shift
output_string = cyclic_right(input_string)

# Result
print(output_string)



# =============================================== TASK 2  ========================================
# vahram

def create_numbers(nums):
    for i in range(len(nums)):
        n = nums[i]
        for j in range(len(nums)):
            if i != j:
                item = nums[i] // nums[j]
                if item & 1:
                    return True
        return False


def create():
    dt0 = [9000, 3000, 300, 990]
    dt1 = [3, 33, 17, 35, 999]
    dt2 = [4, 89, 4, 77, 4, 16]
    dt3 = [5, 1, 999, 87, 33, 325, 999]
    dt4 = [5, 2, 87, 33, 325, 999]

    print(create_numbers(dt1))  # Output: False
    print(create_numbers(dt2))  # Output: True
    print(create_numbers(dt3))  # Output: True


create()
