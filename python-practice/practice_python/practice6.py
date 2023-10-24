def program():
    user_string = input("Enter a word: ")
    user_string_reverse = user_string[::-1]
    if user_string == user_string_reverse:
        print("The string is a palindrome!")
    else:
        print("Not Palindrome.")
program()