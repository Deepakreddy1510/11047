import math
import matplotlib.pyplot as plt

def x_n(n):
    if n < 0:
        return 0
    else:
        return  (2*n-3)/6

# Get N from the user
print("//This program will plot the terms of the sequence up to x(n)// \n")
N = int(input("Enter the value of n: "))

# Generate the sequence up to N
n_values = list(range(-2, N+1))
x_values = [x_n(n) for n in n_values]

# Plot the terms
plt.stem(n_values, x_values, markerfmt='o', linefmt='b-', basefmt='r-')
plt.title('Terms of the Sequence x(n)')
plt.xlabel('n')
plt.legend()
plt.ylabel('x(n)')
plt.grid(True)
plt.show()
plt.savefig

