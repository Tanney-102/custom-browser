import socket
import ssl
from .constants import NEW_LINE

def createSocketManager(host, needSSL):
  socketManager = socket.socket(
    family = socket.AF_INET,
    type = socket.SOCK_STREAM,
    proto = socket.IPPROTO_TCP,
  )
  if needSSL:
    socketManager = wrapSocketBySSL(socketManager, host)
  
  return socketManager

def wrapSocketBySSL(socketManager, host):
  ctx = ssl.create_default_context()
  return ctx.wrap_socket(
    sock = socketManager,
    server_hostname = host,
  )

def parseResponse(response):
  statusLine = response.readline()
  version, status, explanation = statusLine.split(' ', 2)
  # status 200인 경우만 처리
  assert status == '200', '{}: {}'.format(status, explanation)

  headers = getHeaders(response)
  body = response.read()
  
  return {
    'headers': headers,
    'body': body,
  }

def getHeaders(response):
  headers = {}
  line = response.readline()

  while line != NEW_LINE:
    header, value = line.split(':', 1)
    headers[header.lower()] = value.strip()
    line = response.readline()
  return headers
