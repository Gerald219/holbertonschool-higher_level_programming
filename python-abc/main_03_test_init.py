#!/usr/bin/env python3
from task_03_countediterator import CountedIterator

# create a counted iterator with a list
ci = CountedIterator([10, 20, 30])

print("Iterator created:", ci)
print("Inner iterator:", ci.iterator)
print("Current count:", ci.count)
