from tkinter import *
from gui import Gui
import os
from graph import Graph
class Logic(Gui):
    '''
    Logic class to handle the logic of the application
    param: Gui
    return: None
    '''
    def __init__(self, window):
        '''
        Initializes the logic class. Also initializes the inherited Gui class
        param: window
        return: None
        '''
        super().__init__(window)


    def submit(self):
        '''
        Checks to make sure that the data is valid. If so, data gets written to the text file votes.txt
        param: None
        return: None
        '''
        if self.radio_var.get() == -1:
            self.repeatVote.config(text="Please Select a Candidate", fg="red")
            
        elif self.input_ID.get() == "":
            self.repeatVote.config(text="Please Enter an ID", fg="red")
        elif self.input_ID.get().strip().isdigit() == False:
            self.repeatVote.config(text="ID must be a number", fg="red")
        
        else:
            if os.path.exists("votes.txt") == False:
                with open ("votes.txt", "w") as fileMake:
                    fileMake.write("")
                    fileMake.close()
            if self.checkIfVoted() == False:
                self.repeatVote.config(text="Already Voted", fg="red")
                self.input_ID.delete(0, END)
                self.radio_var.set(-1)
            else:
                with open ("votes.txt", "a") as file:
                    file.write(self.input_ID.get().strip() + " " + str(self.radio_var.get()) + "\n")
                    file.close()
                    self.input_ID.delete(0, END)
                    self.radio_var.set(-1)
                    self.repeatVote.config(text="Vote Submitted", fg="green")
    def checkIfVoted(self):
        '''
        Checks to see if the ID has already voted
        param: None
        return: Boolean
        '''
        with open("votes.txt", "r") as file:
            for line in file:
                id = line.split(" ")[0]
                if id == self.input_ID.get().strip():
                    file.close()
                    return False
            file.close()
            return True
    def graph(self):
        '''
        makes a graph using the graph class
        param: None
        return: None
        '''
        if self.password.get() == "supersecretpassword":
            Graph().plot()