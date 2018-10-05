#jacob jensen
#10/3/18

def int_input(num1, num2):
    var_value = input(message)
    if var_value.isdigit():
        var_value=int(var_value)
        return var_value
    else:
        display_output("that wasn't a number")
        get_int_input(message)

def add_num(num1, num2):
    sum_plus = num1+num2
    return sum_plus

def subtract_num(num1, num2):
    difference = num2 - num1
    return difference
def divide(num1, num2):
    division = num1 / num2
    return division
def multiply(num1 ,num2):
    multiplication = num1*num2
    return multiplication
#def output():
    

def get_input():
    choice = 0
    while choice == 0:
        print("what would you like to do with the numbers +, -, *,or /")
        choice = input("what would you like to do with the numbers +, -, *,or /")
        if choice == +:
            add = add_num()
            choice = 0

        elif choice == -:
            subtract = subtract_num()
            choice = 0

        
     
def check_math():
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num2 / num1)
    elif operator == "%":
        print(num1 % num2)
def main():
    num1 = get_int_input("please enter a number:")
    num2 = get_int_input("please enter a number")
    operator = get_input("what is your operation enter + - * / or % only")
    if operator == "+":
        test_value = add(num1, num2)
    elif operator == "-":
        test_value = subtract(num1,num2)
    elif operator == "*":
        test_value = multiply(num1,num2)
    elif operator == "/":
        test_value = divide(num1,num2)
    elif operator == "%":
        test_value = remander(num1,num2)
    else:
        display_output("this is not a valid operation")
        main()
    if check_math(test_valu, opeator, num1, num2):
        display_output("after a second check the corect answer is " +str(test_value))
    else:
        display_output("something in the calculation was wrong try it one more time")
        main()

main()

    
