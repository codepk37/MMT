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

plt.plot(x, y)

# for i in range(len(x) - 1):
#     plt.scatter([x[i], x[i+1]], [y[i], y[i+1]], color='blue')

# plt.xlabel("X-axis data")
# plt.ylabel("Y-axis data")
plt.title('P30')
# plt.show()


# Plot the data as individual points without connecting lines


plt.xlabel('Session Number')
plt.ylabel('Dynamic RI')
# plt.title('Points Connecting Consecutively')
plt.savefig('Plot1.png')
plt.show()