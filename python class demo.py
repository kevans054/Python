class Employee:
    def __init__(self, f_name, l_name, pay, title, hire_day):
        self.first_name = f_name
        self.last_name = l_name
        self.salary = pay
        self.position = title
        self.start_date = hire_day

    def tiny_pay_raise(self):
        self.salary = self.salary + 0.01

    def custom_pay_raise(self, amount):
        self.salary = self.salary + amount


employee_one = Employee('Karen', 'Evans', 100000, 'Director', '2021-02-05')

print(employee_one.first_name + " " + employee_one.last_name + " " + "is now paid: " + str(employee_one.salary))

employee_one.tiny_pay_raise()
employee_one.custom_pay_raise(1000000)

employee_two = Employee('Ethan', 'Winters', 2000000, 'CEO', '2021-02-05')

print(employee_two.first_name + " " + employee_two.last_name + " " + "is now paid: " + str(employee_two.salary))
