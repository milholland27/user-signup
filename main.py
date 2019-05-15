from flask import Flask, request, render_template, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def user_signup():
    
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    verify = request.form['verify']

    username_error = ''
    if len(username) <= 3 or len(username) >= 20 or " " in username:
        username_error = "That's not a valid username"

    password_error = ''
    if len(password) <= 3 or len(password) >= 20 or " " in password:
        password_error = "That's not a valid password"
        
    verify_error = ''    
    if verify != password:
        verify_error = "Passwords don't match"
        
    email_error = ''
    if len(email) > 0 and  len(email) <= 3 or len(email) >= 20 and email.count("@") != 1 or email.count(".") != 1:
        email_error = "That's not a valid email"

    if username_error or password_error or verify_error or email_error:
        return render_template ('index.html',
            username_error = username_error, password_error = password_error,
            email_error = email_error, verify_error = verify_error)
    else:
        return render_template('welcome.html', username = username)
        
app.run()
       
    