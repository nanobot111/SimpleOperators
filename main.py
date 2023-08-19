#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
  calculated_tip = round(tip_percent/100 * meal_cost)
  calculated_tax = round(tax_percent/100 * meal_cost)
  total_meal = (meal_cost + calculated_tax + calculated_tip)
  
  print(int(total_meal))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
