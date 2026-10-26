"""Guess Number from chapter 3 with a GUI"""

from tkinter import *
import random  

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.the_number = random.randint(1, 100)
        self.tries = 1
        self.create_widgets()

    def create_widgets(self):
        self.instruction = Text(self, width = 60, height = 3, wrap = WORD)
        self.instruction.grid(row = 0, column =0, columnspan = 4, sticky = W)
        instruction = "Witaj w grze 'Jaka to liczba'!"
        instruction += "\nMam na myśli pewną liczbę z zakresu od 1 do 100."
        instruction += "\nSpróbuj ją odgadnąć w jak najmniejszej liczbie prób."
        self.instruction.insert(0.0, instruction)     

        Label(self,
              text = "Ta liczba to: ",
              ).grid(row = 1, column = 0, sticky = W)
        self.guess_entry = Entry(self)
        self.guess_entry.grid(row = 1, column = 1, sticky = W)

        Button(self,
               text = "Sprawdź",
               command = self.check_number
               ).grid(row = 2, column = 0, sticky = W)

        self.result_txt = Text(self, width = 45, height = 3)
        self.result_txt.grid(row = 3, column = 0, columnspan = 4, sticky = W)


    def check_number(self):
        guess = self.guess_entry.get()
        
        if int(guess) != self.the_number:
            if int(guess) > self.the_number:
                result = "Za duża..."
                result += str(self.tries)
                
            else:
                result = "Za mała..."
                result += str(self.tries)
            self.tries += 1
                
        else:
            result = "Brawo! Zgadłeś! Potrzebowałeś "
            result += str(self.tries)
            result += " prób."

        self.result_txt.delete(0.0,END)
        self.result_txt.insert(0.0, result)
                    


root = Tk()
root.title("guess_number")
app = Application(root)
root.mainloop()
