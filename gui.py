from tkinter import *
import os
from graph import Graph
class Gui:
    '''
    the gui class makes the physical gui for the application
    '''
    def __init__(self, window):
        self.window: Tk = window
        self.header: Label = Label(window, text="VOTING APPLICATION", font=("Arial", 16))
        self.header.pack()
        self.frame_one: Frame = Frame(window)
        self.input_ID_label: Label = Label(self.frame_one, text="ID")
        self.input_ID: Entry = Entry(self.frame_one)
        self.input_ID_label.pack(side='left')
        self.input_ID.pack(side='left')
        self.frame_one.pack()
        self.frame_two: Frame = Frame(window)
        self.filler: Label = Label(self.frame_two, text="")
        self.filler.pack()
        self.canidates_label: Label = Label(self.frame_two, text="CANIDATES")
        self.canidates_label.pack()
        self.radio_var: IntVar = IntVar(value=-1)
        self.canidate_1: Radiobutton = Radiobutton(self.frame_two, text="John", value=1, variable = self.radio_var)
        self.canidate_2: Radiobutton = Radiobutton(self.frame_two, text="Jane", value=2, variable = self.radio_var)
        self.canidate_1.pack()
        self.canidate_2.pack()
        self.button_submit: Button = Button(self.frame_two, text="Submit", command=self.submit)
        self.button_submit.pack()
        self.frame_two.pack()
        self.repeatVote: Label = Label(window, text="", font=("Arial", 16), fg="red")
        self.repeatVote.pack()
        self.filler2: Label = Label(window, text="")
        self.filler2.pack()
        self.filler3: Label = Label(window, text="")
        self.filler3.pack()
        self.password_label: Label = Label(window, text="Password")
        self.password_label.pack()
        self.password: Entry = Entry(window, )
        self.password.pack()
        self.graph: Button = Button(window, text="Graph", command=self.graph)
        self.graph.pack()

            


