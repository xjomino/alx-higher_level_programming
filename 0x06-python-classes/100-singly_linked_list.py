#!/usr/bin/python3


class Node:
    ''' node of a singly linked list'''

    def __init__(self, data, next_node=None):
        ''' initialized a node
        '''
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        ''' method that returns the data of a node
        '''
        return self._data

    @data.setter
    def data(self, value):
        ''' method that sets the data of a node
        '''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        ''' method that returns the next node
        '''
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        ''' method that sets the next node
        '''
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    ''' a singly linked list
    '''
    def __init__(self):
        ''' initializes a singly linked list
        '''
        self._head = None

    def __str__(self):
        ''' the printable representation of the linked list
        '''
        res = []
        curr = self._head
        while curr:
            res.append(str(curr.data))
            curr = curr.next_node
        return "\n".join(res)

    def sorted_insert(self, value):
        ''' method that inserts a node into a linked list
        '''
        new_node = Node(value)
        if not self._head:
            self._head = new_node
            return
        if self._head.data >= value:
            new_node.next_node = self._head
            self._head = new_node
            return
        curr = self._head
        while curr.next_node and curr.next_node.data < value:
            curr = curr.next_node
        new_node.next_node = curr.next_node
        curr.next_node = new_node
