from flask import Flask, render_template, abort
from markupsafe import escape
import markdown
import requests

user = "maciekwin3"
repo = "blog"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/articles")
def get_articles_from_github(): 
    url = "https://api.github.com/repos/{}/{}/git/trees/main?recursive=1".format(user, repo)
    r = requests.get(url)
    res = r.json()

    articles : str = []
    for file in res["tree"]:
        if file["path"].endswith(".md") and file["path"] != "README.md":
            # get me just name of file without whole path
            articles.append(file["path"].split("/")[-1].split(".")[0])

    return render_template("articles.html", articles=articles)

@app.route("/articles/<name>")
def get_article_from_github(name): 
    url = "https://api.github.com/repos/{}/{}/git/trees/main?recursive=1".format(user, repo)
    url_raw = "https://raw.githubusercontent.com/MaciekWin3/blog/main/"
    r = requests.get(url)
    res = r.json()

    for file in res["tree"]:
        if file["path"].endswith(".md") and file["path"] != "README.md":
            if file["path"] == "articles/" + escape(name) + ".md":
                content = requests.get(url_raw + file["path"])
                md = markdown.markdown(content.text)
                return render_template("article.html", content=md)
            else:
                continue

    abort(404)