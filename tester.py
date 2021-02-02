import json
from pprint import pprint
import re

import requests

server_pattern = re.compile(
    r"^https?://(?P<server>.+)\.open2ch\.net/(?P<name>.+)/$"
)

if __name__ == "__main__":
    # create session
    sess = requests.Session()
    
    # # /bbslist test
    # test_list = [
    #     "http://0.0.0.0:5000/bbslist/main", 
    #     "http://0.0.0.0:5000/bbslist/opunu"]
    # print("-*-*- BBS list test -*-*-")
    # for u in test_list:
    #     print(f"\nTEST {u}")
    #     res = sess.get(url=u)
    #     data = json.loads(res.text)
    #     print(f"URL: {res.url}\n====\nresponce: {data}")

    # # /subject test
    # url = "http://0.0.0.0:5000"
    # test_board = [
    #     ("Linux作る板" ,"open", "1609418086"),
    #     ("なんでも実況(ジュピター)", "hayabusa", "livejupiter")
    #     ]
    # print("-*-*- BBS subject test -*-*-")
    # for b in test_board:
    #     print(f"\nTEST {b[0]}")
    #     res = sess.get(url=f"{url}/bbs/{b[1]}/{b[2]}/subject")
    #     data = json.loads(res.text)
    #     print(f"URL: {res.url}\n====\nresponce: {data}")

    # dat test
    opunu_json = json.loads(
        sess.get("http://0.0.0.0:5000/bbslist/opunu").text
    )
    opunu_dic = {
        key: server_pattern.search(val).groupdict() \
            for key, val in opunu_json.items()
    }
    print(opunu_dic)
    linux_server = opunu_dic.get("Linux作る板")
    subj_json = json.loads(
        sess.get(
            f"http://0.0.0.0:5000/bbs/{linux_server['server']}/{linux_server['name']}/subject"
            ).text
    )
    dat_key = subj_json["おーぷんをpythonで読めるか実験するスレ"]["dat"]
    thread_json = json.loads(
        sess.get(
            f"http://0.0.0.0:5000/bbs/{linux_server['server']}/{linux_server['name']}/dat/{dat_key}"
        ).text
    )
    for v in thread_json.values():
        print(v)