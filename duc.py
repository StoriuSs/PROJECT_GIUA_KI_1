import tkinter as tk
from tkinter import messagebox, ttk
from gpt import clear_main_frame


def analyze_by_major(students, main_frame):
        clear_main_frame(main_frame)
        tk.Label(main_frame, text="Phân tích điểm số theo ngành").pack()
        def perform_analysis():
            major_input = entry_major.get().lower().strip()
            if not major_input:
                messagebox.showwarning("Cảnh báo", "Vui lòng nhập tên ngành!")
                return

            analysis = {
                "total_students": 0,
                "total_grade": 0,
                "count_excellent": 0,
                "count_good": 0,
                "count_average": 0,
                "count_pass": 0,
                "count_fail": 0
            }

            for student in students:
                if student['major'].lower() == major_input:
                    analysis['total_students'] += 1
                    analysis['total_grade'] += float(student['grade'])
                    
                    grade = float(student['grade'])
                    if grade >= 9.0:
                        analysis['count_excellent'] += 1
                    elif grade >= 8.0:
                        analysis['count_good'] += 1
                    elif grade >= 7.0:
                        analysis['count_average'] += 1
                    elif grade >= 5.0:
                        analysis['count_pass'] += 1
                    else:
                        analysis['count_fail'] += 1

            if analysis["total_students"] == 0:
                messagebox.showinfo("Kết quả", f"Ngành '{major_input}' không tồn tại!")
                return

            avg_grade = analysis["total_grade"] / analysis["total_students"]

            result_text = (
                f"Ngành: {major_input}\n"
                f"  - Điểm trung bình: {avg_grade:.2f}\n"
                f"  - Số sinh viên: {analysis['total_students']}\n"
                f"  - Xuất sắc (9-10): {analysis['count_excellent']} sinh viên\n"
                f"  - Giỏi (8-8.9): {analysis['count_good']} sinh viên\n"
                f"  - Khá (7-7.9): {analysis['count_average']} sinh viên\n"
                f"  - Trung bình (5-6.9): {analysis['count_pass']} sinh viên\n"
                f"  - Yếu (<5): {analysis['count_fail']} sinh viên"
            )

            text_result.config(state="normal")
            text_result.delete("1.0", tk.END)
            text_result.insert(tk.END, result_text)
            text_result.config(state="disabled")

        window = tk.Tk()
        window.title("Phân tích ngành học")

        tk.Label(window, text="Nhập tên ngành: ").pack(pady=5)
        entry_major = tk.Entry(window, width=30)
        entry_major.pack(pady=5)

        btn_analyze = tk.Button(window, text="Phân tích", command=perform_analysis)
        btn_analyze.pack(pady=10)

        text_result = tk.Text(window, width=50, height=15, state="disabled")
        text_result.pack(pady=10)

def analyze_by_class(students, main_frame):
        clear_main_frame(main_frame)
        tk.Label(main_frame, text="Phân tích điểm số theo lớp").pack()

        def perform_analysis():
            class_input = entry_class.get().lower().strip()  
            if not class_input:
                messagebox.showwarning("Cảnh báo", "Vui lòng nhập tên lớp!")
                return

            analysis = {
                "total_students": 0,
                "total_grade": 0,
                "count_excellent": 0,
                "count_good": 0,
                "count_average": 0,
                "count_pass": 0,
                "count_fail": 0
            }

            for student in students:
                if student['Class'].lower() == class_input:
                    analysis['total_students'] += 1
                    analysis['total_grade'] += float(student['grade'])

                    grade = float(student['grade'])
                    if grade >= 9.0:
                        analysis['count_excellent'] += 1
                    elif grade >= 8.0:
                        analysis['count_good'] += 1
                    elif grade >= 7.0:
                        analysis['count_average'] += 1
                    elif grade >= 5.0:
                        analysis['count_pass'] += 1
                    else:
                        analysis['count_fail'] += 1

            if analysis["total_students"] == 0:
                messagebox.showinfo("Kết quả", f"Lớp '{class_input}' không tồn tại!")
                return

            avg_grade = analysis["total_grade"] / analysis["total_students"]

            result_text = (
                f"Lớp: {class_input}\n"
                f"  - Điểm trung bình: {avg_grade:.2f}\n"
                f"  - Số sinh viên: {analysis['total_students']}\n"
                f"  - Xuất sắc (9-10): {analysis['count_excellent']} sinh viên\n"
                f"  - Giỏi (8-8.9): {analysis['count_good']} sinh viên\n"
                f"  - Khá (7-7.9): {analysis['count_average']} sinh viên\n"
                f"  - Trung bình (5-6.9): {analysis['count_pass']} sinh viên\n"
                f"  - Yếu (<5): {analysis['count_fail']} sinh viên"
            )

            text_result.config(state="normal")
            text_result.delete("1.0", tk.END)
            text_result.insert(tk.END, result_text)
            text_result.config(state="disabled")

        window = tk.Tk()
        window.title("Phân tích lớp học")

        tk.Label(window, text="Nhập tên lớp: ").pack(pady=5)
        entry_class = tk.Entry(window, width=30)
        entry_class.pack(pady=5)

        btn_analyze = tk.Button(window, text="Phân tích", command=perform_analysis)
        btn_analyze.pack(pady=10)

        text_result = tk.Text(window, width=50, height=15, state="disabled")
        text_result.pack(pady=10)