"""
USER REGISTRATION
"""

import tkinter as tkr

master = tkr.Tk()
userlist = []


"""Edit Window"""
master.title("New user Registration")
master.geometry("200x117")

tkr.Label(master, text="New User Registration").grid(row=0, columnspan=2)
tkr.Label(master, text="First Name").grid(row=1)
tkr.Label(master, text="Last Name").grid(row=2)
tkr.Label(master, text="Password").grid(row=3)


e1 = tkr.Entry(master)
e2 = tkr.Entry(master)
e3 = tkr.Entry(master,show='*')


e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)



def call1():
    userlist.append([e1.get(), e2.get(), e3.get()])
    print(userlist)
    userverification = tkr.Tk()
    userverification.title("userverification")
    userverification.geometry("200x100")
    tkr.Label(userverification, text="Your Account has been Created").grid(row=1)

"""Button"""
button1 = tkr.Button(master, width=7,height=1, text="Register", command=call1) 
button1.grid(row=4,column=1, padx=3, pady=3)
button2 = tkr.Button(master, width=7,height=1, text="Quit", command=master.destroy) 
button2.grid(row=4,column=0, padx=3, pady=3)


tkr.mainloop()