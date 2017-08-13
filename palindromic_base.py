"""
   Author: Juan M Navarro
   Date: 8/8/2017
   Notes: 
      --- Finds the lowest palindromic base for the first 1000 positive integers, starting with 0
      --- Run unit tests with this command: python -m unittest -v juan_navarro_palindromic_base
"""

import unittest
import sys
import string

class PalindromicBaseTestCases(unittest.TestCase):
   def test_is_palindrome(self):
      test_cases = [(2, True), (44, True), (10, False), (5665, True), (565, True), ('aab', False), ('bba', False), ('aba', True), ('', True), ('c', True), ('cc', True)]
      for k, v in test_cases:
         self.assertEqual(is_palindrome(k), v)

   def test_convert_base_of_2_to_3(self):
      self.assertEqual(convert_to_base(2, 3), '2')
   def test_convert_base_of_10_to_2(self):
      self.assertEqual(convert_to_base(10, 2), '1010')
   def test_convert_base_of_5_to_2(self):
      self.assertEqual(convert_to_base(5, 2), '101')
   def test_convert_base_of_19_to_18(self):
      self.assertEqual(convert_to_base(19, 18), '11')
   def test_convert_base_of_19_to_40(self):
      with self.assertRaises(AssertionError) as context:
         convert_to_base(19, 40)      
   def test_convert_base_of_19_to_1(self):
      with self.assertRaises(AssertionError) as context:
         convert_to_base(19, 1)      
   def test_convert_base_of_negative_20_to_2(self):
      with self.assertRaises(AssertionError) as context:
         convert_to_base(-20, 2)      

   def test_get_lowest_palindromic_base(self):
      test_cases = [(2, 3), (5, 2), (11, 10), (19, 18)] # input, output: (x, y) where x is the number to test, y is the lowest palindromic base
      for k, v in test_cases:
         self.assertEqual(get_lowest_palindromic_base(k), v)

# check if a number is a palindrome
def is_palindrome(num):
   result = True
   num_list = [x for x in str(num)]  # convert number to a list of integers
   num_count = len(num_list)

   for i in range(0, num_count/2):
      if num_list[i] != num_list[num_count - 1 - i]:
         result = False

   return result

# convert num to base x, and return the new representation as a string 
def convert_to_base(num, base):
    num_new_base = ''

    assert(num >= 0)
    assert(1 < base < 37)

    while num > 0:
        num_new_base = string.printable[num % base] + num_new_base
        num //= base

    return num_new_base

# gets the lowest base that is a palindrome for number num
def get_lowest_palindromic_base(num):
   result = num - 1 # this base will always be palindromic

   if num == 0 or num == 1:  # handle special cases
      result = 2
   elif num == 2:
      result = 3

   for base in range(2, 37): # start checking with base 2
      num_in_new_base = convert_to_base(num, base)
      if is_palindrome(num_in_new_base):
         result = base
         break
   return result

if __name__ == '__main__':
   for i in range(0, 1000):
      base = get_lowest_palindromic_base(i)
      print "%s, %s" % (i, base)
