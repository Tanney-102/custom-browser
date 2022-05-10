import packages.request as request
# from packages.browser import Browser
from packages.htmlParser import HTMLParser
from packages.utils import printHTMLTree

def printTextInTagsOnly(textHtml):
  inAngle = False
  for char in textHtml:
    if char == '<':
      inAngle = True
    elif char == '>':
      inAngle = False
    elif not inAngle:
      print(char, end='')

if __name__ == '__main__':
  import sys

  DEFAULT_URL = 'http://example.org' 
  url = DEFAULT_URL if len(sys.argv) <= 1 else sys.argv[1]

  # printTextInTagsOnly(response['body'])

  # browser = Browser()
  # browser.run()
  # browser.loadPage(url)
  
  response = request.get(url)
  nodes = HTMLParser(response['body']).parse()
  printHTMLTree(nodes)