from Task2_encode_decode import *


def rep_dec_enc():
    print("Choose what you want to do:Encode or Decode? ")
    answer = input("Type 1 or 2: ")
    if answer == "1":
        word = input("Please input a string: ")
        print(f"The answer is: {en_code1(word)}")  # or en_code
    else:
        while True:
            bin_type = input("Please input a binary code(it can contain only 0 or 1): ")
            if de_code_input(bin_type) == True:
                break
        print(f"The answer is: {de_code2(bin_type)}")  # or de_code


rep_dec_enc()