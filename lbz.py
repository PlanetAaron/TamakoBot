import pylistenbrainz
import urllib3

def doesAccExist(uname):
    url = "https://listenbrainz.org/user/" + uname