from flask import Flask, request, render_template
application = Flask(__name__)

@application.route("/", methods=["GET","POST"])
def index():    
    if request.method == "POST":        
        r = float(request.form.get("rate"))
        return(render_template("index.html",result=r*(-50.6)+90.2))    
    else:
        return(render_template("index.html",result="waiting.........."))

if __name__ == "__main__":    
    application.run()

