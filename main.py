import csv
from gpt import display_table
from hieu import load_students, save_students, filter_students
from huy import add_student
from duc import analyze_by_major, analyze_by_class
from dat import view_students, sort_students
from hoang import edit_student, delete_student

STUDENTS = 'students.csv'
ACCOUNTS = 'accounts.csv'

  
def register():
    # Yêu cầu người dùng nhập tên đăng nhập và mật khẩu
    username = input("Nhập tên đăng nhập: ")
    password = input("Nhập mật khẩu: ")
    repeat_password = input("Nhập lại mật khẩu: ")
    role = input("Nhập vai trò (gv/sv): ").lower()  # Chỉ cho phép vai trò là 'gv' (giảng viên) hoặc 'sv' (sinh viên)
    registered = False  # Biến theo dõi trạng thái đăng ký thành công hay không
    
    try:
        # Mở file chứa tài khoản để kiểm tra xem tên đăng nhập đã tồn tại chưa
        with open(ACCOUNTS, "r") as accounts_file:
            accounts = csv.DictReader(accounts_file)
            for account in accounts:
                if username == account["username"]:  # Nếu tên đăng nhập đã tồn tại
                    print("Tên đăng nhập đã tồn tại! \n")
                    return registered  # Dừng quá trình đăng ký và trả về False
    except FileNotFoundError:
        # Nếu file chưa tồn tại (chưa có tài khoản nào), thông báo lỗi
        print("Có lỗi xảy ra!")
        pass
    
    # Kiểm tra các trường nhập liệu
    if not username or not password or not repeat_password:  # Nếu bỏ trống bất kỳ trường nào
        print("Vui lòng nhập tên đăng nhập và mật khẩu.\n")
        return registered
    if password != repeat_password:  # Nếu mật khẩu nhập lại không khớp
        print("Mật khẩu nhập lại không đúng.\n")
        return registered
    if role not in ["gv", "sv"]:  # Nếu vai trò không hợp lệ
        print("Vui lòng nhập đúng vai trò (gv/sv).\n")
        return registered
    
    # Lưu thông tin tài khoản mới vào file
    with open(ACCOUNTS, "a") as accounts_file: 
        writer = csv.DictWriter(accounts_file, fieldnames=["username", "password", "role"])
        writer.writerow({"username": username, "password": password, "role": role})
    
    # Thông báo đăng ký thành công và cập nhật trạng thái
    print("Đăng ký tài khoản thành công! Chuyển hướng qua đăng nhập.\n")
    registered = True
    return registered
    
    
def login():
    # Yêu cầu người dùng nhập tên đăng nhập và mật khẩu
    username = input("Nhập tên đăng nhập: ")
    password = input("Nhập mật khẩu: ")
    
    # Mở file chứa tài khoản để kiểm tra thông tin đăng nhập
    with open(ACCOUNTS, "r") as accounts_file:
        accounts = csv.DictReader(accounts_file)
        for account in accounts:
            # Kiểm tra tên đăng nhập và mật khẩu có khớp không
            if username == account["username"] and password == account["password"]: 
                print("Đăng nhập thành công!\n")
                return account["role"]  # Trả về vai trò của người dùng (giảng viên hoặc sinh viên)
        
        # Nếu không tìm thấy tài khoản khớp
        print("Sai tên đăng nhập hoặc mật khẩu! Vui lòng nhập lại hoặc đăng ký tài khoản mới.\n") 
        return  # Kết thúc hàm mà không trả về giá trị nào


def menu_gv():
    print("=== Chương trình Quản lý Sinh viên ===")
    print("1. Hiển thị danh sách sinh viên")
    print("2. Thêm sinh viên")
    print("3. Sửa thông tin sinh viên")
    print("4. Xóa sinh viên")
    print("5. Bộ lọc sinh viên")
    print("6. Sắp xếp sinh viên") 
    print("7. Phân tích điểm số theo ngành")
    print("8. Phân tích điểm số theo lớp")
    print("9. Thoát")
    print()


def menu_sv():
    print("=== Chương trình Quản lý Sinh viên ===")
    print("1. Hiển thị danh sách sinh viên")
    print("2. Bộ lọc sinh viên")
    print("3. Sắp xếp sinh viên") 
    print("4. Phân tích điểm số theo ngành")
    print("5. Phân tích điểm số theo lớp")
    print("6. Thoát")
    print()


def main():
    print("Vui lòng đăng nhập hoặc đăng ký tài khoản để tiếp tục: ")
    while True:  
        # Vòng lặp chính để người dùng lựa chọn đăng ký hoặc đăng nhập
        print("1. Đăng ký")  
        print("2. Đăng nhập")  
        selection = input("Chọn một tùy chọn (1-2): ")  # Yêu cầu người dùng chọn chức năng

        if selection == "1": 
            registered = register()  # Gọi hàm register() để thực hiện đăng ký
            if registered:  
                # Nếu đăng ký thành công
                role = login()  # Gọi hàm login() để đăng nhập ngay sau khi đăng ký
                break  # Thoát vòng lặp chính, chuyển qua giao diện chức năng khác

        elif selection == "2":  
            role = login()  # Gọi hàm login() để thực hiện đăng nhập
            if role: 
                # Nếu đăng nhập thành công (hàm login() trả về vai trò)
                break  # Thoát vòng lặp chính, chuyển qua giao diện chức năng khác

        else:  
            # Nếu người dùng nhập tùy chọn không hợp lệ (không phải '1' hoặc '2')
            print("Vui lòng chỉ nhập 1 hoặc 2.\n")  # Hiển thị thông báo yêu cầu nhập lại
    
    students = load_students(STUDENTS)
    if role == "gv":
        while True:
            menu_gv()
            choice = input("Chọn một tùy chọn (1-9): ")
            if choice == '1':
                view_students(students)
            elif choice == '2':
                add_student(students)
            elif choice == '3':
                edit_student(students)  
            elif choice == '4':
                delete_student(students)  
            elif choice == '5':
                filter_students(students)
            elif choice == '6':  
                sort_students(students)
            elif choice == '7':  
                analyze_by_major(students)
            elif choice == '8':  
                analyze_by_class(students)
            elif choice == '9':  
                print("Đã thoát chương trình!")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chỉ nhập các số như trên!\n")

    else:
        while True:
            menu_sv()
            choice = input("Chọn một tùy chọn (1-6): ")
            if choice == '1':
                view_students(students)
            elif choice == '2':
                filter_students(students)  
            elif choice == '3':  
                sort_students(students)
            elif choice == '4':  
                analyze_by_major(students)
            elif choice == '5':  
                analyze_by_class(students)
            elif choice == '6':  
                print("Đã thoát chương trình!")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chỉ nhập các số như trên!\n")
                
                
# Chỉ chạy hàm main khi đây là chương trình chính chứ không phải được import và dùng như 1 module
if __name__ == "__main__":
    main()