def read_employee_file(filename):
    employees = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')

                emp = {
                    "empno": int(data[0]),
                    "name": data[1],
                    "deptno": int(data[2]),
                    "basic": float(data[3]),
                    "da": float(data[4]),
                    "hra": float(data[5]),
                    "conveyance": float(data[6])
                }

                employees.append(emp)

    except FileNotFoundError:
        print("File not found!")

    return employees


def print_salary_slip(employees, emp_no):
    for emp in employees:
        if emp["empno"] == emp_no:

            total_salary = (
                emp["basic"]
                + emp["da"]
                + emp["hra"]
                + emp["conveyance"]
            )

            print("\n------ Salary Slip ------")
            print(f"Employee No : {emp['empno']}")
            print(f"Name        : {emp['name']}")
            print(f"Department  : {emp['deptno']}")
            print(f"Basic       : {emp['basic']}")
            print(f"DA          : {emp['da']}")
            print(f"HRA         : {emp['hra']}")
            print(f"Conveyance  : {emp['conveyance']}")
            print(f"Total Salary: {total_salary}")
            print("-------------------------\n")

            return

    print("Employee not found!")


def print_employees_by_department(employees, dept_no):

    print(f"\nEmployees in Department {dept_no}:")

    found = False

    for emp in employees:
        if emp["deptno"] == dept_no:
            print(f"EmpNo: {emp['empno']}, Name: {emp['name']}")
            found = True

    if not found:
        print("No employees found in this department.")


# Main Program
filename = "employees.txt"

employees = read_employee_file(filename)

while True:

    print("\n1. Print Salary Slip")
    print("2. Print Employees by Department")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        emp_no = int(input("Enter Employee Number: "))
        print_salary_slip(employees, emp_no)

    elif choice == '2':
        dept_no = int(input("Enter Department Number: "))
        print_employees_by_department(employees, dept_no)

    elif choice == '3':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")