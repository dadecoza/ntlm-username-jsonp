#!/usr/bin/env python
from flask import Flask, request, Response
from waitress import serve
import base64
import json

app = Flask(__name__)


@app.route('/js')
def index():
    callback = request.args.get('callback') or "setUsername"
    auth = request.headers["Authorization"] if "Authorization" in request.headers else None
    if auth and auth.startswith("NTLM"):
        data = base64.b64decode(auth[5:])
        if ord(data[8]) == 1:
            msg1 = bytearray([b'N', b'T', b'L', b'M', b'S', b'S', b'P', 0, 2, 0, 0, 0, 0, 0, 0, 0, 40, 0, 0, 0, 1, 130, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            auth1 = "NTLM " + base64.b64encode(msg1)
            return Response(status=401, headers={"WWW-Authenticate": auth1})
        elif ord(data[8]) == 3:
            pos = ord(data[40])
            end = pos+(ord(data[38])-1)
            username = data[pos:end]
            username = username.replace("\0","")
            js = "%s(%s)" % (callback, json.dumps({"username": username}))
            return js

    if not auth:
        return Response(status=401, headers={"WWW-Authenticate": "NTLM"})
    js = "%s(%s)" % (callback, json.dumps({"username": None}))
    return js


if __name__ == '__main__':
    serve(app, port=8080)
