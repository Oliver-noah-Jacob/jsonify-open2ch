import os
import pathlib
import time
from typing import List, Union

from cachecontrol import CacheControl 
from cachecontrol.caches import FileCache

PathSegments = Union[
    str, pathlib.Path, os.PathLike, 
    List[str], List[pathlib.Path], List[os.PathLike]
    ]