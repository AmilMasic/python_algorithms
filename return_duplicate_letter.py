# Given a string, create a function that returns the first repeating character
# if such doesn't exist, return the null character

# my solution
# using a hashmap
def first_repeating_character(words):
    check_letters = {}
    for letter in words:
        if check_letters.get(letter):
            return letter
        else:
            check_letters[letter] = True
    return '\0'



# ***Video solutions ***
# Brute force is having two for loops

# sorting doesn't work since we need the first repeating character
# sorting could give back the char that was not the first one being repeated

# Hash table solution
# Exactly how I did it
# it's O(n) time and space complexity
# def first_repeating_character(words):


print(first_repeating_character("asdsagvbb"))
