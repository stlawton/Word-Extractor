def first_word(string):  # Return the first word in a string
    index = 0
    word = ""
    while string[index] != " ":  # Run while loop until first space is encountered
        word += string[index]    # Add each character before the space to a new variable to extract the first word
        index += 1               # Increment the index
    return word

def second_word(string):         # Return the second word in a string
    index = 0
    while string[index] != " ":  # Increase the index until the first space
        index += 1
    word = ""
    index += 1                   # Move the index to the frist character after the first space
    while index < len(string):   # The while loop checks to see if the second word is the last word in the string
        if string[index] != " ":   # Check for a space after second word incase it is not the last word in the string
            word += string[index]
            index += 1
    return word

def last_word(string):          # Returns the last word in the string
    index = len(string) - 1     # Set the index to the last character of the string
    word = ""
    while string[index] != " ": # Move the index backwards until the first space is found
        index -= 1
    return string[index +1:]    # Return the string from the first character after the space to the end of the string
