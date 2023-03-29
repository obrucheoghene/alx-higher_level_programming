#!/usr/bin/python3
"""A mode that defines a node and singly linked list classes"""


class Node:
    """A that defines the node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Node construtor"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Get node data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set node data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get next node"""
        self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next node"""
        if type(value) is not type(self) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list"""

    def __init__(self):
        """Contruct initialized object"""
        self.__head = None

    def sorted_insert(self, value):
        """A method that inserts a new Node into
        the correct sorted position in the
        list (increasing order)
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node

            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Class string methon"""
        temp = self.__head
        values = []
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
