# problem1
# 1st version
def en_code():
    word = input("Please input a string: ")
    bin_word = []
    for item in word:
        bin_word.append(bin(ord(item))[2:])
    result = "".join(bin_word)
    return result


print(en_code())


# 2nd version
def en_code1():
    word = input("Please input a string: ")
    return "".join([bin(ord(item))[2:] for item in word])


print(en_code1())
# problem 2
# 1st version


def de_code_input(bin_type):
    for item in bin_type:
        if item not in ("0", "1"):
            return False
    return True


def de_code():
    stack_num = []
    word = []
    while True:
        bin_type = input("Please input a binary code(it can contain only 0 or 1): ")
        if de_code_input(bin_type) == True:
            break
    new_bin_type = [item for item in bin_type]
    while len(new_bin_type) > 0:
        while len(stack_num) < 8:
            stack_num.append(new_bin_type.pop(0))
        word.append(chr(int("".join(stack_num), 2)))
        stack_num.clear()
    return "".join(word)


print(de_code())
# 2nd version


def de_code2():
    while True:
        bin_type = input("Please input a binary code(it can contain only 0 or 1): ")
        if de_code_input(bin_type) == True:
            break
    return "".join([chr(int(item1, 2))for item1 in [bin_type[item:item+8] for item in range(0, len(bin_type), 8)]])


print(de_code2())
