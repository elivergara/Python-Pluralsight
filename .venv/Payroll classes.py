class Employee:
    def __init__(self, emp_id, name, hourly_rate):
        self.emp_id = emp_id
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = 0
        self.bonus = 0

    def log_hours(self, hours):
        self.hours_worked += hours

    def add_bonus(self, amount):
        self.bonus += amount

    def calculate_salary(self):
        return (self.hours_worked * self.hourly_rate) + self.bonus

# Example of calculating payroll for employees
employee1 = Employee(101, "Alice", 25)
employee2 = Employee(102, "Bob", 30)

# Log hours and add bonuses
employee1.log_hours(160)  # Alice worked 160 hours this month
employee2.log_hours(170)  # Bob worked 170 hours
employee2.add_bonus(500)  # Bob receives a $500 bonus

# Calculate salaries
print(f"{employee1.name}'s Salary: ${employee1.calculate_salary()}")
print(f"{employee2.name}'s Salary: ${employee2.calculate_salary()}")
