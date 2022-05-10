from packages.node import Text, Element

SELF_CLOSING_TAGS = [
  'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
  'link', 'meta', 'param', 'source', 'track', 'wbr',
]

class HTMLParser:
  def __init__(self, body):
    self.body = body
    self.unfinishedTagStack = []
  
  def parse(self):
    text = ''
    inTag = False
    for char in self.body:
      if char == '<':
        inTag = True
        if text: self.addText(text)
        text = ''
      elif char == '>':
        inTag = False
        self.addTag(text)
        text = ''
      else:
        text += char
    if not inTag and text:
      self.addText(text)
    return self.finish()

  def addText(self, text):
    if text.isspace(): return 
    
    parent = self.unfinishedTagStack[-1]
    textNode = Text(text, parent)
    parent.children.append(textNode)
    
  def addTag(self, tag):
    if tag.startswith('!'): return
    
    tag, attributes = self.getAttributes(tag)
    
    if tag.startswith('/'):
      self.closeRecentTag()
    elif tag in SELF_CLOSING_TAGS:
      parent = self.unfinishedTagStack[-1]
      node = Element(tag, attributes, parent)
      parent.children.append(node)
    else:
      self.openNewTag(tag, attributes)
   
  def closeRecentTag(self):   
    if len(self.unfinishedTagStack) == 1: return
    recentNode = self.unfinishedTagStack.pop()
    parent = self.unfinishedTagStack[-1]
    parent.children.append(recentNode)
  
  def openNewTag(self, tag, attributes):
    parent = self.unfinishedTagStack[-1] if self.unfinishedTagStack else None
    newNode = Element(tag, attributes, parent)
    self.unfinishedTagStack.append(newNode)
  
  def getAttributes(self, text):
    parts = text.split()
    tag = parts[0].lower()
    attributes = {}
    for attrPair in parts[1:]:
      if '=' in attrPair:
        key, value = attrPair.split('=', 1)
        if len(value) > 2 and value[0] in ["'", "\""]:
          value = value[1:-1]
        attributes[key.lower()] = value
      else:
        attributes[attrPair.lower()] = ''
    return tag, attributes

      
  def finish(self):
    if len(self.unfinishedTagStack) == 0:
      self.addTag('html')
    while len(self.unfinishedTagStack) > 1:
      self.closeRecentTag()
    return self.unfinishedTagStack.pop()