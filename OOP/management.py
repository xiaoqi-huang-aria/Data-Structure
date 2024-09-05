import pickle

class Employee:
    def __init__(self, name, id, department, job):
        self.name = name
        self.id = id
        self.department = department
        self.job = job

    def __str__(self):
        return "Name: " + self.name + "\n" + "ID Number: " + self.id + "\n" + "Department: " + self.department + "\n" + "Job Title: " + self.job

def load_data(file_name):
    try:
        with open(file_name, 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return {}

def save_data(file_name, data):
    with open(file_name, 'wb') as file:
        pickle.dump(data, file)

def display_menu():
    print("\nMenu:")
    print("1. Look up an employee")
    print("2. Add a new employee")
    print("3. Change an existing employee’s details")
    print("4. Delete an employee")
    print("5. Quit")

def lookup_employee(employees):
    id_number = input("Enter the employee ID number to look up: ")
    if id_number in employees:
        print(employees[id_number])
    else:
        print("Employee not found.")

def add_employee(employees):
    name = input("Enter the employee's name: ")
    id_number = input("Enter the employee's ID number: ")
    department = input("Enter the employee's department: ")
    job_title = input("Enter the employee's job title: ")
    if id_number not in employees:
        employees[id_number] = Employee(name, id_number, department, job_title)
        print("Employee added successfully.")
    else:
        print("An employee with this ID number already exists.")

def change_employee(employees):
    id_number = input("Enter the employee ID number to change details: ")
    if id_number in employees:
        name = input("Enter the new employee's name: ")
        department = input("Enter the new employee's department: ")
        job_title = input("Enter the new employee's job title: ")
        employees[id_number].name = name
        employees[id_number].department = department
        employees[id_number].job_title = job_title
        print("Employee details updated successfully.")
    else:
        print("Employee not found.")

def delete_employee(employees):
    id_number = input("Enter the employee ID number to delete: ")
    if id_number in employees:
        del employees[id_number]
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")

def main():
    file_name = 'employees.pickle'
    employees = load_data(file_name)

    employees['47899'] = Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
    employees['39119'] = Employee('Mark Jones', '39119', 'IT', 'Programmer')
    employees['81774'] = Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            lookup_employee(employees)
        elif choice == '2':
            add_employee(employees)
        elif choice == '3':
            change_employee(employees)
        elif choice == '4':
            delete_employee(employees)
        elif choice == '5':
            save_data(file_name, employees)
            print("Data saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()