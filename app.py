from flask import Flask, render_template, request
from datetime import date
from validation_methods import validate_all

supported_languages = ["en", "pl"]

app=Flask(__name__)

@app.route("/", methods=["get"])
@app.route("/<language>", methods=["get"])
def index(language=None):
    if language==None:
        language = request.accept_languages.best_match(supported_languages)
    return render_template(language+"/index.html")
    

@app.route("/<language>/place_order", methods=["get"])
def place_order(language):
    error=validate_all(request.args.get("e-mail"), request.args.get("telephone"), request.args.get("postcode"), language)
    if error!="":
        return  render_template(language+"/index.html", warning=error)
    arguments=request.args.items()
    file=open("data.csv", "a+" )
    line=date.today().strftime("%d/%m/%Y")
    for k, v in arguments:
        line=line+";"+v
    line=line+"\n"
    file.write(line)
    file.close()
    return render_template(language+"/confirmation.html", name=request.args.get("name"), email=request.args.get("e-mail"), telephone_number=request.args.get("telephone"), address=request.args.get("address"), post_code=request.args.get("postcode"))
   