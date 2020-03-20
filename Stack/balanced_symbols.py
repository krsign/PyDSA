# -*- coding: utf-8 -*-

from PyDSA.BDS.stack__push__pop import Stack

def parentheses(paren):
    
    """ 
    Problem : is to check for different parentheses '({[]})' is balanced or
        not ?
        
        Algorithm : 
        This problem is same as for one type of symbols but but little bit 
        different.
        
        1. find opening symbols '({[' using 'in'
        2. push it the stack and if other opening symbol is found push them too
        3. if opening symbol is not there in called string return False
        4. if stack is not empty pop the items by comparing top one to opening 
           parenthese
        5. if top not matches to close one set balanced to false
        6. define one function which matches opening and closing symbos and return 
        true or false
        7. this function will decide whether top is balanced to compared symbols
        
        @ krsign
        
    """
    
    s = Stack()
    balanced = True
    index = 0
    
    while index < len(paren) and balanced:
        
        symbols = paren[index]
        
        if symbols in '([{':
            s.push(symbols)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbols):
                    balanced = False
        index = index + 1
        
    if balanced and s.is_empty():
        return True
    else:
        return False
    
def matches(open,close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)
        
print(parentheses('[[[{()}]]]'))