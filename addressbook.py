# Roohan Kunta
# Final Project - Addressbook
# Python version 2


from Tkinter import *
import tkMessageBox as msgBox
from contacts  import *
import csv
import pandas as pd

""" Welcome to the AddressBook program, its just like an normal phonebook or adressbook 
which holds the contact information of people like Name, Phone Number, Address and Email.

We can enter the details of the person and ADD it to the contact list. We can perform
Editing or Deleting or Retrieving a contact by highlighting the contact and clicking 
on the respective buttons to do the necessary action we want to perform. 

To save the entire contact list we can click the 'SAVE' button at the bottom of the 
scroll view and it will save the contact details of the people you have entered by
writing it to a CSV file using pandas. If the Save button is not clicked the changes 
made to the contacts will not be save for future referals or retrievals.
"""  

def cselect():
	""" This the function which sets the location when the cursor selects an contact from the list"""
	return int(select.curselection()[0])

def addF():
	""" This function will add all the details of a new contact like first name, last name,phone number,
	address and email address to the list of contacts when the 'ADD' button is clicked.
	"""
	contacts.append([fname1.get(),lname1.get(),phone1.get(),address1.get(),email1.get()])
	selF()
	msgBox.showinfo("Message","Contact has been added.")
		
def editF():
	"""This function will save the changes made to an existing contact and update the list of contacts"""
	contacts[cselect()]=[fname1.get(),lname1.get(),phone1.get(),address1.get(),email1.get()]
	selF()
	msgBox.showinfo("Message","Contact has been updated.")

def delF():
	"""This function will deleted the contact. It will only deleted the selected contact and re-sort all the contacts. """
	del contacts[cselect()]
	selF()
	msgBox.showinfo("Message","Contact has been deleted.")

def loadF():
	""" This function is used to retreive the contact details of a person from the existing list of contacts.
	When a contact is selected and "Load" button is clicked it will display the details of the contact.
	"""
	fname,lname,phone,address,email=contacts[cselect()]
	fname1.set(fname)
	lname1.set(lname)
	phone1.set(phone)
	address1.set(address)
	email1.set(email)

def saveF():
	""" This is used to save the changes made to the contacts list. If this is not clicked then it will not save
	the changes and when the contacts are opened once again, the changes will not be updated.
	It is important to click save to save all the changes made.
	
	This will also create a csv file which will save the contact details to the file each time the 'SAVE'
	button is clicked.
	"""
	writeF()
	selF()
	f=open("contacts.py","w")
	f.write("contacts=["+"\n")
	for fname,lname,phone,address,email in contacts:
		f.write("".join(["['%s','%s','%s','%s','%s'],"%(fname,lname,phone,address,email)])+"\n")
	f.write("]")
	
	msgBox.showinfo("Message","All Contacts are saved.")

def writeF():
	"""This is used to write the saved contacts to a csv file name phonebook using
	 pandas."""
	df = pd.DataFrame(contacts)
	df.to_csv('phonebook.csv',index=False,header=["First Name","Last Name","Phone","Address","Email"])

def selF():
	""" The contacts are sorted here and displayed in the gui window for the user to view"""
	contacts.sort()
	select.delete(0,END)
	for fname,lname,phone,address,email in contacts :
		select.insert(END,fname+","+lname)


def main_window():
	""" This will create the GUI with all the fields placed in order for the user to enter the contact details.
	The layout of the gui and positions of the fields and textboxs are all defined in this function
	""" 
	global fname1,lname1, phone1, address1, email1, select
	win = Tk()
	win.title("Address Book")
	win.geometry("550x500")
	frame1 = Frame(win)
	frame1.pack()
	
	labf=Label(frame1, text="First Name")
	labf.grid(row=0, column=0, sticky=W)
	fname1 = StringVar()
	fname = Entry(frame1, textvariable=fname1)
	fname.grid(row=0, column=1, sticky=W)
	
	labl=Label(frame1, text="Last Name")
	labl.grid(row=1, column=0, sticky=W)
	lname1 = StringVar()
	lname = Entry(frame1, textvariable=lname1)
	lname.grid(row=1, column=1, sticky=W)
	
	labp=Label(frame1, text="Phone")
	labp.grid(row=2, column=0, sticky=W)
	phone1= StringVar()
	phone= Entry(frame1, textvariable=phone1)
	phone.grid(row=2, column=1, sticky=W)
	
	laba=Label(frame1, text="Address")
	laba.grid(row=3, column=0, sticky=W)
	address1= StringVar()
	address= Entry(frame1, textvariable=address1)
	address.grid(row=3, column=1, sticky=W)
	
	labe=Label(frame1, text="Email")
	labe.grid(row=4, column=0, sticky=W)
	email1= StringVar()
	email= Entry(frame1, textvariable=email1)
	email.grid(row=4, column=1, sticky=W)
	
	frame2 = Frame(win)       
	frame2.pack()
	b1 = Button(frame2,text=" Add  ",command=addF)
	b2 = Button(frame2,text="Update",command=editF)
	b3 = Button(frame2,text="Delete",command=delF)
	b4 = Button(frame2,text=" Load ",command=loadF)
	b1.pack(side=LEFT); b2.pack(side=LEFT)
	b3.pack(side=LEFT); b4.pack(side=LEFT)
	
	frame3 = Frame(win)       
	frame3.pack()
	scroll = Scrollbar(frame3, orient=VERTICAL)
	select = Listbox(frame3, yscrollcommand=scroll.set, height=10)
	scroll.config (command=select.yview)
	scroll.pack(side=RIGHT, fill=Y)
	select.pack(side=LEFT,  fill=BOTH, expand=1)
	
	frame4 = Frame(win)
	frame4.pack()
	b1 = Button(frame4,text=" Save ",command=saveF)
	b1.pack(side=LEFT)
	return win


win = main_window()
selF()
win.mainloop()
