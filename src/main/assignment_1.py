import math

def approximation_algorithm(x0, tol):
    i = 0
    x = x0
    diff = x0
    print(f"{i} : {x}")

    while diff >= tol:
        i += 1
        y = x
        x = (x / 2) + (1 / x)
        print(f"{i} : {x}")

        diff = abs(x - y)
    
    print(f"\nConvergence after {i} iterations")
    return x