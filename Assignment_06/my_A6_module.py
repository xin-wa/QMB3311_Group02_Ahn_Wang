# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Jaemin Ahn, Xin Wang
#
# Date: 2/20/25
# 
##################################################
#
# Sample Script for Assignment 4: 
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
def ln_taylor(z:float,n:float) -> float:
    """
    
    
    """
    ln_out = 0
    for k in range(n):
        k+=1
        ln_out += 0 + ((-1)**(k-1))*((1/k)*(z-1)**k)
    return ln_out

#Step 2, transform into root-finding problem e**x - z = 0
def exp_x_diff(x:float,z:float) -> float:
    """
    """
    return math.exp(x) - z

#Step 3, bisection method
def ln_z_bisect(z:float, a_0:float, b_0:float, num_iter:float) ->float:
    """
    """
    #check sign of a_0 b_0, needs to be different
    if exp_x_diff(a_0, z)*exp_x_diff(b_0, z) > 0:
        print("Error! +/- sign of function endpoints a_0 and b_0 are the same.")
        return None
    #assign a_0 b_0 based on their sign
    if exp_x_diff(a_0, z) > 0:
        pos = a_0
        neg = b_0
    else:
        pos = b_0
        neg = a_0
    #forloop that recursively checks midpoints of function
    for k in num_iter:
        m_i = (pos+neg)/2
        f_mid = exp_x_diff(m_i, z)
        
        if f_mid == 0: #if f_mid==0, func is solved
            return m_i
        elif f_mid > 0: #else keep iterating by assigning midpoint as new +/- values
            pos = m_i
        else:
            neg = m_i
    
    return m_i

#Step 4, derivative of e**x - z
def exp_x_diff_prime(x:float,z:float) -> float:
    """
    """
    return math.exp(x) #the derivative is e**x

def ln_z_newton(z:float, x0:float, tol:float, num_iter:float) -> float:
    """
    """
    
    x_i = x0
    for i in range(num_iter):
        
        x_i = x_i - exp_x_diff(x_i,z)/exp_x_diff_prime(x_i,z)
        if (abs(exp_x_diff(x_i)) < tol):
            return x_i

    print("Exceeded maximum number of iterations.")
    return None

def exp_x_fp_fn(x:float,z:float) -> float:
    """
    """
    return (z - math.exp(x) + 2*x)/2

def ln_z_fixed_pt(z:float,x0:float,tol:float,num_iter:float) -> float:
    """
    """
    x_star = x0
    for i in range(num_iter):
        x_next = exp_x_fp_fn(x_star, z)
        if abs(exp_x_fp_fn(x_star,z)-x_star) < tol:
            print("Tolerance reached."
                  +" Iterations: "+str(i))
            return x_star
        x_star = x_next
    if i == num_iter - 1 and abs(exp_x_fp_fn(x_star,z)-x_star) > tol:
        print('Maximum number of iterations reached.')

##################################################
# Test examples.
##################################################
if __name__ == "__main__":
    doctest.testmod()
    
##################################################
# End
##################################################