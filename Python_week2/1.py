# login successfully

# if username and password is correct then login successfully otherwise login failed
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "password":
    print("Login successful!")
else:
    print("Login failed!")