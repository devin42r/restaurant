#!/usr/bin/env python3

class CircularLinkedList(object):
    '''
    A circularly-linked list implementation that holds arbitrary objects.
    '''
    
    def __init__(self):
        '''Creates a circ linked list.'''
        self.head = None
        self.size = 0
        
    def debug_print(self):
        '''Prints a representation of the entire list.'''
        myList = []
        if self.head is not None:
            t = self.head
            while t.next is not self.head:
                myList.append(t.value)
                t = t.next
            myList.append(t.value)
        print('{} >>> {}'.format(self.size, ', '.join([ str(item) for item in myList ])))
        
        
    def debug_cycle(self, count):
        '''Prints a representation of the entire cycled list up to count items'''
        print('{} >>> {}'.format(self.size, ', '.join([ str(item) for item in count ])))
    
    def check_bounds(self, index):
        if 0 > index or index >= self.size:
            raise Exception('{} is not within the bounds of the current list.'.format(index))    

    def getAtIndex(self, index, variation = 0):
        t = self.head
        for i in range(index - variation):
            t = t.next
        return t     
        
    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        newnode = Node(item)
        if self.size == 0:
            self.head = newnode
            newnode.next = self.head
        else:
            tail = self.getAtIndex(self.size - 1)
            tail.next = newnode
            newnode.next = self.head
        self.size += 1
        
        
    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        self.check_bounds(index)
        newnode = Node(item)
        # handle a new head node
        if index == 0:
            newnode.next = self.head
            self.head = newnode
            self.getAtIndex(self.size - 1).next = self.head
        # inside the list somewhere, so go to the right position
        else:
            prev = self.getAtIndex(index - 1)
            newnode.next = prev.next
            prev.next = newnode
        # increment the size
        self.size += 1
    
    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        self.check_bounds(index)
        self.getAtIndex(index).value = item
        
    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        self.check_bounds(index)
        return self.getAtIndex(index).value
    
    def delete(self, index):
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
        # handle a deleted head node
        self.check_bounds(index)
        if index == 0:
            if self.head == None:
                raise IndexError('The given index is not within the bounds of the current list.') 
            self.head = self.head.next
            self.getAtIndex(self.size - 1).next = self.head
            
        # inside the list somewhere, so go to the right position
        else:
            prev = self.getAtIndex(index - 1)
            if prev.next == None:
                raise IndexError('The given index is not within the bounds of the current list.')
            prev.next = prev.next.next
        # decrease the size
        self.size -= 1
        
    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        self.check_bounds(index1)
        self.check_bounds(index2)
        # find each item
        node1 = self.getAtIndex(index1)
        node2 = self.getAtIndex(index2)
        # swap the items
        node1.value, node2.value = node2.value, node1.value
        
        
######################################################
###   A node in the linked list
        
class Node(object):
    '''A node on the linked list'''
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return '<Node: {}>'.format(self.value)

######################################################
###   An iterator for the circular list

class CircularLinkedListIterator(object):
    def __init__(self, circular_list):
        '''Starts the iterator on the given circular list.'''
        self.Cll = circular_list
        self.currentIndex = 0
        
    def has_next(self):
        '''Returns whether there is another value in the list.'''
        if self.Cll.get(self.currentIndex + 1).value != None:
            return True
        return False
        
    def next(self):
        '''Returns the next value, and increments the iterator by one value.'''
        # if we're at the end, need to cycle
        if self.currentIndex == self.Cll.size:
            self.currentIndex = 0
        value = self.Cll.get(self.currentIndex)
        self.currentIndex += 1
        return value