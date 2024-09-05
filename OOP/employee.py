class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number
    
    def get_name(self):
        return self.__name
    
    def get_number(self):
        return self.__number
    
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        super().__init__(name, number)
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

    def get_shift_number(self):
        return self.__shift_number
    
    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate
    
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

class ShiftSupervisor(Employee):
    def __init__(self, name, number, annual_salary, annual_bonus):
        super().__init__(name, number)
        self.__annual_salary = annual_salary
        self.__annual_bonus = annual_bonus
    
    def get_annual_salary(self):
        return self.__annual_salary

    def get_annual_bonus(self):
        return self.__annual_bonus
    
    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary
    
    def set_annual_bonus(self, annual_bonus):
        self.__annual_bonus = annual_bonus

def create_production_worker():
    name = input("Enter the employee's name: ")
    number = input("Enter the employee's number: ")
    shift_number = int(input("Enter the shift number (1 for day, 2 for night): "))
    hourly_pay_rate = float(input("Enter the hourly pay rate: "))

    worker = ProductionWorker(name, number, shift_number, hourly_pay_rate)
    
    return worker

def create_shift_supervisor():
    name = input("Enter the supervisor's name: ")
    number = input("Enter the supervisor's number: ")
    annual_salary = float(input("Enter the annual salary: "))
    annual_bonus = float(input("Enter the annual bonus: "))

    supervisor = ShiftSupervisor(name, number, annual_salary, annual_bonus)
    
    return supervisor

def main():
    worker = create_production_worker()
    
    print("\nEmployee Information:")
    print("Name:", worker.get_name())
    print("Number:", worker.get_number())
    print("Shift Number:", worker.get_shift_number())
    print("Hourly Pay Rate: ${:.2f}".format(worker.get_hourly_pay_rate()))

    supervisor = create_shift_supervisor()
    
    print("\nShift Supervisor Information:")
    print("Name:", supervisor.get_name())
    print("Number:", supervisor.get_number())
    print("Annual Salary: ${:.2f}".format(supervisor.get_annual_salary()))
    print("Annual Bonus: ${:.2f}".format(supervisor.get_annual_bonus()))

if __name__ == "__main__":
    main()