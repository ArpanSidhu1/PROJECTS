import pickle
def createaccount():
    f=open("hdfcbank.dat","ab")
    print("ENTER THE REQUIRED DETAILS")
    nm=input("Enter Your Name : ")
    an=int(input("Enter Your Account Number : "))
    im=int(input("Enter the Initial Amount : "))
    at=input("Enter Account Type - Saving  or Current : ")
    custd=[an,nm,im,at]
    pickle.dump(custd,f)
    f.close()
    print("********************** Account Created **********************")
def deposit():
    n=int(input("Enter Your Account Number : " ))
    k=int(input("Enter the Sum You Want to Deposit : "))
    f=open("hdfcbank.dat","rb")
    l=[]
    while True :
        try:
            record=pickle.load(f)
            if(record[0]==n):
                record[2]+=k
            l.append(record)
        except:
            print("\n\t\t\t\tAmount Deposited")
            f.close()
            break
    f=open("hdfcbank.dat","wb")
    for record in l:
        pickle.dump(record,f)  
def withdraw():
    f=open("hdfcbank.dat","rb")
    n=int(input("Enter Your Account Number : " ))
    k=int(input("Enter the Sum You Want to Withdraw : "))
    l=[]
    while True :
        try:
            record=pickle.load(f)
            if(record[0]==n):
                record[2]-=k
            l.append(record)                
        except:
            print("\n\t\t\t\tAmount WithDrawn")
            f.close()
            break
    f=open("hdfcbank.dat","wb")
    for record in l:
        pickle.dump(record,f)
def search():
    f=open("hdfcbank.dat","rb")
    print('''What Do You Want To Do:
             1) Search By Name
             2) Search By Account Number''')
    n=int(input("Enter Your Choice : "))
    if n==1:
        k=input("Enter the Name : ")
        while True:
            try:
                br=pickle.load(f)
                if(br[1]==k):
                    print("\n DETAILS \n")
                    print("Account No.  = ",br[0])
                    print("Name         = ",br[1])
                    print("Amount       = ₹",br[2])
                    print("Account Type = ",br[3])
            except:
                    print("")
                    f.close()
                    break
    elif n==2:
         k=int(input("Enter the Account Number : "))
         while True:
            try:
                br=pickle.load(f)
                if(br[0]==k):
                    print("\n DETAILS \n")
                    print("Account No.  = ",br[0])
                    print("Name         = ",br[1])
                    print("Amount       = ₹",br[2])
                    print("Account Type = ",br[3])
            except:
                    print("")
                    f.close()
                    break          
def checkbal():
    f=open("hdfcbank.dat","rb")
    n=int(input("Enter Your Account Number : " ))
    while True :
        try:
            br=pickle.load(f)
            if(br[0]==n):
                print("\n",br[1]," Sir, Your Current Balance is : ₹",br[2])
        except:
            print("")
            f.close()
            break
def display():
    print("\n|||||||||||||||||||||| ALL ACCOUNT DETAILS ||||||||||||||||||||||\n")
    f=open("hdfcbank.dat","rb")
    print("ACC. NUMBER\t | NAME\t                 | AMOUNT\t\t | ACCOUNT TYPE ")
    while True:
        try:
            brec=pickle.load(f)
            print(brec[0],"     \t |",brec[1],"\t\t | ₹",brec[2],"\t\t |",brec[3])
        except:
            print("\n")
            f.close()
            break
def delete():
    f=open("hdfcbank.dat","rb")
    k=int(input("Enter the Account Number : "))
    n=input("Enter the Name : ")
    l=[]
    while True:
        try:
            record=pickle.load(f)
            if(record[0]==k and record[1]==n):
                print("Account Deleted")    
        except:
             print("")
             f.close()
             break
#Function Ends Here        
while True:
    print("\n||||||||||||||||||Welcome to HDFC BANK||||||||||||||||||")
    print('''\nWhat Do You Want to do :
             1. Create a Account
             2. Deposit a Amount
             3. Withdraw The Amount
             4. Search a Account
             5. Check Balance
             6. Display All
             7. Delete Account
             8. Exit''')
    n=int(input("Enter Your Choice : "))
    if n==1:
        createaccount()
    elif n==2:
        deposit()
    elif n==3:
        withdraw()
    elif n==4:
        search()
    elif n==5:
        checkbal()
    elif n==6:
        display()
    elif n==7:
        delete()
    elif n==8:
        print("||||||||||||||||||Thanks For Visiting||||||||||||||||||")
        exit()
        
        


















