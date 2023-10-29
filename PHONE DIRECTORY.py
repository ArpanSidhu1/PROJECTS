d={}
while True:
    print('''What do you Want to Do :
             1. Add a Contact
             2. Search a Contact
             3. Delete a Contact
             4. Modify a Contact
             5. Display a Contact
             6. Exit''')
    k=int(input("Enter Your Choice : "))
    if k==1:#ADDING A NUMBER
        k=input("Enter Name :")
        p=int(input("Enter Phone Number :"))
        a=input("Enter Address :")
        d[k]=[p,a]
        print("Contact Added")
    elif k==2:#SEARCHING
        print('''What do You Want To do:
                1. Search By Name
                2. Search By Phone Number
                3. Search By Address''')
        k=int(input("Enter Your Choice : "))
        if k==1:#SEARCH BY NAME
            n=input("Enter the Name you want to search : ")
            if n in d:
                print("Name       :",n)
                print("Contact No :",d[n][0])
                print("Address    :",d[n][1])
        elif k==2:# SEARCH BY NUMBER
            n=int(input("Enter the Number You want to search : "))
            for k in d:
                if(n==d[k][0]):
                    print("Name       :",k)
                    print("Contact No :",d[k][0])
                    print("Address    :",d[k][1])
        elif k==3:
            n=input("Enter the Address You want to search : ")
            for k in d:# SEARCH BY ADDRESS
                if(n==d[k][1]):
                    print("Name       :",k)
                    print("Contact No :",d[k][0])
                    print("Address    :",d[k][1])            
    elif k==3:#DELETE
        n=input("Enter the Name you want to delete : ")
        if n in d:
            print(" Record is Deleted")
            d.pop(n)
        else:
            print("Record Not Found")
    elif k==4:#MODIFY
        n=input("Enter the Name You want To Modify")
        for k in d:
            if(n==k):
                s=int(input("Enter New Phone Number :"))
                n=input("Enter New Address:")
                d[k]=[s,n]
    elif k==5:#DISPLAY
        print("LIST OF RECORDS")
        for p in d:
            print("\nName     :",p)
            print("Phone No :",d[p][0])
            print("Address  :",d[p][1])
    elif k==6:#EXIT
        print("Exiting...........")
        exit()
