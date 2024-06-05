# Task 1: Number Masking

def is_balanced(parentheses):
    prnt_list = list(parentheses)
    stack_list = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    for prnt in prnt_list:
        if prnt in "([{":
            stack_list.append(prnt)
        elif prnt in ")]}":
            if len(stack_list) == 0 or not (brackets.get(stack_list[-1], None) == prnt):
                return False
            else:
                stack_list.pop()
    return True


print(is_balanced("(aaaa)aaaa[aaaa(aaaa)aaaa]aaaa{aaaa}aaaa"))
print(is_balanced("(aaaa)aaaa]aaaa[aaaa{aaaa}aaaa"))
