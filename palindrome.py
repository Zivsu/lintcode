# !/usr/bin/env python
# coding=utf-8

import re

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

# Implement a function to check if a linked list is a palindrome.
# Given 1->2->1, return true

def is_palindrome1(head):
    if head is None: return True
    tmp_list = [head.val]
    while head.next:
        head = head.next
        tmp_list.append(head.val)
    return (tmp_list == tmp_list[::-1])

def is_palindrome2(head):
    if head is None: return True
    slow = fast = head
    stack = []
    stack.append(slow.val)
    while (fast.next and fast.next.next):
    	slow = slow.next
        fast = fast.next.next
        stack.append(slow.val)
    
    if fast.next is None: stack.pop()
    while slow.next:
        slow = slow.next
        if stack.pop() != slow.val:
            return False
    return True

# Given a string, determine if it is a palindrome, 
# Considering only alphanumeric characters and ignoring cases.
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

 def is_palindrome3(s):
    filter_str = re.sub(r"\W+", "", s).lower()
    return(filter_str == filter_str[::-1])

