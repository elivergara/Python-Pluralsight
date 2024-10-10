class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email_static = first + "." + last + "@email.com"  # Static attribute

    # @property
    def email_dynamic(self):
        return f"{self.first}.{self.last}@email.com"  # Dynamic property

emp_1 = Employee("John", "Smith")

print(emp_1.email_static)   # John.Smith@email.com
print(emp_1.email_dynamic)  # John.Smith@email.com

emp_1.first = 'Jim'

print(emp_1.email_static)   # John.Smith@email.com (Doesn't change)
print(emp_1.email_dynamic)  # Jim.Smith@email.com (Changes dynamically)


