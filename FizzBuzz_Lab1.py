#########LAB 1 Intro to Python #########
#######FizzBuzz #######
string = " "
for count in range(1,101):
    if count % 3 == 0 and count % 5 == 0:
        string = string + "FizzBuzz "
    elif count % 3 == 0:
        string = string + "Fizz "
    elif count % 5 == 0:
        string = string + "Buzz "
    else:
        string = string + str(count) + " "
print (string)
