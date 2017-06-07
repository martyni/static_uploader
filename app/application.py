from flask import Flask, Response, request, url_for, redirect, jsonify, render_template
import boto3
import datetime
import re
from requests import get

app = Flask(__name__)
client = boto3.client("s3")

cache = {}
time_format = "%Y-%M-%d %H:%M:%s"
author = "Martyn Pratt"
email = "martynjamespratt@gmail.com"
s3_link = "https://s3-eu-west-1.amazonaws.com/{}/"


def url_sanitizer(raw_path):
    if ".amazonaws.com" not in request.url:
        return raw_path.replace('/prod', '').replace('/stge', '').replace('/dev', '')
    else:
        return raw_path


def path_sanitizer(raw_path):
    return raw_path.lower().replace("_", " ")


def url_4(*args, **qwargs):
    raw_path = url_for(*args, **qwargs)
    return url_sanitizer(raw_path)


def time_dump():
    return datetime.datetime.utcnow().strftime(time_format)


def time_load(time_string):
    return datetime.datetime.strptime(time_string, time_format)


def time_diff(time_1, time_2):
    if type(time_1) == str:
        time_1 = datetime.datetime.strptime(time_1,  time_format)
    if type(time_2) == str:
        time_2 = datetime.datetime.strptime(time_2,  time_format)
    return time_1 - time_2


def main(path=""):
    return {"path": path}


def api(path="", error=None, meta={}):
    error_status_code = 400
    path = path_sanitizer(path)
    payload = {
        "error": error,
        "path": path,
        "response": {},
        "meta": meta
    }
    payload["meta"]["date"] = time_dump()
    payload["meta"]["url"] = url_sanitizer(request.url)
    payload["meta"]["remote_addr"] = request.remote_addr
    payload["meta"]["user_agent"] = str(request.user_agent)
    payload["meta"]["status"] = 200
    payload["response"] = main(path=path)
    if payload["response"].get("error"):
        payload["error"] = payload["response"]["error"]
    if not payload["response"]:
        payload["error"] = "Series {} not found".format(path)
    if not payload["error"]:
        return jsonify(payload)
    else:
        payload["meta"]["status"] = error_status_code
        response = jsonify(payload)
        response.status_code = error_status_code
        return response

@app.route('/test')
def test():
    return 'OMG'


@app.route('/error_test')
def error_test():
    return api(path="error_test", error="here is an error")


@app.route('/')
def list_files():
    request_path = url_4("list_files")
    request_path = request_path + "/" if request_path[-1] != "/" else request_path
    print request_path
    return render_template("base.html", request_path=request_path, links={"api_root": url_4("api_root")})

@app.route('/api')
def api_root():
    return api()


@app.route('/api/<path>')
def api_path(path):
    return api(path=path)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
