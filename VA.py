import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Simulated seismic data (x, y, z coordinates and magnitude)
data = np.random.rand(100, 4) * 100  # Replace with your seismic data

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = data[:, 0]
y = data[:, 1]
z = data[:, 2]
magnitude = data[:, 3]

# Create a scatter plot with color representing magnitude
scatter = ax.scatter(x, y, z, c=magnitude, cmap='viridis', s=20)

# Add a color bar which maps values to colors
cbar = plt.colorbar(scatter)
cbar.set_label('Magnitude')

# Set labels for the axes
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.title('Lunar Seismic Activity')
plt.show()
