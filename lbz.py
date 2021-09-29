import pylistenbrainz
import urllib3

def doesAccExist(uname):
    url = "https://listenbrainz.org/user/" + uname
    http = urllib3.PoolManager()
    req = http.request('GET', url)
    if(req.status == 404):
        return false
    else:
        return true
