# -*- coding: utf-8 -*-

from stack__push__pop import Stack

s = Stack()

# checks stack is empty or not 
print(s.is_empty())

# pushing or adding a elements at the top
s.push(22)
s.push('Python')

# peek checks the top items 
print(s.peek())

# size checks total size of the stack
print(s.size())

print(s.is_empty())

s.push('Django')
print(s.peek())

# pop is basically removing items from top
print(s.pop())
print(s.pop())
print(s.pop())

print(s.is_empty())

 