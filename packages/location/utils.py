def sliceProtocol(url):
  SUPPORTED_PROTOCOLS = ['http', 'https']
  DELIMITER = '://'

  protocol, restUrl = url.split(DELIMITER)
  assert protocol in SUPPORTED_PROTOCOLS, 'unsupported protocol {}'.format(protocol)

  return (restUrl, protocol)

def sliceFragment(url):
  return sliceSlug(url, '#')

def sliceSearch(url):
  assert not '#' in url, 'should slice "fragment" first'
  return sliceSlug(url, '?')

def slicePathname(url):
  assert not '#' in url, 'should slice "fragment" first'
  assert not '?' in url, 'should slice "search" first'
  return sliceSlug(url, '/', 1)

def slicePort(url):
  assert not '#' in url, 'should slice "fragment" first'
  assert not '?' in url, 'should slice "search" first'
  assert not '/' in url, 'should slice "pathname" first'
  return sliceSlug(url, ':')

def sliceSlug(url, delimiter, maxSplitCount = -1):
  url, *slug = url.split(delimiter, maxSplitCount)
  assert len(slug) <= 1, 'invalid url'
  return (
    url, 
    delimiter + slug[0] if len(slug) == 1 else ''
  )
