string = str(input("Enter a word: "))

def IfPalindrome(string):
    string = string.lower()
    string = string.replace(" ", "")
    characters = "!\"£$%^&*()-=_+[]{}/?.,<>';:@#~¬`"
    for chars in characters:
        for character in string:
            if chars == character:
                string = string.replace(character, "")
    if string[::-1] == string:
        return "Palindrome"
    else:
        return "Not Palindrome"
    
print(IfPalindrome(string))