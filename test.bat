class Employee:
    def__init__(self, f_name, l_name, pay, title, hire_day):
        self.first_name = f_name
        self.last_name = l_name
        self.salary = pay
        self.position = title
        self.start_date = hire_day

        employee_one = Employee('Karen', 'Evans', 100,000, 'Director', '2021-02-05')

        print(employee_one.first_name + '' + employee_one.last_name)

