# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Jaemin Ahn, Xin Wang
#
# Date: 01/20/2025
#
##################################################
#
# Sample Script for Assignment 2:
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module


##################################################
# Function Definitions
##################################################

# Exercise 1

def present_value(cash_flow: float, interest_rate: float, num_yrs: float) -> float:
    """Return the present value of cash_flow expected num_yrs from now
    discounted at interest_rate.

    >>> present_value(110, 0.10, 1)
    100.0
    >>> present_value(121, 0.10, 2)
    100.0
    >>> next example goes here
    """
    answer = code_goes_here

    return answer

# Define the rest of your functions for Exercises 2-5.

# Exercise 1
def present_value(cash_flow: float, interest_rate: float, num_yrs: float) -> float:
    """Return the present value of cash_flow expected num_yrs from now discounted at interest_rate."""
    
    answer = cash_flow/((1 + interest_rate) ** num_yrs)
    return answer

# Exercise 2
def future_value(cash_flow: float, interest_rate: float, num_yrs: float) -> float:
    """Return the future value of cash_flow expected num_yrs from now discounted at interest_rate
    """
    answer = cash_flow * ((1 + interest_rate) ** num_yrs)
    return answer

# Exercise 3
def total_revenue(units_sold: float, unit_price: float) -> float:
    """
    """
    answer = units_sold * unit_price
    return answer

# Exercise 4
def total_cost(units_produced: float, fixed_cost: float, cost_per_unit_sq: float) -> float:
    """
    """
    answer = cost_per_unit_sq * (units_produced ** 2) + fixed_cost
    return answer

# Exercise 5








##################################################
# Run the examples to test these functions
##################################################


# Test the examples and print the results.


print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")

print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating present_value(110, 0.10, 1)")
print("Expected: " + str(100.0))
print("Got: " + str(present_value(110, 0.10, 1)))


print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating present_value(121, 0.10, 2)")
print("Expected: " + str(100.0))
print("Got: " + str(present_value(121, 0.10, 2)))


print("#" + 50*"-")
print("Exercise 1, Example 3:")
# Code goes here.



print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")


# ...


# Continue with the rest of your examples.
# Test all functions with three examples each.

# Choose good examples that will test interesting cases.
# Make sure they all work correctly.


##################################################
# End
##################################################
