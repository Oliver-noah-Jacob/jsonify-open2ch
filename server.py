from flask import Flask, jsonify, request
from func import bbs_list, bbs_board, bbs_thread
from func import typedef as td
# for open2ch
import requests

app = Flask(__name__)

raw_s = requests.Session()

@app.route("/")
def root():
    return "42"

@app.route("/bbslist/opunu")
def bbs_opunu():
    """bbslist(opunu)

    return:
        json
    """
    resp: td.OpenAccessReturn = bbs_list.read_opunu(raw_s)
    print(resp)
    return jsonify(resp.responce)

@app.route("/bbslist/main")
def bbs_main():
    """return bbslist(main)

    return:
        json
    """
    resp: td.OpenAccessReturn = bbs_list.read_main(raw_s)
    print(resp)
    return jsonify(resp.responce)

@app.route("/bbs/<server>/<name>/subject", methods=["get"])
def subject(server=None, name=None):
    resp: td.OpenAccessReturn = bbs_board.subject(
        raw_s, server, name
    )
    print(resp)
    return jsonify(resp.responce)

@app.route("/bbs/<server>/<name>/dat/<dat_key>", methods=["get"])
def dat(server=None, name=None, dat_key=None):
    resp: td.OpenAccessReturn = bbs_thread.read_dat(
        raw_s, server, name, dat_key
    )
    print(resp)
    return jsonify(resp.responce)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)