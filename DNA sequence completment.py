import os
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
from tkinter import scrolledtext

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
    Read_frame.delete(0.0, END)
    try:
        with open(filename,"r") as new_file:
            for each_line in new_file:
                Read_frame.insert(INSERT, each_line)
    except FileNotFoundError as reason:
        tkinter.messagebox.showinfo(title="Warning!", message="Please select a txt file!")

def RUNNING():
    ref_list = ['A', 'G', 'C', 'T', 'a', 'g', 'c', 't', ' ']
    Out_frame.delete(0.0, END)
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

def add_adapter():

    def R_Adapter():
        RH_A = RH_adapt.get()
        RL_A = RL_adapt.get()

        Raw_Out = Out_frame.get(0.0, END)
        Out_frame.delete(0.0, END)
        Raw_Out_data = Raw_Out.split('\n')
        Raw_Out_data.remove('')
        new_Raw_Out_data = [RH_A + q + RL_A for q in Raw_Out_data]
        for a_line in new_Raw_Out_data:
            Out_frame.insert(INSERT, a_line + '\n')

    def F_Adapter():
        FH_A = FH_adapt.get()
        FL_A = FL_adapt.get()

        Read_Raw_Out = Read_frame.get(0.0, END)
        Read_frame.delete(0.0, END)
        Read_Raw_Out_data = Read_Raw_Out.split('\n')
        Read_Raw_Out_data.remove('')
        new_Read_Raw_Out_data = [FH_A + q + FL_A for q in Read_Raw_Out_data]
        for a_line in new_Read_Raw_Out_data:
            Read_frame.insert(INSERT, a_line + '\n')

    root = Tk()
    root.geometry('300x150')
    root.title("Add Adapter")
    root.wm_attributes('-topmost',1 )

    FH_label = Label(root, text='FH Adapter:').grid(row = 0, column = 0)
    fh_adapt_text=StringVar()
    FH_adapt = Entry(root, textvariable=fh_adapt_text, width = 8)
    FH_adapt.grid(row = 0, column = 1)
    FL_label = Label(root, text='FL Adapter:').grid(row = 0, column = 3)
    fl_adapt_text = StringVar()
    FL_adapt = Entry(root, textvariable=fl_adapt_text, width=8)
    FL_adapt.grid(row=0, column=4)
    Space1 = Label(root, text=' ').grid(row=0, column=2)
    Space2 = Label(root, text=' ').grid(row = 1, column = 1)
    Space3 = Label(root, text=' ').grid(row=3, column=1)
    RH_label = Label(root, text='RH Adapter:').grid(row = 2, column = 0)
    rh_adapt_text = StringVar()
    RH_adapt = Entry(root, textvariable=rh_adapt_text, width=8)
    RH_adapt.grid(row=2, column=1)
    RL_label = Label(root, text='RL Adapter:').grid(row = 2, column = 3)
    rl_adapt_text = StringVar()
    RL_adapt = Entry(root, textvariable=rl_adapt_text, width=8)
    RL_adapt.grid(row=2, column=4)
    root_button1 = Button(root, text="R Adapter",command=R_Adapter, width = 8)
    root_button1.grid(row=4, column=4)
    root_button2 = Button(root, text="F Adapter", command=F_Adapter, width=8)
    root_button2.grid(row=4, column=1)

top = Tk()
top.title("DNA Reverse Complement®" + " - Version 1.0 Beta")
top.geometry('620x400')

menubar = Menu(top)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=get_file)
filemenu.add_command(label="Save", command=savebutton)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=QUIT)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Add adapter", command=add_adapter)
menubar.add_cascade(label="Edit", menu=editmenu)
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
