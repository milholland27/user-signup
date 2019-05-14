from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def user_signup():
    resp = ("")
    for field in request.form.keys():
        resp += "<b>{key}</b>: {value}<br>".format(key=field, value=request.form[field])

    return resp
    
app.run()
       
    