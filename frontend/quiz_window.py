import tkinter as tk
from tkinter import messagebox

class QuizWindow:
    def __init__(self, master, questions):
        self.master = master
        self.master.title("Quiz Time!")
        self.master.geometry("600x600")
        self.master.configure(bg="#f7f7f7")

        self.questions = questions
        self.current_q = 0
        self.score = 0
        self.selected_answer = tk.StringVar()

        # Header
        tk.Label(master, text="Let's Begin the Quiz!", font=("Helvetica", 20, "bold"),
                 bg="#4a90e2", fg="white", pady=15).pack(fill="x")

        # Question area
        self.frame = tk.Frame(master, bg="#f7f7f7")
        self.frame.pack(pady=40)

        self.question_label = tk.Label(self.frame, text="", wraplength=500,
                                       bg="#f7f7f7", font=("Helvetica", 14))
        self.question_label.pack(pady=10)

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.frame, text="", variable=self.selected_answer,
                                value="", font=("Helvetica", 12), bg="#f7f7f7", anchor="w")
            rb.pack(fill="x", padx=20, pady=5)
            self.radio_buttons.append(rb)

        # Navigation buttons
        nav_frame = tk.Frame(master, bg="#f7f7f7")
        nav_frame.pack(pady=20)

        self.next_btn = tk.Button(nav_frame, text="Next", bg="#4a90e2", fg="white",
                                  font=("Helvetica", 12, "bold"), width=12, command=self.next_question)
        self.next_btn.pack()

        self.load_question()

    def load_question(self):
        q = self.questions[self.current_q]
        self.question_label.config(text=f"Q{self.current_q+1}. {q['question']}")
        self.selected_answer.set(None)
        for i, opt in enumerate(q['options']):
            self.radio_buttons[i].config(text=opt, value=opt)

    def next_question(self):
        selected = self.selected_answer.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select an answer.")
            return

        if selected == self.questions[self.current_q]['answer']:
            self.score += 1

        self.current_q += 1
        if self.current_q < len(self.questions):
            self.load_question()
        else:
            self.finish_quiz()

    def finish_quiz(self):
        messagebox.showinfo("Quiz Completed", f"You scored {self.score} / {len(self.questions)}")
        self.master.destroy()
