from . import typedef as td

# for open2ch
import lxml.html
import requests

def read_opunu(s: requests.Session) -> td.OpenAccessReturn:
    """return opunu board

    parameters:
        s(requests.Session): session
    
    returns:
        OpenAccessReturn
    """
    res = s.get("https://r.open2ch.net/list")
    opunu = lxml.html.fromstring(res.text)
    resp_dict = {
        a.attrib.get("title"): a.attrib.get("href") for a \
            in opunu.xpath("//div[@class='list']/a") if a.attrib.get("title")
        }

    return td.OpenAccessReturn(
        url="https://r.open2ch.net/list",
        status_code = res.status_code,
        responce=resp_dict
    )

def read_main(s: requests.Session) -> td.OpenAccessReturn:
    """return main board

    parameters:
        s(requests.Session): session
    
    returns:
        OpenAccessReturn
    """
    res = s.get("https://menu.open2ch.net/bbsmenu.html")
    bbsmenu = lxml.html.fromstring(res.text)
    resp_dict = {
        a.text: a.attrib.get("href") for a \
            in bbsmenu.xpath("//a[contains(@href, 'open2ch.net/')]") if a.text
        }

    return td.OpenAccessReturn(
        url="https://menu.open2ch.net/bbsmenu.html",
        status_code=res.status_code,
        responce=resp_dict
    )