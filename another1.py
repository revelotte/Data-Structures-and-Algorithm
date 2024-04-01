import matplotlib.pyplot as plt
import numpy as np

# Define the functions
def f1(x):
    return x**2 + 7*x + 2

def f2(x):
    return 3*x + 2

def f3(x):
    return x**2

def f4(x):
    return x**3

def f5(x):
    return x**5

def f6(x):
    return x**3 + 2*x**2 + x + 10

def f7(x):
    return x**4 - 3*x**3 + 2*x**2 - x + 11

def f8(x):
    return np.sin(x)

def f9(x):
    return x * np.sin(x)

def f10(x):
    return x**5 + 4*x**4 + x**3 - 2*x**2 + 100

# Loop to continuously ask for the value of x
while True:
    # Get user input for x
    x =float(input("Enter the value of x: "))

    # Generate x values from 1 to 50
    x_values = np.arange(1, 51)

    # Plot each function individually with the user-provided value of x

    # Plot f1(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, f1(x_values), label=f'f1(x) = {x**2 + 7*x + 2}')
    plt.title(f'f1(x) = x^2 + 7x + 2 at x = {x}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot f2(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, f2(x_values), label=f'f2(x) = {3*x + 2}')
    plt.title(f'f2(x) = 3x + 2 at x = {x}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot f3(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, f3(x_values), label=f'f3(x) = {x**2}')
    plt.title(f'f3(x) = x^2 at x = {x}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot f4(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, f4(x_values), label=f'f4(x) = {x**3}')
    plt.title(f'f4(x) = x^3 at x = {x}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot f5(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, f5(x_values), label=f'f5(x) = {x**5}')
    plt.title(f'f5(x) = x^5 at x = {x}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot f6(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, f6(x_values), label=f'f6(x) = {x**3 + 2*x**2 + x + 10}')
    plt.title(f'f6(x) = x^3 + 2x^2 + x + 10 at x = {x}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot f7(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, f7(x_values), label=f'f7(x) = {x**4 - 3*x**3 + 2*x**2 - x + 11}')
    plt.title(f'f7(x) = x^4 - 3x^3 + 2x^2 - x + 11 at x = {x}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot f8(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, f8(x_values), label=f'f8(x) = {np.sin(x)}')
    plt.title(f'f8(x) = sin(x) at x = {x}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot f9(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, f9(x_values), label=f'f9(x) = {x * np.sin(x)}')
    plt.title(f'f9(x) = x*sin(x) at x = {x}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot f10(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, f10(x_values), label=f'f10(x) = {x**5 + 4*x**4 + x**3 - 2*x**2 + 100}')
    plt.title(f'f10(x) = x^5 + 4x^4 + x^3 - 2x^2 + 100 at x = {x}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


    # Plot all functions together
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, f1(x_values), label=f'f1(x) = {x**2 + 7*x + 2}')
    plt.plot(x_values, f2(x_values), label=f'f2(x) = {3*x + 2}')
    plt.plot(x_values, f3(x_values), label=f'f3(x) = {x**2}')
    plt.plot(x_values, f4(x_values), label=f'f4(x) = {x**3}')
    plt.plot(x_values, f5(x_values), label=f'f5(x) = {x**5}')
    plt.plot(x_values, f6(x_values), label=f'f6(x) = {x**3 + 2*x**2 + x + 10}')
    plt.plot(x_values, f7(x_values), label=f'f7(x) = {x**4 - 3*x**3 + 2*x**2 - x + 11}')
    plt.plot(x_values, f8(x_values), label=f'f8(x) = {np.sin(x)}')
    plt.plot(x_values, f9(x_values), label=f'f9(x) = {x * np.sin(x)}')
    plt.plot(x_values, f10(x_values), label=f'f10(x) = {x**5 + 4*x**4 + x**3 - 2*x**2 + 100}')
    plt.title(f'Graphs of Functions at x = {x}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Writing data to a text file
    with open('result.txt', 'w') as file:
        for i, val in enumerate(x_values):
            file.write(f'x={val}, f1={f1(val)}, f2={f2(val)}, f3={f3(val)}, f4={f4(val)}, f5={f5(val)}, f6={f6(val)}, f7={f7(val)}, f8={f8(val)}, f9={f9(val)}, f10={f10(val)}\n')

    print("Data has been written to result.txt")
