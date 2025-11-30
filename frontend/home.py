import tkinter as tk
from tkinter import filedialog, messagebox
from .quiz_window import QuizWindow

# ------------------------- Functions -------------------------
def upload_pdf():
    filename = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if filename:
        lbl_file.config(text=filename)
    else:
        lbl_file.config(text="No file selected")
    return filename

from backend import pdf_reader, gpt_quiz_gen

def start_quiz():
    selected_difficulty = difficulty_var.get()
    filename = lbl_file.cget("text")

    if filename == "No file selected":
        messagebox.showerror("Error", "Please upload a PDF first!")
        return

    # Step 1: Extract text
    pdf_text = pdf_reader.extract_text_from_pdf(filename)
    if not pdf_text:
        messagebox.showerror("Error", "Could not extract text from the PDF.")
        return

    # Step 2: Generate questions
    messagebox.showinfo("Please wait", "Generating quiz questions using AI...")
    questions = gpt_quiz_gen.generate_quiz_questions(pdf_text, selected_difficulty)
    if not questions:
        messagebox.showerror("Error", "Quiz generation failed.")
        return

    # Step 3: Open quiz window
    quiz_window = tk.Toplevel(root)
    QuizWindow(quiz_window, questions)


# ------------------------- Main Window -------------------------
root = tk.Tk()
root.title("Quiz Maker - Home")
root.geometry("600x600")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

# Use grid layout
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=0)
root.grid_columnconfigure(0, weight=1)

# ------------------------- Header -------------------------
header_frame = tk.Frame(root, bg="#4a90e2", height=100)
header_frame.grid(row=0, column=0, sticky="nsew")
header_label = tk.Label(header_frame, text="Quiz Maker Dashboard", bg="#4a90e2",
                        fg="white", font=("Helvetica", 22, "bold"))
header_label.pack(pady=30)

# ------------------------- Content Frame -------------------------
content_frame = tk.Frame(root, bg="#f0f0f0")
content_frame.grid(row=1, column=0, sticky="nsew")

# Upload PDF
btn_upload = tk.Button(content_frame, text="Upload PDF", width=20, bg="#4a90e2", fg="white",
                       font=("Helvetica", 12, "bold"), command=upload_pdf)
btn_upload.pack(pady=10)

lbl_file = tk.Label(content_frame, text="No file selected", bg="#f0f0f0", font=("Helvetica", 12))
lbl_file.pack(pady=5)

# Difficulty Selection
tk.Label(content_frame, text="Select Difficulty Level:", bg="#f0f0f0", font=("Helvetica", 14, "bold")).pack(pady=15)

difficulty_var = tk.StringVar(value="basic")
for level in ["basic", "medium", "hard"]:
    tk.Radiobutton(content_frame, text=level.capitalize(), variable=difficulty_var, value=level,
                   bg="#f0f0f0", font=("Helvetica", 12)).pack(anchor="w", padx=180, pady=5)

# ------------------------- Start Quiz Button -------------------------
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.grid(row=2, column=0, sticky="ew", pady=20)

btn_start = tk.Button(btn_frame, text="Start Quiz", width=20, bg="#50e3c2", fg="white",
                      font=("Helvetica", 14, "bold"), command=start_quiz)
btn_start.pack(pady=10)

root.mainloop()







def start_quiz():
    selected_difficulty = difficulty_var.get()
    if lbl_file.cget("text") == "No file selected":
        messagebox.showerror("Error", "Please upload a PDF first!")
        return

    messagebox.showinfo("Quiz Started", f"Starting {selected_difficulty.capitalize()} quiz...")

    # Replace this with GPT-generated questions later
    sample_questions = [
        {"question": "What does AI stand for?",
         "options": ["Artificial Intelligence", "Advanced Integration", "Automated Input", "Analog Interface"],
         "answer": "Artificial Intelligence"},
        {"question": "Who developed Python?",
         "options": ["Guido van Rossum", "Elon Musk", "Bill Gates", "James Gosling"],
         "answer": "Guido van Rossum"},
        {"question": "Which library is used for Machine Learning in Python?",
         "options": ["TensorFlow", "NumPy", "Matplotlib", "Pandas"],
         "answer": "TensorFlow"}
    ]

    quiz_window = tk.Toplevel(root)
    QuizWindow(quiz_window, sample_questions)

