#from textblob import TextBlob
from flask import Flask

application = Flask(__name__)
from flask import render_template,request

@application.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        q = request.form.get("q")
        print(q)
        #r = TextBlob(q).sentiment
        return(render_template("index.html", r=q))
    else:
        return(render_template("index.html", result="waiting"))

if __name__=="__main__":
    application.run()
