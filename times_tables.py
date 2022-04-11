from tkinter import *

class TimesTablesGUI:
    def __init__(self, parent):
        root_frame = Frame(parent)
        root_frame.grid()


class TimesTableQuestion:
    def __init__(self):
        pass
    
    def is_correct_answer(self, selected):
        pass

if __name__ == "__main__":
    root = Tk()
    TimesTablesGUI(root)
    root.mainloop()