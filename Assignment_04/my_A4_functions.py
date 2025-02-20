# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Jaemin Ahn, Xin Wang
#
# Date: 2/17/25
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

# import name_of_module
import numpy as np
import math
import doctest
##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1
def matrix_inverse(mat_in):
    """Calculates the inverse of a 2×2 matrix using the analytical formula,
    ensuring it is invertible. Uses nested loops to construct the inverse matrix
    and returns the result as a 2×2 NumPy array.

    >>> matrix_inverse([[1,2],[1,2]])
    Error! Determinant is 0
    >>> matrix_inverse([[2,3],[1,2]])
    array([[ 2., -3.],
           [-1.,  2.]])
    >>> matrix_inverse([[0,10],[11,2]])
    array([[-0.01818182,  0.09090909],
           [ 0.1,         0.        ]]
    """
    if mat_in[0][0]*mat_in[1][1] == mat_in[0][1]*mat_in[1][0]:
        print("Error! Determinant is 0")
        return None
    s = (2,2)
    mat_out = np.zeros(s)
    factor = 1 / (mat_in[0][0]*mat_in[1][1]-mat_in[0][1]*mat_in[1][0])
    for i in range(2):
        for j in range(2):
           if i == j:
               mat_out[i][j] = factor * mat_in[1-i][1-j]
           else:
               mat_out[i][j] = factor * -1 * mat_in[i][j]
    return mat_out
if __name__ == "__main__":
    doctest.testmod() 
# Exercise 2
import numpy as np
import math
import doctest
def logit_like_sum(y:list, x:list, b0:float, b1:float):
    """
    logit_like_sum calculates the sum of all log likelihood events giving
    that the observation y equals 1 if the event occurred and 0 if it did not.
    The function uses logit link functions to compute the chances of an event
    happening and sums the log likelihood across all observations.

    >>> logit_like_sum([1,2,1],[1,12,2],10,1)
    y must equal 0 or 1
    >>> logit_like_sum([1,1],[1,12,2],10,1)
    Error! y and x must contain same number of items
    >>> logit_like_sum([1,2,1],[1,12,2],.1,.2)
    """
    sum = 0
    if len(y) == len(x):
        for i in range(len(y)):
            logit = math.exp(b0 + x[i] * b1)/(1+math.exp(b0 + x[i] * b1))
            if y[i] != 1 or 0:
                print("y must equal 0 or 1")
                return None
                break
            if y[i] == 1:
                sum += math.log(logit)
            if y[i] == 0:
                if 1 - logit <= 0:
                    print("Error! log of number must be positive.")
                    return None
                else:
                    sum += math.log(1 - logit)
                    return sum
            else:
                print("y must equal 0 or 1")
                break
    else:
        print("Error! y and x must contain same number of items")
if __name__ == "__main__":
    doctest.testmod()          

# Exercise 3

def logit_like_grad(y: list, x: list, b0: float, b1: float) -> float:
    """Calculates the gradient vector of the likelihood function
    for the bivariate logistic regression model
    for sevaral pairs of observations in the lists x and y,
    coefficients beta_0 and beta_1.
    
    Notice if you are missing the space after the >>>, 
    it causes an error.
    Also, an example without the >>> does not get run with doctest.
    
    >>> logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], 0.0, 0.0)
    [0.0, 0.0]
    >>> logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], math.log(3), 0.0)
    [-1.0, -10.0]
    >>> logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], math.log(7), 0.0)
    [-1.5, -15.0]
    >>> logit_like_grad([1, 0, 1], [1, 1, 1], 0.0, math.log(2))
    [0.0, 0.0]
    >>> logit_like_grad([1, 0, 1], [1, 1, 1], 0.0, math.log(5))
    [-0.5, -0.5]
    >>> logit_like_grad([1, 0, 1], [3, 3, 3], 0.0, math.log(2))
    [-2/3, -2.0]
    """
    re = [0,0]
    sum = 0 
    for i in range(len(y)):
        logit = math.exp(b0 + x[i] * b1)/(1+math.exp(b0 + x[i] * b1))
        if y[i] == 1:
            sum += (1-logit)
        if y[i] == 0:
            sum += -logit
        re[0] = sum
    sum = 0
    for i in range(len(y)):
        logit = math.exp(b0 + x[i] * b1)/(1+math.exp(b0 + x[i] * b1))
        if y[i] == 1:
            sum += x[i]*(1-logit)
        if y[i] == 0:
            sum += x[i]*(-logit)
        re[1] = sum
    return re
if __name__ == "__main__":
    doctest.testmod()

# Exercise 4
def CESutility_multi(x: list, a: list, r: float) -> float:
    """
    Calculates the Constant Elasticity of Substitution utility function for valid
    values of the parameters x, a, and r when the consumer's utility is more than two
    goods.

    >>> CESutility_multi([2, -3], [0.5, 0.5], 0.5)
    'Error: x and a must be nonnegative'
    >>> CESutility_multi([5, 3], [0.5, 0.5], 1)
    4
    >>> CESutility_multi([2, 3], [1, 0.5], 1)
    3.5
    >>> CESutility_multi([4, 3], [0.5, 2], -1)
    'Error: Total utility is invalid'
    >>> CESutility_multi([1, 2], [0.5, 0.5], -5)
    'Error: Total utility is invalid'
    """

    if len(x) != len(a):
        return "Error: x and a must have the same number of items."
    
    for i in range(len(x)):
        if x[i] < 0 or a[i] < 0:
            return "Error: x and a must be nonnegative"
    
    if r == 0 or r == 1:
        total = sum(a[i] * x[i] for i in range(len(x)))
        return total
    
    total = 0
    for i in range(len(x)):
        total += a[i]**(1 - r) * (x[i]**r)
    
    if r <= 0:
        return "Error: Total utility is invalid"

    return total ** (1 / r)

if __name__ == "__main__":
    doctest.testmod()

##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


# Make sure to include exampes in your docstring
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 




##################################################
# End
##################################################
