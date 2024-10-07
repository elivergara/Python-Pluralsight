import pandas as pd

class MedicalDataProcessor:
    def __init__(self, data):
        """Initialize with data as a DataFrame."""
        self.data = data

    def clean_nulls(self):
        """Remove rows with NULL or NA values."""
        self.data = self.data.dropna()
        return self

    def format_dates(self, date_columns):
        """Format specific columns as datetime."""
        for col in date_columns:
            self.data[col] = pd.to_datetime(self.data[col], errors='coerce')
        return self

    def filter_active(self):
        """Filter out inactive records based on the 'Status' column."""
        self.data = self.data[self.data['Status'] == 'Active']
        return self

    def get_data(self):
        """Return the processed DataFrame."""
        return self.data

# Example usage:
# Load some sample data
data1 = pd.DataFrame({
    'PatientID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Status': ['Active', 'Inactive', 'Active'],
    'DateOfVisit': ['2023-03-01', '2023-03-05', None]
})

# Create an instance of the class
processor = MedicalDataProcessor(data1)

# Clean, format, and filter the data
cleaned_data = (
    processor
    .clean_nulls()            # Remove rows with NULLs
    .format_dates(['DateOfVisit'])  # Format 'DateOfVisit' as datetime
    .filter_active()          # Keep only active patients
    .get_data()               # Get the processed DataFrame
)

print(cleaned_data)
