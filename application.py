from flask import Flask, request, render_template
application = Flask(__name__)

@application.route("/", methods=["GET","POST"])
def index():    
    if request.method == "POST":        
        q = request.form.get("q")
        return(render_template("index.html",result=r))    
    else:
        return(render_template("index.html",result="waiting.........."))

if __name__ == "__main__":    
    application.run()
