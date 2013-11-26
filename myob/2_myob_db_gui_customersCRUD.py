#!/usr/bin/python3

# FIX, PLEASE URL ON CONFIG FILE!

#TODO, place hud loading!

#TODO, SEPARATE MYOB CRUD ON OWN CLASS! COMO dbSchema es crud, pero crud para MYOB!

#TEMPLATE CODING STYLE OBJ!!

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as tkMessageBox

import dbSchema1

import sys
import requests
import base64

root = Tk()
usernameVal = StringVar()

userUpdatenameVal = StringVar()


db = dbSchema1.database(filename = 'timeSheets.db', table = 'Employee')
customerList = []


userName = "administrator:"
password = ""
construida = "".join((userName, password))
encoded = base64.b64encode (bytes(construida, "utf-8"))

class myclass():

		def __init__(self):
			self.initDB()
			self.getCustomerData() #ponerle un HUD!
			
			self.main() #atencion! es un loop! se quedara aqui!
				# en objC [self main]

		def submitForm(self,*args):
				try:
						print("submitForm pressed")
						customerName = self.usernameVal.get()
						#nota GETTER N SETTER! DE EL WIDGET ATRAVEZ DE VAR!!
						print('name is %s' %customerName ) #mira como hace el print!
						self.usernameVal.set("")
 
						#save to db!
						db.insert(dict(name = customerName, surname = 1))

						#update MYOB
						r = requests.post("http://localhost:8080/AccountRight/6680178c-1cb2-44b4-ab9f-8ca75155f9f5/Contact/Customer",headers={"x-myobapi-cftoken":encoded});
						
						print(r.text)

						data = r.json()

						print("tu status code", r.status_code)

						#alert confirm
						result = tkMessageBox.showinfo(title="titu", message="Customer created \n.)")
#.showinfo(title, message, options)

				except ValueError:
						pass

		def updateForm(self, *args):
			print()
			try:
				print("submitForm pressed")
				print('name is %s' % self.userUpdatenameVal.get())
				self.userUpdatenameVal.set("")
			except ValueError:
				pass


		def initDB(self):
			#db = dbSchema1.database(filename = 'timeSheets.db', table = 'Employee')
			print('Create table Employee')
			db.sql_do('drop table if exists Employee') #borra siempre?
			db.sql_do('create table Employee ( name text, surname int )')
			

		def getCustomerData(self):

			#test db mock!


			print ("mellammmo")
			#userName = "administrator:"
			#password = ""
			#construida = "".join((userName, password))
			#encoded = base64.b64encode (bytes(construida, "utf-8"))
			
			print (construida)

			print ("tu enconded", encoded)
			r = requests.get("http://localhost:8080/AccountRight/6680178c-1cb2-44b4-ab9f-8ca75155f9f5/Contact/Customer",headers={"x-myobapi-cftoken":encoded});
			data = r.json()
			#print(data) 
			#print (data["Items"] [0])
			#print(data["Items"])

			print("length data array: %i" %len(data))

			arraya = data["Items"]
			i = 0
			for itemDicto in arraya:
					print ("tiu mare")
					print (itemDicto["CoLastName"])
					customerList.insert(i, itemDicto["CoLastName"])

					#insert!
					db.insert(dict(name = itemDicto["CoLastName"], surname = 1))


					i += 1

			print('Create rows')
			#db.insert(dict(name = 'one', surname = 1))
			#db.insert(dict(name = 'two', surname = 2))
			#db.insert(dict(name = 'three', surname = 3))
			#db.insert(dict(name = 'four', surname = 4))
			for row in db: print(row)

 

		def test(self):
			print ("huhuha")

		def main(self):
 
				print("from main")

				#self.test

				print(customerList)
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
				usernameTf.grid(column=1 , row=1, sticky=(W,E))

				button = Button(mainframe, text='Save New', command=self.submitForm)
				button.grid(column=1, row=2, sticky=(E))  

				customerLbl = Label(mainframe, text='Update Customers')
				customerLbl.grid(column=0 , row=3, sticky=(W,E))

				l = Listbox(mainframe, height=5)
				l.grid(column=1, row=3, sticky=(N, W, E, S))
				s = Scrollbar(mainframe, orient=VERTICAL, command=l.yview)
				s.grid(column=2, row=3, sticky=(N, S, W))
				l['yscrollcommand'] = s.set 
			 
				index = 0

				for lana in customerList:
					print (lana)
					l.insert(index, lana)
					index += 1

				#Update
				updateLbl = Label(mainframe, text='Edit Customer')
				updateLbl.grid(column=0 , row=4, sticky=(W,E))

				self.userUpdatenameVal = StringVar()
				usernameUpdateTf = Entry(mainframe, textvariable = self.userUpdatenameVal)
				usernameUpdateTf.grid(column=1 , row=4, sticky=(W,E))

				saveUpdatebutton = Button(mainframe, text='Save Edit', command=self.updateForm)
				saveUpdatebutton.grid(column=1, row=5, sticky=(E))
				
				
			

		#my loop
				root.mainloop()

if __name__ == "__main__":
		myclass()