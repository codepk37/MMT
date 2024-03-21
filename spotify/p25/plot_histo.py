

import json
import matplotlib.pyplot as plt
import numpy as np

# Read the JSON file
with open('ri_sessionwise.json', 'r') as f:
    data = json.load(f)

# Exclude the last item from the dataset
data_without_last = {k: v for k, v in data.items() if k.isdigit() }


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

# Example usage:
data = y
variance = calculate_variance(data)




# Create histogram
hist, bins = np.histogram(y, bins=5)
bin_centers = 0.5 * (bins[:-1] + bins[1:])
hist_normalized = hist / np.sum(hist) *100  # Normalize frequencies to sum up to 1

# Plot histogram
plt.barh(bin_centers, hist_normalized, height=(bins[1] - bins[0]), edgecolor='black')
# plt.title('Histogram')
plt.title('Histogram ( Variance of RI overall: {:.3f})'.format(variance)) 
plt.xlabel('Session count (scaled 100%)')
plt.ylabel('Dynamic RI-session')

# Set y-axis limits from 0 to 1
plt.ylim(0, 1)

plt.savefig('plot_histo.png')

plt.show()
