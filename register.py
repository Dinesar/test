from tkinter import *
from tkinter import ttk


master = Tk()


w = Canvas(master, width=650, height=600)
w.create_rectangle(475, 175, 175, 475, fill="#FFFFFF", outline = 'black')
w.place(x=10,y=20)
font1 = ('Verdana',10)
font2 = ('Verdana',20)
hoofdtitel = ttk.Label(master, text='Registreren', font=font2)
titel = ttk.Label(master, text="SMS code:", font=font1, background="#FFFFFF")
titel2 = ttk.Label(master, text="Telefoonummer:", font=font1, background="#FFFFFF")
titel3 = ttk.Label(master, text="Wachtwoord:", font=font1, background="#FFFFFF")
titel4 = ttk.Label(master, text="Naam:", font=font1, background="#FFFFFF")
naam_entry = ttk.Entry(master)
ww_entry = ttk.Entry(master)
sms_entry = ttk.Entry(master)
tel_entry = ttk.Entry(master)
A = ttk.Button(master, text='Terug naar hoofdmenu')
A.pack()
titel.pack()
hoofdtitel.pack()
tel_entry.place(x=330,y=340)
sms_entry.place(x=330,y=390)
ww_entry.place(x=330,y=290)
naam_entry.place(x=330,y=240)
hoofdtitel.place(x=245,y=90)
titel.place(x=190,y=390)
titel2.place(x=190,y=340)
titel3.place(x=190,y=290)
titel4.place(x=190,y=240)
A.place(x=20,y=560, height=30, width=175)

w.pack()

master.resizable(0,0)
mainloop()

