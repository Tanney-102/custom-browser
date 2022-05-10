class Element:
  def __init__(self, tagName, attributes, parent):
    self.tagName = tagName
    self.attributes = attributes
    self.children = []
    self.parent = parent
    
  def __repr__(self):
    return '<' + self.tagName + '>'
    