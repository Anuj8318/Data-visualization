# 1.Hi  i new to Python numpy. Can you generate some real world situations where I can use a nimpy array with some source code
import numpy as np


sales = np.array([150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700])


total_sales = np.sum(sales)
print("Total Sales:", total_sales)


average_sales = np.mean(sales)
print("Average Sales:", average_sales)

# Hi! Let's creste a real the example involving weather data. Use NumPy to analyze temperature data for a week, perform slicing operations, and calculate various statistics indexing, shaping, and reshaping
import numpy as np

# Temperature data for a week (rows: days, columns: times of day)
temperature_data = np.array([
    [15, 20, 18, 14],  # Day 1
    [16, 21, 19, 15],  # Day 2
    [14, 22, 17, 13],  # Day 3
    [17, 23, 20, 16],  # Day 4
    [18, 24, 21, 17],  # Day 5
    [19, 25, 22, 18],  # Day 6
    [20, 26, 23, 19]   # Day 7
])

print("Temperature Data (Week):")
print(temperature_data)

# Slicing: Temperatures at noon for the whole week
noon_temperatures = temperature_data[:, 1]
print("\nNoon Temperatures (Week):")
print(noon_temperatures)

# Calculating statistics
mean_temperature_week = np.mean(temperature_data)
print("\nMean Temperature (Week):", mean_temperature_week)

max_temperature_week = np.max(temperature_data)
print("Max Temperature (Week):", max_temperature_week)

min_temperature_week = np.min(temperature_data)
print("Min Temperature (Week):", min_temperature_week)

mean_temperature_time_of_day = np.mean(temperature_data, axis=0)
print("\nMean Temperature (Time of Day):", mean_temperature_time_of_day)

max_temperature_time_of_day = np.max(temperature_data, axis=0)
print("Max Temperature (Time of Day):", max_temperature_time_of_day)

min_temperature_time_of_day = np.min(temperature_data, axis=0)
print("Min Temperature (Time of Day):", min_temperature_time_of_day)

# Indexing: Get the temperature on Day 3 at evening
day3_evening_temperature = temperature_data[2, 2]
print("\nTemperature on Day 3 (Evening):", day3_evening_temperature)

# Reshaping the data to a 1D array
temperature_data_reshaped = temperature_data.reshape(-1)
print("\nReshaped Temperature Data (1D):")
print(temperature_data_reshaped)

# Reshaping the data back to its original shape
temperature_data_original_shape = temperature_data_reshaped.reshape(7, 4)
print("\nReshaped Back to Original (Week):")
print(temperature_data_original_shape)
