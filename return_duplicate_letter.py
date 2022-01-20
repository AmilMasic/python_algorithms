# Given a string, create a function that returns the first repeating character
# if such doesn't exist, return the null character

# my solution 
def first_repeating_character(words):
    check_letters = {}
    for letter in words:
        if check_letters.get(letter):
            return letter
        else:
            check_letters[letter] = True
    return '\0'


print(first_repeating_character("asdsagvbb"))
