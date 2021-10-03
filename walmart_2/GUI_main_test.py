from tkinter import *
import tkinter.messagebox as messagebox
import main

password='JTD'

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.PW = Entry(self,width='50')
        self.PW.pack()
        self.alertButton = Button(self, text='Start',height='5',width='10', command=self.run)
        self.alertButton.pack()
    def run(self):
        if self.PW.get()==password:
            statu=True
            messagebox.showinfo('Warning', 'this is a test demo still, the usage of it is not highly recommanded')
            messagebox.showinfo('Warning', 'And it has not stop button yet')
            main.main(statu)
        else:
            messagebox.showwarning('Message','Incorrect password')
            self.destroy()

app = Application()
app.master.title('stopping not supported')
app.mainloop()