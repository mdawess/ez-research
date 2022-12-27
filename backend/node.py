"""
A "tree" of knowledge, where each node is a piece of knowledge
previously learned, and each edge is a relationship between two
or more nodes. 
"""

class Node:
    """
    A node represents a piece of knowledge.
    """
    def __init__(self, title: str, tldr: str) -> None:
        """Initialize a new node."""
        self.id = None
        self.title = title
        self.tldr = tldr
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

    def is_empty(self) -> bool:
        """Return True if the node has no links."""
        return len(self.links) == 0