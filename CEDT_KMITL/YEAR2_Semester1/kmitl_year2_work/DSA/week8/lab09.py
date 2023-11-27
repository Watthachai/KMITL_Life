def isPalindrome(str):
    if len(str) < 2:
        return True
    elif str[0] != str[-1]:
        return False
    else:
        return isPalindrome(str[1:-1])


print(isPalindrome("abcdcba"))
print(isPalindrome("atoyota"))
print(isPalindrome("kmitl"))
print(isPalindrome("manassanan"))
print(isPalindrome("programming"))
print(isPalindrome("fundamental"))
print("\n")


def isAscending(list_of_integer):
    if len(list_of_integer) < 2:
        return True
    elif list_of_integer[0] > list_of_integer[1]:
        return False
    else:
        return isAscending(list_of_integer[1:])


print("@@@@@ 2222 @@@@@")
print(isAscending([1, 2, 3, 4, 5, 6, 7]))
print(isAscending([3, 4, 2, 5, 6, 1, 2]))
print(isAscending([9, 8, 7, 6, 5, 4]))
print(isAscending([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
print(isAscending([6, 7, 8, 9, 10, 11, 12]))
print(isAscending([6, 3, 8, 7, 9, 2, 3, 1, 5]))


def group_of_no_1(island_list, point_no):

    count = 0

    left_index = point_no
    while left_index >= 0 and island_list[left_index] == 1:
        count += 1
        left_index -= 1

    right_index = point_no + 1
    while right_index < len(island_list) and island_list[right_index] == 1:
        count += 1
        right_index += 1

    return count


island_list = [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]
island_list2 = [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
island_list3 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

point_no = 1
print(group_of_no_1(island_list, point_no))
point_no = 5
print(group_of_no_1(island_list, point_no))
point_no = 4
print(group_of_no_1(island_list2, point_no))
point_no = 10
print(group_of_no_1(island_list2, point_no))
point_no = 1
print(group_of_no_1(island_list2, point_no))
point_no = 7
print(group_of_no_1(island_list3, point_no))


def valid_parentheses(str):
    # Base case
    if str == "":
        return True

    open_paren = str.find("(")
    if open_paren == -1:
        return False

    close_paren = str.find(")", open_paren)
    if close_paren == -1:
        return False

    return valid_parentheses(str[:open_paren] + str[open_paren + 1:close_paren] + str[close_paren + 1:])


print("@@@@@ 4444 @@@@@")
print(valid_parentheses("(()()(())())"))
print(valid_parentheses("((()()"))
print(valid_parentheses("())()()("))
print(valid_parentheses("(((()))((())))"))
print(valid_parentheses("()()(((())))"))
print(valid_parentheses("()"))

print("test")
print(valid_parentheses("(()()(()))"))
print(valid_parentheses("((()()()(()))"))
