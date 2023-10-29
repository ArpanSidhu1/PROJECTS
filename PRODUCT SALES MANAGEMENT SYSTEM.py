import time
pno=[ ]
pnm=[ ]
pcost=[ ]
cnm=[ ]    #TAKING USER CHOICE
while True:
    print('''\nWhat Do You want To do
            1. Add a Product
            2. Search a Product
            3. Modify Cost of the Product
            4. Delete a Product
            5. Dislay All Product
            6. Exit''')
    ch=int(input("Enter Your Choice : "))
    if ch==1:#ADDING A PRODUCT
        print("""*******************ADD PRODUCT MENU***************************""")
        PN=input("Enter Product Name : ")
        pnm.append(PN)

        NM=int(input("Enter Product No   : "))
        pno.append(NM)       

        C=int(input("Enter Product Cost : "))
        pcost.append(C)

        CN=input("Enter Company Name : ")
        cnm.append(CN)

        print("\n\nProduct Added")
    elif ch==2:#SEARCHING A PRODUCT
        print('''Enter the Type for Which you want to search the Product
               1. By Product Name
               2. By Product No
               3. By Product Cost''')
        ee=int(input("Enter Your Choice : "))
        if ee==1:#SEARCHING BY PRODUCT NAME
                  t=input("Enter Product Name : ")
                  flag=0
                  for i in pnm:
                      if(t==i):
                          flag=1
                          k=pnm.index(i)
                  if(flag==1):
                          print("\nProduct No   :",pno[k])
                          print("Product Name :",pnm[k])
                          print("Product Cost :",pcost[k])
                          print("Company Name :",cnm[k])
                  else:
                          print("We Don't Have Any Product After This Name")
        elif ee==2:#SEARCHING BY PRODUCT NUMBER
                   j=int(input("Enter Product No :"))
                   flag=0
                   for i in pno:
                       if(j==i):
                           flag=1
                           k=pno.index(i)
                   if(flag==1):
                          print("\nProduct No   :",pno[k])
                          print("Product Name :",pnm[k])
                          print("Product Cost :",pcost[k])
                          print("Company Name :",cnm[k])
                   else:
                          print("We Don't Have Any Product After This Name")        
        elif ee==3:#SEARCHING BY COST RANGE
                    print('''Enter Product Range
                                1. Below 500
                                2. between 500 and 1000
                                3. Above 1000''')
                    w=int(input("Enter Your Choice : "))
                    if w==1:
                        flag=0
                        for i in pcost:
                            flag=0
                            if(i<500): 
                                 k=pcost.index(i)
                                 flag=1
                                 if(flag==1):
                                      print("\nProduct No   :",pno[k])
                                      print("Product Name :",pnm[k])
                                      print("Product Cost :",pcost[k])
                                      print("Company Name :",cnm[k])         
                    elif w==2:
                        flag=0
                        for i in pcost:
                            flag=0
                            if(i>499 and i<1001):
                                 flag=2
                                 m=pcost.index(i)
                                 if(flag==2):
                                      print("\nProduct No   :",pno[m])
                                      print("Product Name :",pnm[m])
                                      print("Product Cost :",pcost[m])
                                      print("Company Name :",cnm[m])
                                 
                    elif w==3:
                        flag=0
                        for i in pcost:
                            flag=0
                            if(i>1000):    
                                 flag=3
                                 n=pcost.index(i)
                                 if(flag==3):
                                      print("\nProduct No   :",pno[n])
                                      print("Product Name :",pnm[n])
                                      print("Product Cost :",pcost[n])
                                      print("Company Name :",cnm[n])
                                    
                    elif w==4: 
                        flag=0
                        for i in pcost:
                             if(i>1000 and i<1500):    
                                 flag=4
                                 n=pcost.index(i)
                        if(flag==4):
                          print("\nProduct No   :",pno[n])
                          print("Product Name :",pnm[n])
                          print("Product Cost :",pcost[n])
                          print("Company Name :",cnm[n])
                        else:
                          print("We Don't Have Any Product in This Range")
                          break     
    elif ch==3: #TO MODIFY COST
        
         u=int(input("Enter the Product Number of the Product you want to Modify Cost of : "))
         nc=int(input("Enter New Cost : "))
         for i in pno:
             if(i==u):
                 k=pno.index(i)
                 pcost[k]=nc
         print("Cost Updated")
    elif ch==4: #TO DELETE A PRODUCT
         d=int(input("Enter the Product Number of the product You want to Delete :"))
         for i in pno:
             if(i==d):
                 k=pno.index(i)
                 del(pno[k], pnm[k] , pcost[k] , cnm[k])
         print("Product Deleted")        
    elif ch==5: #DISPLAYING THE PRODUCT
        print("******************ALL PRODUCTS LIST***********************")
        print("PRODUCT NO |  PRODUCT NAME |  PRODUCT COST |  COMPANY NAME")
        for i in range(len(pnm)):
            print(pno[i]  ,"\t\t", pnm[i],"\t\t",   "$",pcost[i],"\t\t", cnm[i])
    elif ch==6: #EXIT
        print("Exiting...")
        print("****************Thanks Visit Again***************")
        break

