# Substring in Python
# ======================\n
'''
Input: Substring = "geeks" 
            String="geeks for geeks"
Output: yes
Input: Substring = "geek"
           String="geeks for geeks"
Output: yes
Explanation: In this, we are checking if the substring is present in a given string or not.
'''
# Types
# ===\n
# Using the If-Else 
# Using In Operator
# Checking using split() method
# Using find() method
# Using “count()” method
# Using index() method
# Using list comprehension 
# Using lambda function 
# Using  __contains__” magic class.
# Using Slicing Function
# Using regular expressions 
# using operator contains() method
#==========================================================\n
# using operator.contains() method
# ===============================\n
import operator as op 
s="geeks for geeks"
s2="geeks"
if(op.contains(s,s2)): 
    print("yes") 
else: 
    print("no")
    
