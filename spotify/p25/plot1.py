import json
import matplotlib.pyplot as plt

# Read the JSON file
with open('ri_sessionwise.json', 'r') as f:
    data = json.load(f)


# Exclude the last item from the dataset
# data_without_last =  list(data)[0:-1:1]
data_without_last = {k: v for k, v in data.items() if k != list(data.keys())[-1]}



print(list(data_without_last)[-1])

x = [int(session_number) for session_number in data_without_last.keys()]
y = [float(value) for value in data_without_last.values()]


def calculate_variance(data):
    # Calculate the mean
    mean = sum(data) / len(data)
    
    # Calculate the squared differences from the mean
    squared_diff = [(x - mean) ** 2 for x in data]    
    # Calculate the variance
    variance = sum(squared_diff) / len(data)    
    return variance

# Calculate variance
data = y
variance = calculate_variance(data)


plt.plot(x, y)


plt.title('P25')
# plt.show()


# Plot the data as individual points without connecting lines


plt.xlabel('Session Number')
plt.ylabel('Dynamic RI')
# plt.title('Points Connecting Consecutively')
plt.title('Points Connecting Consecutively ( Variance of RI : {:.3f})'.format(variance)) 
plt.savefig('Plot1.png')
plt.show()