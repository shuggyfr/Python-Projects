def is_valid_ip(s):
    parts = s.split(".")

    if len(parts) != 4:                 
        return False

    for part in parts:
        if part.isdigit()==False :             
            return False
        if int(part) > 255:             
            return False

    return True              

print(is_valid_ip("172.10.23.23.123"))

# new way to reason problems - check if the requirements are false, if they are not false then the ip or case is True 