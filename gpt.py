from tabulate import tabulate

def display_table(data, headers=["Mã SV", "Tên", "Tuổi", "Ngành", "Lớp", "Điểm"]):
    table = [[i + 1, student["id"], student["name"], student["age"], student["major"], student["Class"], student["grade"]] for i, student in enumerate(data)]
    
    print(tabulate(table, headers=headers, tablefmt="grid"))
    print()