import pandas as pd
from datetime import datetime, timedelta

class Patient:
    def __init__(self, patient_id, name, condition, last_appointment_date, follow_up_interval):
        """
        Initialize a patient record.
        """
        self.patient_id = patient_id
        self.name = name
        self.condition = condition
        self.last_appointment_date = datetime.strptime(last_appointment_date, "%Y-%m-%d")
        self.follow_up_interval = follow_up_interval

    def next_appointment(self):
        """
        Calculate and return the date of the next appointment.
        """
        return self.last_appointment_date + timedelta(days=self.follow_up_interval)

    def is_overdue(self):
        """
        Check if the patient is overdue for their appointment.
        """
        return datetime.now() > self.next_appointment()

    def __str__(self):
        """
        String representation of the patient object for easy display.
        """
        return (f"Patient: {self.name}, Condition: {self.condition}, "
                f"Last Appointment: {self.last_appointment_date.strftime('%Y-%m-%d')}, "
                f"Next Appointment: {self.next_appointment().strftime('%Y-%m-%d')}, "
                f"Overdue: {'Yes' if self.is_overdue() else 'No'}")


class PatientManagement:
    def __init__(self):
        """
        Initialize a patient management system with an empty patient list.
        """
        self.patients = []

    def add_patient(self, patient):
        """
        Add a new patient to the management system.
        """
        self.patients.append(patient)

    def load_patients_from_csv(self, file_path):
        """
        Load patients from a CSV file and add them to the management system.
        """
        df = pd.read_csv(file_path)
        for _, row in df.iterrows():
            patient = Patient(
                patient_id=row['Patient ID'],
                name=row['Name'],
                condition=row['Condition'],
                last_appointment_date=row['Last Appointment Date'],
                follow_up_interval=int(row['Follow-Up Interval (Days)'])
            )
            self.add_patient(patient)

    def track_appointments(self):
        """
        Generate a list of all patients' appointment status.
        
        Returns:
        - List of dictionaries containing each patient's appointment details.
        """
        appointments = []
        for patient in self.patients:
            appointments.append({
                "Patient ID": patient.patient_id,
                "Name": patient.name,
                "Condition": patient.condition,
                "Last Appointment Date": patient.last_appointment_date.strftime('%Y-%m-%d'),
                "Next Appointment Date": patient.next_appointment().strftime('%Y-%m-%d'),
                "Overdue": "Yes" if patient.is_overdue() else "No"
            })
        return appointments

    def get_overdue_patients(self):
        """
        Get a list of patients who are overdue for an appointment.
        
        Returns:
        - List of dictionaries containing overdue patient details.
        """
        overdue_patients = []
        for patient in self.patients:
            if patient.is_overdue():
                overdue_patients.append({
                    "Patient ID": patient.patient_id,
                    "Name": patient.name,
                    "Condition": patient.condition,
                    "Last Appointment Date": patient.last_appointment_date.strftime('%Y-%m-%d'),
                    "Next Appointment Date": patient.next_appointment().strftime('%Y-%m-%d'),
                    "Reminder": f"Reminder: {patient.name} is overdue for an appointment!"
                })
        return overdue_patients

    def export_appointments_to_csv(self, output_file):
        """
        Export the appointment tracking information to a CSV file.
        """
        appointments = self.track_appointments()
        df = pd.DataFrame(appointments)
        df.to_csv(output_file, index=False)
        print(f"Appointments exported successfully to {output_file}")

    def export_reminders_to_csv(self, output_file):
        """
        Export the overdue patients' reminders to a CSV file.
        """
        overdue_patients = self.get_overdue_patients()
        df = pd.DataFrame(overdue_patients)
        df.to_csv(output_file, index=False)
        print(f"Overdue reminders exported successfully to {output_file}")


# Sample Usage:

# Create a PatientManagement system
management = PatientManagement()

# Load patients from the CSV file (adjust path if necessary)
management.load_patients_from_csv("/home/elivergara/Downloads/sample_patient_data.csv")

# Export the tracking status of all appointments to a CSV file
management.export_appointments_to_csv("tracked_appointments.csv")

# Export reminders for overdue patients to a separate CSV file
management.export_reminders_to_csv("overdue_reminders.csv")
