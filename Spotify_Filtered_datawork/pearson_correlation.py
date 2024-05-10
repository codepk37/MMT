import csv
from scipy.stats import spearmanr

k10_lis ={}

flag=1
# Open the CSV file in read mode
with open('TOBEUSED_jatin_aggregateScores_of_spotify_user.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        if flag:
             flag=0
             continue
        # print(f"{lines[0]} {lines[5]}")
        k10_lis[int(lines[0][1:])]  =int(lines[5])

# k10_lis.pop(0)


print("K10-",k10_lis)
# print(len(k10_lis))

###################


static_dict={}

from datetime import datetime
import os
sessions=[]

def list_folders_relative_to_script():
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print("script dir ",script_dir)
    # Get a list of all items (files and directories) in the script directory
    items = os.listdir(script_dir)
    # Iterate through each item
    for item in items:
        # Check if the item is a directory
        if os.path.isdir(os.path.join(script_dir, item)):
            # If it is a directory, print its name
            # print(item)
            script_dirn=script_dir+f"\\{item}"
            if(item[0]!='p'):
                 continue
            # print(item,"--") #****            
            import json     
            session_track_dict={}

            inti_tot=0
            with open(item+"\\ri_sessionwise.json", 'r',encoding='utf-8') as file:
                    data = json.load(file)

                    # Print the data
                    # print(data[0])
                    sessions.append(len(data)-2)
                    # last_sess= data["ri_tillnow"]#.get("sessionumber")
                    # print("len--data ",len(data))
                    static_dict[int(item[1:])]=data["ri_tillnow"]
                  

# # # Call the function to list folders relative to the script directory
list_folders_relative_to_script()
# print(static_dict)

myKeys = sorted(static_dict.keys())

# Create a new dictionary with sorted keys
sorted_dict = {key: static_dict[key] for key in myKeys}

# Print the sorted dictionary
print("Sorted dictionary:" ,sorted_dict)
# print(sorted_dict)
del sorted_dict[421]
del sorted_dict[141]
del sorted_dict[142]
del sorted_dict[79]
del sorted_dict[367]
del sorted_dict[340]
del sorted_dict[407]
del sorted_dict[184]
del sorted_dict[220]
del sorted_dict[353]

# diff
# print(k10_lis)
# print(set_k10)
print(" --------------  ",set(k10_lis.keys()).difference(set(sorted_dict.keys())))
all_static_list=list(sorted_dict.values()) ##******
# print(sorted_dict)
# all_static_list=sessions

print("sorted ri dict ",sorted_dict.values())

# Example usage
print(len(k10_lis))
print(len(all_static_list))

# Check if the lengths match

# Calculate Pearson correlation coefficient
all_static_list = [float(x) for x in all_static_list]
k10_lis = [float(x) for x in k10_lis]


# # Calculate Spearman correlation coefficient
correlation_coefficient, p_value = spearmanr(all_static_list, k10_lis)

print("Spearman correlation coefficient:", correlation_coefficient)
print("P-value:", p_value)
# # ///////////////////////

# import matplotlib.pyplot as plt
# import numpy as np



# # Define the ranges and corresponding colors
# ranges = [(0, 15), (16, 21), (22, 29), (30, 1000)]
# colors = ['green', 'lightgreen', '#ffad33', '#b30000']

# # Assuming you have all_static_list and k10_lis as lists

# # Convert string values to float
# all_static_list = [float(x) for x in all_static_list]
# k10_lis = [float(x) for x in k10_lis]

# # Determine the range for each k10 value
# k10_ranges = []
# for k10 in k10_lis:
#     for i, (low, high) in enumerate(ranges):
#         if low <= k10 <= high:
#             k10_ranges.append(colors[i])
#             break

# # Create a scatter plot
# plt.scatter(all_static_list, k10_lis, c=k10_ranges, alpha=0.5)

# # Add color bar
# # plt.colorbar(label='k10 range')

# # Add labels and title
# plt.title("Static RI score vs K10 per person")
# plt.xlabel("Static RI")
# plt.ylabel("k10")

# plt.text(0.3, 1.1, f'Spearman correlation coefficient: {correlation_coefficient:.3f}', fontsize=10, color='red', transform=plt.gca().transAxes, ha='center')
# plt.text(.9, 1.1, f'P-value:  {round(p_value,3)}', fontsize=10, color='red', transform=plt.gca().transAxes, ha='center')


# # plt.savefig('correlation_staticRI_k10.png')
# # Show the plot
# plt.show()
