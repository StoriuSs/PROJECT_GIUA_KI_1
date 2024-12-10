from gpt import display_table


# In ra tất cả các sinh viên hiện có trong students.csv bằng display_table()
def view_students(students):
    
    if not students:
        print("Chưa có sinh viên nào trong danh sách!\n")
    else:
        print("Danh sách sinh viên:")
        display_table(students)
        
        
def sort_students(students):
    print("Chọn tiêu chí sắp xếp:")
    print("1. Theo tên")
    print("2. Theo tuổi")
    print("3. Theo điểm")
    
    choice = input("Nhập lựa chọn (1-3): ")
    
    if choice not in ['1', '2', '3']:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại.\n")
        return
    
    
    print("Chọn thứ tự sắp xếp:")
    print("1. Tăng dần")
    print("2. Giảm dần")
    
    order = input("Nhập lựa chọn (1-2): ")
    
    if order == '1':
        reverse = False
    elif order == '2':
        reverse = True
    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại.\n")
        return
    
    
    if choice == '1':
        # Sắp xếp theo thứ tự: Tên, Tên đệm, họ
        students.sort(key=lambda student: (student["name"].split()[-1].lower(), student["name"].split()[-2].lower(), student["name"].split()[-3].lower()), reverse=reverse)
        print("Đã sắp xếp theo tên.\n")
        display_table(students)
    
    elif choice == '2':
        students.sort(key=lambda student: int(student["age"]), reverse=reverse)
        print("Đã sắp xếp theo tuổi.\n")
        display_table(students)
    
    elif choice == '3':
        students.sort(key=lambda student: float(student["grade"]), reverse=reverse)
        print("Đã sắp xếp theo điểm.\n")
        display_table(students)
    
    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại.\n")
        
        