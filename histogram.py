import pandas as pd
import matplotlib.pyplot as plt

# Load data from Excel file
file_path = 'data.xlsx'
df = pd.read_excel(file_path)

# Extract the 'x' values from the DataFrame
x_values = df['his']

# Create a histogram
plt.hist(x_values, bins=30, color='blue', edgecolor='black', alpha=0.7)
#plt.hist(x_values, bins=30, density=True, color='blue', edgecolor='black', alpha=0.7)

# Set axis labels and title
plt.xlabel('X Values')
plt.ylabel('Frequency')
plt.title('Histogram of X Values')

# Add grid
plt.grid(True, linestyle='dotted', alpha=0.5)

# Save the plot as histogram.png
plt.savefig('histogram-frequency.png')

# Show the plot
plt.show()

