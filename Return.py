'''
IMPORTING all necessary packages
'''
import List as l
import date as dt
def returnB(): # Declaring Function
    name=input("Borrower Name: ") # Taking input from user
    a="Borrow-"+name+".txt" # Getting borrower bill after thr name is inserted
    try: # Using Try statement
        with open(a,"r") as f: # Open and read the file 
            lines=f.readlines()
            lines=[a.strip("$") for a in lines]
    
        with open(a,"r") as f: # Open and read the file
            data=f.read()
            print(data)
    except: # using Except staement
        print("ERROR!! Status: Incorrect Name")
        returnB()

    b="Return-"+name+".txt" # creating return bill
    with open(b,"w+")as f: # open and read $ write the file
        f.write("                Library Management System \n")
        f.write("                   Returned By: "+ name+"\n")
        f.write("    Date: " + dt.getDate()+"    Time:"+ dt.getTime()+"\n\n")
        f.write("S.N.\t\tBookname\t\tCost\n")


    total=0.0
    for i in range(3): # Using loop statemtent 
        if l.bookname[i] in data:
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t"+l.bookname[i]+"\t\t$"+l.cost[i]+"\n")
                l.quantity[i]=int(l.quantity[i])+1
            total+=float(l.cost[i])
            
    print("\t\t\t\t\t\t\t"+"$"+str(total))
    print("Is the book return date expired?")
    print("Press 'Y' for Yes and 'N' for No: ")
    stat=input() 
    if(stat.upper()=="Y"): # Conditon to check if the choice is in uppercase letter
        print("By how many days was the book returned late?: ") 
        day=int(input())
        fine=2*day # Adding fine to the total if the days are late
        with open(b,"a")as f: 
            f.write("\t\t\t\t\tFine: $"+ str(fine)+"\n")
        total=total+fine
    
    
    print("\nSUCCESS. Your Book has been returned successfuly to our library. \nPlease pay your Total Amount in the counter.\n ")
    print("Total Amount: "+ "$"+str(total))
    print("*" * 20)
    with open(b,"a")as f: # open and read the file after appending
        f.write("\t\t\t\t\tTotal: $"+ str(total))
    
        
    with open("Stock.txt","w+") as f: # open and read and write the file after appending
            for i in range(3): # Using loop statement
                f.write(l.bookname[i]+","+l.authorname[i]+","+str(l.quantity[i])+","+"$"+l.cost[i]+"\n")
