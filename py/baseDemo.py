#!/usr/bin/env python
# @Time    : 2026/9/3 11:42
# @Author  : tushanfirm
# @File    : baseDemo.py
# @Software: PyCharm
import flask

app = flask.Flask(__name__)

app.config["FLAG"] = "test"


@app.route("/")
def index():
    return open(__file__).read()


@app.route("/shrine/<path:shrine>")
def shrine(shrine):

    def safe_jinja(s):
        s = s.replace("(", "").replace(")", "")
        blacklist = ["config", "self"]
        return "".join(["{{% set {}=None%}}".format(c) for c in blacklist]) + s

    return flask.render_template_string(safe_jinja(shrine))


if __name__ == "__main__":
    app.run(debug=True)
