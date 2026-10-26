"""Milk Bar Menu"""

from tkinter import *
import random

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()

        self.create_widgets()

    def create_widgets(self):
        self.welcome = Text(self, width = 60, height = 3, wrap = WORD)
        self.welcome.grid(row = 0, column =0, columnspan = 4, sticky = W)
        welcome = "Welcome to the Coconut Milk Bar!"
        welcome += "\nWe have all other types of milk as well."
        welcome += "\nWhat do you want for a drink?"
        self.welcome.insert(0.0, welcome) 

        Label(self,
              text = "Drink:",
              ).grid(row = 1, column = 0, sticky = W)

        self.choose_drink = StringVar()
        self.choose_drink.set(None)

        drinks = ["Coffe", "English tea", "Milkshake"]
        column = 1
        for drink in drinks:
            Radiobutton(self,
                        text = drink,
                        variable = self.choose_drink,
                        value = drink
                        ).grid(row = 2, column = column, sticky = W)
            column += 1

        Label(self,
              text = "Additions",
              ).grid(row = 3, column = 0, sticky = W)

        self.is_sugar = BooleanVar()

        Checkbutton(self,
                    text = "Sugar",
                    variable = self.is_sugar
                    ).grid(row = 3, column = 1, sticky = W)

        self.is_spices = BooleanVar()
        Checkbutton(self,
                    text = "Spices",
                    variable = self.is_spices
                    ).grid(row = 3, column = 2, sticky = W) 

        Label(self,
              text = "Type of milk used",
              ).grid(row = 4, column = 0, sticky = W)

        self.milk_type = StringVar()
        self.milk_type.set(None)
        milk_types = ["Cow", "Coconut", "Young mom"]
        column = 1
        for type in milk_types:
            Radiobutton(self,
                        text = type,
                        variable = self.milk_type,
                        value = type
                        ).grid(row = 4, column = column, sticky = W)
            column += 1
                                      


root = Tk()
root.title("Milk_bar")
app = Application(root)
root.mainloop()
