def printHTMLTree(node, indent = 0):
  print(' ' * indent, node)
  for child in node.children:
    printHTMLTree(child, indent + 2)