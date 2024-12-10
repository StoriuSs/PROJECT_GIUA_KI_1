from hieu import save_students

def edit_student(students):
    id = input("Nhập mã sinh viên bạn muốn sửa: ")  # Yêu cầu người dùng nhập mã sinh viên cần chỉnh sửa
    
    for student in students:  # Duyệt qua danh sách sinh viên
        if student["id"] == id:  # Nếu tìm thấy sinh viên có mã trùng khớp
            print("Thông tin hiện tại:")  # Hiển thị thông tin hiện tại của sinh viên
            print(f"name: {student['name']}, age: {student['age']}, major: {student['major']}, class: {student['Class']}, grade: {student['grade']}")
            
            whattoedit = input("Chọn thông tin để sửa: ")  # Người dùng chọn trường thông tin để sửa
            
            try:
                if student[whattoedit]:  # Kiểm tra trường được chọn có tồn tại
                    if whattoedit == 'age':  # Nếu chỉnh sửa tuổi
                        while True:
                            try:
                                age = input('Nhập giá trị mới: ').strip()  # Yêu cầu nhập tuổi mới
                                if age.isdigit() and int(age) > 0:  # Kiểm tra tuổi hợp lệ
                                    student[whattoedit] = age
                                    break
                                print("Giá trị nhập không hợp lệ!")  # Báo lỗi nếu không hợp lệ
                            except ValueError:
                                print("Giá trị nhập không hợp lệ!")    

                    elif whattoedit == 'grade':  # Nếu chỉnh sửa điểm
                        while True:
                            try:
                                grade = float(input('Nhập giá trị mới: ').strip())  # Yêu cầu nhập điểm mới
                                if 0 <= grade <= 10:  # Điểm phải nằm trong khoảng 0-10
                                    student[whattoedit] = grade
                                    break
                                print("Điểm không hợp lệ. Vui lòng nhập một số từ 0 đến 10.")
                            except ValueError:
                                print("Điểm không hợp lệ. Vui lòng nhập một số thực.")

                    else:  # Chỉnh sửa các thông tin khác
                        student[whattoedit] = input("Nhập giá trị mới: ")  # Nhập giá trị mới cho trường được chọn
                    
                    save_students(students, "students.csv")  # Lưu thay đổi vào file CSV
                    print("> Thông tin sinh viên đã được cập nhật <")
                else:
                    print("Giá trị nhập không hợp lệ!")  # Báo lỗi nếu trường thông tin không tồn tại
            except KeyError:
                print("Giá trị nhập không hợp lệ!")  # Báo lỗi nếu có lỗi truy cập trường thông tin
            
            # Hỏi người dùng có muốn tiếp tục sửa thông tin hay không
            print()
            print("Bạn có muốn tiếp tục sửa?")
            print("1. Có")
            print("2. Không")
            choice = input("Chọn 1 hoặc 2: ")
            if choice == '1':
                edit_student(students)  # Gọi lại hàm để sửa thông tin khác
            elif choice == '2':
                pass  # Kết thúc việc sửa thông tin
            else:
                return  # Thoát hàm nếu nhập sai
            
    print("Không tìm thấy sinh viên với mã đã nhập.\n")  # Báo lỗi nếu không tìm thấy sinh viên có mã trùng khớp


def delete_student(students):
    id = input("Nhập mã sinh viên bạn muốn xóa: ")  # Yêu cầu người dùng nhập mã sinh viên cần xóa
    
    for student in students:  # Duyệt qua danh sách sinh viên
        if student["id"] == id:  # Nếu tìm thấy sinh viên có mã trùng khớp
            print("Thông tin hiện tại:")  # Hiển thị thông tin sinh viên
            print(f"name: {student['name']}, age: {student['age']}, major: {student['major']}, class: {student['Class']}, grade: {student['grade']}")
            
            print("Bạn có chắc muốn xóa sinh viên này khỏi hệ thống? (Nhập y nếu có)")  # Yêu cầu xác nhận từ người dùng
            
            choice = input().lower()  # Lấy lựa chọn của người dùng (y/n)
            if choice == "y":  # Nếu người dùng xác nhận xóa
                students.remove(student)  # Xóa sinh viên khỏi danh sách
                save_students(students, "students.csv")  # Lưu danh sách đã chỉnh sửa vào file CSV
                print("Đã xóa sinh viên khỏi hệ thống.\n")
                return  # Thoát hàm sau khi xóa thành công
            else:
                return  # Thoát hàm nếu người dùng không xác nhận xóa
    
    print("Không tìm thấy sinh viên với mã đã nhập.\n")  # Báo lỗi nếu không tìm thấy sinh viên có mã trùng khớp
