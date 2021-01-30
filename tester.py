import json
import requests

if __name__ == "__main__":
    # create session
    sess = requests.Session()
    
    # /bbslist test
    test_list = [
        "http://0.0.0.0:5000/bbslist",
        "http://0.0.0.0:5000/bbslist/main", 
        "http://0.0.0.0:5000/bbslist/opunu"]
    print("-*-*- BBS list test -*-*-")
    for u in test_list:
        print(f"\nTEST {u}")
        res = sess.get(url=u)
        data = json.loads(res.text)
        print(f"URL: {res.url}\n====\nresponce: {data}")

    # /subject test
    url = "http://0.0.0.0:5000/subject"
    test_board = ["Linux作る板","なんでも実況J", "河川・ダム等", "R-18"]
    print("-*-*- BBS subject test -*-*-")
    for b in test_board:
        print(f"\nTEST {b}")
        res = sess.get(url=url + '/' + b)
        data = json.loads(res.text)
        print(f"URL: {res.url}\n====\nresponce: {data}")
