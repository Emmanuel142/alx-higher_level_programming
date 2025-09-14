#!/usr/bin/python3

"""Create a class Node that define the node of
    a single linked list
    """


class Node:
    """This class create a node for a linked list
    Args:
        data (int): The data in the linked list
        next_node: Address of the next node
    Attributes:
        No attributes
    """
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if not isinstance(next_node, Node) or next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        """This property set data in the list
        Args:
            value (int): The input in the list
        Raises:
            TypeError: if the value is not an integer
            """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """This property set the next_node
        Args:
            value (object): This stores the node
        """
        if value is not None or value not isinstance(value,Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SingleLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if new_node.next_node is None or self.__head.data < value:
            if value > current_node.data:
                new_node.next_node = self.__head
                self.__head = new_node
            else:
                current = self.__head


