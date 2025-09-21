#!/usr/bin/python3
"""Classes for a simple linked list."""


# Node holds one number and the link to the next
class Node:
    """Node with int data and next_node."""

    def __init__(self, data, next_node=None):
        """Start node with data and optional next."""
        self.data = data            # must be int
        self.next_node = next_node  # None or Node

    @property
    def data(self):
        """Get data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data (int only)."""
        if not isinstance(value, int):  # must be int
            raise TypeError("data must be an integer")
        self.__data = value             # save int

    @property
    def next_node(self):
        """Get next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next (None or Node)."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value        # save link


class SinglyLinkedList:
    """Singly linked list with print and sorted insert."""

    def __init__(self):
        """Start empty."""
        self.__head = None  # no nodes yet

    def __str__(self):
        """Show numbers line by line."""
        out = []  # collect strings
        cur = self.__head  # start at head
        while cur is not None:  # walk chain
            out.append(str(cur.data))  # add number
            cur = cur.next_node  # move next
        return "\n".join(out)  # join with newline

    def sorted_insert(self, value):
        """Insert value in ascending order."""
        new = Node(value)  # new node

        if self.__head is None or value <= self.__head.data:
            # insert at head
            new.next_node = self.__head
            self.__head = new
            return

        cur = self.__head
        while cur.next_node is not None and cur.next_node.data < value:
            cur = cur.next_node  # move forward

        # insert new node here
        new.next_node = cur.next_node
        cur.next_node = new
