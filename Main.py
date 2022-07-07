'''
IMPORTING all necessary packages
'''
import Return as r
import List as l
import date as dt
import Borrow as b


def main(): # Declaring Function
    while(True): # Using while statement
        print("\t", "-" * 60)
        print("\t\t   Welcome to the library management system     ") # Using print statement
        print("\t", "-" * 60)
        print("Press 1. Display Stocks of Books in Library\n")
        print("Press 2. To Borrow a book from Library\n")
        print("Press 3. To return a book from Library\n")
        print("Press 4. EXIT\n")

        try: # Using try statement
            a = int(input("Select from '1 - 4': ")) # Taking input from the user for different option
            print()

            if(a == 1): # If condition
                l.list() # Calling list
                print('+'+'-'* 80+'+')
                print(f'| {"S.N.":<5} | {"Book Name":<25} | {"Author Name":<20} | {"Quantity":<10} |  Price |') # Creating Heading
                print('+'+'-'* 80+'+')
                for i in range(len(l.bookname)):
                    print(f'| {str(i+1)+".":<5} | {l.bookname[i]:<25} | {l.authorname[i]:<20} | {l.quantity[i]:<10} |  {"$"+l.cost[i]:5} |') 
                print('+'+'-'* 80+'+')

            elif (a < 0): # Else If condition
                print("ERROR!! Negative Values aren't valid to select.")

            elif(a == 2):
                l.list()
                b.borrowB()

            elif(a == 3):
                l.list()
                r.returnB()

            elif(a == 4):
                print("\t", "-" * 60)
                print("\t\t   Thank you for using library management system")
                print("\t", "-" * 60)
                break

            else: # Using else if any of the condition do not match
                print("ERROR!! Please enter a valid choice from 1-4")
        except ValueError: # Using except statement
            print("Error!! Please input the asked values only")


main()
