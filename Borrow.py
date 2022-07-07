'''
IMPORTING all necessary packages
'''
import date as dt
import List as l

def borrowB(): # Declaring Function
    borr = False

    while(True): # Using while function if True
        firstName = input("First Name: ")
        if firstName.isalpha():
            break
        print("Please input alphabet from A-Z") # Using print statement

    while(True):
        lastName = input("Last Name: ")
        if lastName.isalpha(): # Using isplpha to returns True if all the characters are alphabet letters (a-z).
            break
        print("please input alphabet from A-Z")

    t = "Borrow-"+firstName+".txt" 

    with open(t,"w+") as f: # Using open function to read as well as write
        f.write("\t\t  Library Management System  \n\n") 
        f.write("\tBorrowed By: "+ firstName+" "+lastName+"\n")
        f.write("\tDate: " + dt.getDate()+"    Time:"+ dt.getTime()+"\n\n")
        f.write("S.N. \tBookname \t   Authorname  \t\tCost\n" )

    while borr == False: # Setting borr boolean value to False
        print("\nPlease select a option below:\n")
        for i in range(len(l.bookname)): # Using loop statement
            print("Press", i, "to borrow book,", l.bookname[i])

        total = 0.0 # Setting total to 0 while declaring
        try:   # Using Try statement
            a=int(input()) 
            try:
                if(int(l.quantity[a])>0): # Checking if the quantity of the book is availabe or not
                    print("\nSUCCESS - Status: Book Borrowed Successfuly\n")
                    with open(t,"a") as f:
                        f.write("1. \t"+ l.bookname[a]+"\t   "+l.authorname[a]+"\t\t "+l.cost[a]+"\n")

                    l.quantity[a]=int(l.quantity[a])-1
                    with open("Stock.txt","w+") as f:
                        for i in range(3):
                            f.write(l.bookname[i]+","+l.authorname[i]+","+str(l.quantity[i])+","+"$"+l.cost[i]+"\n")

                    total += float(l.cost[a])

                    '''
                    Code for multiple book borrowing
                    '''
                    loop=True # Setting loop boolean value to True 
                    count=1
                    while loop==True:
                        choice=str(input("Do you want to borrow more books?\nPress 'y' for yes and 'n' for no.: "))
                        if(choice.upper()=="Y"): # Conditon to check if the choice is in uppercase letter
                            count=count+1
                            print("Please select an option below:")
                            for i in range(len(l.bookname)):
                                print("Press: ", i, " to borrow book", l.bookname[i])
                            a=int(input())

                            with open(t, "r") as f: # open and read the file
                                r = f.read()
                            
                            if l.bookname[a] in r:
                                print("ERROR!! Cant borrow same book twice")
                                continue

                            if(int(l.quantity[a])>0):
                                print("SUCCESS - Status: Book Borrowed Successfuly\n")
                                with open(t,"a") as f: # Open and write the file after appending
                                    f.write(str(count) +". \t"+ l.bookname[a]+"\t   "+l.authorname[a]+"\t\t"+l.cost[a]+"\n")

                                total += float(l.cost[a])

                                l.quantity[a]=int(l.quantity[a])-1
                                with open("Stock.txt","w+") as f: # open and read and write the file 
                                    for i in range(3):
                                        f.write(l.bookname[i]+","+l.authorname[i]+","+str(l.quantity[i])+","+"$"+l.cost[i]+"\n")
                                        borr=False
                            else:
                                loop=False
                                break
                        elif (choice.upper()=="N"): # Conditon to check if the choice is in lowercase letter
                            print("\nTotal: " + str(total), "\n")
                            with open(t,"a") as f: # open and read the file after appending
                                f.write("\n\t\t\t\t\t\t   Total: " + str(total))
                            print ("Thank you for borrowing books from our Library. ")
                            print("")
                            loop=False
                            borr=True
                            print("*" * 80)
                            print("This is the bill for your borrowed book from our library")
                            print("")
                            with open(t, 'r') as f: # open function to display the bill to the borrower
	                            bill_display = f.read()
	                            print(bill_display)
                        else: 
                            print("Please choose as instructed") # Print statement after non of the condition are met
                        
                else:
                    print("Book is not available")  # Print statement after non of the condition are met
                    borrowB()
                    borr=False
            except IndexError: # Using except statement
                print("")
                print("Please choose book acording to their number.")
        except ValueError: # Using except statement
            print("")
            print("Please choose as suggested.")
