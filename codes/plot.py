import math
import matplotlib.pyplot as plt
import numpy as np

start_n = -2 
end_n = 12
x = np.arange(start_n, end_n + 1, 1)
y = (2*x -3)/6

# Plot the terms
plt.stem(x, y, markerfmt='o', linefmt='b-', basefmt='r-')
plt.title('Terms of the Sequence x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.show()