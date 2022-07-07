def list(): # Declaring List function
    global bookname # Calling global variable
    global authorname
    global quantity
    global cost
    bookname=[] # Making empty list for storing variable
    authorname=[]
    quantity=[]
    cost=[]
    
    with open("stock.txt","r") as f: # Using Open fucntion to read the stock.txt
        
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)): # Using loop
            choice=0 # Appending all the values in list after the choice is met
            for x in lines[i].split(','):
                if(choice==0):
                    bookname.append(x)
                elif(choice==1):
                    authorname.append(x)
                elif(choice==2):
                    quantity.append(x)
                elif(choice==3):
                    cost.append(x.strip("$"))
                choice+=1