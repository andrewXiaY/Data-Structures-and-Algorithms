# Node class for linked list
class Node(object):
    def __init__(self, data=None):
        self.data = data

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.data == other.data
        else:
            raise Exception("Comparison between {} and {} has not been implemented".format("<class 'Node'>", type(other)))

    def __ge__(self, other):
        if isinstance(other, Node):
            return self.data >= other.data
        else:
            raise Exception("Comparison between {} and {} has not been implemented".format("<class 'Node'>", type(other)))

    def __le__(self, other):
        if isinstance(other, Node):
            return self.data <= other.data
        else:
            raise Exception("Comparison between {} and {} has not been implemented".format("<class 'Node'>", type(other)))

    def __gt__(self, other):
        if isinstance(other, Node):
            return self.data > other.data
        else:
            raise Exception("Comparison between {} and {} has not been implemented".format("<class 'Node'>", type(other)))

    def __lt__(self, other):
        if isinstance(other, Node):
            return self.data < other.data
        else:
            raise Exception("Comparison between {} and {} has not been implemented".format("<class 'Node'>", type(other)))