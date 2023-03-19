#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

def quadratic_eqn_roots(a, b, c):
    """
    Determine the roots of the quadratic equation ax^2 + bx + c = 0
    using bisection method algorithm.
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero.")
    
    # Calculate discriminant
    disc = b**2 - 4*a*c
    
    if disc < 0:
        # No real roots
        return None
    
    elif disc == 0:
        # Single root
        return -b / (2*a)
    
    else:
        # Two roots
        x1 = (-b - math.sqrt(disc)) / (2*a)
        x2 = (-b + math.sqrt(disc)) / (2*a)
        
        # the tolerance for accuracy of the solution
        tol = 1e-6
        
        # the maximum number of iterations
        max_iter = 1000
        
        # Implement the bisection method algorithm
        for i in range(max_iter):
            mid = (x1 + x2) / 2
            fmid = a*mid**2 + b*mid + c
            
            if abs(fmid) < tol:
                return mid
            
            if (a*x1**2 + b*x1 + c) * fmid < 0:
                x2 = mid
            else:
                x1 = mid
        
        # Bisection method failed to converge
        return None

# Get input from the user
a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

# Solve the quadratic equation
roots = quadratic_eqn_roots(a, b, c)

# Print the roots
if roots is None:
    print("The equation has no real roots.")
elif isinstance(roots, float):
    print("The equation has a single root: {:.6f}".format(roots))
else:
    print("The roots of the equation are: {:.6f} and {:.6f}".format(roots[0], roots[1]))
    #the time complexity is
    #O(log)n
    


# In[ ]:




