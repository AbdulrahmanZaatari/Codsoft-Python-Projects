import random
def crp(x):
    password = ""
    for i in range (x):
        password += chr(random.randint(33,126))
    return password
def main():
    name = input ("Please enter your name: ")
    print ("Hello " + name + "!\n")
    print ("Today we're going to create a powerful password for you!")
    length = int(input("Please enter the length of your password: \n"))
    last_password = crp(length)
    print("Here is your password: " + last_password + "\n")
    flag = True
    while flag == True:
        choice = input("Do you want to create another password (Yes or No)?")
        if choice == "Yes":
            length = int(input("Please enter the length of your password: \n"))
            last_password = crp(length)
            print("Here is your password: " + last_password + "\n")
        elif choice == "No":
            print("Last password created: " + last_password + "\n")
            print("System exitted successfully.")
            flag = False
        else:
            print("Choose Yes or No only!")
main()
        
