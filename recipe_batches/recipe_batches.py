#!/usr/bin/python

# 1. Understand the Question
# What are the keys and values that we are using.
# Keys are the ingredient names, while the values are the ingredient amounts
# We are given two dictionaries, recipe and ingredient.
# The recipe dictionary represents the amount of each ingredient necessary to create 1 complete batch
# Meanwhile, the ingredient dictionary represents the amount of each ingredient that we posses to create our batches.
# To find our total number of batches, we will need to divide the recipe amounts by the available ingredient amounts. (recipe//ingredients).
# The output we are looking for is the total number of complete batches that can be made with the ingredients provided. (Whole numbers, no fractions).
# If no complete batches can be made, just return 0.

# 2. Create Plan
# Start out by establishing a variable for total number of batches.
# Compare the recipe amounts to the ingredient amounts.
# Most likely using a loop to iterate through our keys/values.
# Find how many batches that can be made with our provided amounts.
# Return our total number of batches

# 3. Implement Plan
# Create our variables
# Write our loop
# Establish our conditional
# Find our total

# 4. Revise and Improve


import math

def recipe_batches(recipe, ingredients):
  batch_count = 1000 
  for key, value in recipe.items():
    if key not in ingredients:
      return 0

    complete_batch = (ingredients[key] // value)
    if complete_batch < batch_count:
      batch_count = complete_batch

  return batch_count
     
# def recipe_batches(recipe, ingredients):
#   batch_count = 0
#   have_ingredients = True

#   while have_ingredients:
#     for key in recipe:
#       if key in ingredients:
#         if recipe[key] <= ingredients[key]:
#           ingredients[key] = ingredients[key] - recipe[key]
#         else:
#           have_ingredients = False
#       else:
#         have_ingredients = False
#     if have_ingredients:
#       batch_count += 1
#   return batch_count


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))