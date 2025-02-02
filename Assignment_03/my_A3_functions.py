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
    """CESutility_valid finds"""
    if x < 0:
        print("Error! x cannot be negative.")
        return None
    if y < 0:
        print("Error! y cannot be negative.")
        return None
    if r < 0:
        print("Error! r must be positive")
        return None
    else:
        answer = (x**r + y**r)**(1/r)
        return answer

# Exercise (b)
def CESutility_in_budget(x:float, y:float, r:float, p_x:float, p_y:float, w:float) -> float:
    """CESutility_in_budget calculates"""
    if w <= ((p_x * x) + (p_y * y)):
        print("Error! Not in budget.")
        return None
    else:
        return CESutility_valid(x, y, r)

# Exercise (c)
def logit(x, b_0, b_1) -> float:
    answer = (e ** (b_0 + x * b_1))/(1 + e ** (b_0 + x * b_1))
    return answer

# Exercise (d)
def logit_like(y_i, x_i, b_0, b_1) ->float:
    if y_i == 1:
        x = x_i
        return logit(x, b_0, b_1)
    if y_i == 0:
        x = x_i
        return (1 - logit(x, b_0, b_1))


# Only function definitions above this point. 


##################################################
# Run the examples to test these functions
##################################################


# Code goes here.



##################################################
# End
##################################################
