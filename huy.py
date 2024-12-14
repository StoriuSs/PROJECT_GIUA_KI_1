import tkinter as tk
from tkinter import messagebox
from gpt import clear_main_frame, show_students


def add_student(students, main_frame):
    # Giao diện thêm sinh viên
    clear_main_frame(main_frame)
    tk.Label(main_frame, text="Thêm sinh viên").pack()
    fields = ["id", "name", "age", "major", "Class", "grade"]
    entries = {}

    for field in fields:
        row = tk.Frame(main_frame)
        row.pack(fill="x", padx=5, pady=5)
        tk.Label(row, text=field.capitalize()).pack(side="left")
        entry = tk.Entry(row)
        entry.pack(side="right", expand=True, fill="x")
        entries[field] = entry

    # Hàm lưu sinh viên đã được thêm vào danh sách
    def save_added_student():
        try:
            new_student = {
                "id": entries["id"].get(),
                "name": entries["name"].get(),
                "age": int(entries["age"].get()),
                "major": entries["major"].get(),
                "Class": entries["Class"].get(),
                "grade": float(entries["grade"].get()),
            }

                
            for student in students:
                if student["id"] == new_student["id"]:
                    raise ValueError("ID đã tồn tại.")
            if new_student["age"] < 0:
                raise ValueError("Tuổi phải lớn hơn 0.")
            if new_student["grade"] < 0 or new_student["grade"] > 10:
                raise ValueError("Điểm phải nằm trong khoảng từ 0 đến 10.")
            for info in new_student.values():
                if not info:    
                    raise ValueError("Không được để trống thông tin.")

            students.append(new_student)
            messagebox.showinfo("Thông báo", "Thêm sinh viên thành công!")
            show_students(students, main_frame)
        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))

    tk.Button(main_frame, text="Thêm", command=save_added_student).pack(pady=10)