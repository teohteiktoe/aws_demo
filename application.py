from textblob import TextBlob
from flask import Flask

application = Flask(__name__)
from flask import render_template,request

@application.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        print(text)
        r = TextBlob(text).sentiment
        return(render_template("index.html", result=r))
    else:
        return(render_template("index.html", result="waiting"))

if __name__=="__main__":
    application.run()
