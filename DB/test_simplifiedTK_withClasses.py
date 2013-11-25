#!/usr/bin/python3

#TEMPLATE CODING STYLE OBJ!!

from tkinter import *
from tkinter import ttk


root = Tk()
usernameVal = StringVar()
class myclass():

    def __init__(self):
        self.main()
        # en objC [self main]

    def submitForm(self,*args):
        try:
            print("submitForm pressed")

            #nota GETTER N SETTER! DE EL WIDGET ATRAVEZ DE VAR!!
            print('name is %s' % self.usernameVal.get()) #mira como hace el print!
            self.usernameVal.set("")

        except ValueError:
            pass

    def main(self):

    #container view
        mainframe = Frame(root) #  mainframe contained by root!, init

        mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) #  add subview mainframe
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

    #UI widgets
        createLbl = Label(mainframe, text='Create login & Password')
        createLbl.grid(column=2 , row=1, sticky=(W,E))

    # user name
        nameLbl = Label(mainframe, text='User Name')
        nameLbl.grid(column=1 , row=2, sticky=(W,E))

        self.usernameVal = StringVar()
        usernameTf = Entry(mainframe, textvariable = self.usernameVal)
        usernameTf.grid(column=2 , row=2, sticky=(W,E))

        button = Button(mainframe, text='Create User', command=self.submitForm)
        button.grid(column=3 , row=2, sticky=(W,E))  

    #my loop
        root.mainloop()

if __name__ == "__main__":
    myclass()