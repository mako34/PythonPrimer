#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
 
root = Tk()
usernameVal = StringVar()

def submitForm(*args):
    try:
        print("submitForm pressed")

        print('name is %s' % usernameVal.get()) #mira como hace el print!

        usernameVal.clear(1.0, END) 

    except ValueError:
        pass
 
def main():
 
#container view
    mainframe = ttk.Frame(root, padding="3 3 12 12") #  mainframe contained by root!, init

    mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) #  add subview mainframe
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

#UI widgets
    createLbl = ttk.Label(mainframe, text='Create login & Password')
    createLbl.grid(column=2 , row=1, sticky=(W,E))

# user name
    nameLbl = ttk.Label(mainframe, text='User Name')
    nameLbl.grid(column=1 , row=2, sticky=(W,E))

    #usernameVal = StringVar()
    usernameTf = ttk.Entry(mainframe, textvariable = usernameVal)
    usernameTf.grid(column=2 , row=2, sticky=(W,E))

    button = ttk.Button(mainframe, text='Create User', command=submitForm)
    button.grid(column=3 , row=2, sticky=(W,E))  

#my loop
    root.mainloop()

if __name__ == "__main__": main()




