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
    """Return the present value of cash_flow expected num_yrs from now discounted at interest_rate.

    >>> present_value(110, 0.10, 1)
    100.0
    >>> present_value(121, 0.10, 2)
    108.26
    >>> present_value(100, .1, 5)
    62.09
    """
    
    answer = cash_flow/((1 + interest_rate) ** num_yrs)
    return answer

def future_value(cash_flow: float, interest_rate: float, num_yrs: float) -> float:
    """Return the future value of present cash_flow num_yrs from now discounted at interest_rate.
    
    >>> future_value(110, 0.10, 1)
   100.0
   >>> future_value(200, 0.10, 2)
   242.0
   >>> future_value(400, .08, 5)
   587.73
    """
    answer = cash_flow * ((1 + interest_rate) ** num_yrs)
    return answer

# Exercise 3
def total_revenue(units_sold: float, unit_price: float) -> float:
    """Return total revenue from all units_sold at unit_price.
    
    >>> total_revenue(100, 4)
   400.0
   >>> total_revenue(1000000, 120.5)
   120500000.0
   >>> total_revenue(344, 6.45)
   2218.8
    """
    answer = units_sold * unit_price
    return answer

# Exercise 4
def total_cost(units_produced: float, fixed_cost: float, cost_per_unit_sq: float) -> float:
    """Return total cost of units_produced using constant cost_per_unit_sq plus fixed cost.
    
    >>> total_cost(900, 3, 60)
   30004.0
   >>> total_cost(1000, 10, 3.42)
   3420010.0
   >>> total_cost(1000000, 100000, 45)
   45000000100000.0
    """
    answer = cost_per_unit_sq * (units_produced ** 2) + fixed_cost
    return answer

# Exercise 5
def CESutility(x: float, y: float, r: float) -> float:
    """Return the theoretical degree of satisfaction a customer may get from goods x and y 
    using r, the degree which the goods are complements or substitutes.
    
    >>> CESutility(40, 30, .5)
   8.615612366938898
   >>> CESutility(40, 30, -.5)
   139.28
   >>> CESutility(5, 5, 1)
   10
    """
    answer = (x ** r + y ** r) ** (1/r)
    return answer




##################################################
# Run the examples to test these functions
##################################################


# Test the examples and print the results.

# Exercise 1
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
print("Expected: " + str(108.26))
print("Got: " + str(present_value(131, 0.10, 2)))


print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating present_value(100, 0.10, 5)")
print("Expected: " + str(62.09))
print("Got: " + str(present_value(100, 0.10, 5)))

# Exercise 2
print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")
print("#" + 50*"-")
print("Exercise 2, Example 1:")
print("Evaluating future_value(110, 0.10, 1)")
print("Expected: " + str(121.0))
print("Got: " + str(future_value(110, 0.10, 1)))


print("#" + 50*"-")
print("Exercise 2, Example 2:")
print("Evaluating future_value(200, 0.10, 2)")
print("Expected: " + str(242.0))
print("Got: " + str(future_value(200, 0.10, 2)))


print("#" + 50*"-")
print("Exercise 2, Example 3:")
print("Evaluating future_value(400, 0.08, 5)")
print("Expected: " + str(587.73))
print("Got: " + str(future_value(400, 0.08, 5)))

# Exercise 3

print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")
print("#" + 50*"-")
print("Exercise 3, Example 1:")
print("Expected: " + str(400.0))
print("When a firm sells 100 units of sponges that cost $4.00, the total revenue is: $" + str(total_revenue(100,4)))


print("#" + 50*"-")
print("Exercise 3, Example 2:")
print("Expected: " + str(120500000.0))
print("When a firm sells 1,000,000 units of shoes that cost $120.50, the total revenue is: $" + str(total_revenue(1000000,120.5)))


print("#" + 50*"-")
print("Exercise 3, Example 3:")
print("Expected: " + str(2218.8))
print("When a firm sells 344 units of sponges that cost $6.45, the total revenue is: $" + str(total_revenue(344,6.45)))


# Exercise 4

print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")
print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Expected: " + str(30004))
print("When a firm produces 900 units of towels, each selling for $3.00, with a fixed cost of $60, the total cost is: $" + str(total_cost(100,4,3)))


print("#" + 50*"-")
print("Exercise 4, Example 2:")
print("Expected: " + str(3420010))
print("When a firm produces 1000 units of shirts, each selling for $3.42, with a fixed cost of $10, the total cost is: $" + str(total_cost(1000,10,3.42)))


print("#" + 50*"-")
print("Exercise 5, Example 3:")
print("Expected: " + str(45000000100000))
print("When a firm produces 1,000,000 units of pants, each selling for $45.00, with a fixed cost of $100,000, the total cost is: $" + str(total_cost(1000000,100000,45)))


# Exercise 5

print("#" + 50*"-")
print("Testing my Examples for Exercise 5.")
print("#" + 50*"-")
print("Exercise 5, Example 1:")
print("Expected: " + str(8.62))
print("The theoretical degree of satisfaction a consumer may get when the price of good 1 is $40.00 and good 2 is $30.00, with it being a complement is:",+(CESutility(40, 30, -.5)))


print("#" + 50*"-")
print("Exercise 5, Example 2:")
print("Expected: " + str(139.28))
print("The theoretical degree of satisfaction a consumer may get when the price of good 1 is $40.00 and good 2 is $30.00, with it being a substitute is:",+(CESutility(40, 30, .5)))


print("#" + 50*"-")
print("Exercise 5, Example 3:")
print("Expected: " + str(10.0))
print("The theoretical degree of satisfaction a consumer may get when the price of good 1 and 2 are equal to $5.00, with it being a perfect substitute is:",+(CESutility(5, 5, 1)))




# ...


# Continue with the rest of your examples.
# Test all functions with three examples each.

# Choose good examples that will test interesting cases.
# Make sure they all work correctly.


##################################################
# End
##################################################
