# -*- coding: utf-8 -*-
"""
Algorithm to Convert decimal to octal or hexadecimal
    1. take two number in function number and it's base
    2. define digit = '123456789ABCDEF' because we are converting till hexa decimal
    3. loop until number is less than 0 and store in stack
    4. define variable to store reverse value 
    5. return
    
    @ krsign

"""
from PyDSA.BDS.stack__push__pop import Stack

def dec_bin_oct_hex(num,base):
    
    digits = '123456789ABCDEF'
    reminder_stack = Stack()
    
    while num > 0:
        rem = num % base
        reminder_stack.push(rem)
        num = num // base
        
    bin_oct_hex = ''
    
    while reminder_stack.is_empty() == False:
        bin_oct_hex = bin_oct_hex + digits[reminder_stack.pop()]
        
    return bin_oct_hex
        
print(dec_bin_oct_hex(25,8))
