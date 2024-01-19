from flask import Flask, render_template, render_template_string, abort
from markupsafe import escape
from urllib.request import urlopen
import markdown
import requests

user = "maciekwin3"
repo = "blog"

app = Flask(__name__)

@app.route("/")
def template():
    return render_template("index.html")

@app.route("/article/<name>")
def get_articles_from_github(name): 
    url = "https://api.github.com/repos/{}/{}/git/trees/main?recursive=1".format(user, repo)
    url_raw = "https://raw.githubusercontent.com/MaciekWin3/blog/main/"
    r = requests.get(url)
    res = r.json()
    print(res)

    for file in res["tree"]:
        if file["path"].endswith(".md") and file["path"] != "README.md":
            if file["path"] == "articles/" + escape(name) + ".md":
                content = requests.get(url_raw + file["path"])
                md = markdown.markdown(content.text)
                return render_template_string(md)
            else:
                continue

    abort(404)