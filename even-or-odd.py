def num_check(num):
    #num = int(input("write a number "))
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")

num_check(2)
num_check(4)
num_check(6)
num_check(9999999999999999999999999999999999999999)