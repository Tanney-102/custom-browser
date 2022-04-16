from packages.location import Location
from packages.request.utils import createSocketManager, parseResponse
from packages.request.constants import NEW_LINE

def get(url):
  return send(url, 'GET')

def send(url, method):
  location = Location(url)
  needSSL = location.protocol == 'https'
  socketManager = createSocketManager(location.host, needSSL)
  requestPath = location.pathname + location.search + location.fragment
  if requestPath == '':
    requestPath = '/'

  socketManager.connect((location.host, location.port))
  socketManager.send(
    bytes('{} {} HTTP/1.0 {}'.format(
      method.upper(), 
      requestPath, 
      NEW_LINE,
    ), 'utf-8') +
    bytes('Host: {0}{1}{1}'.format(location.host, NEW_LINE), 'utf-8')
  )

  response = socketManager.makefile('r', encoding = 'utf-8', newline = NEW_LINE)
  parsedResponse = parseResponse(response)
  socketManager.close()

  return parsedResponse

