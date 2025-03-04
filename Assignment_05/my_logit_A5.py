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
# copied functions
def logit(x:float, b_0:float, b_1:float) -> float:
    # calc
    p = math.exp(b_0 + x * b_1)
    return p/(1 + p)
def logit_like(y_i:int, x_i:float, b_0:float, b_1:float) -> float:
     # precondition check
    if y_i != 0 and y_i != 1: # if y_i is not 0 and y_i is not 1 at the same time
        #using OR does not work b/c OR shortcircuits for the left operand, and returns immediate True if y!=0 is True even if y=1
        print("Error! y_i must be equal to 1 or 0.")   
    # calc
    elif y_i == 1:
        return math.log(logit(x_i, b_0, b_1))
    elif y_i == 0:
        x = x_i
        return math.log(1 - logit(x, b_0, b_1))
def logit_like_sum(y:list, x:list, b0:float, b1:float) -> float:
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
    return likelihood_sum
##################################################

# Exercise a
def logit_d_i(x_i:float, k:float) -> float:
    """
    """
    # precheck
    if k != 0 or k != 1:
        print("undefined")
        return None
    elif k == 0 or k == 1:
        d_i = (x_i ** k)
        return d_i
        
# Exercise b
def logit_dLi_dbk(y_i:float,x_i:float,beta_0:float,beta_1:float) -> float:
    """
    """
    # precheck
    if y_i != 0 or y_i != 1:
        print("undefined")
        return None
    # calc
    k = [0,1] # k initialized b/c not provided in function
    dbk = logit_d_i(x_i, k)
    dLi = (1-y_i)-logit(x_i, beta_0, beta_1)
    return [(dbk[0]*dLi),(dbk[1]*dLi)]


##################################################
# Test examples.
##################################################
if __name__ == "__main__":
    doctest.testmod()
    
##################################################
# End
##################################################
