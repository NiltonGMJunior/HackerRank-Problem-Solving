#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

'''
The following is my attempt at the solution

It couldn't be tested due to issues on the template code at HackerRank

The following solution creates the paths of each linked-list and then 
walks along the path starting from the their respective tails going towards the heads.
Whenever the end of the path coincides, the tail is 'clipped-off' and the process continues 
up until the paths diverge, which indicates the node of convergence.

There is another method available to be implemented:
Create two pointers, pointing to the heads of each list.
The pointers advance one node each time until they are pointing to the same node,
which is the node of convergence, or until the end of a list is reached.
If the end of the list is reached, that pointer only is directed towards the head of the
other list in the next iteration, and the process loops until the node of convergence is found.
'''
def findMergeNode(head1, head2):
    path1 = [head1]
    path2 = [head2]

    while path1[-1].next or path2[-1].next:
        if path1[-1].next:
            path1.append(path1[-1].next)
        
        if path2[-1].next:
            path2.append(path2[-1].next)
        
    while path1[-1] == path2[-1]:
        path1 = path1[:-1]
        path2 = path2[:-1]
    
    return path1[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)
            
        ptr1 = llist1.head;
        ptr2 = llist2.head;

        for _ in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next
        
        for _ in range(llist2_count):
            if i != llist2_count-1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        fptr.write(str(result) + '\n')

    fptr.close()