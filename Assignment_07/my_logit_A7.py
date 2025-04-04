"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Jaemin Ahn, Xin Wang
#
# Date: 4/7/25
# 
##################################################
#
# Sample Script for Assignment 7: 
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
# 1
def logit(x:float, b_0:float, b_1:float) -> float:
    """logit computes the logistic function using x as the input, and b_0 as the intercept,
    and b_1 as the coefficient.
    """
    # calc
    p = math.exp(b_0 + x * b_1)
    return p/(1 + p) # just in case there is a rounding issue
def logit_like(y_i:int, x_i:float, b_0:float, b_1:float) ->float:
    """logit_like is a wrapper which computes the log-likelihood and models binary events, where 1 equals
    if the event occured and 0 if it did not, using x_i as the predictor variable and y_i
    as the binary outcome.
    """
    # precondition check
    if y_i != 0 and y_i != 1: # if y_i is not 0 and y_i is not 1 at the same time
        #using OR does not work b/c OR shortcircuits for the left operand, and returns immediate True if y!=0 is True even if y=1
        print("Error! y_i must be equal to 1 or 0.")   
    # calc
    elif y_i == 1:
        x = x_i # necessary for wrapper, but it is also possible to write it as logit(x_i)
        return math.log(logit(x, b_0, b_1)) # missed taking the log of the function (-2)
    elif y_i == 0:
        x = x_i
        return math.log(1 - logit(x, b_0, b_1))
def logit_like_sum(y:list, x:list, b0:float, b1:float): # expected output? (-1)
    """
    logit_like_sum calculates the sum of all log likelihood events giving
    that the observation y equals 1 if the event occurred and 0 if it did not.
    The function uses logit link functions to compute the chances of an event
    happening and sums the log likelihood across all observations.
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
    return likelihood_sum
def logit_d_i(x_i: float, k: float) -> float:
    """
    Calculates the term d_i in the gradient vector for logistic regression.
    If the parameter k is 0, it returns 1; if k is 1, it returns the value
    x_i, otherwise the function returns undefined.
    """
    # precheck
    if k != 0 and k != 1:
        print("undefined")
        return None
    elif k == 0 or k == 1:
        d_i = (x_i ** k)
        return d_i
def logit_dLi_dbk(y_i: float, x_i: float, beta_0: float, beta_1: float) -> list[float]:
    """
    Calculates an individual term in the gradient vector for logistic regression.
    Uses the formula for the partial derivative of the likelihood function L_i
    with respect to beta_k.
    """
    # precheck
    if y_i != 0 and y_i != 1:
        print("undefined")
        return None
    # calculate
    dbk_0 = logit_d_i(x_i, 0)  # k = 0
    dbk_1 = logit_d_i(x_i, 1)  # k = 1
    logit_value = logit(x_i, beta_0, beta_1)
    if y_i == 1:
        dLi = (1 - logit_value)
    elif y_i == 0:
        dLi = (-logit_value)
    return [(dbk_0 * dLi), (dbk_1 * dLi)]

# 2
def logit_like_sum_opt(beta, y, x):
    """
    """
    return None
def logit_like_grad(beta, y, x):
    """
    """
    return None

##################################################
# Test examples.
##################################################
if __name__ == "__main__":
    doctest.testmod()
##################################################
# End
##################################################