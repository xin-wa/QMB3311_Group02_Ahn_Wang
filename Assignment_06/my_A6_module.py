# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Jaemin Ahn, Xin Wang
#
# Date: 3/31/25
# 
##################################################
#
# Sample Script for Assignment 6: 
# Function Definitions
#
##################################################
"""

##################################################
# Import Required Modules
##################################################
import math
import doctest

##################################################
# Function Definitions
##################################################

#Step 1, Taylor Series, works best around 0>z>2
def ln_taylor(z:float,n:int) -> float:
    """
    An infinite sum that approximates the natural logarithm function around z = 1.
    This series converges best when the z is close to 1.
    >>> ln_taylor(1.5, 5)
    .40729
    >>> ln_taylor(2, 10)
    .64563
    >>> ln_taylor(.5, 20)
    -.69315
    """
    tay_out = 0
    for k in range(n):
        k+=1
        tay_out += 0 + ((-1)**(k-1))*((1/k)*(z-1)**k)
    return tay_out
#Step 2, transform into root-finding problem e**x - z = 0
def exp_x_diff(x:float,z:float) -> float:
    """
    Returns the value of e^x-z
    >>> exp_x_diff(1,3)
    -0.2817181715409549
    >>> exp_x_diff(.5,10)
    -8.351278729299871
    >>> exp_x_diff(4,1)
    53.598150033144236
    """
    return math.exp(x) - z

#Step 3, bisection method
def ln_z_bisect(z:float, a_0:float, b_0:float, num_iter: int) ->float:
    """
    Calculating the natural logarithm using the bisection method involves finding
    the root of a function by repeatedly halving an interval. The function ln_z_bisect(z, a0, b0, num_iter)
    first checks that the function values at the endpoints have opposite signs to ensure a root exists.
    It then updates the interval by selecting the midpoint and replacing an endpoint based on sign changes.
    After a set number of iterations, the midpoint provides an approximation of the natural logarithm.
    >>> ln_z_bisect(2, 0, 2, 20)
    0.69314
    >>> ln_z_bisect(1, 0, 0, 20)
    0.0
    >>> ln_z_bisect(1, 0, .5, 10)
    0.00048
    """
    #check sign of a_0 b_0, needs to be different
    if exp_x_diff(a_0, z) * exp_x_diff(b_0, z) > 0:
        print("Error! The signs of function endpoints a_0 and b_0 are the same.")
        return None

    # Assign a_0, b_0 based on their sign
    if exp_x_diff(a_0, z) > 0:
        pos, neg = a_0, b_0
    else:
        pos, neg = b_0, a_0

    # Loop through the specified number of iterations
    for k in range(num_iter):
        m_i = (pos + neg) / 2  # Midpoint of the interval
        f_mid = exp_x_diff(m_i, z)

        # If the function at the midpoint is zero, we have found the root
        if f_mid == 0:
            return m_i
        # If the function value at the midpoint is positive, update the positive bound
        elif f_mid > 0:
            pos = m_i
        # Otherwise, update the negative bound
        else:
            neg = m_i

    # Return the midpoint after the maximum number of iterations
    return m_i

#Step 4, derivative of e**x - z
def exp_x_diff_prime(x:float,z:float) -> float:
    """
    Returns the derivative of exp_x_diff(x, z) with respect to x. Note that
    z is a constant in this function
    >>> exp_x_diff_prime(2,3)
    7.389
    >>> exp_x_diff_prime(0, 5)
    1.0
    >>> exp_x_diff_prime(1, 10)
    2.718
    """
    return math.exp(x) #the derivative is e**x

#Step 5, Newton method
def ln_z_newton(z:float, x0:float, tol:float, num_iter:int) -> float:
    """
    Calculates the approximate natural log of z using Newton's method, starting from
    an initial guess. It updates the guess until the difference between
    the function value and the desired tolerance is small enough
    >>> ln_z_newton(10, 2, 1e-6, 50)
    2.3025
    >>> ln_z_newton(0.5, -1, 1e-6, 100)
    -0.6931
    >>> ln_z_newton(2, 10, 1e-6, 20)
    0.6931
    """
    
    x_i = x0
    for i in range(num_iter):
        x_i = x_i - (exp_x_diff(x_i,z)/exp_x_diff_prime(x_i,z))
        #if (e**x - z) < tol, return x_i
        if (abs(exp_x_diff(x_i, z)) < tol):
            return x_i
    #finished forloop w/out reaching tol
    print("Maximum number of iterations reached.")
    return None

#Step 6, fixed point function
def exp_x_fp_fn(x:float,z:float) -> float:
    """
    Returns the value of g(x) for a given value of x, this is used
    for the fixed point function where g(x) is a value of x* such that
    g(x*) = x*
    >>> exp_x_fp_fn(2, 4)
    0.3054
    >>> exp_x_fp_fn(2, 0)
    -1.6945
    exp_x_fp_fn(0, 23)
    11.0
    """
    return (z - math.exp(x) + 2*x)/2
#Step 7, solving using fixed point method
def ln_z_fixed_pt(z:float,x0:float,tol:float,num_iter:int) -> float:
    """
    Using the fixed point method to find the natural logarithm of z.
    Using the recurrence relation x_i+1 = g(x_i) repeatedly until it reaches
    a value x_n.
    >>> ln_z_fixed_pt(2, 1, 1e-6, 50)
    Tolerance reached. Iterations: 3
    0.6931
    >>> ln_z_fixed_pt(2, 10, 1e-6, 20)
    Maximum number of iterations reached.
    None
    >>> ln_z_fixed_pt(-1, 1, 1e-6, 50)
    Maximum number of iterations reached.
    None
    """
    x_star = x0
    for i in range(num_iter):
        x_next = exp_x_fp_fn(x_star, z)
        #if (.5*(z - e**x + 2x) - x_star) < tol
        if abs(exp_x_fp_fn(x_star,z)-x_star) < tol:
            print("Tolerance reached."+
                   " Iterations: "+str(i))
            return x_star
        x_star = x_next
    #forloop finished w/out reaching tolerance
    print('Maximum number of iterations reached.')
    return None
##################################################
# Test examples.
##################################################
if __name__ == "__main__":
    doctest.testmod()
    
##################################################
# End
##################################################
