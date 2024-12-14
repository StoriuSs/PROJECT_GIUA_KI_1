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
    tk.Label(main_frame, text="Xóa sinh viên", font=("Arial", 16)).pack(pady=10)
    tk.Label(main_frame, text="Nhập ID sinh viên cần xóa:", font=("Arial", 12)).pack(pady=5)
    
    id_entry = tk.Entry(main_frame, font=("Arial", 12))
    id_entry.pack(pady=5)

    def delete_by_id():
        student_id = id_entry.get().strip()
        student = None  
        
        for s in students:  
            if s["id"] == student_id:  
                student = s  
                break  
        
        if not student:
            messagebox.showerror("Lỗi", "Không tìm thấy sinh viên với ID này.")
            return
        
        student_info = (
            f"ID: {student['id']}\n"
            f"Tên: {student['name']}\n"
            f"Tuổi: {student['age']}\n"
            f"Ngành: {student['major']}\n"
            f"Lớp: {student['Class']}\n"
            f"Điểm: {student['grade']}"
        )
        confirm = messagebox.askyesno(
            "Xác nhận xóa",
            f"Bạn có chắc chắn muốn xóa sinh viên này không?\n\n{student_info}"
        )
        
        if confirm:
            students.remove(student)
            messagebox.showinfo("Thành công", "Sinh viên đã được xóa.")
            show_students(students, main_frame)
        else:
            messagebox.showinfo("Hủy bỏ", "Đã hủy thao tác xóa sinh viên.")
    
    tk.Button(main_frame, text="Xóa", font=("Arial", 12), command=delete_by_id).pack(pady=10)
