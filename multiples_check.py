def multiples_check():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} - FizzBuzz")
        elif i % 3 == 0:
            print(f"{i} - Fizz")
        elif i % 5 == 0:
            print(f"{i} - Buzz")
        else:
            print(i)
multiples_check()

# put the most specific conditions first.
# in this case if ( if i % 3 == 0 and i % 5 == 0:) is placed last like the question , it is never reached because it is beaten by the first two conditions because the FizzBuzz numbers are  also multiples of 3 and 5 individually