# problem1
# 1st version
def en_code(word):
    bin_word = []
    for item in word:
        bin_word.append("{:08b}".format(ord(item)))
    result = "".join(bin_word)
    return result


# 2nd version
def en_code1(word):
    return "".join("{:08b}".format(ord(item)) for item in word)

# problem 2
# 1st version


def de_code_input(bin_type):
    if len(bin_type) % 8 != 0:
        return False
    for item in bin_type:
        if item not in ("0", "1"):
            return False
    return True


def de_code(bin_type):
    stack_num = []
    word = []
    new_bin_type = [item for item in bin_type]
    while len(new_bin_type) > 0:
        while len(stack_num) < 8:
            stack_num.append(new_bin_type.pop(0))
        word.append(chr(int("".join(stack_num), 2)))
        stack_num.clear()
    return "".join(word)


# 2nd version
def de_code2(bin_type):
    return "".join([chr(int(item1, 2))for item1 in [bin_type[item:item+8] for item in range(0, len(bin_type), 8)]])

