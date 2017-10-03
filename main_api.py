#!/usr/bin/env python3
from circularlist_api import CircularLinkedList, CircularLinkedListIterator
from doublylinkedlist_api import DoublyLinkedList
from stack_api import Stack
from queue_api import Queue


class Processor(object):
    
    def __init__(self):
        '''Creates the lists'''
        self.callahead = DoublyLinkedList()
        self.waiting = DoublyLinkedList()
        
        # self.waiting.debug_print()
        # self.waiting.add('a')
        # self.waiting.add('b')
        # self.waiting.add('c')
        # self.waiting.debug_print()
        
        self.appetizers = Queue()
        self.buzzers = Stack()
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.songs = CircularLinkedList()
        self.songs.add('Song 1')
        self.songs.add('Song 2')
        self.songs.add('Song 3')
        self.songs_iter = CircularLinkedListIterator(self.songs)

    def run(self, f):
        '''Processes the given file stream.'''
        for index, line in enumerate(f):
            line = line.rstrip()
            print('{}:{}'.format(index, line))
            parts = line.split(',')
            # try:
            func = getattr(self, '{}'.format(parts[0].lower()))
            func(*parts[1:])
            # except Exception as e:
            #     print('Error: {}'.format(e))
            # split and handle the commands here

            

    def debug(self, *args):
        self.callahead.debug_print()
        self.waiting.debug_print()
        self.appetizers.debug_print()
        self.buzzers.debug_print()
        self.songs.debug_print()
    
    def song(self, *args):
        print(self.songs_iter.next())
    
    def appetizer(self, *args):
        try:
            print("{} >>> {}".format(self.appetizers.dequeue(), ', '.join([ str(item) for item in self.waiting.getLastThree() ]) ))
        except Exception as e:
            print('Error:',  e)

    def appetizer_ready(self, *args):
        self.appetizers.enqueue(args[0])

    def seat(self, *args):
        self.buzzers.push('Buzzer')
        print(self.waiting.get(0))
        self.waiting.delete(0)

    def call(self, *args):
        self.callahead.add(args[0])
    
    def arrive(self, *args):
        if (self.callahead.deleteByValue(args[0]) == True):
            self.waiting.insert(self.getFiveIn(self.waiting.size), args[0])
        else:
            sws = self.waiting.size
            self.waiting.insert(sws if sws >= 0 else 0, args[0])
        self.buzzers.pop()

    def leave(self, *args):
        self.waiting.deleteByValue(args[0])
        self.buzzers.push('Buzzer')

    def getFiveIn(self, size):
        return size - 4 if size - 4 >= 0 else 0

#######################
###   Main loop

# callahead = DoublyLinkedList()
# callahead.add('gibber')
# callahead.add('ishy')
# callahead.debug_print()
# callahead.deleteByValue('ishy')
# callahead.debug_print()

with open('example_data.csv', newline='') as f:
    processor = Processor()
    processor.run(f)

