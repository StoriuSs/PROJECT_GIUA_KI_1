import tkinter as tk
from tkinter import messagebox, ttk
import csv
from gpt import clear_main_frame

STUDENTS_FILE = "students.csv"
ACCOUNTS_FILE = "accounts.csv"

# Load dữ liệu sinh viên 
def load_students():
    students = []
    try:
        with open(STUDENTS_FILE, mode="r", newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['age'] = int(row['age'])
                row['grade'] = float(row['grade'])
                students.append(row)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể tải dữ liệu: {e}")
    return students

# Lưu dữ liệu vào file CSV
def save_students(students):
    try:
        with open(STUDENTS_FILE, mode="w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "name", "age", "major", "Class", "grade"])
            writer.writeheader()
            writer.writerows(students)
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lưu dữ liệu: {e}")
        
# Load dữ liệu tài khoản
def load_accounts():
    accounts = []
    try:
        with open(ACCOUNTS_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                accounts.append(row)
    except FileNotFoundError:
        with open(ACCOUNTS_FILE, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["username", "password", "role"])
            writer.writeheader()
    return accounts

# Bộ lọc
def filter_students(students, main_frame):
        clear_main_frame(main_frame)

        # Tạo giao diện lọc
        tk.Label(main_frame, text="Bộ lọc sinh viên", font=("Arial", 14)).pack(pady=10)
        filters = {}

        # Các trường nhập liệu cho bộ lọc
        fields = [
            ("Tên (hoặc bỏ qua)", "name"),
            ("Ngành học (hoặc bỏ qua)", "major"),
            ("Lớp (hoặc bỏ qua)", "Class"),
            ("Tuổi tối thiểu (măc định: -1)", "min_age"),
            ("Tuổi tối đa (mặc định: 200)", "max_age"),
            ("Điểm tối thiểu (mặc định: -1.0)", "min_grade"),
            ("Điểm tối đa (mặc định: 10.0)", "max_grade"),
        ]

        for label, key in fields:
            frame = tk.Frame(main_frame)
            frame.pack(fill="x", padx=5, pady=2)
            tk.Label(frame, text=label).pack(side="left", padx=5)
            entry = tk.Entry(frame)
            entry.pack(side="right", expand=True, fill="x", padx=5)
            filters[key] = entry

        def apply_filter():
            # Lấy giá trị từ các trường nhập liệu
            name_filter = filters["name"].get().lower()
            major_filter = filters["major"].get().lower()
            class_filter = filters["Class"].get().lower()

            try:
                min_age = int(filters["min_age"].get() or -1)
                max_age = int(filters["max_age"].get() or 200)
            except ValueError:
                messagebox.showerror("Lỗi", "Tuổi phải là số nguyên. Đã sử dụng giá trị mặc định.")
                min_age, max_age = -1, 200

            try:
                min_grade = float(filters["min_grade"].get() or -1.0)
                max_grade = float(filters["max_grade"].get() or 10.0)
            except ValueError:
                messagebox.showerror("Lỗi", "Điểm phải là số thực. Đã sử dụng giá trị mặc định.")
                min_grade, max_grade = -1.0, 10.0

            # Áp dụng bộ lọc
            results = [
                student for student in students
                if (not name_filter or name_filter in student['name'].lower())
                and (not major_filter or student['major'].lower() == major_filter)
                and (not class_filter or student['Class'].lower() == class_filter)
                and (min_age <= student['age'] <= max_age)
                and (min_grade <= student['grade'] <= max_grade)
            ]

            # Hiển thị kết quả
            clear_main_frame(main_frame)
            if results:
                tree = ttk.Treeview(main_frame, columns=("stt", "id", "name", "age", "major", "Class", "grade"), show="headings")
                tree.pack(fill="both", expand=True)

                for col in ["stt", "id", "name", "age", "major", "Class", "grade"]:
                    tree.heading(col, text="STT" if col == "stt" else col.capitalize())
                    tree.column(col, anchor="center")

                for idx, student in enumerate(results, start=1):
                    tree.insert("", "end", values=(idx, student["id"], student["name"], student["age"], student["major"], student["Class"], student["grade"]))
            else:
                tk.Label(main_frame, text="Không tìm thấy sinh viên nào phù hợp với các tiêu chí đã nhập.", font=("Arial", 12), fg="red").pack(pady=10)
                
        tk.Button(main_frame, text="Áp dụng bộ lọc", command=apply_filter).pack(pady=10)