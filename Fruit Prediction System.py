import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
#Importing the Dataframe
df = pd.read_csv("D:\\python\\dataset\\fruits.csv")
features   =  df.iloc[:,:-1].values
target     =  df.iloc[:,-1:].values
knc = KNeighborsClassifier()
knc.fit(features,target)

def prefruit():
    height = float(h_entry.get())
    weight = int(w_entry.get())
    prediction = knc.predict([[height,weight]])
    r_entry.delete(0,END)
    r_entry.insert(0,prediction[0])
    
from tkinter import *

# Creating Parent Window.

mywin = Tk() # window created
mywin.state('zoomed') # Maximized the Window
mywin.title('Fruit Prediction System')

mywin.configure(bg='blanchedalmond') # Set the the background colour of the main window

mywin.resizable(width=False, height=False) # to restrict the size of the window

# Creating a Header Window.

header = Frame(mywin) # Created a frame within a window
header.configure(bg="beige")
header.place(x=0,y=0,relwidth=1,relheight=0.20) # Determining the placement of the frame.

# Creating a title in the header .
title = Label(header,text = " FRUIT PREDICTION SYSTEM ",font=('Verdana',40,'bold'))
title.pack()

# Creating a body in the Main Window.
body = Frame(mywin)
body.configure(bg="darkgoldenrod1")
body.place(x=0,y=200,relwidth=1,relheight=0.80)

# 3 Text Labels
height = Label(body,text= " Enter Height :  ",font=('Verdana',20),bg="ghostwhite")
height.place(relx=0.2,rely=0.1)

width = Label(body,text = " Enter Weight :  ",font=('Verdana',20),bg="ghostwhite")
width.place(relx=0.2,rely=0.25)

result = Label(body,text = "  Result : ",font=('Verdana',20),bg="ghostwhite")
result.place(relx=0.2,rely=0.4)

# 3 Text Fields
h_entry = Entry(body,font=('Verdana',20),bd=4)
h_entry.place(relx=0.4,rely=0.1)

w_entry = Entry(body,font=('Verdana',20),bd=4)
w_entry.place(relx=0.4,rely=0.25)

r_entry = Entry(body,font=('Verdana',20),bd=2)
r_entry.place(relx=0.4,rely=0.4)

# Button
Predict = Button(body,text = " Predict Fruit ",font=('Verdana',20),bd=6,command=prefruit)
Predict.place(relx=0.4,rely=0.6)

mywin.mainloop()



