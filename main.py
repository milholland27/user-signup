from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/form-inputs")
def display_form_inputs():
    return index.html

@app.route("/form-inputs", methods=['POST'])
def print_form_values():
    resp = ""
    for field in request.form.keys():
        resp += "<b>{key}</b>: {value}<br>".format(key=field, value=request.form[field])

    return resp
    
app.run()
       
    