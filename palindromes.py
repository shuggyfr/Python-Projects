def is_palindrome(text):
    cleaned = ""
    for char in text:
        if char.isalnum():                      
            cleaned += char.lower()           # add it, lowercased

    reversed_text = ""
    for i in range(len(cleaned)-1, -1, -1): # walk backwards through cleaned
        reversed_text += cleaned[i]         # add the character at index i

    return reversed_text == cleaned

    #return cleaned == cleaned[::-1].       # shortcut to reverse the list and then compare against the original
                                            # return with the comparison operator gives true of false so no need for an if else statement that returns true or false         

print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("hello"))  
