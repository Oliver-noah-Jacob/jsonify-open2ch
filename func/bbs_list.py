from typing import Optional
import re

# for API
from flask import jsonify

# for open2ch
from cachecontrol import CacheControl 
from cachecontrol.caches import FileCache
import lxml.html
import requests

# regex for dat, title, count
re_dat=re.compile(r"(^[0-9]+\.dat).+")
re_title=re.compile(r"<>(.+)\s")
re_count=re.compile(r"<>.+\s\(([0-9]+)\)")


def read_opunu(s: requests.Session)->dict:
    res = s.get("https://r.open2ch.net/list")
    opunu = lxml.html.fromstring(res.text)
    return {
        "opunu" : {a.attrib.get("title"): a.attrib.get("href") for a in opunu.xpath("//div[@class='list']/a") if a.attrib.get("title")},
        "state" : dict(s.headers),
        "resp" : dict(res.headers),
    }

def read_main(s: requests.Session)->dict:
    res = s.get("https://menu.open2ch.net/bbsmenu.html")
    bbsmenu = lxml.html.fromstring(res.text)
    return {
        "main" : {a.text: a.attrib.get("href") for a in bbsmenu.xpath("//a[contains(@href, 'open2ch.net/')]") if a.text},
        "state" : dict(s.headers),
        "resp" : dict(res.headers),
    }

def read_board(s: requests.Session, name: str)->Optional[dict]:
    #if mode == "main":
    #    print("read main board")
    #    bbs_dict=read_main(s)["main"]
    #elif mode == "opunu":
    #    print("read opunu board")
    #    bbs_dict=read_opunu(s)["opunu"]
    #else:
    #    print(f"Invalid mode: {mode}")
    #    return f"Invalid mode: {mode}"
    bbs_dict = read_main(s)["main"]
    bbs_dict.update(read_opunu(s)["opunu"])

    print(bbs_dict)
    if name in bbs_dict.keys():
        subject_url = bbs_dict[name] + "subject.txt"
        print(f"{name} found -> {subject_url}")
        res = s.get(subject_url)
        subject_dict = {
            re_title.search(s).group(1) : {
                "dat" : re_dat.search(s).group(1),
                "count" : re_count.search(s).group(1)
            } for s in res.text.split("\n") if s
        }
        return jsonify(subject_dict)
    else:
        print(f"{name} not found")
        return f"{name} not found"