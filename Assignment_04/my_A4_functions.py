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
import numpy as np
import math
import doctest

##################################################
# Function Definitions
##################################################

# Exercise 1
def matrix_inverse(mat_in:list) -> list:
    """Calculates the inverse of a 2×2 matrix using the analytical formula,
    ensuring it is invertible. Uses nested loops to construct the inverse matrix
    and returns the result as a 2×2 NumPy array.

    >>> matrix_inverse([[1,2],[1,2],[2,3]])
    Error! mat_in must be 2x2 array
    >>> matrix_inverse([[1,2],[1,2]])
    Error! Determinant is 0
    >>> matrix_inverse([[1,0],[0,1]])
    array([[ 1., -0.],
           [-0.,  1.]])
    >>> matrix_inverse([[1,2],[1,0]])
    array([[0. ,  1. ],
           [0.5, -0.5]])
    >>> matrix_inverse([[2,3],[3,4]])
    array([[-4.,  3.],
           [ 3., -2.]])
    >>> matrix_inverse([[0,10],[20,2]])
    array([[-0.01,  0.05],
           [ 0.1 ,  0.  ]])
    """
    # test cases do not have proper input format. (-1)
    # precondition checks, first for dimensions, and then for determinant feasibility
    if np.shape(mat_in) != (2,2): # CHECK if dimensions of array are not 2x2
        print("Error! mat_in must be 2x2 array")
        return None
    elif mat_in[0][0]*mat_in[1][1] == mat_in[0][1]*mat_in[1][0]: # CHECK if ad - bc = 0
        print("Error! Determinant is 0")
        return None
    # calc
    mat_out = [[0,0],[0,0]] # initialize 2x2 matrix [[a,b][c,d]]. Also possible to use np.zeros([2,2])
    factor = 1 / (mat_in[0][0]*mat_in[1][1] - mat_in[0][1]*mat_in[1][0]) # calculate the factor 1/(ad - bc)
    
    for i in range(2):
        for j in range(2): 
            if i == j: # mat_in[0][0] and mat_in[1][1] (a and d)
                mat_out[i][j] = factor * mat_in[1-i][1-j] # swap a to [1][1] and d to [0][0]
            else:
                mat_out[i][j] = (-factor) * mat_in[i][j] # b and c do not require swap but need to become negative
    # answer: return mat_out
    return np.array(mat_out) # factor * [[d,-b],[-c,a]] in NumPy array
    ########################

# Exercise 2

def logit_like_sum(y:list, x:list, b0:float, b1:float): # expected output? (-1)
    """
    logit_like_sum calculates the sum of all log likelihood events giving
    that the observation y equals 1 if the event occurred and 0 if it did not.
    The function uses logit link functions to compute the chances of an event
    happening and sums the log likelihood across all observations.

    >>> logit_like_sum([1,2,1],[1,12],10,1)
    Error! y and x must contain same number of items
    Error! y must be 0 or 1 only
    Number of errors: 2
    >>> logit_like_sum([1,0,1],[1,12,2],100,20)
    Cannot take log of nonpositive number. When y=1, logit must be less than or equal to 1
    >>> logit_like_sum([1,0],[math.log(2),math.log(.5)],0,1)
    -0.811
    """
    # precondition checks
    error = 0
    if len(y) != len(x): # CHECK if y and x lengths are not equal
        print("Error! y and x must contain same number of items")
        error += 1
    if not all(observation in [0,1] for observation in y): # CHECK if items in y are not only 0 or 1
        print("Error! y must be 0 or 1 only")
        error += 1
    if error > 0:
        print("Number of errors: " + str(error))
        return None
    # calc
    likelihood_sum = 0 # initialize variable before forloop

    for i in range(len(y)): # for all items in range the length of y
        p = math.exp(b0 + x[i]*b1)
        logit = p/(1 + p) # logit must be inside loop to iterate x[i]
        
        # special inside loop check that relies on x[i] and y[i]
        if y[i] == 0 and logit >= 1 : # CHECK if log of 0 or negative number, edge case which only occurs when y=0
            print("Cannot take log of nonpositive number. When y=1, logit must be less than or equal to 1")
            return None
        else:
            likelihood_sum += math.log(1 - y[i] + logit*(-1)**(1-y[i]))
            # if y[i]=1, takes the log of 1-1 + logit*1
            # if y[i]=0, takes the log of 1-0 + logit*-1
    
    # answer
    return likelihood_sum
    #################

# Exercise 3
def logit_like_grad(y: list, x: list, b0: float, b1: float) -> float:
    """Calculates the gradient vector of the likelihood function
    for the bivariate logistic regression model
    for sevaral pairs of observations in the lists x and y,
    coefficients beta 0 (b0) and beta 1 (b1).
    
    >>> logit_like_grad([1,0,2],[12,1],0,0)
    Error! y and x must have same number of items
    Error! y must be 0 or 1 only
    Number of errors: 2
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
    # precondition checks w/ multiple error msgs
    error = 0
    if len(y) != len(x): # CHECK y and x lengths are not equal
        print("Error! y and x must have same number of items")
        error += 1
    if not all(observation in [0,1] for observation in y): # CHECK items in y are not only 0 or 1
        print("Error! y must be 0 or 1 only")
        error += 1 
    if error > 0:
        print("Number of errors: " + str(error))
        return None
    # calc
    re = [0,0] # initialize vector where re item 0 is k=0 and re item 1 is k=1 before forloop
    k = [0,1] # list of values of k
    
    for i in range(len(y)): # for each item i in range the length of y
        for j in k: # for each item j in list k
            p = math.exp(b0 + x[i]*b1)
            logit = p/(1 + p) # logit function must be inside loop to iterate x[i]

            re[k[j]] += x[i]**k[j] * (y[i] - logit)
            # re[k[j]]==re[0] for k=0; re[k[j]]==re[1] for k=1
            # x[i]**k[j]==1 for k=0; x[i]**k[j]==x[i] for k=1
            # (y[i] - logit)==(1 - logit) for y=1, and (y[i] - logit)==(-logit) for y=0
    
    # previous calculation, left to show work
    """
    re = [0,0] # initialize vector where re item 0 is k=0 and re item 1 is k=1 before the forloop

    for i in range(len(y)): # for items in range of list the length of y
        logit = math.exp(b0+x[i]*b1)/(1+math.exp(b0+x[i]*b1))
    
        if y[i] == 1: # for cases where y[i]=1
            re[0] += 1-logit # for k=0, d_i = 1
            re[1] += x[i]*(1-logit) # for k=1, d_i = x[i]
        if y[i] == 0: # for cases where y[i]=0
            re[0] += -logit # for k=0
            re[1] += -x[i]*logit # for k=1
    """

    # rounding, did not use np.array b/c of spaces that broke doctest checking       
    round_re = [re[0],re[1]]
    # answer
    return round_re 
    ################

# Exercise 4
def CESutility_multi(x: list, a: list, r: float) -> float:
    """
    Calculates the Constant Elasticity of Substitution utility function for valid
    values of the parameters x, a, and r when the consumer's utility is more than two
    goods.

    >>> CESutility_multi([5],[0.5,-0.5],0)
    Error! x and a must have matching length
    Error! all items in x and a must be nonnegative
    Error! r must be positive
    Number of errors: 3
    >>> CESutility_multi([1,2,3,4],[1,0.5,100,11],1)
    10.0
    >>> CESutility_multi([1,1,4],[16,9,4],.5)
    121.0
    """
    # precondition checks w/ multiple error msgs
    error = 0
    if len(x) != len(a):
        print("Error! x and a must have matching length") # CHECK if x and a length not equal
        error += 1
    if not all(quantity > 0 for quantity in x) or not all(weight > 0 for weight in a): # CHECK if x and a <=0
        print("Error! all items in x and a must be nonnegative")
        error += 1
    if r <= 0: # CHECK r is positive number and not 0
        print("Error! r must be positive")
        error += 1
    if error > 0:
        print("Number of errors: " + str(error))
        return None
    # calc
    CES_sum = 0 # initialize variable
    for i in range(len(x)):
        CES_sum += a[i]**(1-r) * x[i]**r
    # answer CES_sum^(1/r)
    return CES_sum**(1/r)
    #####################


##################################################
# Test the examples in your docstrings
##################################################

if __name__ == "__main__":
    doctest.testmod()

# Question 2: Test using the doctest module. 

# Make sure to include exampes in your docstring
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 
##################################################
# End
##################################################
