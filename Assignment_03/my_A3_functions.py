# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Jaemin Ahn, Xin Wang
#
# Date: Feb 03, 2025
# 
##################################################
#
# Sample Script for Assignment 3: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module
from math import e


##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise (a)
def CESutility_valid(x:float, y:float, r:float) -> float:
    """CESutility_valid finds the Constant Elasticity of Substitution utility function,
    it calculates the two goods x and y, and the elasticity parameter r, when given 
    non-negative numbers for x and y and a strictly positive number for r.
    
    >>> CESutility_valid(3, 2, 1)
    5.0
    >>> CESutility_valid(-3, 2, 1)
    Error! x cannot be negative.
    None
    >>> CESutility_valid(3, -2, 1)
    Error! y cannot be negative.
    None
    """
    if x < 0:
        print("Error! x cannot be negative.")
        return None
    if y < 0:
        print("Error! y cannot be negative.")
        return None
    if r <= 0:
        print("Error! r must be positive")
        return None
    else:
        answer = (x**r + y**r)**(1/r)
        return answer

# Exercise (b)
def CESutility_in_budget(x:float, y:float, r:float, p_x:float, p_y:float, w:float) -> float:
    """CESutility_in_budget is a wrapper of CESutility_valid, making sure that the purchase is
    withing budget by checking on the total expenditures of the first two goods x and y and checking
    to see if it exceeds the budget w, within the prices set by p_x and p_y.
    
    >>> CESutility_in_budget(5, 4, .5, 6, 2, 56)
    17.95
    >>> CESutility_in_budget(2, 4, .5, 6, 2, 12)
    Error! Not in budget.
    None
    >>> CESutility_in_budget(-2, 4, 5, 6, 2, 12)
    Error! x cannot be negative.
    None
    """
    if w < ((p_x * x) + (p_y * y)):
        print("Error! Not in budget.")
        return None
    else:
        return CESutility_valid(x, y, r)

# Exercise (c)
def logit(x:float, b_0:float, b_1:float) -> float:
    """logit computes the logistic function using x as the input, and b_0 as the intercept,
    and b_1 as the coefficient.
    
    >>> logit(2, .5, 3)
    .998
    >>> logit(-14, .5, 3)
    9.48E-19
    >>> logit(-1, -1, 4)
    .00669
    """
    answer = (e ** (b_0 + x * b_1))/(1 + e ** (b_0 + x * b_1))
    return answer

# Exercise (d)
def logit_like(y_i:int, x_i:float, b_0:float, b_1:float) ->float:
    """logit_like is a wrapper which computes the log-likelihood and models binary events, where 1 equals
    if the event occured and 0 if it did not, using x_i as the predictor variable and y_i
    as the binary outcome.

    >>> logit_like(1, .5, 3, 2)
    .9820
    >>> logit_like(0, .5, 3, 2)
    .0180
    >>> logit_like(1, -12, 3, 2)
    7.58256E-10
    """
    if y_i == 1:
        x = x_i
        return logit(x, b_0, b_1)
    if y_i == 0:
        x = x_i
        return (1 - logit(x, b_0, b_1))
    else:
        print("Error! y_i must be equal to 1 or 0.")
        return None

# Only function definitions above this point. 


##################################################
# Run the examples to test these functions
##################################################


# Code goes here.

#Exercise (a)

print("#" + 50*"-")
print("Testing my Examples for Exercise A.")
print("#" + 50*"-")
print("Exercise A, Example 1:")
print("Evaluating CESutility_valid(3, 2, 1)")
print("Expected: " + str(5))
print("Got: " + str(CESutility_valid(3, 2, 1)))

print("#" + 50*"-")
print("Exercise A, Example 2:")
print("Evaluating CESutility_valid(-3, 2, 1)")
print("Expected: " + str('"Error! x cannot be negative" followed by None'))
print("Got: " + str(CESutility_valid(-3, 2, 1)))

print("#" + 50*"-")
print("Exercise A, Example 3:")
print("Evaluating CESutility_valid(3, -2, 1)")
print("Expected: " + str('"Error! y cannot be negative" followed by None'))
print("Got: " + str(CESutility_valid(3, -2, 1)))


#Exercise (b)
print("#" + 50*"-")
print("Testing my Examples for Exercise B.")
print("#" + 50*"-")
print("Exercise B, Example 1:")
print("Evaluating CESutility_in_budget(5, 4, .5, 6, 2, 56)")
print("Expected: " + str(17.94))
print("Got: " + str(CESutility_in_budget(5, 4, .5, 6, 2, 56)))

print("#" + 50*"-")
print("Testing my Examples for Exercise B.")
print("#" + 50*"-")
print("Exercise B, Example 2:")
print("Evaluating CESutility_in_budget(2, 4, .5, 6, 2, 12)")
print("Expected: " + str('"Error! Not in budget." followed by None'))
print("Got: " + str(CESutility_in_budget(2, 4, .5, 6, 2, 12)))


print("#" + 50*"-")
print("Testing my Examples for Exercise B.")
print("#" + 50*"-")
print("Exercise B, Example 3:")
print("Evaluating CESutility_in_budget(-2, 4, 5, 6, 2, 12)")
print("Expected: " + str('"Error! x cannot be negative." followed by None'))
print("Got: " + str(CESutility_in_budget(2, 4, 5, 6, 2, 12)))


#Exercise (c)
print("#" + 50*"-")
print("Testing my Examples for Exercise C.")
print("#" + 50*"-")
print("Exercise C, Example 1:")
print("Evaluating logit(2, .5, 3)")
print("Expected: " + str(.998))
print("Got: " + str(logit(2, .5, 3)))

print("#" + 50*"-")
print("Exercise C, Example 2:")
print("Evaluating logit(-14, .5, 3)")
print("Expected: " + str(9.48E-19))
print("Got: " + str(logit(-14, .5, 3)))

print("#" + 50*"-")
print("Exercise C, Example 3:")
print("Evaluating logit(-1, -1, 4)")
print("Expected: " + str(0.00669))
print("Got: " + str(logit(-1, -1, 4)))


#Exercise (d)
print("#" + 50*"-")
print("Testing my Examples for Exercise D.")
print("#" + 50*"-")
print("Exercise D, Example 1:")
print("Evaluating logit_like(1, .5, 3, 2)")
print("Expected: " + str(0.9820))
print("Got: " + str(logit_like(1, .5, 3, 2)))

print("#" + 50*"-")
print("Exercise D, Example 2:")
print("Evaluating logit_like(0, .5, 3, 2)")
print("Expected: " + str(0.0180))
print("Got: " + str(logit_like(0, .5, 3, 2)))

print("#" + 50*"-")
print("Exercise D, Example 3:")
print("Evaluating logit_like(1, -12, 3, 2)")
print("Expected: " + str(7.58256E-10))
print("Got: " + str(logit_like(1, -12, 3, 2)))
##################################################
# End
##################################################
