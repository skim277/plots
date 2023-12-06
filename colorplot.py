import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

# Load data from Excel file
file_path = 'data.xlsx'
df = pd.read_excel(file_path)

# Extract x, y, and z values from the DataFrame
x = df['x']
y = df['y']
z = df['z']


# Set fixed min and max values for the color map
min_z = z.min()
max_z = z.max()


# Create scatter plot with color map
scatter = plt.scatter(x, y, c=z, cmap='jet', vmin=min_z, vmax=max_z)

# Add color bar
cbar = plt.colorbar(orientation='horizontal', ticks=[min_z, max_z])
cbar.set_label('Z Values')

# Set custom labels for the color bar
cbar.set_ticklabels([f'{min_z:.2e}', f'{max_z:.2e}'])

# Set axis labels and title
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Scatter Plot with Color Map')
plt.grid(True, linestyle='dotted', alpha=0.5)

# save the plot as scatterplot.png
plt.savefig('scatterplot.png')

# Show the plot
plt.show()

