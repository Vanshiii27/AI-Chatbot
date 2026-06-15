import tkinter as tk

# ----------------- Admission Window -----------------
def open_admission_window():
    win = tk.Toplevel()
    win.title("Admission Information")
    win.geometry("400x300")

    tk.Label(
        win,
        text="ADMISSION DETAILS",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    info = (
        "• Admission process is ONLINE\n"
        "• Visit college official website\n"
        "• Fill application form\n"
        "• Upload required documents\n"
        "• Pay admission fees\n"
        "• Confirmation via email"
    )

    tk.Label(win, text=info, justify="left").pack(padx=20, pady=10)

# ----------------- Exam Schedule Window -----------------
def open_exam_window():
    win = tk.Toplevel()
    win.title("Exam Schedule")
    win.geometry("450x350")

    tk.Label(
        win,
        text="EXAM SCHEDULE",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    schedule = (
        "Semester Exams Schedule\n\n"
        "• Mathematics : 10 March 2026\n"
        "• Computer Science : 13 March 2026\n"
        "• English : 16 March 2026\n"
        "• Database Management : 18 March 2026\n"
        "• Practical Exams : 22–25 March 2026\n\n"
        "Exam Timing: 10:00 AM – 1:00 PM"
    )

    tk.Label(win, text=schedule, justify="left").pack(padx=20, pady=10)

# ----------------- Chatbot Logic -----------------
def get_reply(event=None):
    user_input = entry.get().lower()

    if user_input == "":
        return

    chat.insert(tk.END, "You: " + user_input + "\n")

    if "admission" in user_input:
        chat.insert(tk.END, "Chatbot: Opening admission window...\n\n")
        open_admission_window()

    elif "exam" in user_input:
        chat.insert(tk.END, "Chatbot: Opening exam schedule...\n\n")
        open_exam_window()

    elif "fees" in user_input:
        chat.insert(
            tk.END,
            "Chatbot: Fee details are available in the accounts department.\n\n"
        )

    elif "internship" in user_input:
        chat.insert(
            tk.END,
            "Chatbot: Internship support is provided by the placement cell.\n\n"
        )

    elif "library" in user_input:
        chat.insert(
            tk.END,
            "Chatbot: Library is open from 9 AM to 5 PM.\n\n"
        )

    elif "hello" in user_input or "hi" in user_input:
        chat.insert(
            tk.END,
            "Chatbot: Hello! How can I help you today?\n\n"
        )

    else:
        chat.insert(
            tk.END,
            "Chatbot: Sorry, I am still learning. Please try another query.\n\n"
        )

    entry.delete(0, tk.END)

# ----------------- Clear Chat -----------------
def clear_chat():
    chat.delete(1.0, tk.END)
    chat.insert(
        tk.END,
        "🤖 Welcome to AI Student Helpdesk Chatbot\n\n"
    )

# ----------------- GUI Window -----------------
window = tk.Tk()
window.title("AI Student Helpdesk Chatbot")
window.geometry("500x550")

chat = tk.Text(window, wrap=tk.WORD)
chat.pack(pady=10)

scroll = tk.Scrollbar(window, command=chat.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
chat.config(yscrollcommand=scroll.set)

entry = tk.Entry(window, width=45)
entry.pack(pady=5)
entry.bind("<Return>", get_reply)

send_btn = tk.Button(window, text="Send", command=get_reply)
send_btn.pack()

clear_btn = tk.Button(window, text="Clear Chat", command=clear_chat)
clear_btn.pack(pady=5)

chat.insert(
    tk.END,
    "🤖 Welcome to AI Student Helpdesk Chatbot\n\n"
)

window.mainloop()