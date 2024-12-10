import csv
from gpt import display_table
# Hàm tải thông tin sinh viên có trong students.csv
def load_students(FILE_NAME):
    # Tạo 1 list trống để lưu thông tin sinh viên
    students = []
    try:
        # Mở file ở chế độ read
        with open(FILE_NAME, 'r') as file:
            # Dùng DictReader để đọc thông tin trong students.csv như các dictionaries
            # Dòng đầu tiên của file là các key, còn các dòng phía dưới là các value
            # Reader là 1 iterator lưu các dictionaries. Mỗi dictionary lưu thông tin của một sinh viên 
            reader = csv.DictReader(file)
            for student in reader:
                # Lặp qua và thêm từng dictionary vào list students
                students.append(student)
    except FileNotFoundError:
        # Nếu file students.csv không tồn tại, bỏ qua và trả về list rỗng
        pass
    # Trả về list các sinh viên đã đọc được từ file
    return students


# Hàm lưu thông tin các sinh viên sau khi đã thêm, xóa, sửa
def save_students(students, FILE_NAME):    
    # Mở file ở chế độ write, nếu file đã tồn tại sẽ bị ghi đè
    with open(FILE_NAME, 'w') as file:
        # Xác định các cột để ghi thông tin vào file
        fieldnames = ['id', 'name', 'age', 'major', 'Class', 'grade']
        # Đặt biến writer là 1 đối tượng của class csv.DictWriter
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # Ghi dòng đầu tiên (các key)
        writer.writeheader()
        # Nhận vào list students để ghi các dòng còn lại 
        writer.writerows(students)
        
        
# Hàm lọc sinh viên
def filter_students(students):
    name_filter = input("Nhập tên (hoặc bỏ qua): ").lower()
    major_filter = input("Nhập ngành học (hoặc bỏ qua): ").lower()
    class_filter = input("Nhập tên lớp (hoặc bỏ qua): ")
    
    try:
        # Nhập tuổi tối thiểu và tối đa. Nếu người dùng chỉ nhấn Enter, mặc định là -1 và 200
        min_age = int(input("Nhập tuổi tối thiểu (hoặc mặc định: -1): ") or -1)
        max_age = int(input("Nhập tuổi tối đa (hoặc mặc định: 200): ") or 200)
    except ValueError:
        # Nếu người dùng không nhập số, in ra thông báo 
        print("Bạn không nhập số! Đã chọn giá trị mặc định.")
        min_age, max_age = -1, 200

    try:
        # Nhập điểm tối thiểu và tối đa. Nếu người dùng chỉ nhấn Enter, mặc định là -1.0 và 10.0
        min_grade = float(input("Nhập điểm tối thiểu (mặc định: -1.0): ") or -1.0)
        max_grade = float(input("Nhập điểm tối đa (mặc định: 10.0): ") or 10.0)
    except ValueError:
        print("Bạn không nhập số! Đã chọn giá trị mặc định.")
        min_grade, max_grade = -1.0, 10.0

    # Áp dụng các bộ lọc
    results = [
        student for student in students
        if (not name_filter or name_filter in student['name'].lower())
        and (not major_filter or student['major'].lower() == major_filter)
        and (not class_filter or student['Class'] == class_filter)
        and (min_age <= int(student['age']) <= max_age)
        and (min_grade <= float(student['grade']) <= max_grade)
    ]
    
    # Hiển thị kết quả
    if results:
        display_table(results)
    else:
        print("Không tìm thấy sinh viên nào phù hợp với các tiêu chí đã nhập.\n")

