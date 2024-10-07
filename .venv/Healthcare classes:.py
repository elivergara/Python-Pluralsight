class Patient:
    def __init__(self, patient_id, name, age, weight, height):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.weight = weight  # in kg
        self.height = height  # in meters
        self.medical_history = []

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def add_medical_history(self, condition):
        self.medical_history.append(condition)

    def get_health_risk(self):
        bmi = self.calculate_bmi()
        if bmi > 30:
            return "High Risk (Obesity)"
        elif bmi > 25:
            return "Moderate Risk (Overweight)"
        else:
            return "Low Risk"

# Example patient management
patient1 = Patient(201, "John Doe", 45, 95, 1.75)
patient2 = Patient(202, "Jane Smith", 34, 65, 1.68)

# Add medical conditions and calculate health risk
patient1.add_medical_history("Hypertension")
patient2.add_medical_history("Asthma")

# Print BMI and health risk
print(f"{patient1.name}'s BMI: {patient1.calculate_bmi():.2f}, Health Risk: {patient1.get_health_risk()}")
print(f"{patient2.name}'s BMI: {patient2.calculate_bmi():.2f}, Health Risk: {patient2.get_health_risk()}")

