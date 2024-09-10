import random
from tkinter import *
import binascii

class passwordsystem():
    def __init__ (self):
        window = Tk()
        self.window = window
        self.window.title("Password System")
        self.enter_user = Button(window, text="Enter", command=lambda: passwordsystem.Enter(self))
        self.user_entry_username = Entry(window)
        self.user_entry_password = Entry(window, show="*")
        self.userentryuserLabel= Label(window, text="Username")
        self.userentrypassLabel = Label(window, text="Password")
        self.outputlabeltext = StringVar()
        self.outputtext = Label(window, textvariable=self.outputlabeltext)
        self.searchBox = Entry(window)

        self.userentryuserLabel.pack()
        self.user_entry_username.pack()
        self.userentrypassLabel.pack()
        self.user_entry_password.pack()
        self.enter_user.pack()
        self.outputtext.pack()
        
        
    def Enter(self):
        userCheck = passCheck = False
        user = username = self.user_entry_username.get()
        password = self.user_entry_password.get()
        self.user = user
        password = self.user_entry_password.get()
        file = open("./users.txt","r")
        database = file.read()
        database = database.split(";")
        file.close()
        for a in database:
           database[database.index(a)] = a.split(":")
        self.database = database
        try:
           for a in self.database:
              for b in a:
                  if (username == (a[a.index("username")+1])) and (password == self.Decrypt(a[a.index("password")+1])):
                      user_pass_name = True
                      user = a[a.index("username")+1]
                      raise StopIteration
                  user_pass_name = False
        except StopIteration: pass
        if user_pass_name == True:
            self.database = database
            self.user = user
            self.outputlabeltext.set("Assess Granted")
            self.outputtext.config(fg="green")
            self.window.update()
            self.userentryuserLabel.destroy()
            self.user_entry_username.destroy()
            self.userentrypassLabel.destroy()
            self.user_entry_password.destroy()
            self.enter_user.destroy()
            self.outputtext.destroy()
            self.searchBox.pack(side=BOTTOM)
            self.usernamelabel = Label(self.window, text=self.user)
            self.usernamelabel.pack(side=TOP)
            self.passwordnamelist = Listbox(self.window)
            self.passwordnamelist.pack(side=LEFT)
            self.newpassword = Button(self.window, text="Enter a new password", command = lambda: self.new_password_box())
            self.newpassword.pack(side=RIGHT)
            self.window.after(1000, self.createDatabase())
        else:
            self.outputlabeltext.set("Assess Denied")
            self.outputtext.config(fg="red")

    def createDatabase(self):
        self.passwordnamelist.delete(0, END)
        file = open("./userdata/"+self.user+".txt", "r")
        self.database = file.read()
        self.database = self.database.split(":")
        for item in self.database:
            if self.database.index(item) % 2 == 0:
                if self.searchBox.get() == None:
                    self.passwordnamelist.insert(END, str(item)+"    -    "+self.Decrypt(self.database[self.database.index(item)+1]))
                    self.window.update()
                else:
                     if item.startswith(self.searchBox.get()):
                        self.passwordnamelist.insert(END, str(item)+"    -    "+self.Decrypt(self.database[self.database.index(item)+1]))
                        self.window.update()
        file.close()
        

    def new_password_box(self):
        self.window2 = Tk()
        self.newpassnamelabel = Label(self.window2, text="Enter the name of the new password")
        self.newpassname = Entry(self.window2)
        self.newpasspasslabel = Label(self.window2, text="Enter the new password")
        self.newpasspass = Entry(self.window2)
        self.enternewpass = Button(self.window2, text="Enter the new password", command = lambda: self.enternewpassword())
        self.newpassnamelabel.pack()
        self.newpassname.pack()
        self.newpasspasslabel.pack()
        self.newpasspass.pack()
        self.enternewpass.pack()

    def enternewpassword(self):
        self.window2.destroy()
        file = open("./userdata/"+self.user+".txt", "a")
        file.write(":"+str(self.newpassname.get())+":"+str(self.Encrypt(self.newpasspass.get())))
        file.close()
        self.createDatabase()
        
    
    def Encrypt(self, input_to_encrypt):
        encrypted = bin(int.from_bytes(input_to_encrypt.encode(), 'big'))
        return encrypted

    def Decrypt(self, input_to_decrypt):
        input_to_decrypt = int(input_to_decrypt, 2)
        decrypted = input_to_decrypt.to_bytes((input_to_decrypt.bit_length() + 7) // 8, 'big').decode()
        return decrypted

    
passwordsystem()
