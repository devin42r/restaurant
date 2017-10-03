#!/usr/bin/env python3
from linkedlist_api import LinkedList

class Queue(object):
    '''
    A linked list implementation of a queue.
    
    This contains a LinkedList internally.  It does not extend LinkedList.
    In other words, this class uses "Composition" rather than "Inheritance".
    '''
    
    def __init__(self):
        '''Constructor'''
        self.ll = LinkedList()
    
    def debug_print(self):
        '''Prints a representation of the entire queue.'''
        self.ll.debug_print()

    def enqueue(self, item):
        '''Adds an item to the end of the queue'''
        self.ll.add(item)
        
    def dequeue(self):
        value = self.ll.get(0)
        self.ll.delete(0)
        return value
        '''
        Dequeues the first item from the list.  This involves the following:
            1. Get the first node in the list.
            2. Delete the node from the list.
            3. Return the value of the node.
        '''

    def size(self):
        '''Returns the number of items in the queue'''
        return self.ll.size
