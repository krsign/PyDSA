# -*- coding: utf-8 -*-

from PyDSA.BDS.stack__push__pop import Stack

def parentheses(paren):
    s = Stack()
    balanced = True
    index = 0
    
    while index < len(paren) and balanced:
        
        symbol = paren[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced  = False
            else:
                s.pop()
                
        index = index + 1
        
    if balanced and s.is_empty():
        return True
    else:
        return False

print(parentheses('(())'))