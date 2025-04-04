# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Jaemin Ahn, Xin Wang
#
# Date: 3/14/25
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
import doctest

##################################################
# Function Definitions
##################################################
# copied functions
def CESutility(x: float, y: float, r: float) -> float:
    # precondition check
    if r == 0:
        print("Error! r cannot equal 0.")
    # calc
    answer = (x ** r + y ** r) ** (1/r)
    return answer
def CESutility_valid(x:float, y:float, r:float) -> float:
    # precondition checks
    if x < 0:
        print("Error! x cannot be negative.")
        return None
    if y < 0:
        print("Error! y cannot be negative.")
        return None
    if r <= 0:
        print("Error! r must be positive")
        return None
    # calc
    answer = CESutility(x, y, r)
    return answer
def CESutility_in_budget(x:float, y:float, r:float, p_x:float, p_y:float, w:float) -> float:
    # precondition checks for new variables not found in CESutility_valid
    if p_x <= 0 or p_y <= 0:
        # if either p_x or p_y is < 0
        print("Error! Prices must be positive")
        return None
    elif w < ((p_x * x) + (p_y * y)):
       # print("Error! Not in budget.")
        return None
    # calc, relies on CESutility_valid as a wrapper
    else:
        return CESutility_valid(x, y, r)

##################################################
# Exercise c
def CESdemand_calc(r:float,p_x:float,p_y:float,w:float) -> list[float]:
    """
    Return a list of two values that achieve the maximum value of CES_utility(),
    subject to the budget constraint that the consumers basket of goods should
    cost no more than their wealth.
    
    >>> CESdemand_calc(1, 3, 2, 5)
    Error! r cannot equal 1
    >>> CESdemand_calc(.1, 4, 2, 5)
    [1.3, 0.6]
    >>> CESdemand_calc(0.5, 3, 1, 10)
    [7.5, 0.83]
    """
    # precheck
    if r == 1:
        print("Error! r cannot equal 1")
        return None
    if p_y<=0 or p_x<=0:
        print("Error! Prices x and y must be positive")
        return None
    if w <= 0:
        print("Error! Wealth w must be positive")
        return None
    # calc
    r_exp = r/(r-1)
    det = (p_x**r_exp + p_y**r_exp)
    x_star = w * (p_x**(1/(r-1)))/det
    y_star = w * (p_y**(1/(r-1)))/det
    return [round(x_star,2), round(y_star,2)]

# Exercise d
def max_CES_xy(x_min:float,x_max:float,y_min:float,y_max:float,step:float,
               r:float,p_x:float,p_y:float,w:float) -> list[float]:
    """
    
    Finds values of x and y that maximizes the CESutility_in_budget within
    a budget constraint. It takes the input ranges for x and y, the step size
    between values, and parameters like the elasticity of subsitution, prices,
    and wealth
    
    >>> max_CES_xy(1, 10, 1, 10, 0.5, 0.5, 3, 2, 100)
    [9.5, 9.5]
    >>> max_CES_xy(5, 3, 1, 10, 0.5, 0.5, 3, 2, 100)
    Error! Prices x and y maximums must be greater than minimums
    >>> max_CES_xy(0, 10, 0, 10, -0.5, 0.5, 3, 2, 100)
    Error! Prices x and y must be positive
    """
    # precheck
    if x_min >= x_max or y_min >= y_max:
        print("Error! Prices x and y maximums must be greater than minimums")
    if x_min<0 or x_max<=0 or y_min<0 or y_max<=0:
        print("Error! Cannot have less than zero consumption")
        return None
    if r<=0:
        print("Error! r must be positive")
        return None
    if w<=0:
        print("Error! Wealth w must be positive")
        return None
    if step<=0:
        print("Error! Step must be positive")
        return None
    if p_x <= 0 or p_y <= 0:
        print("Error! Prices must be positive")
        return None
    # init
    x_list = np.arange(x_min,x_max,step)
    y_list = np.arange(y_min,y_max,step)
    
    max_CES = float("-inf")
    i_max = 0
    j_max = 0
    # calc

    for i in range(len(x_list)):
        for j in range(len(y_list)):
            
            CES_ij = CESutility_in_budget(x_list[i], y_list[j], r, p_x, p_y, w)

            if not CES_ij == None and CES_ij > max_CES:
                max_CES = CES_ij
                i_max = i
                j_max = j
    return [x_list[i_max],y_list[j_max]]

x_min, x_max, y_min, y_max, step, r, p_x, p_y,w = 0, 12/2, 0, 12/4, 0.1, 1/2, 2, 4, 12

##################################################
# Test examples.
##################################################
if __name__ == "__main__":
    doctest.testmod()
    
##################################################
# End
##################################################
