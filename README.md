# Assignment: Restaurant

Create a new project and copy your linked list class to it.  Create the following additional classes for a total of five (5) data structure classes:

1. Circular Linked List
1. Doubly Linked List
1. Stack
1. Queue

Create five unit test classes (one for *each* list type).  Each unit test class should contain at least four methods.  You should be testing expected results as well as possible exceptions that may occur.


## Circular Linked List

This is a full, new class that extends object.  I suggest modifying a copy of your linked list class instead of starting from scratch. 

Compared to regular linked lists:

* The Node class in a circular list is the same.
* The circular list contains one additional method: `debug_cycle`, which prints the values (including cycling back to the front) for `count` number of iterations.
* Be careful not to loop infinitely through the list (it's circular :).
* Many methods are the same as linked list.  Small changes are needed in `add`, `delete`, `insert`, and `get` to deal with the circular nature.
* The `debug_print` method output is the same as linked list.

In a circular list, the `.next` field is never null.  When the size is 0, `head` is null.  When the size is 1, `head.next` points to `head`.

Throw an exception if operations are performed that are outside the size of the structure (such as inserting beyond the end of the list).

### Circular Linked List Iterator

Create a class that iterates infinitely over a circular linked list.  Define the following methods:

* has_next() - Whether additional items are available.
* next() - Retrieve the next item in the list (and move the iterator forward by one).


## Doubly-Linked List

This is a full, new class that extends object.   I suggest modifying a copy of your linked list class instead of starting from scratch. Your Node class should contain three fields: prev, next, and value.  Ensure the 

Compared to regular linked lists:

* The Node class in a doubly-linked list has three fields: `prev`, `next`, and `value`.
* The doubly-linked list has the same methods as a regular linked list.
* Always ensure that `prev` and `next` point to the previous and next nodes in the list.  This will require changes to `add`, `delete`, `insert`, `get`, and perhaps others of your methods.
* The `debug_print` method output is different than linked list.  The output should contain the list values in forward **and** reverse directions.  The format is count, forward print, reverse print.  Use the .prev and the .next fields to print the two directions.  For a list of three items, the output should be as follows:

        3 >>> a, b, c >>> c, b, a

In a doubly-linked list, the `.next` field is null for the tail item, and the `.prev` field is null for the head item.  

Throw an exception if operations are performed that are outside the size of the structure (such as inserting beyond the end of the list).


## Stack


Create a stack class that **extends** your linked list class.  The class should define two additional methods to those it inherits:

1. `push` - adds an item to the top of the stack (end of the list).
1. `pop` - removes and returns the item at the top of the stack (end of the list).

We are not using the `.peek` method, so you do not need to add it to the class.

Compared to regular linked lists:

* The stack inherits from linked list, so it has all the methods of linked list.
* The stack has two additional methods (defined above).  These methods should simply call the appropriate methods in the superclass.

Throw an exception if operations are performed that are outside the size of the structure (such as popping when empty).


## Queue

Using the composition pattern, create a queue class that **contains** a linked list field.  The queue class should extend `object`, **not** linked list.  Add the following methods to the class:

1. debug_print - prints the values, exactly the same as linked list (i.e. call the linked list method).
1. enqueue - adds an item to the end of the queue.
1. dequeue - removes and returns the first item in the list.

Throw an exception if operations are performed that are outside the size of the structure (such as dequeuing when empty).



## Getting Started

I suggest that you create and test one method at a time as you work through `add`, `insert`, `set`, `get`, `delete`, and `swap`.  Write your unit tests as you code.

For example, as your program the `insert` function, test the following:

* Inserting when your head is null.
* Inserting when your list has data.
* Inserting with an invalid index (< 0 or >= the current size).


## The File of Instructions

The assignment comes with a CSV file named `data.csv`.  This file contains the instructions you should run on your classes.  It will assist in grading your work.

In your `main.py` file, start by start by creating five structures. It will acts on these structures according to the instructions in `data.csv`.  

1. `callahead` holds customers who have called ahead for seating.  This should be a doubly-linked list.  When a party arrives that called ahead, they are placed up to five spots ahead of the end of the `waiting` line and removed from this list.
1. `waiting` holds customers who are present and waiting for a table.  This should be a doubly-linked list.
1. `appetizers` holds the appetizers that can be given to customers.  New appetizers are added to this queue periodically, and appetizers are given to waiting customers periodically.  This should be a queue.
1. `buzzers` holds the buzzers that are handed out to customers as they start waiting.  This should be a stack.  Push eight initial buzzers onto the stack before starting the data run.
1. `songs` holds the songs we play in the background.  This should be a circular list.  Add three initial songs: Song 1, Song 2, and Song 3.

Once the four lists are created, read `data.csv` and interate through the commands.  You can either use a CSV library in your language, or you can simply split each line by comma (there are no commas in the values).  On each line, call the appropriate method in your data structures.   

Each time you run a command, print the zero-based file line number followed by the command, in this format:

`LineNum:FileLine`

Note that some commands in the file are meant to fail, such as trying to insert a value beyond the bounds of the linked list.  You need to wrap each call in a try/catch exception block and print the following when this occurs:

`Error: <msg from your class here>`


## Example

The `data_example.csv` file contains an example set of instructions you can work with.  I suggest you cut this file down to one or two instructions at a time as you develop rather than try to run the entire file at once.

I've included the output of my assignment in the `output_example.txt` file so you can see exactly how your output should look. 


## Submitting the Assignment

Zip the following files and submit on Learning Suite:

```
main.py
linkedlist.py
circularlist.py
doublylinkedlist.py
stack.py
queue.py
data.csv
output.txt
(add any additional files needed to run your program)
```