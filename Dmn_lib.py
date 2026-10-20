"""tkinter excercise"""

from tkinter import *

class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text = "Enter data for a new story"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        Label(self,
              text = "Enter the hero name:"
              ).grid(row = 1, column = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column = 1,sticky = W )              

        Label(self,
              text = "Enter hero traits"
              ).grid(row = 2, column = 0, sticky = W)

        self.is_big = BooleanVar()
        Checkbutton(self,
                    text = "Big",
                    variable = self.is_big
                    ).grid(row = 3, column = 0, sticky = W)

        self.is_brave = BooleanVar()
        Checkbutton(self,
                    text = "Brave",
                    variable = self.is_brave
                    ).grid(row = 3, column = 1, sticky = W)

        Label(self,
              text = "Hero skills"
              ).grid(row = 4, column = 0, sticky = W)

        self.hero_skill = StringVar()
        self.hero_skill.set(None)

        hero_skills = ["sword", "bow", "magic"]
        column = 1
        for skill in hero_skills:
            Radiobutton(self,
                        text = skill,
                        variable = self.hero_skill,
                        value = skill
                        ).grid(row = 4, column = column, sticky = W)
            column += 1

        Button(self,
               text = "Tell story",
               command = self.tell_story
               ).grid(row = 5, column = 0, sticky = W)

        self.story_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_txt.grid(row = 6, column = 0, columnspan = 4, sticky = W)

    def tell_story(self):
        person = self.person_ent.get()
        adjectives = ""
        if self.is_big.get():
            adjectives += "big, "
        if self.is_brave.get():
            adjectives += "brave"
        hero_skill = self.hero_skill.get()

        story = "Well known hero "
        story += person
        story += " took a quest from a king. The quest was to slay the great dragon, "
        story += "who terrorized his kingdom. As a reward, the king offered half "
        story += "of his kingdom and his daughter, the princess, to marry. "
        story += "The hero was "
        story += adjectives
        story += " and handsome. He fought the dragon with his "
        story += hero_skill
        story += " and won. The dragon, laying on the cave floor, said: - Hey hero, "
        story += "you are so "
        story += adjectives
        story += " and handsome. Let's marry and conquer the kingdomn and all the world "
        story += "together - Hero thought for a moment and said - OK - And that is "
        story += "how the half-drake dynasty of warrior kings was created. THE END"

        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)


root = Tk()
root.title("Mad Lib dmn")
app = Application(root)
root.mainloop()
            
