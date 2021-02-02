import re

from . import typedef as td

from cachecontrol import CacheControl 
from cachecontrol.caches import FileCache
import requests

post_pattern = re.compile(
    r"^(?P<name>.*)<>(?P<mail>.*)<>(?P<timestamp>.+)\sID:(?P<ID>[a-zA-Z0-9\?]{3})<>\s(?P<text>.*)\s<>(?P<title>.*)$"
    )

def read_dat(
    sess: requests.Session,
    server: str,
    name: str,
    dat_key: str
    ) -> td.OpenAccessReturn:
    """Read dat.

    parameters:
        sess(requests.Session): session
        server(str): name of the server; hayabusa, open etc.
        name(str): name of the board
        dat_key(str): dat key; like 1234567890.dat
    
    returns:
        OpenAccessReturn
    """

    # access open2ch
    url = f"https://{server}.open2ch.net/{name}/dat/{dat_key}"
    dat = sess.get(url=url)
    dat_line = [l for l in dat.text.split('\n') if l]
    # for l in dat_line:
    #     print(post_pattern.search(l).groupdict())
    dat_dict = {
        i+1 : post_pattern.search(l).groupdict() \
            for i, l in enumerate(dat_line)
    }

    return td.OpenAccessReturn(
        url=url,
        status_code=dat.status_code,
#        responce=dat_dict
        responce=dat_dict
    )