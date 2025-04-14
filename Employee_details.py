class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

def get_employee_data(num_employees):
    employees = []
    for i in range(num_employees):
        name = input(f"Enter name for employee {i+1}: ")
        age = int(input(f"Enter age for employee {i+1}: "))
        salary = float(input(f"Enter salary for employee {i+1}: "))
        employee = Employee(name, age, salary)
        employees.append(employee)
    return employees

def main():
    num_employees = int(input("Enter the number of employees: "))
    employees = get_employee_data(num_employees)
    for employee in employees:
        print(employee)

if __name__ == "__main__":
    main()
