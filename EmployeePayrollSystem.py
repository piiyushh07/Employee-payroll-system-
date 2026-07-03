def log_salary(func):
    def wrapper(self):
        salary = func(self)
        with open("salary_log.txt", "a") as file:
            file.write(f"{self.name} - Salary: ₹{salary}\n")
        return salary
    return wrapper


class Employee:
    def __init__(self, name):
        self.name = name

    @log_salary
    def calculate_salary(self):
        return 0


class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    @log_salary
    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate

    @log_salary
    def calculate_salary(self):
        return self.hours * self.rate


employees = []

while True:
    print("\n===== Employee Payroll System =====")
    print("1. Add Full-Time Employee")
    print("2. Add Part-Time Employee")
    print("3. Display Salaries")
    print("4. Export Payroll")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        salary = float(input("Enter Monthly Salary: "))
        employees.append(FullTimeEmployee(name, salary))

    elif choice == "2":
        name = input("Enter Name: ")
        hours = float(input("Enter Hours Worked: "))
        rate = float(input("Enter Hourly Rate: "))
        employees.append(PartTimeEmployee(name, hours, rate))

    elif choice == "3":
        for emp in employees:
            print(emp.name, "- Salary: ₹", emp.calculate_salary())

    elif choice == "4":
        with open("payroll.txt", "w") as file:
            for emp in employees:
                file.write(f"{emp.name},{emp.calculate_salary()}\n")
        print("Payroll exported successfully.")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
