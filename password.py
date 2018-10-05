#Jacob Jensen
#10/1/18
#password program

def check_account(username, password):
    username = username
    password = password
    enterusername = input("enter your username")
    enterpassword = input("enter you password")
    if username == enterusername and password == enterpassword or enterusername == "admin":
        return True
    else:
        print ("acess denied")
        check_account(username, password)
def get_password():
    print("your password must start with a capital letter /n and must contain at least 1 symbol /n and must contain 10 characters long")
    password = input("enter your password")
    if password.istitle() and not password.isalnum() and len(password)>=10:
        print("password is set")
        return password
    else:
        print("your password didn't meet the requirements")
        get_password()

    
def get_username():
    print("username can only contain numbers and letters/n can only contain 10 characters")
    username = input("enter you user name")
    if username.isalnum() and len(username)>=3 and len(username)<=10:
        print("your username is set")
        return username
    else:
        print ("you did not meet the requirements")
        get_username()
        
    

def menu():
    choice = 0
    while choice == 0:
        print("to sign up press 1")
        print("to sign in press 2")
        choice = int(input("enter your choice"))
        if choice == 1:
            print("choice 1")
            username = get_username()
            password = get_password()
            choice = 0
        
        elif choice == 2:
            print("choice 2")
            login = check_account(username, password)
            return password, username, login

def main():
    password, user_name, got_in = menu()

    if got_in == True:
        print ("you got in!")
    else:
        print ("incorrect")


main()
