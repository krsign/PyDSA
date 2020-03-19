# -*- coding: utf-8 -*-

from PyDSA.BDS.stack__push__pop import Stack

def rev_string(my_str):
    """
    To reverse the string using stack:
        Algorithm should be followed:
            1. accept string 
            2. declair stack and empty string
            3. push every characters to stack (use loop)
            3. pop the elements from stack and push it to empty string
            4. return second stack
    """
    s = Stack()
    rev = ''
    for char in my_str:
        s.push(char)
    
    while not s.is_empty():
        rev = rev + s.pop()
    return rev

if __name__ == '__main__':
    print(rev_string('krsign'))
    