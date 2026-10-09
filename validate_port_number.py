def validate_port_number():

    # catch the user input
    # check against valid port number rule 
    # keeps checking until a valid one is given
    
    while True:
        try:
            port_number = int(input("enter port number "))
            

        except ValueError:
            print("not a number")

            continue

        if 1 <= port_number <= 65535:
            print("valid port number")
            return port_number

        else:
            print("port number is not in range")

validate_port_number()
            
# the while True keeps the loop running until the conditon is met and the try and except block allows for the program to continue even in the case of a value error 