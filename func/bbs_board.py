from typing import Optional, Tuple
import re

from . import typedef as td

# for open2ch
from cachecontrol import CacheControl 
from cachecontrol.caches import FileCache
import lxml.html
import requests

# regex for dat, title, count
re_dat=re.compile(r"(^[0-9]+\.dat).+")
re_title=re.compile(r"<>(.+)\s\([0-9]+\)")
re_count=re.compile(r"<>.+\s\(([0-9]+)\)")

def subject(sess: requests.Session, server: str, name: str) -> td.OpenAccessReturn:
    """Read subject.txt.

    parameters:
        sess(requests.Session): session
        server(str): name of the server; hayabusa, open etc.
        name(str): name of the board
    
    returns:
        OpenAccessReturn
    """

    # access open2ch
    url = f"http://{server}.open2ch.net/{name}/subject.txt"
    subject = sess.get(url=url)

    subject_dict = {
        re_title.search(s).group(1) : {
            "dat" : re_dat.search(s).group(1),
            "count" : re_count.search(s).group(1)
        } for s in subject.text.split('\n') if s
    }

    return td.OpenAccessReturn(
        url=url,
        status_code=subject.status_code,
        responce=subject_dict
    )