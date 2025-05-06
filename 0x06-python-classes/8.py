#!/usr/bin/python3

Sort = __import__('100-singly_linked_list').SingleLinkedList

s1 = Sort()

s1.sorted_insert(3)
s1.sorted_insert(1)

print(s1.__dict__)

