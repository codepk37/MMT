from datetime import datetime

# datetime_string = "2021-09-18 15:50"
# datetime_object = datetime.strptime(datetime_string, "%Y-%m-%d %H:%M")
# seconds_since_epoch = datetime_object.timestamp()

# print(seconds_since_epoch)
# datetime_string = "2021-09-19 15:16"
# datetime_object = datetime.strptime(datetime_string, "%Y-%m-%d %H:%M")
# seconds_since_epoch = datetime_object.timestamp()
# print(seconds_since_epoch)

import os

all_static_list=[]

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
            # print(script_dirn) ****

            
            import json
            

            session_track_dict={}

            inti_tot=0
            with open(item+"\\ri_sessionwise.json", 'r',encoding='utf-8') as file:
                    data = json.load(file)

                    # Print the data
                    # print(data[0])
                    last_sess= data["varinace"]#.get("sessionumber")
                    # print("item ",item,"last session  ",last_sess)
                    all_static_list.append(last_sess)


# # # Call the function to list folders relative to the script directory
list_folders_relative_to_script()

import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
     "static ri violin plot": all_static_list
    # 'Category A': [5, 7, 8, 7, 4, 2],
    # 'Category B': [4, 6, 7, 8, 6, 3],
    # 'Category C': [2, 5, 6, 6, 4, 2]
}

# Convert data to DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Create violin plot
sns.violinplot(data=df, inner="quartile")
plt.title('Violin Plot considering all users')
plt.xlabel('Categories')
plt.ylabel('Variance RI')
plt.show()
