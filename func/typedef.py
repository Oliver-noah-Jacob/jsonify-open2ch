from enum import Enum
import os
import pathlib
import time
from typing import List, Literal, NamedTuple ,Union

from cachecontrol import CacheControl 
from cachecontrol.caches import FileCache
import requests

# Type class

class OpenAccessReturn(NamedTuple):
    url: str
    status_code: Literal[requests.status_codes]
    responce: dict

    def __str__(self) ->str:
        return f"url: {self.url}[code {self.status_code}] \n{self.responce}"

class FileAccessMode(Enum):
    rt = 'rt'
    rb = 'rb'
    at = 'at'
    ab = 'ab'
    wt = 'wt'
    wb = 'wb'
    xt = 'xt'
    xb = 'xb'

# Type alias

PathSegments = Union[
    str, pathlib.Path, os.PathLike, 
    List[str], List[pathlib.Path], List[os.PathLike]
    ]

WritableMode = Literal[
    FileAccessMode.at, FileAccessMode.ab, 
    FileAccessMode.wt, FileAccessMode.wb,
    FileAccessMode.xt, FileAccessMode.xb
    ]

ReadableMode = Literal[
    FileAccessMode.rt, FileAccessMode.rb
]