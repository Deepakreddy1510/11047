import matplotlib.pyplot as plt

# Open the file in read mode
with open("data.txt", "r") as file:
    # Read the content of the file
    lines = file.readlines()

    # Parse the data
    data = [list(map(float, line.split())) for line in lines]

    # Extract x and y values
    x, y = zip(*data)

    # Plot the terms
    plt.stem(x, y, markerfmt='o', linefmt='b-', basefmt='r-')
    plt.title('Terms of the Sequence x(n)')
    plt.xlabel('n')
    plt.ylabel('x(n)')
    plt.grid(True)
    plt.show()
    plt.savefig('plot.png')
