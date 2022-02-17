#This is the first file
import numpy

#This is a function containing a bug to fix
def multiply_numbers_in_list(list_numbers):
  result = 1.
  for num_i in list_numbers:
    result= result**num_i
  return result
