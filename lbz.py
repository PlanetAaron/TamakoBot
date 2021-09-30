import pylistenbrainz
import urllib3

lbz = pylistenbrainz.ListenBrainz()

def doesAccExist(uname):
    uname = str(uname)
    url = "https://listenbrainz.org/user/" + uname
    http = urllib3.PoolManager()
    req = http.request('GET', url)
    if(req.status == 404):
        return False
    else:
        return True

def nowPlaying(uname):
    # is someone's username is just numbers we need to fix it here
    uname = str(uname)
    np = lbz.get_playing_now(uname)
    if(np == None):
        return None
    print(np)
    print(np.track_name)
    return np