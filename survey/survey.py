from flask import Flask , render_template , request , session , redirect
app = Flask(__name__)
app.secret_key = 'kgraham'


@app.route('/')
def askforinfo():
    return render_template('survey.html')


@app.route('/result' , methods =['post'])
def collectinfoentered():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['notes'] = request.form['notes']
    return redirect('/showresult')



@app.route('/showresult' )
def showinfoentered():
    return render_template('results.html' , first_name = session['first_name'], last_name = session['last_name'] , notes = session['notes'])









if __name__=="__main__":      
    app.run(debug=True) 