import unittest
from circularlist_api import CircularLinkedList

class CllTest(unittest.TestCase):
  def testInsertion(self):  
    
    songs = CircularLinkedList()
    # with self.assertRaises(Exception):
    #   self.songs.insert(3, 'no')
    songs.add('Song 1')
    self.assertEqual('Song 1', songs.get(0))
    
    songs.add('Song 1')
    songs.debug_print()

    songs.debug_print
