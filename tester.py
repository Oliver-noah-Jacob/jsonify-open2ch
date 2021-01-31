import json
import requests

if __name__ == "__main__":
    # create session
    sess = requests.Session()
    
    # /bbslist test
    # test_list = [
    #     "http://0.0.0.0:5000/bbslist",
    #     "http://0.0.0.0:5000/bbslist/main", 
    #     "http://0.0.0.0:5000/bbslist/opunu"]
    # print("-*-*- BBS list test -*-*-")
    # for u in test_list:
    #     print(f"\nTEST {u}")
    #     res = sess.get(url=u)
    #     data = json.loads(res.text)
    #     print(f"URL: {res.url}\n====\nresponce: {data}")

    # /subject test
    url = "http://0.0.0.0:5000"
    test_board = [
        ("Linux作る板" ,"open", "1609418086"),
        ("なんでも実況(ジュピター)", "hayabusa", "livejupiter")
        ]
    print("-*-*- BBS subject test -*-*-")
    for b in test_board:
        print(f"\nTEST {b[0]}")
        res = sess.get(url=f"{url}/bbs/{b[1]}/{b[2]}/subject")
        data = json.loads(res.text)
        print(f"URL: {res.url}\n====\nresponce: {data}")
