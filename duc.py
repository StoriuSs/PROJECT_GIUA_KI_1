import csv


def analyze_by_major(students): 
    
    major_input = input("Nhập tên ngành cần phân tích: ").lower()
    analysis = {
        "total_students": 0,
        "total_grade": 0,
        "count_excellent": 0,
        "count_good": 0,
        "count_average": 0,
        "count_pass": 0,
        "count_fail": 0
    }
    
    with open('students.csv', 'r') as file:
        reader = csv.DictReader(file)
        for student in reader:
            if student['major'].lower() == major_input:
                analysis['total_students'] += 1
                analysis['total_grade'] += float(student['grade'])
                
                if float(student['grade']) >= 9.0:
                    analysis['count_excellent'] += 1
                elif float(student['grade']) >= 8.0:
                    analysis['count_good'] += 1
                elif float(student['grade']) >= 7.0:
                    analysis['count_average'] += 1
                elif float(student['grade']) >= 5.0:
                    analysis['count_pass'] += 1
                else:
                    analysis['count_fail'] += 1
            
             
    if analysis["total_students"] == 0:
        print(f"Ngành '{major_input}' không tồn tại!")
        return

    
    avg_grade = analysis["total_grade"] / analysis["total_students"]
    
    
    print(f"Ngành: {major_input}")
    print(f"  - Điểm trung bình: {avg_grade:.2f}")
    print(f"  - Số sinh viên: {analysis['total_students']}")
    print(f"  - Xuất sắc (9-10): {analysis['count_excellent']} sinh viên")
    print(f"  - Giỏi (8-8.9): {analysis['count_good']} sinh viên")
    print(f"  - Khá (7-7.9): {analysis['count_average']} sinh viên")
    print(f"  - Trung bình (5-6.9): {analysis['count_pass']} sinh viên")
    print(f"  - Yếu (<5): {analysis['count_fail']} sinh viên\n")
    
    
def analyze_by_class(students): 
    
    class_input = input("Nhập tên lớp cần phân tích: ").lower()
    analysis = {
        "total_students": 0,
        "total_grade": 0,
        "count_excellent": 0,
        "count_good": 0,
        "count_average": 0,
        "count_pass": 0,
        "count_fail": 0
    }
    
    with open('students.csv', 'r') as file:
        reader = csv.DictReader(file)
        for student in reader:
            if student['Class'].lower() == class_input:
                analysis['total_students'] += 1
                analysis['total_grade'] += float(student['grade'])
                
                if float(student['grade']) >= 9.0:
                    analysis['count_excellent'] += 1
                elif float(student['grade']) >= 8.0:
                    analysis['count_good'] += 1
                elif float(student['grade']) >= 7.0:
                    analysis['count_average'] += 1
                elif float(student['grade']) >= 5.0:
                    analysis['count_pass'] += 1
                else:
                    analysis['count_fail'] += 1
            
             
    if analysis["total_students"] == 0:
        print(f"Lớp '{class_input}' không tồn tại!")
        return

    
    avg_grade = analysis["total_grade"] / analysis["total_students"]
    
    
    print(f"Lớp: {class_input}")
    print(f"  - Điểm trung bình: {avg_grade:.2f}")
    print(f"  - Số sinh viên: {analysis['total_students']}")
    print(f"  - Xuất sắc (9-10): {analysis['count_excellent']} sinh viên")
    print(f"  - Giỏi (8-8.9): {analysis['count_good']} sinh viên")
    print(f"  - Khá (7-7.9): {analysis['count_average']} sinh viên")
    print(f"  - Trung bình (5-6.9): {analysis['count_pass']} sinh viên")
    print(f"  - Yếu (<5): {analysis['count_fail']} sinh viên\n")