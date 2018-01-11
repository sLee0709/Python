import os
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
from tkinter import scrolledtext
from datetime import datetime

filename = ""

def about():
    tkinter.messagebox.showinfo(title = "About", message = "DNA Reverse Complement® \r Version: 1.0 Beta \r Written by Li Shen")

def QUIT():
    top.quit()

def textdel_read():
    Read_frame.delete(0.0,END)

def textdel_out():
    Out_frame.delete(0.0,END)

def get_file():
    global filename
    filename = tkinter.filedialog.askopenfilename(filetypes=[("text file", "*.txt")])
    INPUT_text.set(filename)
    try:
        with open(filename,"r") as new_file:
            for each_line in new_file:
                Read_frame.insert(INSERT, each_line)
    except FileNotFoundError as reason:
        tkinter.messagebox.showinfo(title="Warning!", message="Please select a txt file!")

def RUNNING():
    ref_list = ['A', 'G', 'C', 'T', 'a', 'g', 'c', 't', ' ']
    try:
        Raw_data = Read_frame.get("0.0", END)
        IN = Raw_data.split( '\n')
        for line in IN:
            alist = list(line)

            for elements in alist:
                if elements not in ref_list:
                    Out_frame.insert(INSERT, 'Please check your sequence! \n')
                    break

            if elements in ref_list:
                alist.reverse()
                new_list = [' ' if i == ' ' else '' if i == '\n'else 't' if i == 'a' else 'a' if i == 't'else 'g' if i == 'c' else 'c' if i == 'g' else 'T' if i == 'A' else 'A' if i == 'T'else 'G' if i == 'C' else 'C' if i == 'G' else i for i in alist]
                result = ''.join(new_list)
                result_af = result + '\n'
                Out_frame.insert(INSERT, result_af)
        tkinter.messagebox.showinfo(title="Success!", message="Finished!")
    except UnboundLocalError as reason2:
        tkinter.messagebox.showinfo(title="Warning!", message="Please Enter Your Sequence!")

def savebutton():
    yesorno = tkinter.messagebox.askyesno(title="Warning!", message="Save Data?")
    if yesorno == True:
        Values = Out_frame.get('0.0', END)
        if Values:
            saveas = tkinter.filedialog.asksaveasfile(defaultextension="*.txt",filetypes=[("text file", "*.txt")])
            if saveas:
                saveas.write(Values)
                tkinter.messagebox.showinfo(title="Success!", message="Data has been successfully saved!")

top = Tk()
top.title("DNA Reverse Complement®" + " - Version 1.0 Beta")
top.geometry('620x400')

menubar = Menu(top)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=get_file)
filemenu.add_command(label="Save", command=savebutton)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=QUIT)
menubar.add_cascade(label="File",menu=filemenu)
menubar.add_command(label="About", command=about)
top.config(menu=menubar)

INPUT_text = StringVar()
label1 = Label(text="File Path:").grid(row = 1, column = 3)
INPUT = Entry(top, textvariable = INPUT_text, width = 32).grid(row = 1, column = 4)
bt1 = Button(top, text="Open ...", width = 10, command=get_file).grid(row = 1, column = 5)
Read_frame = scrolledtext.ScrolledText(top, width=30, height=20)
Read_frame.grid(row=3, column=4)
Out_frame = scrolledtext.ScrolledText(top, width=30, height=20)
Out_frame.grid(row = 3, column = 5)
bt2 = Button(top, text="Run!", width = 10, command=RUNNING).grid(row = 5, column = 6)
bt3 = Button(top, text="Save", width = 10, command=savebutton).grid(row = 6, column = 6)
bt4 = Button(top, text="Clear", width = 32, command=textdel_read).grid(row = 4, column = 4)
bt5 = Button(top, text="Clear", width = 32, command=textdel_out).grid(row = 4, column = 5)

top.mainloop()
