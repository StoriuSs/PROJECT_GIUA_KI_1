import tkinter as tk
from tkinter import messagebox, ttk
import csv
from gpt import show_students
from hieu import load_students, save_students, load_accounts, filter_students
from huy import add_student
from hoang import edit_student, delete_student
from dat import sort_students, export_to_excel
from duc import analyze_by_major, analyze_by_class

STUDENTS_FILE = "students.csv"
ACCOUNTS_FILE = "accounts.csv"

# Đăng ký tài khoản
def show_register_window():
    # Giao diện đăng kí
    register_window = tk.Toplevel()
    register_window.title("Đăng ký tài khoản")

    tk.Label(register_window, text="Tên đăng nhập:").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(register_window, text="Mật khẩu:").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(register_window, text="Xác nhận mật khẩu:").grid(row=2, column=0, padx=5, pady=5)
    tk.Label(register_window, text="Vai trò:").grid(row=3, column=0, padx=5, pady=5)

    username_entry = tk.Entry(register_window)
    password_entry = tk.Entry(register_window, show="*")
    confirm_password_entry = tk.Entry(register_window, show="*")
    role_combobox = ttk.Combobox(register_window, values=["gv", "sv"], state="readonly")

    username_entry.grid(row=0, column=1, padx=5, pady=5)
    password_entry.grid(row=1, column=1, padx=5, pady=5)
    confirm_password_entry.grid(row=2, column=1, padx=5, pady=5)
    role_combobox.grid(row=3, column=1, padx=5, pady=5)

    # Hàm quản lý logic khi đăng kí
    def register():
        username = username_entry.get().strip()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        role = role_combobox.get()
            
        def save_account(username, password, role):
            with open(ACCOUNTS_FILE, mode="a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["username", "password", "role"])
                writer.writerow({"username": username, "password": password, "role": role})
        
        def username_exists(username):
            accounts = load_accounts()
            return any(account["username"] == username for account in accounts)
        
        if not username or not password or not confirm_password or not role:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return

        if username_exists(username):
            messagebox.showerror("Lỗi", "Tên đăng nhập đã tồn tại.")
            return

        if password != confirm_password:
            messagebox.showerror("Lỗi", "Mật khẩu xác nhận không khớp.")
            return

        save_account(username, password, role)
        messagebox.showinfo("Thành công", "Đăng ký tài khoản thành công.")
        register_window.destroy()

    tk.Button(register_window, text="Đăng ký", command=register).grid(row=4, columnspan=2, pady=10)
    
# Đăng nhập
def show_login_window():
    def login():
        username = username_entry.get().strip()
        password = password_entry.get()

        def validate_login(username, password):
            accounts = load_accounts()
            for account in accounts:
                if account["username"] == username and account["password"] == password:
                    return account["role"]
            return None
        
        if not username or not password:
            messagebox.showerror("Lỗi", "Vui lòng nhập tên đăng nhập và mật khẩu.")
            return

        role = validate_login(username, password)
        if role:
            messagebox.showinfo("Thành công", f"Đăng nhập thành công với vai trò: {role}")
            root.destroy()
            init_ui(role)
        else:
            messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không chính xác.")

    # Giao diện đăng nhập
    root = tk.Tk()
    root.title("Đăng nhập")

    tk.Label(root, text="Tên đăng nhập:").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(root, text="Mật khẩu:").grid(row=1, column=0, padx=5, pady=5)

    username_entry = tk.Entry(root)
    password_entry = tk.Entry(root, show="*")

    username_entry.grid(row=0, column=1, padx=5, pady=5)
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Button(root, text="Đăng nhập", command=login).grid(row=2, columnspan=2, pady=10)
    tk.Button(root, text="Đăng ký", command=show_register_window).grid(row=3, columnspan=2, pady=10)

    root.mainloop()

# Sao lưu dữ liệu
def save_data(students):
    save_students(students)
    messagebox.showinfo("Thông báo", "Dữ liệu đã được lưu.")
    
# Hàm tạo giao diện chính của chương trình
def init_ui(role):
    students = load_students()
    
    root = tk.Tk()
    root.title("Chương Trình Quản Lý Sinh Viên")
    root.state('zoomed')
   
    # Màn hình hiển thị chính
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True)
    
    # Thanh menu
    menu = tk.Menu(root)
    root.config(menu=menu)

    file_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Save Data", command=lambda: save_data(students))
    file_menu.add_command(label="Export to Excel", command=lambda: export_to_excel(students))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    actions_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Actions", menu=actions_menu)

    # Chỉnh sửa các tính năng có thể có của thanh menu tùy thuộc vào role của người dùng
    if role == "gv":
        actions_menu.add_command(label="Hiển thị danh sách", command=lambda: show_students(students, main_frame))
        actions_menu.add_command(label="Thêm sinh viên", command=lambda: add_student(students, main_frame))
        actions_menu.add_command(label="Sửa sinh viên", command=lambda: edit_student(students, main_frame))
        actions_menu.add_command(label="Xóa sinh viên", command=lambda: delete_student(students, main_frame))
        actions_menu.add_command(label="Bộ lọc", command=lambda: filter_students(students, main_frame))
        actions_menu.add_command(label="Sắp xếp", command=lambda: sort_students(students, main_frame))
        actions_menu.add_command(label="Phân tích điểm ngành", command=lambda: analyze_by_major(students, main_frame))
        actions_menu.add_command(label="Phân tích điểm lớp", command=lambda: analyze_by_class(students, main_frame))
    else:
        actions_menu.add_command(label="Hiển thị danh sách", command=lambda: show_students(students, main_frame))
        actions_menu.add_command(label="Bộ lọc", command=lambda: filter_students(students, main_frame))
        actions_menu.add_command(label="Sắp xếp", command=lambda: sort_students(students, main_frame))
        actions_menu.add_command(label="Phân tích điểm ngành", command=lambda: analyze_by_major(students, main_frame))
        actions_menu.add_command(label="Phân tích điểm lớp", command=lambda: analyze_by_class(students, main_frame))

    load_students()
    show_students(students, main_frame)

    root.mainloop()
    
# Chạy chương trình
if __name__ == "__main__":
    show_login_window()