"""
A "tree" of knowledge, where each node is a piece of knowledge
previously learned, and each edge is a relationship between two
or more nodes. 
"""

class Node:
    """
    A node represents a piece of knowledge.
    """
    def __init__(self, title: str, info: str) -> None:
        """Initialize a new node."""
        self.title = title
        self.info = info
        self.links = {}

    # need to add pruning method to promote/demote links
    # and to help avoid duplicates
    def add_link(self, node: 'Node', weight: int) -> None:
        """Add a link to another node. The weight is the
        frequency in which the node is accessed from the current
        node. The weight is used to determine the importance of 
        the node when looking to make connections to other nodes.
        """
        if node not in self.links:
            self.links[node] = weight

    def get_links(self) -> list:
        """Return a list of links."""
        return self.links

    def increment_link(self, node: 'Node') -> None:
        """Increment the weight of a link."""
        self.links[node] += 1

    def is_empty(self) -> bool:
        """Return True if the node has no links."""
        return len(self.links) == 0


class KnowledgeTree:
    """
    A "tree" of knowledge, where each node is a piece of knowledge.
    there may be completely unrelated nodes, or nodes that are
    related to each other, hence the need for a tree.
    """
    def __init__(self, username: str) -> None:
        """Initialize a new knowledge tree."""
        self.root = Node(username, "where it all begins...")

    def add_node(self, node: Node) -> None:
        """Add a node to the tree."""
        if self.root.links.is_empty():
            self.root.add_link(node, 1)
        else:
            # recursively check it's not in the tree
            # TODO: figure out how to add a node such that
            # it is not duplicated anywhere in the tree
            pass

