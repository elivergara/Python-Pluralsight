""# ---------------------------------------------------------------------------------
# Code Owner: Eli Vergara
# Date: 4-October-2024
#
# Purpose:
# This script is designed to automate the process of copying a specified worksheet
# from an existing Excel workbook multiple times. Specifically, it takes a sheet named
# 'July' and makes copies of it named 'August', 'September', 'October', 'November',
# and 'December'. This can be useful for tasks like preparing monthly reports.
#
# Instructions:
# 1. Update the 'folder_path' variable with the path to your Excel workbook directory.
# 2. Update the 'filename' variable with the name of your Excel file.
# 3. Ensure that the workbook contains a sheet named 'July'.
# 4. Run the script to create copies of the 'July' worksheet with the new names specified.
# ---------------------------------------------------------------------------------

import openpyxl
import os

class ExcelSheetCopier:
    def __init__(self, folder_path, filename, sheet_to_copy, new_sheet_names):
        # Initialize the instance with the provided folder path, file name, sheet to copy, and new sheet names
        self.folder_path = folder_path
        self.filename = filename
        self.filepath = os.path.join(folder_path, filename)
        self.sheet_to_copy = sheet_to_copy
        self.new_sheet_names = new_sheet_names
        self.workbook = None  # Placeholder for the workbook; will be assigned later

    def load_workbook(self):
        # Load the Excel workbook from the specified file path
        if not os.path.exists(self.filepath):
            # If the file does not exist, print an error message and return False
            print(f"The file at {self.filepath} does not exist.")
            return False
        # Load the workbook using openpyxl and assign it to self.workbook
        self.workbook = openpyxl.load_workbook(self.filepath)
        return True

    def copy_sheets(self):
        # Copy the specified sheet to create new sheets with the given names
        if self.sheet_to_copy not in self.workbook.sheetnames:
            # If the sheet to copy does not exist, print an error message and exit the method
            print(f"The sheet '{self.sheet_to_copy}' does not exist in the workbook.")
            return
        
        # Get the original sheet that needs to be copied
        original_sheet = self.workbook[self.sheet_to_copy]
        # Loop through the list of new sheet names and create copies of the original sheet
        for new_sheet_name in self.new_sheet_names:
            # Create a copy of the original sheet
            new_sheet = self.workbook.copy_worksheet(original_sheet)
            # Rename the newly created sheet to the new sheet name
            new_sheet.title = new_sheet_name

    def save_workbook(self):
        # Save the workbook to the same file path, including all changes
        self.workbook.save(self.filepath)
        print("Sheets copied successfully.")

    def execute(self):
        # Execute the complete process: load the workbook, copy sheets, and save changes
        if self.load_workbook():
            self.copy_sheets()
            self.save_workbook()

# Set the folder path and file name to your Excel file here
folder_path = r"your\path\to\folder"
filename = "workbook.xlsx"
# Specify the sheet to be copied and the new sheet names
sheet_to_copy = 'July'
new_sheet_names = ['August', 'September', 'October', 'November', 'December']

# Create an instance of ExcelSheetCopier and execute the process
sheet_copier = ExcelSheetCopier(folder_path, filename, sheet_to_copy, new_sheet_names)
sheet_copier.execute()