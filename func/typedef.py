import os
import pathlib
import time
from typing import List, NamedTuple ,Union

from cachecontrol import CacheControl 
from cachecontrol.caches import FileCache
import requests

PathSegments = Union[
    str, pathlib.Path, os.PathLike, 
    List[str], List[pathlib.Path], List[os.PathLike]
    ]

class OpenAccessReturn(NamedTuple):
    url: str
    status_code: int
    responce: dict

    def __str__(self) ->str:
        return f"url: {self.url}[code {self.status_code}] \n{self.responce}"