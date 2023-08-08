import tkinter

class TextInput:
    # obligatory constructor function
    # window is a tkinter widget
    def __init__(self, window, defaultText=""):
        self.defaultText = defaultText
        self.Element = tkinter.Entry(window, fg='grey')
        self.Element.insert(0, defaultText)

    # maybe not a necessary one
    def resetText(self):
        self.Element.delete(0, tkinter.END)
        self.Element.insert(0, self.defaultText)

    # binded functions for focusing in and out
    def textFocusIn(self):
        currentText = self.Element.get()

        if currentText == self.defaultText:
            # clear all of the text within this input
            self.Element.delete(0, tkinter.END)
        self.Element.config(fg='black')

    def textFocusOut(self):
        currentText = self.Element.get()

        if currentText == "":
            self.Element.config(fg='grey')

    # this is what places the entry somewhere and then binds events to it.
    def packAndPlace(self, xPos=0, yPos=0):
        self.Element.pack()
        self.Element.place(x=xPos, y=yPos)
        self.Element.bind("<FocusIn>", lambda x: self.textFocusIn() )
        self.Element.bind("<FocusOut>",lambda x: self.textFocusOut())
