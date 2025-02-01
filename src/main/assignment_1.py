import math

def approximation_algorithm(x0, tol):
    print("Approximation Algorithm\n")
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
    
    print(f"Convergence after {i} iterations\n")
    return x

def bisection_method(left, right, N0, tol):
    print("Bisection Method\n")
    p = 0
    i = 0
    
    while abs(right - left) > tol and i < N0:
        i += 1
        p = (left + right) / 2
        print(f"{i} : {p}")

        f_left = math.pow(left, 3) + 4 * left * left - 10
        f_p = math.pow(p, 3) + 4 * p * p - 10

        if (f_left < 0 and f_p > 0) or (f_left > 0 and f_p < 0):
            right = p
        else:
            left = p

    print(f"\np = {p}\n")
    return p


def fixed_point_iteration(p0, N0, tol):
    print("Fixed Point Iteration\n")
    i = 1
    while i <= N0:
        p = p0 - p0 * p0 * p0 - 4 * p0 * p0 + 10  
        # p = math.sqrt(10 - p0*p0*p0) / 2  

        if math.isnan(p):
            print("\nResult diverges\n")
            return None

        print(f"{i} : {p}")

        if abs(p - p0) < tol:
            print(f"\nSUCCESS after {i} iterations\n")
            return p

        i += 1
        p0 = p

    print("Max iterations reached.\n")
    return None

def newton_raphson_method(p_prev, tol, N0):
    print("Newton-Raphson Method\n")
    i = 1
    print(f"{i} : {p_prev}")
    
    while i <= N0:
        f_prev = math.cos(p_prev) - p_prev
        df_prev = -math.sin(p_prev) - 1
        
        if df_prev != 0:
            p_next = p_prev - (f_prev / df_prev)
            
            if abs(p_next - p_prev) < tol:
                print(f"\np_next = {p_next}")
                print("SUCCESS\n")
                break
            
            i += 1
            p_prev = p_next
            print(f"{i} : {p_prev}")
        else:
            print("FAIL\n")
            break
    
    if i > N0:
        print("Max iterations reached.\n")
    return p_next

if __name__ == "__main__":
    approximation_algorithm(1.5, 0.000001)
    bisection_method(1, 2, 20, 0.001)
    fixed_point_iteration(1.5, 25, 0.000001)
    newton_raphson_method(math.pi/4, 15 * 10**-15, 50)