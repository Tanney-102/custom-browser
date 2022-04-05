from .utils import sliceProtocol, sliceFragment, sliceSearch ,slicePathname, slicePort

class Location:
  def __init__(self, url):
    self.url = url
    self.protocol = ''
    self.fragment = ''
    self.search = ''
    self.pathname = ''
    self.host = ''
    self.port = ''

    self._parse()
  
  def _parse(self):
    restUrl = self.url
    restUrl, self.protocol = sliceProtocol(restUrl)
    restUrl, self.fragment = sliceFragment(restUrl)
    restUrl, self.search = sliceSearch(restUrl)
    restUrl, self.pathname = slicePathname(restUrl)
    self.host, self.port = slicePort(restUrl)

    defaultPort = 80 if self.protocol == 'http' else 443
    self.port = self.port.replace(':', '')
    self.port = int(self.port) if not self.port == '' else defaultPort

