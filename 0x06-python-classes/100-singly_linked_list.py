#!/usr/bin/python3
"""
A module that defines a class Node of a singly linked list
"""


class Node:
    """
    Node Class

    Attributes:
        data (int): Integer contained in the node.
        next_node (Node): Pointer to the next node.
    """

    def __init__(self, data, next_node=None):
        """
        The __init__ method initializes attributes that are instantiated whenever an object is created

        Args:
            data (int): Integer held by the node.
            next_node (:obj:`Node`, optional): Pointer to the next node. Defaults to None.

        Raises:
            TypeError: If the data provided is not an integer
        """

        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """ Getter that returns the data """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for data

        Args:
            value (int): Integer.

        Raises:
            TypeError: If data provided is not an integer.
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Getter that returns the next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for next_node

        Args:
            value (:obj:`Node`:): Node object.

        Raises:
            TypeError: If the next node is not a node object.
        """

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """str: data string"""
        return str(self.__data)


class SinglyLinkedList(object):
    """
    SinglyLinkedList Class

    Attributes:
        head (Node): Head node.
    """

    def __init__(self):
        self.__head = None

    def __str__(self):
        """str: string"""
        current_node = self.__head
        count = 0
        sll = ""
        while current_node is not None:
            if count > 0:
                sll += "\n"
            sll += "{:d}".format(current_node.data)
            count += 1
            current_node = current_node.next_node
        return sll

    def sorted_insert(self, value):
        """
        sorted insert function

        Args:
            value (int): integer

        """

        new_node = Node(value)
        current_node = self.__head
        previous_node = None
        if current_node is None:
            self.__head = new_node
        else:
            while current_node is not None:
                if (current_node.data >= new_node.data and
                        previous_node is None):
                    new_node.next_node = current_node
                    self.__head = new_node
                    break
                if current_node.data >= new_node.data:
                    previous_node.next_node = new_node
                    new_node.next_node = current_node
                    break
                previous_node = current_node
                current_node = current_node.next_node
            if current_node is None:
                if previous_node is not None:
                    previous_node.next_node = new_node
