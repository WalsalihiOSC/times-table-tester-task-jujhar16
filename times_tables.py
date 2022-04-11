from random import randint
from secrets import choice
from tkinter import *

MIN = 1
MAX = 10

# all the available colors that look good on a light background
DARK_COLORS = ["black", "red", "green", "blue", "magenta"]

class TimesTablesGUI:
    def __init__(self, parent):
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)

        root_frame = Frame(parent)
        root_frame.grid(row=0, column=0, sticky="news")
        root_frame.columnconfigure(tuple(range(2)), weight=1)
        root_frame.rowconfigure(tuple(range(3)), weight=1)

        self.question = TimesTableQuestion.random_question(MIN, MAX)
        question_frame = Frame(root_frame)
        question_frame.grid(row=0, column=0, columnspan=2)
        self.question_label = Label(question_frame, text=self.question.question_string())
        self.question_label.grid(row=0, column=0)
        self.answer_entry = Entry(question_frame)
        self.answer_entry.grid(row=0, column=1)

        Button(root_frame, text="Check Answer", command=self.check_answer).grid(row=1, column=0, sticky="s")
        Button(root_frame, text="Next", command=self.next_question).grid(row=1, column=1, sticky="s")

        self.answer_check_label = Label(root_frame, text="")
        self.answer_check_label.grid(row=2, column=0, columnspan=2)

    def check_answer(self):
        try:
            self.answer_check_label["text"] = "Correct" if self.question.is_correct_answer(int(self.answer_entry.get())) else "Incorrect"
        except:
            self.answer_check_label["text"] = "Invalid Input"
        previous_color = self.answer_check_label["fg"]
        color = previous_color
        # TODO: this loop could run forever technically
        while color == previous_color:
            color = choice(DARK_COLORS)
        self.answer_check_label["fg"] = color

    def next_question(self):
        self.question = TimesTableQuestion.random_question(MIN, MAX)
        self.question_label["text"] = self.question.question_string()
        self.answer_check_label["text"] = ""


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