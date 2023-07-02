#!/usr/bin/python3
"""Defines Singly Linked List"""


class Node:
    """Represents a Singly linked list node

    Args:
        data (int): the value of the node
        next_node (Node): the next node pointer
            (defaults to None)
    Attributes:
        data (int): the value of the node
        next_node (Node): the next node pointer
    """

    def __init__(self, data: int, next_node=None) -> None:
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value
        pass

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not (type(value) is not Node or type(value) is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a Singly linked list"""

    def __init__(self) -> None:
        self.__head = Node(0)
        pass

    def sorted_insert(self, value: int):
        if self.__head.data == 0:
            self.__head = Node(value)
        else:
            new_node = Node(value)
            tmp_head = self.__head
            if tmp_head.data > value:
                new_node.next_node = tmp_head
                self.__head = new_node
            else:
                while (tmp_head.next_node is not None
                        and tmp_head.next_node.data < value):
                    tmp_head = tmp_head.next_node
                new_node.next_node = tmp_head.next_node
                tmp_head.next_node = new_node

    def __str__(self) -> str:
        tmp_head = self.__head
        printable = ''
        while (tmp_head is not None):
            printable = printable+str(tmp_head.data)+'\n'
            tmp_head = tmp_head.next_node
        printable = printable[0:-1]
        return printable
