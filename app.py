from flask import Flask, render_template, render_template_string
from markupsafe import escape
from urllib.request import urlopen
import markdown
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! </p>"

@app.route("/")
def template():
    return render_template("index.html")


#def get_articles_from_github(): 
    

@app.route('/call')
def get_html_content():
    text = """
    write me markdown with image
    ![alt text](https://raw.githubusercontent.com/MaciekWin3/Moonwalk/master/docs/logo.png)
    """
    url = 'https://raw.githubusercontent.com/MaciekWin3/TermKeyVault/master/README.md'
    
    try:
        # Make an HTTP request to the URL and read the HTML content
        with urlopen(url) as response:
            html_content = response.read().decode('utf-8')
        
        # Parse the HTML content as Markdown
        markdown_content = markdown.markdown(html_content)
        
        return render_template_string(markdown_content)
    except Exception as e:
        return f"Failed to retrieve or parse content. Error: {str(e)}"