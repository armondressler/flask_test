from application import app
from flask import redirect,request,url_for,render_template

user = {"username": "hund"}
navigation_bar = ["hase","huhn"]

@app.route('/')
def view_root():
    return redirect('/login')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        print(request.form['username'], request.form['password'])
    return render_template('greeting.html',title="Fubartitel",user=user,navigation_bar=navigation_bar)
#    return redirect(url_for('static',filename='somepage.html'))
