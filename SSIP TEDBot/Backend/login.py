import pandas as pd

# Load the Excel file into a DataFrame
excel_file = 'Database\\Educator.xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(excel_file)

# Input the phone number you want to search for
phone_number_to_search = '6665554443'  # Replace with the phone number you're looking for

# Search for the phone   number in the DataFrame
result = df[df['6665554443'] == phone_number_to_search]  # Replace 'Phone Number' with the actual column name

# Check if the phone number was found
if not result.empty:
    print("Phone number found in the Excel sheet.")
    print(result)
else:
    print("Phone number not found in the Excel sheet.")
