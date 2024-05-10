import csv
import ast
import numpy as np

#NOTE DATA IS CORRECT AS PER PERSON'S (YOU AR GREAT)


#######################################################

from datetime import datetime



import os


dict_data={}


def list_folders_relative_to_script():
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # print("script dir ",script_dir)
    # Get a list of all items (files and directories) in the script directory
    items = os.listdir(script_dir)
    # Iterate through each item
    for item in items:
        # Check if the item is a directory
        if os.path.isdir(os.path.join(script_dir, item)):
            # If it is a directory, print its name
            # print(item)
            if(item[0]!='p'):
                continue

            script_dirn=script_dir+f"\\{item}"
            # print(script_dirn) ****
            import json
            session_track_dict={}
           
            with open(item+"\dance.json", 'r',encoding='utf-8') as file:
                    data = json.load(file)
                    # print(int(item[1:]), "--",data,"\n")

                    dict_data[int(item[1:])]=data

# Call the function to list folders relative to the script directory
list_folders_relative_to_script()



#by keys: audio list per person
dict_data = dict(sorted(dict_data.items()))
# print(dict_data.keys())
allfeat=dict_data.values()
# print(allfeat)

#All person in correct index wise already
dance_vara =[]
energy_vara =[]
loudness_vara =[]
mode_vara =[]
speechiness_vara =[]
acoustic_vara =[]
instrument_vara =[]
liveness_vara =[]
valence_vara=[] 
tempo_vara=[]

dance_autocorr =[]
energy_autocorr =[]
loudness_autocorr =[]
mode_autocorr =[]
speechiness_autocorr =[]
acoustic_autocorr =[]
instrument_autocorr =[]
liveness_autocorr =[]
valence_autocorr =[]
tempo_autocorr =[]


for i in allfeat:
    # print(i['tempo_autocorr'])
    dance_vara.append(i["dance_vara"])
    energy_vara.append(i["energy_vara"])
    loudness_vara.append(i["loudness_vara"])
    mode_vara.append(i["mode_vara"])
    speechiness_vara.append(i["speechiness_vara"])
    acoustic_vara.append(i["acoustic_vara"])
    instrument_vara.append(i["instrument_vara"])
    liveness_vara.append(i["liveness_vara"])
    valence_vara.append(i["valence_vara"])
    tempo_vara.append(i["tempo_vara"])

    dance_autocorr.append(i["dance_autocorr"])
    energy_autocorr.append(i["energy_autocorr"])
    loudness_autocorr.append(i["loudness_autocorr"])
    mode_autocorr.append(i["mode_autocorr"])
    speechiness_autocorr.append(i["speechiness_autocorr"])
    acoustic_autocorr.append(i["acoustic_autocorr"])
    instrument_autocorr.append(i["instrument_autocorr"])
    liveness_autocorr.append(i["liveness_autocorr"])
    valence_autocorr.append(i["valence_autocorr"])
    tempo_autocorr.append(i["tempo_autocorr"])



list_of_strings = [str(num) for num in dict_data.keys()]



#//////////////
k10_lis ={}
swls_lis={}
SSQ_Family_lis={}
SSQ_Friends_lis={}
# Open the CSV file in read mode
with open('TOBEUSED_jatin_aggregateScores_of_spotify_user copy.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        # print(f"{lines[0]} {lines[5]}")
        k10_lis[lines[0][1:]]=(lines[5])
        swls_lis[lines[0][1:]]=(lines[17])
        SSQ_Family_lis[lines[0][1:]]=(lines[14])
        SSQ_Friends_lis[lines[0][1:]]=(lines[15])


del k10_lis['oded']
del swls_lis['oded']
del SSQ_Family_lis['oded']
del SSQ_Friends_lis['oded']
# print(k10_lis.keys())
# print(k10_lis.values())
#////////////////



#you have ///////////////////////////////////////////

# Convet in int elemnet beofre using it
k10_lis.values() #k10 list
swls_lis.values() #swls list
SSQ_Family_lis.values() #ssq_family_lis
SSQ_Friends_lis.values() #ssq_friends_lis
dance_vara
energy_vara
loudness_vara
mode_vara
speechiness_vara
acoustic_vara
instrument_vara
liveness_vara
valence_vara 
tempo_vara

dance_autocorr
energy_autocorr
loudness_autocorr
mode_autocorr
speechiness_autocorr
acoustic_autocorr
instrument_autocorr
liveness_autocorr
valence_autocorr
tempo_autocorr

#///////////////////////////

from scipy import stats


k10_lis= list(map(int, k10_lis.values()))

swls_lis= list(map(int, swls_lis.values()))
SSQ_Family_lis= list(map(float, SSQ_Family_lis.values()))
SSQ_Friends_lis= list(map(float, SSQ_Friends_lis.values()))



correlation_coefficient, p_value = stats.spearmanr(k10_lis,speechiness_autocorr)

print("Spearman correlation coefficient:", correlation_coefficient)
print("P-value:", p_value)


#--------------------------------------------gpt 
from scipy import stats
import numpy as np

# Define the variables in the first set
variables_set1 = [
    dance_vara,
    energy_vara,
    loudness_vara,
    mode_vara,
    speechiness_vara,
    acoustic_vara,
    instrument_vara,
    liveness_vara,
    valence_vara,
    tempo_vara
]

# Define the variables in the second set as a list containing k10_lis
variables_set2 = [k10_lis]

# Create an empty matrix to store correlation coefficients
correlation_matrix = np.zeros((len(variables_set1), len(variables_set2)))

# Calculate Spearman correlation for each pair of variables
for i, var1 in enumerate(variables_set1):
    for j, var2 in enumerate(variables_set2):
        correlation_coefficient, _ = stats.spearmanr(var1, var2)
        correlation_matrix[i, j] = correlation_coefficient

# Print the correlation matrix
print("Spearman Correlation Matrix:")
print(correlation_matrix)


#///////////////////////////////gpt 2

# import matplotlib.pyplot as plt
# import seaborn as sns

# # Define the variables in the first set
# variables_set1 = [
#     dance_vara,
#     energy_vara,
#     loudness_vara,
#     mode_vara,
#     speechiness_vara,
#     acoustic_vara,
#     instrument_vara,
#     liveness_vara,
#     valence_vara,
#     tempo_vara
# ]

# # Define the variables in the second set
# variables_set2 = [
#     k10_lis,
#     swls_lis,
#     SSQ_Family_lis,
#     SSQ_Friends_lis
# ]

# # Calculate Spearman correlation for each pair of variables
# correlation_matrix = np.zeros((len(variables_set1), len(variables_set2)))

# for i, var1 in enumerate(variables_set1):
#     for j, var2 in enumerate(variables_set2):
#         correlation_coefficient, _ = stats.spearmanr(var1, var2)
#         correlation_matrix[i, j] = correlation_coefficient

# # Transpose the correlation matrix
# correlation_matrix_transposed = correlation_matrix.T

# # Create a heatmap of the transposed Spearman correlation matrix
# plt.figure(figsize=(10, 6))
# sns.heatmap(correlation_matrix_transposed, annot=True, fmt=".2f", cmap="coolwarm", 
#             xticklabels=["dance", "energy", "loudness", "mode", 
#                          "speechiness", "acoustic", "instrument", 
#                          "liveness", "valence", "tempo"], 
#             yticklabels=["k10_lis", "swls_lis", "SSQ_Family_lis", "SSQ_Friends_lis"])
# plt.title("Spearman Correlation Heatmap for Variability")
# # plt.xlabel("Variables in the first set")
# # plt.ylabel("Variables in the second set")
# plt.savefig("ishan_Vara_corr.png")
# plt.show()



import matplotlib.pyplot as plt
import seaborn as sns

# Define the variables in the first set
variables_set1 = [
    dance_autocorr,
    energy_autocorr,
    loudness_autocorr,
    mode_autocorr,
    speechiness_autocorr,
    acoustic_autocorr,
    instrument_autocorr,
    liveness_autocorr,
    valence_autocorr,
    tempo_autocorr
]

# Define the variables in the second set
variables_set2 = [
    k10_lis,
    swls_lis,
    SSQ_Family_lis,
    SSQ_Friends_lis
]

# Calculate Spearman correlation for each pair of variables
correlation_matrix = np.zeros((len(variables_set1), len(variables_set2)))
p_values_matrix = np.zeros((len(variables_set1), len(variables_set2)))

for i, var1 in enumerate(variables_set1):
    for j, var2 in enumerate(variables_set2):
        correlation_coefficient, p_value = stats.spearmanr(var1, var2)
        correlation_matrix[i, j] = correlation_coefficient
        p_values_matrix[i, j] = p_value

# Transpose the correlation matrix
correlation_matrix_transposed = correlation_matrix.T

# Create a mask where True indicates significant p-values (p < 0.06)
significant_mask = p_values_matrix < 0.06

# Create a custom annotation matrix with stars for significant p-values and empty strings for others
annotation_matrix = [['*' if sig else '' for sig in row] for row in significant_mask]

# Create the heatmap with custom annotations and transposed representation
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix_transposed, annot=True, fmt=".2f", cmap="coolwarm", 
            yticklabels=["k10_lis", "swls_lis", "SSQ_Family_lis", "SSQ_Friends_lis"], 
            xticklabels=["dance", "energy", "loudness", "mode", 
                         "speechiness", "acoustic", "instrument", 
                         "liveness", "valence", "tempo"])
plt.title("Spearman Correlation Heatmap for Intertia (autocorrelation with lag 1 session)")


# Loop through cells and annotate significant p-values with stars
for i in range(len(variables_set2)):
    for j in range(len(variables_set1)):
        if p_values_matrix[j, i] < 0.06:
            plt.text(j + 0.5, i + 0.5, "*", ha="center", va="center", color="black")

plt.ylabel("* represents significant p < 0.05".upper(),fontsize=12)
plt.savefig("ishan_Inertia_pvalStar.png")
plt.show()
