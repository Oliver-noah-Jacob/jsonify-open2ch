from flask import Flask, jsonify, request
from func import bbs_list, bbs_board
from func import typedef as td
# for open2ch
#from cachecontrol import CacheControl 
#from cachecontrol.caches import FileCache
import lxml.html
import requests

app = Flask(__name__)

raw_s = requests.Session()
#cached_session = CacheControl(raw_s, cache=FileCache('.webcache'))

@app.route("/")
def root():
    return "42"

@app.route("/bbslist")
def bbs_all():
    """bbslist(main+opunu)

    return:
        json
    """
    bbs = bbs_list.read_main(raw_s)["main"]
    bbs.update(bbs_list.read_opunu(raw_s)["opunu"])
    return jsonify(bbs)

@app.route("/bbslist/opunu")
def bbs_opunu():
    """bbslist(opunu)

    return:
        json
    """
    return jsonify(bbs_list.read_opunu(raw_s))

@app.route("/bbslist/main")
def bbs_main():
    """return bbslist(main)

    return:
        json
    """
    return jsonify(bbs_list.read_main(raw_s))

@app.route("/bbs/<server>/<name>/subject", methods=["get"])
def subject(server=None, name=None):
    resp: td.OpenAccessReturn = bbs_board.subject(
        raw_s, server, name
    )
    print(resp)
    return jsonify(resp.responce)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)