# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 18:46:30 2015

@author: AshRajBala
"""

import unittest

class ExampleTests(unittest.TestCase):
    def fizzbuzz_goodtest(f):
        output = []
        for n in range(100):
            output.append(str(f(n) + "\n"))

        expected = open("fizzbuzz-output.txt", "r")
        i = 0
        for line in expected:
            if line == output[i]:
                print("Success!")
                i += 1
            else:
                print("Nope. Try Again.")


def fizzbuzz(n):
    ret = ""
    if not (n%3):
        ret += "fizz"
    if not (n%5):
        ret += "buzz"
    return ret or str(n)
   
   
if __name__ == "__main__":
    unittest.main()
    
            
       
