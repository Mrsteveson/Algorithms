#!/usr/bin/python

# 1. Understand the Question
# 2. Create Plan
# 3. Implement Plan
# 4. Revise and Improve

import sys

def rock_paper_scissors(n):
  # Define all the possible play options
  available_options = ['rock', 'paper', 'scissors'] # Three options its rps.
  end_results = [] # Will result in a list of all the possible plays available.
  # Create Recursive Function
  # Using two parameters, rounds and match_results
  # rounds control how long our function will run for.
  # match_results will store the record of all the resulting plays 
  def total_plays(rounds, match_result=[]):
    # Base Case
    # Once the loop is complete, add all of our plays to our end results
    if rounds < 1:
      return end_results.append(match_result)
    else:
      for option in available_options:
        total_plays(rounds - 1, match_result + [option]) 
        # Decrement our number of rounds each time

  total_plays(n) # Trigger the recursion
  return end_results

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')