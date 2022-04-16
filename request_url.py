import packages.request as request

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

  response = request.get(url)
  printTextInTagsOnly(response['body'])