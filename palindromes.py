def is_palindrome(text):
    cleaned = ""
    for char in text:
        if char.isalnum():                      # is this character a letter or digit?
            cleaned += char.lower()           # add it, lowercased

    reversed_text = ""
    for i in range(len(cleaned)-1, -1, -1): # walk backwards through cleaned
        reversed_text += cleaned[i]         # add the character at index i

    return reversed_text == cleaned

print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("hello"))  
