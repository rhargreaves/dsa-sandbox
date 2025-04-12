""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
import sys


def debug(context='', **kwargs):
    print((context + ": " if context else '') +
          ' '.join(f"{k}={v}" for k, v in kwargs.items()), file=sys.stderr)


def check_binary_search_tree_(node):

    def walk(node, min_val, max_val):
        debug("walk", node=node.data, min_val=min_val, max_val=max_val)

        if node.data > max_val or node.data < min_val:
            debug("out of range!", node=node.data, min_val=min_val, max_val=max_val)
            return False
        result = True

        if node.left:
            debug("got left", node=node.data, left=node.left.data)
            if node.left.data < node.data:
                debug("left less. moving")
                result = walk(node.left, min_val, node.data-1)
            else:
                debug("left more. FALSE")
                return False
        else:
            debug("no left")

        if node.right:
            debug("got right", node=node.data, min_val=min_val, max_val=max_val)
            if node.right.data > node.data:
                debug("right more. moving")
                result = result and walk(node.right, node.data+1, max_val)
            else:
                debug("right less. FALSE")
                return False
        else:
            debug("no right")

        debug("result", node=node.data, result=result)
        return result

    return walk(node, -sys.maxsize, sys.maxsize)
