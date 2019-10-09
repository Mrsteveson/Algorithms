#!/usr/bin/python

# 1. Understand the Question
# We are given an array of values, and are searching to find the greatest difference between two values, comparing right to left only.
# No shorting allowed(Left to right), so the two on the end will not affect our outcome with the initially provided array

# 2. Create Plan
# 3. Implement Plan
# 4. Revise and Improve

import argparse

def find_max_profit(prices):
  current_min_profit = prices[0] # Initialize to the first value in our array
  current_max_profit = prices[1] - prices[0] # Max profit is defined as the next value in the array minus the previous value. No shorting allowed.

  for i in range(1, len(prices)): # Loop through our prices array starting at the 2nd index
    if prices[i] < current_min_profit: # If the index is smaller than our smallest current value, swap
      current_min_profit = prices[i]  # Replace our smallest value
    elif prices[i] - current_min_profit > current_max_profit: # If the current index minus the current smallest value is greater than current max, replace our current max.
      current_max_profit = prices[i] - current_min_profit # Max profit is found by subtracting the current smallest value from each index as we loop.

  return current_max_profit
print(f'{find_max_profit([1050, 270, 1540, 3800, 2])}')
print(f'{find_max_profit([10, 2700, 150, 300, 277, 1100, 1500, 5000, 1700])}')


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))