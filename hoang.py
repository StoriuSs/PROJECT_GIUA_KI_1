import tkinter as tk
from tkinter import messagebox
from gpt import clear_main_frame, show_students

def edit_student(students, main_frame):
    clear_main_frame(main_frame)
    tk.Label(main_frame, text="Sửa thông tin sinh viên").pack()
    tk.Label(main_frame, text="Nhập ID sinh viên cần sửa:").pack()
    id_entry = tk.Entry(main_frame)
    id_entry.pack()

    def find_and_edit():
        student_id = id_entry.get()
        student = None
        for s in students:
            if s["id"] == student_id:
                student = s
                break

        if not student:
            messagebox.showerror("Lỗi", "Không tìm thấy sinh viên với ID này.")
            return

        clear_main_frame(main_frame)
        tk.Label(main_frame, text=f"Sửa thông tin sinh viên ID: {student_id}").pack()
        fields = ["id", "name", "age", "major", "Class", "grade"]
        entries = {}
        for field in fields:
            row = tk.Frame(main_frame)
            row.pack(fill="x", padx=5, pady=5)
            tk.Label(row, text=field.capitalize()).pack(side="left")
            entry = tk.Entry(row)
            entry.pack(side="right", expand=True, fill="x")
            entry.insert(0, student[field])
            entries[field] = entry

        def save_edited_student():
            try:
                for field in fields:
                    if field == "age":
                        student[field] = int(entries[field].get())
                    elif field == "grade":
                        student[field] = float(entries[field].get())
                    else:
                        student[field] = entries[field].get()
                messagebox.showinfo("Thông báo", "Sửa thông tin thành công!")
                show_students(students, main_frame)
            except ValueError as e:
                messagebox.showerror("Lỗi", f"Lỗi nhập liệu: {e}")

        tk.Button(main_frame, text="Lưu", command=save_edited_student).pack(pady=10)

    tk.Button(main_frame, text="Tìm và sửa", command=find_and_edit).pack(pady=10)
    
    
def delete_student(students, main_frame):
        clear_main_frame(main_frame)
        tk.Label(main_frame, text="Xóa sinh viên").pack()
        tk.Label(main_frame, text="Nhập ID sinh viên cần xóa:").pack()
        id_entry = tk.Entry(main_frame)
        id_entry.pack()

        def delete_by_id():
            student_id = id_entry.get()
            student = None  
            for s in students:  
                if s["id"] == student_id:  
                    student = s  
                    break  

            if not student:
                messagebox.showerror("Lỗi", "Không tìm thấy sinh viên với ID này.")
                return
            students.remove(student)
            messagebox.showinfo("Thông báo", "Xóa sinh viên thành công!")
            show_students(students, main_frame)

        tk.Button(main_frame, text="Xóa", command=delete_by_id).pack(pady=10)