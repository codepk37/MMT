# import os

# def list_folders_relative_to_script():
#     # Get the directory of the script
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     print("script dir ",script_dir)
#     # Get a list of all items (files and directories) in the script directory
#     items = os.listdir(script_dir)
#     # Iterate through each item
#     for item in items:
#         # Check if the item is a directory
#         if os.path.isdir(os.path.join(script_dir, item)):
#             # If it is a directory, print its name
#             print(item)

# # Call the function to list folders relative to the script directory
# list_folders_relative_to_script()

# # Get the current directory path
# current_directory = os.getcwd()
# print("Current directory:", current_directory)

# current_directory+="\p32"
# print(current_directory)


# def list_files_in_folder(folder_path):
#     # Check if the provided path exists and is a directory
#     if os.path.exists(folder_path) and os.path.isdir(folder_path):
#         # Get a list of all items (files and directories) in the specified folder
#         items = os.listdir(folder_path)
#         # Iterate through each item
#         for item in items:
#             # Check if the item is a file
#             if os.path.isfile(os.path.join(folder_path, item)):
#                 # If it is a file, print its name
#                 print(item)
#     else:
#         print("Invalid folder path or folder does not exist.")

# # Specify the folder path you want to list the files for
# folder_path = current_directory

# # Call the function to list files in the specified folder
# list_files_in_folder(folder_path)

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Example DataFrame
data = pd.DataFrame({
    'A': [1, 1, 1, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 1, 5, 4]
})

# Calculate correlation matrix
corr_matrix = data.corr()

# Plot correlation matrix
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Plot')
plt.show()
