import numpy as np
import matplotlib.pyplot as plt

# Line 1 coordinates
x1 = np.array([-5, 5])
y1 = np.array([7, 2])

# Line 2 coordinates
x2 = np.array([-7, 3])
y2 = np.array([4, -5])

# Mathematical Process for Line 1
slope1 = (y1[1] - y1[0]) / (x1[1] - x1[0])
y_intercept1 = y1[0] - slope1 * x1[0]
equation1 = f'y = {slope1:.2f}x + {y_intercept1:.2f}'

# Mathematical Process for Line 2
slope2 = (y2[1] - y2[0]) / (x2[1] - x2[0])
y_intercept2 = y2[0] - slope2 * x2[0]
equation2 = f'y = {slope2:.2f}x + {y_intercept2:.2f}'

# Plotting
plt.figure(figsize=(8, 8))
plt.plot(x1, y1, '-r', label=f'Line 1: {equation1}')
plt.plot(x2, y2, '-b', label=f'Line 2: {equation2}')
plt.scatter(x1, y1, color='red')
plt.scatter(x2, y2, color='blue')
plt.legend()
plt.grid(True)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Two Lines with Equations')
plt.show()