import tkinter as tk
from tkinter import messagebox

questions = [
    {"question": "What is the capital of India?", "options": ["Delhi", "Mumbai", "Chennai", "Kolkata"], "answer": "Delhi"},
    {"question": "Which is the largest planet?", "options": ["Earth", "Venus", "Jupiter", "Mars"], "answer": "Jupiter"},
    {"question": "Python is a ___", "options": ["Snake", "Language", "Fruit", "Car"], "answer": "Language"},
    {"question": "Which day comes after Friday?", "options": ["Thursday", "Sunday", "Saturday", "Monday"], "answer": "Saturday"},
]

class QuizApp:
    def __init__(self, root):  
        self.root = root
        self.root.title("Quiz App")
        self.q_index = 0
        self.score = 0
        self.selected = tk.StringVar()

        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, justify="left")
        self.question_label.pack(pady=20)

        self.options = []
        for _ in range(4):
            btn = tk.Radiobutton(root, text="", variable=self.selected, font=("Arial", 12), anchor="w", value="")
            btn.pack(fill="x", padx=50, pady=5)
            self.options.append(btn)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        self.selected.set(None)
        q = questions[self.q_index]
        self.question_label.config(text=f"Q{self.q_index + 1}: {q['question']}")
        for i, opt in enumerate(q["options"]):
            self.options[i].config(text=opt, value=opt)

    def next_question(self):
        if not self.selected.get():
            messagebox.showwarning("No Selection", "Please select an answer!")
            return

        if self.selected.get() == questions[self.q_index]["answer"]:
            self.score += 1

        self.q_index += 1
        if self.q_index < len(questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"Your score is: {self.score}/{len(questions)}")
        self.root.destroy()
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
