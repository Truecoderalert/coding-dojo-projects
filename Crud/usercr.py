from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'kgraham'

@app.route('/')
def showusers():
    if 'submitted_form' not in session:
        session['submitted_form'] = []
    return render_template('form.html' , users = session['submitted_form'])


@app.route('/users/new' , methods=['post'])
def index():
    names = []
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['submitted_form'].append(request.form)
    return redirect('/users')


@app.route('/users')
def showuserss():
    return render_template('showinfo.html' , users = session['submitted_form'])

if __name__=='__main__':
    app.run(debug=True)