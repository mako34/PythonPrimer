#!/usr/bin/python3

#TODO, place hud loading!

#TEMPLATE CODING STYLE OBJ!!

from tkinter import *
from tkinter import ttk

import sys

root = Tk()
usernameVal = StringVar()


customerList = []

class myclass():

    def __init__(self):
    	self.main() #atencion! es un loop! se quedara aqui!
        # en objC [self main]

    def submitForm(self,*args):
        try:
            print("submitForm pressed")

            #nota GETTER N SETTER! DE EL WIDGET ATRAVEZ DE VAR!!
            print('name is %s' % self.usernameVal.get()) #mira como hace el print!
            self.usernameVal.set("")

        except ValueError:
            pass

     

    def test(self):
    	print ("huhuha")

    def main(self):
 
        print("from main")

        #self.test

     #container view
        mainframe = Frame(root) #  mainframe contained by root!, init

        mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) #  add subview mainframe
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

    #UI widgets
        createLbl = Label(mainframe, text='Create  Update Read Delete Customer')
        createLbl.grid(column=1 , row=0, sticky=(W,E))

    # user name
        nameLbl = Label(mainframe, text='New Customer')
        nameLbl.grid(column=0 , row=1, sticky=(W,E))

        self.usernameVal = StringVar()
        usernameTf = Entry(mainframe, textvariable = self.usernameVal)
        usernameTf.grid(column=1 , row=1, sticky=(E))

        button = Button(mainframe, text='Save', command=self.submitForm)
        button.grid(column=3 , row=1, sticky=(W,E))  

        customerLbl = Label(mainframe, text='Customers')
        customerLbl.grid(column=0 , row=2, sticky=(W,E))

        l = Listbox(mainframe, height=5)
        l.grid(column=1, row=2, sticky=(N, W, E, S))
        s = Scrollbar(mainframe, orient=VERTICAL, command=l.yview)
        s.grid(column=2, row=2, sticky=(N, S, W))
        l['yscrollcommand'] = s.set
        

        index = 0

        for lana in customerList:
        	print (lana)
        	l.insert(index, lana)
        	index += 1


        #for customerObj in customerList
            #l.insert (index, customerObj)
            #print customerObj
        #for i in range(1,4):
        #	l.insert('end', 'Line %d of 100' % i)


        detailsLbl = Label(mainframe, text='Details')
        detailsLbl.grid(column=3 , row=2, sticky=(W,E))

        l2 = Listbox(mainframe, height=5)
        l2.grid(column=4, row=2, sticky=(N, W, E, S))
        s2 = Scrollbar(mainframe, orient=VERTICAL, command=l2.yview)
        s2.grid(column=5, row=2, sticky=(N, S))
        l2['yscrollcommand'] = s2.set

        l2.insert(0, "mashu pishu")
        #for i in range(1,10):
         #   l2.insert('end', 'Line %d of 100' % i)

    #my loop
        root.mainloop()

if __name__ == "__main__":
    myclass()