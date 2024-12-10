import csv
from hieu import save_students

# Hàm thêm sinh viên. Parameter students là 1 list gồm các dictionaries là thông tin của các sinh viên hiện có trong file students.csv
def add_student(students):
    # Yêu cầu user nhập mã sinh viên
    while True:
        id = input('Nhập mã sinh viên: ').strip()
        if not id:
            print("Mã sinh viên không được để trống. Vui lòng thử lại.")
            continue

        # Kiểm tra nếu mã sinh viên đã tồn tại trong file
        with open("students.csv", 'r') as file:
            reader = csv.DictReader(file)
            if any(student['id'] == id for student in reader):
                print("Mã sinh viên đã tồn tại! Vui lòng nhập mã khác.")
                continue
        break
    
    # Yêu cầu nhập tên sinh viên
    while True:
        name = input('Nhập tên sinh viên: ').strip()
        if name:
            break
        print("Tên sinh viên không được để trống.")

    # Yêu cầu nhập tuổi sinh viên
    while True:
        age = input('Nhập tuổi sinh viên: ').strip()
        if age.isdigit() and int(age) > 0:
            age = int(age)
            break
        print("Tuổi không hợp lệ. Vui lòng nhập một số nguyên dương.")

    # Yêu cầu nhập ngành của sinh viên
    while True:
        major = input('Nhập ngành của sinh viên: ').strip()
        if major:
            break
        print("Ngành không được để trống.")

    # Yêu cầu nhập lớp của sinh viên
    while True:
        Class = input('Nhập lớp của sinh viên: ').strip()
        if Class:
            break
        print("Lớp không được để trống.")

    # Yêu cầu nhập điểm của sinh viên
    while True:
        try:
            grade = float(input('Nhập điểm của sinh viên (0-10): ').strip())
            if 0 <= grade <= 10:
                break
            print("Điểm không hợp lệ. Vui lòng nhập một số từ 0 đến 10.")
        except ValueError:
            print("Điểm không hợp lệ. Vui lòng nhập một số thực.")
    
    # Lưu thông tin của sinh viên này vào 1 dictionary
    new_student = {
        "id": id,
        "name": name,
        "age": age,
        "major": major,
        "Class": Class,
        "grade": grade
    }

    # Thêm dictionary này vào list students
    students.append(new_student)
    # Sao lưu thông tin vào file students.csv
    save_students(students, "students.csv")
    print("Đã thêm sinh viên!\n")