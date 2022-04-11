from random import randint
from tkinter import *

MIN = 1
MAX = 10

class TimesTablesGUI:
    def __init__(self, parent):
        root_frame = Frame(parent)
        root_frame.grid()

        self.question = TimesTableQuestion.random_question(MIN, MAX)
        question_frame = Frame(root_frame)
        question_frame.grid(row=0, column=0, columnspan=2)
        self.question_label = Label(question_frame, text=self.question.question_string())
        self.question_label.grid(row=0, column=0)
        self.answer_entry = Entry(question_frame)
        self.answer_entry.grid(row=0, column=1)

        Button(root_frame, text="Check Answer").grid(row=1, column=0)
        Button(root_frame, text="Next", command=self.next_question).grid(row=1, column=1)
    
    def next_question(self):
        self.question = TimesTableQuestion.random_question(MIN, MAX)
        self.question_label["text"] = self.question.question_string()


class TimesTableQuestion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass

    def random_question(min, max):
        return TimesTableQuestion(randint(min, max), randint(min, max))
    
    def question_string(self):
        return f"{self.x} * {self.y} ="

    def is_correct_answer(self, answer):
        return answer == self.x * self.y

if __name__ == "__main__":
    root = Tk()
    TimesTablesGUI(root)
    root.mainloop()