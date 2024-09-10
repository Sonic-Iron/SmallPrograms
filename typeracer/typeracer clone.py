import random
import time
from tkinter import *
import string
class GUI():
    def __init__(self):
        try:
            self.window.destroy()
        except:
            pass
        window = Tk()
        self.window = window
        self.menu_option = "None"
        self.start_random = Button(self.window, text="Use a random text", command = lambda: self.random_text())
        self.start_random.pack()
        self.charPos = 0
        self.charCorrect = 0
        self.letterswritten = 0
        self.started = False

    def random_text(self):
        self.window.destroy()
        self.window = Tk()
        file = open("./texts.txt","r")
        text = random.choice(file.readlines())
        text = text[text.index("|")+1:]
        self.lentext = len(text)
        self.text_text = Text(self.window)
        self.text_text.insert("1.0",text)
        self.text_text.pack()
        self.user_input = Entry(self.window)
        self.user_input.pack(side=BOTTOM)
        self.keycount = 0
        self.window.bind('<KeyPress>', self.check_keypress)            
        
    def check_keypress(self, event):
        print(event.char)
        if event.char == "":
            return
        if self.started == False:
            self.starttime = time.time()
            self.window.after(10,self.WPMcalculator())
            self.started = True
        if event.char == self.text_text.get("1."+str(self.charPos)):
            self.charPos += 1
            self.text_text.tag_add("green", "1."+str(self.charPos-1))
            self.text_text.tag_configure("green", foreground="green")
            if "correct" in self.text_text.tag_names("1."+str(self.charPos-1)): #have to -1 as the charPos have increased by 1 from the orginal value
                pass
            else:
                self.charCorrect += 1
                self.text_text.tag_add("correct","1."+str(self.charPos-1))
            self.letterswritten += 1
        elif event.char == '\x08':
            if self.charPos > 0:
                self.charPos -= 1
                try:
                    self.text_text.tag_remove("green","1."+str(self.charPos))
                    self.text_text.tag_remove("red","1."+str(self.charPos))
                except:
                    try:
                        self.text_text.tag_remove("red","1."+str(self.charPos))
                        self.text_text.tag_remove("green","1."+str(self.charPos))
                    except:
                        pass             
            else:
                pass
        else:
            self.text_text.tag_add("red", "1."+str(self.charPos))
            self.text_text.tag_configure("red", foreground="red")
            self.charPos += 1
            self.letterswritten += 1
        self.user_input.delete(0,END)
        if (self.charPos == self.lentext-1) and (self.charCorrect == self.lentext-1):
            print("FINISHED")
            self.window.destroy()
            window = Tk()
            self.window = window
            self.WPMcounter = Label(self.window, text = "WPM: "+ str(round(self.WPMvalue)))
            self.accuracycounter = Label(self.window, text="Accuracy: "+str(round(self.accuracyvalue))+"%")
            self.accuracycounterreal = Label(self.window, text="Actual Accuracy: "+str(round(self.accuracyvaluereal))+"%")
            self.WPMcounter.pack()
            self.accuracycounter.pack()
            self.accuracycounterreal.pack()


        

    def WPMcalculator(self):
        try:
            self.WPMvalue = (self.charCorrect/5)/((time.time()- self.starttime)/60)
            self.accuracyvalue = self.charCorrect/(self.charPos)*100
            self.accuracyvaluereal = (self.charCorrect/self.letterswritten)*100
        except:
            pass
        self.window.after(100, self.WPMcalculator)
GUI()
mainloop()
