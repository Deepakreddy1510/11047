import math
import matplotlib.pyplot as plt

def x_n(n):
    return 0 if n < 0 else (2 * n - 3) / 6

# Get N from the user
print("//This program will plot the terms of the sequence up to x(n)// \n")
N = int(input("Enter the value of n: "))

# Generate the sequence up to N using a for loop
n_values = list(range(-2, N + 1))
x_values = []

for n in n_values:
    x_values.append(x_n(n))

# Plot the terms without a label
plt.stem(n_values, x_values, markerfmt='o', linefmt='b-', basefmt='r-')

# Other plot settings
plt.title('Terms of the Sequence x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.show()
