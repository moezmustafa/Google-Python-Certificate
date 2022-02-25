

def is_palindrome(string) :
    new_string = ""
    reversed_string = ""

    for char in string :
        if char != " " :
            new_string += char
            reversed_string = char + reversed_string
        if char == " " :
            new_string += " "
            reversed_string = " " + reversed_string

            new_string = new_string.replace(" ", "")
            new_string = new_string.lower()
            reversed_string = reversed_string.replace(" ", "")
            reversed_string = reversed_string.lower()
            


    print("Revrese string is : " + reversed_string)
    print("New string is : " + new_string)

    print("\n")


    if new_string == reversed_string :
        return True
    else :
        return False

print(is_palindrome("never odd or even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

