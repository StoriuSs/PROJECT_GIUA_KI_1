from tkinter import ttk

def clear_main_frame(main_frame):
    for widget in main_frame.winfo_children():
        widget.destroy()
        
def show_students(students, main_frame):
    clear_main_frame(main_frame)
    tree = ttk.Treeview(main_frame, columns=("stt", "id", "name", "age", "major", "Class", "grade"), show="headings")
    tree.pack(fill="both", expand=True)

    for col in ["stt", "id", "name", "age", "major", "Class", "grade"]:
        tree.heading(col, text=col.capitalize() if col != "stt" else "STT")
        tree.column(col, anchor="center")

    for idx, student in enumerate(students, start=1):
        tree.insert("", "end", values=(idx, student["id"], student["name"], student["age"], student["major"], student["Class"], student["grade"]))
