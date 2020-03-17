# -*- coding: utf-8 -*-

from stack__insertion import Stack

s = Stack()

print(s.is_empty())

s.push('Python3')
s.push(True)

print(s.size())

# removing the items

print(s.pop())
print(s.pop())

# checking again if stack is empty or not?

print(s.is_empty())