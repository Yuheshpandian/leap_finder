# importing tkinter
from tkinter import *

# basic configurations
root = Tk()
root.title('LEAP_FINDER')
root.geometry('600x600')
root.configure(bg='light blue')
p1 = PhotoImage(file = 'clipart1007838.png')
root.iconphoto(False, p1)


# func that checks it is leap year or not
def check_leap(year):
    yearlbl.delete(0,END)
    text = ''
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                text = 'ITS A LEAP YEAR! '
            else:
                text = 'NOT A LEAP YEAR'
        else:
            text = 'ITS A LEAP YEAR!'
    else:
        text = 'NOT A LEAP YEAR'       

    lbl2 = Label(root,text = text,font = ('Arial',25))
    lbl2.config(bg = 'light blue')
    lbl2.place(relx=0.3,rely=0.7)

titlelbl = Label(root, text = 'LEAP FINDER')
titlelbl.place(relx = 0.45 ,rely = 0)
titlelbl.config(bg = 'white')


lbl1 = Label(root, text = 'ENTER THE YEAR THAT YOU NEED CHECK LEAP YEAR OR NOT')
lbl1.config(bg = 'white')
lbl1.place(relx=0.23,rely=0.3)

# gets the year
yearlbl = Entry(root,width=10,borderwidth=20)
yearlbl.config(background = "silver", )
yearlbl.place(relx=0.43,rely=0.4)

# gets input
check = Button(root, text = 'CHECK', padx = 10,pady = 10, command=lambda :check_leap(int(yearlbl.get())))
check.place(relx = 0.455,rely = 0.6)


root.mainloop()
