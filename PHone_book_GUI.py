# -*- coding: utf-8 -*-
"""
Created on Fri May 14 22:22:14 2020

@author: SHUBHAM MORE
"""

import csv
from tkinter import *
from tkinter import messagebox
import datetime


with open('output.csv') as f:
    data = dict(filter(None, csv.reader(f)))


def main():
    # fetching current date
    date = str(datetime.datetime.now().date())

    # creating root object
    root = Tk()
    root.title(" Shubham's Phone book".capitalize())
    root.geometry("650x550+350+200")
    root.resizable(FALSE, FALSE)

    def del_con():
        cmd = get_name.get()
        if cmd in data.keys():

            msg = cmd + ' ' + data.pop(cmd) + ' deleted'
            messagebox.showinfo('Deleted ', msg)
            savedata()
            show_all()
        else:
            print('no contact found.46464.')

    # for saving data into output.csv file
    def savedata():
        w = csv.writer(open("output.csv", "w"))
        for key, val in data.items():
            w.writerow([key, val])

    # searching contact
    def search():
        name_lbl['text'] = 'Enter name'

        res = ""
        key = get_name.get()
        if key == '':
            messagebox.askretrycancel('Error', 'No contact found')
        else:
            res = dict(filter(lambda item: key.casefold() in item[0], data.items()))
        if res == {}:
            messagebox.askretrycancel('Error', 'No contact found')
        else:
            lb.delete(0, 'end')
            for x, y in enumerate(res):
                lb.insert(x + 1, y)

    def validation():
        user_numbr = ''
        user_name = ''
        user_name = get_name.get()
        user_numbr = get_num.get()
        if user_name == '':
            messagebox.askokcancel('Error', "Enter correct input")
        elif user_numbr == '':
            messagebox.showinfo('Error', "Mobile can not be empty")

        elif not user_numbr.isdigit():
            messagebox.askokcancel('Error', "Mobile no takes only integer", icon='warning')

        else:
            return TRUE

    # save contact

    def save():
        name_lbl['text'] = 'Enter Name'
        num_lbl['text'] = 'Enter Number'
        if validation():
            user_name = str(get_name.get())
            user_numbr = get_num.get()
            data[user_name.title()] = user_numbr
            msg = 'Saved ' + user_name + ' ' + user_numbr
            messagebox.showinfo("Saved", msg)
            savedata()
            show_all()

    # show contact in listbox
    def show_all():
        # lb.insert(0,"contact Names")
        lb.delete(0, 'end')
        lb.insert(0, '')
        for x, y in enumerate(data):
            lb.insert(x + 1, y)

            pass

    def clr_entry():
        get_name.delete(0, 'end')
        get_num.delete(0, 'end')

    # show contact in phone book
    def select():
        get_num.delete(0, 'end')
        get_name.delete(0, 'end')
        name = lb.get('active')

        if name == '':
            messagebox.askokcancel('Error', "Please first select Contact..", icon='error')
        else:
            num = data[name]
            name_lbl['text'] = 'Name is'
            num_lbl['text'] = 'Number is'
            get_name.insert(0, name)
            get_num.insert(0, num)

    # GUI
    import tkinter as tk
    root.iconphoto(FALSE, tk.PhotoImage(file='exe.png'))
    # top frame
    top = Frame(root, height=150, bg='#F0F0F0')
    top.pack(fill=X)

    # bottom
    bottom = Frame(root, height=500, bg='#34baeb')
    bottom.pack(fill=X)

    # listbox
    lb = Listbox(bottom, font=('abadi', 12 ), selectmode=BROWSE)
    lb.place(x=10, y=10)

    # loading data into listbox
    show_all()

    # img
    top_img = PhotoImage(file='\\Users\SHUBHAM\PycharmProjects\Phonebook\Phonebook-icon.png')
    top_img_lable = Label(top, image=top_img, background="#F0F0F0")
    top_img_lable.place(x=32, y=32)

    # title Segoe Print
    heading = Label(top, text="My PhoneBook", font=('Edwardian Script ITC', 40, 'bold'), fg='black')
    heading.place(x=105, y=45)

    # Date_time
    date = Label(top, text="Today's date " + date, font='arial 15  ')
    date.place(x=400, y=10)

    # Button 1 save show contact
    showimg = PhotoImage(file=r"info.png")
    showimg = showimg.subsample(4, 4)
    show_contact = Button(bottom, image=showimg, compound=LEFT, text=" Show contact ", font='arial 15 ', command=select)
    show_contact.place(x=60, y=280)

    # Button 2 show view all contact
    list = PhotoImage(file=r"list.png")
    listimg = list.subsample(8)
    view_contact = Button(bottom, image=listimg, compound=LEFT, text=" All contacts", font='arial 15  ',
                          command=show_all)
    view_contact.place(x=252, y=280)

    # Button 3 save add new contact
    add = PhotoImage(file=r"add.png")
    photoimage = add.subsample(4, 4)
    save_contact = Button(bottom, text=" Add contact ", image=photoimage, compound=LEFT, font='arial 15  ',
                          command=save)
    save_contact.place(x=420, y=280)

    # Button 4 search contact
    searchimg = PhotoImage(file=r"search.png")
    searchimg = searchimg.subsample(4, 4)
    search_contact = Button(bottom, image=searchimg, compound=LEFT, text="Search contact ", font='arial 15  ',
                            command=search)
    search_contact.place(x=140, y=340)

    # Button 5 Delete contact
    delimg = PhotoImage(file=r"delete.png")
    delimg = delimg.subsample(4, 4)
    search_contact = Button(bottom, image=delimg, compound=LEFT, text="Delete contact ", font='arial 15  ',
                            command=del_con)
    search_contact.place(x=330, y=340)

    # msg label
    msg_lbl = Label(top, text=" ", font=('arial 15 bold', 15, 'bold'), background='#F0F0F0')
    msg_lbl.place(x=250, y=119)
    # ====================================================================================
    # label and entry for name
    name_lbl = Label(bottom, text="Enter Name", font=('arial 15 bold', 10, 'bold'), background='#34baeb')
    name_lbl.place(x=240, y=10)
    get_name = Entry(bottom, width=20, font=('arial 15 bold', 15, 'bold'))
    get_name.place(x=240, y=35)

    # Entry and label for number
    get_num = Entry(bottom, width=20, font=('arial 15 ', 15, 'italic'))
    get_num.place(x=240, y=90)
    num_lbl = Label(bottom, text="Enter Number", font=('arial 15 bold', 10, 'bold'), background='#34baeb')
    num_lbl.place(x=240, y=67)
    # ---------------------------------------------------------

    root.mainloop()


if __name__ == '__main__':
    main()
