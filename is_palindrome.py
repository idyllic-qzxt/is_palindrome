def is_palindrome(user_input):
    if user_input[::-1] == user_input:
        print(user_input + user_input[::-1])
        message = f"{user_input} is a palindrome."
        return message
    else:
        print(user_input+ user_input[::-1])
        message = f"{user_input} is not a palindrome."
        return message


def test():
    pass


def main():
    test()
    valid_flag = 0
    while valid_flag == 0:
        user_input = input("Enter your string: ")
        if user_input.isalpha():
            print(is_palindrome(user_input))
            valid_flag = 1
        else:
            print("Enter a palindrome in string.")
            continue


if __name__ == "__main__":
    main()
