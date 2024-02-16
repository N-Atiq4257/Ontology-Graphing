import tkinter


class GraphLog:
    """
        initialize it
    """
    def __init__(self):
        self.msg = None # just set up this initially.

    def updateText(self, text):
        # unlock the box

        self.msg.config(state=tkinter.NORMAL)
        self.msg.delete(1.0, "end")  # clear it maybe
        self.msg.insert(1.0, text)
        self.msg.config(state=tkinter.DISABLED)

    def setup(self, window, height=23, width=68):
        self.msg = tkinter.Text(window, height=height, width=width, wrap=tkinter.WORD)
        self.msg.config(state=tkinter.DISABLED)