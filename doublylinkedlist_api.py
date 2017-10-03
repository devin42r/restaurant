#!/usr/bin/env python3


class DoublyLinkedList(object):
    '''
        A doubly-linked list implementation that holds arbitrary objects.
    '''
    
    def __init__(self):
        '''Creates a linked list.'''
        # allocate the initial memory
        self.head = None
        self.size = 0
        
    def debug_print(self):
        '''Prints a representation of the entire list.'''
        myList = []
        if self.head is not None:
            t = self._get_node(self.size - 1)
            while t.prev is not None:
                myList.append(t.value)
                t = t.prev
            myList.append(t.value)
        print('{} >>> {} >>> {}'.format(self.size, ', '.join([ str(item) for item in self ]), ', '.join([ str(item) for item in myList ])))
        
    def getLastThree(self):
        myList = []
        if self.head is not None:
            t = self._get_node(self.size - 1)
            i = 0
            while t.prev is not None:
                myList.append(t.value)
                t = t.prev
                i += 1
                if i == 2:
                    break
            myList.append(t.value)
        return myList
        
    def __iter__(self):
        '''Iterates through the linked list.'''
        return self._iter_nodes(values=True)
        
        
    def _iter_nodes(self, values=False):
        '''Iterates through the nodes of the list, implemented as a generator.'''
        current = self.head
        while current != None:
            yield current.value if values else current 
            current = current.next
        
        
    def _get_node(self, index):
        '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        for i, current in enumerate(self._iter_nodes()):
            if i == index:
                return current
        raise IndexError('The given index is not within the bounds of the current list.')
        
        
    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        newnode = Node(item)
        if self.size == 0:
            self.head = newnode
        else:
            tail = self._get_node(self.size - 1)
            tail.next = newnode
            tail.next.prev = tail
        self.size += 1
        
        
    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        newnode = Node(item)
        # handle a new head node
        if self.head == None:
            self.add(item)
            return
        if index == 0:
            newnode.next = self.head
            self.head = newnode
            self.head.next.prev = self.head
        # inside the list somewhere, so go to the right position
        else:
            prev = self._get_node(index - 1)
            if prev.next != None:
                newnode.next = prev.next 
                prev.next.prev = newnode
            newnode.prev = prev
            prev.next = newnode
        # increment the size
        self.size += 1
        
    
    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        self._get_node(index).value = item
        
        
    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        return self._get_node(index).value
        
    
    def delete(self, index):
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
        # handle a deleted head node
        if index == 0:
            if self.head == None:
                raise IndexError('The given index is not within the bounds of the current list.') 
            self.head = self.head.next
            self.head.prev = None
        # inside the list somewhere, so go to the right position
        else:
            prev = self._get_node(index - 1)
            if prev.next == None:
                raise IndexError('The given index is not within the bounds of the current list.')
            prev.next = prev.next.next
            if prev.next != None:
                prev.next.prev = prev
        # decrease the size
        self.size -= 1
    
    def deleteByValue(self, value):
        t = self.head
        index = 0
        for i in range(self.size):
            if t.value == value:
                self.delete(index)
                return True
            t = t.next
            index += 1
        return False
        
    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        # find each item
        node1 = self._get_node(index1)
        node2 = self._get_node(index2)
        # swap the items
        node1.value, node2.value = node2.value, node1.value
        
        
        
######################################################
###   A node in the linked list
        
class Node(object):
    '''A node on the linked list'''
    
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        
    def __str__(self):
        return '<Node: {}>'.format(self.value)