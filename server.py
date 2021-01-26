from flask import Flask, jsonify, request
from func import bbs_list

# for open2ch
from cachecontrol import CacheControl 
from cachecontrol.caches import FileCache
import lxml.html
import requests

app = Flask(__name__)

raw_s = requests.Session()
cached_session = CacheControl(raw_s, cache=FileCache('.webcache'))

@app.route("/")
def root():
    return "42"

@app.route("/bbslist")
def bbs_all():
    bbs = bbs_list.read_main(cached_session)["main"]
    bbs.update(bbs_list.read_opunu(cached_session)["opunu"])
    return jsonify(bbs)

@app.route("/bbslist/opunu")
def bbs_opunu():
    return jsonify(bbs_list.read_opunu(cached_session))

@app.route("/bbslist/main")
def bbs_main():
    return jsonify(bbs_list.read_main(cached_session))

@app.route("/subject", methods=["get"])
def subject():
    name = request.args.get("name")
    print(f"name : {name}")
    return bbs_list.read_board(cached_session, name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)