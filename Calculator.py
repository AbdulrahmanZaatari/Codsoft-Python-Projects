def summ(x,y):
    return x+y
def multiply(x,y):
    return x*y
def division(x,y):
    if (y==0):
        print("The denominator should not be zero")
        return None
    return x/y
def subtract(x,y):
    return x-y
def menu():
    print ("Here is the menu:\n 1-Add \n 2-Subtract \n 3-Multiply \n 4-Divide \n 5-Exit")
def displayMenu():
    name = input ("Please enter your name: ")
    print ("Hello " + name + "!\n")
    flag = True
    while flag == True:
        print("Please choose from the list below (you can enter either the number or the symbol (+,-,*,/)):\n")
        menu()
        choose = input()
        if choose == '1' or choose == '+':
            x = float(input("Enter the first number to add:\n"))
            y = float(input("Enter the second number to add:\n"))
            print ("Here is the sum: " + str(summ(x,y)) + "\n")

        elif choose == '2' or choose == '-':
            x = float(input("Enter the first number to subtract:\n"))
            y = float(input("Enter the second number to subtract:\n"))
            print ("Here is the difference: " + str(subtract(x,y))+ "\n")

        elif choose == '3' or choose == '*':
            x = float(input("Enter the first number to multiply:\n"))
            y = float(input("Enter the second number to multiply:\n"))
            print ("Here is the product: " + str(multiply(x,y))+ "\n")

        elif choose == '4' or choose == '/':
            x = float(input("Enter the first number to divide:\n"))
            y = float(input("Enter the second number to divide:\n"))
            print ("Here is the division's result: " + str(division(x,y)) + "\n")
        elif choose == '5':
            print("Calculator exitted sucessfully!")
            flag = False;
        else:
            print("Wrong choice, try again!")
def main():
    displayMenu()
main()
        
        
        
    
    
