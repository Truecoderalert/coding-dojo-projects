from flask import Flask, request, render_template, redirect, session
import random 
app = Flask(__name__)

app.secret_key = 'kyree'




@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    return render_template ('ninjagold.html')
#continue fixing lines 18-25
@app.route('/showinfo' , methods = ['post'])
def showinfo():
    if 'house' == request.form['place'] :
            session['gold'] += random.randint(2,5)
    if 'farm' == request.form['place'] :
            session['gold'] += random.randint(10,20)
    if 'cave' == request.form['place'] :
            session['gold'] += random.randint(5,10)
    if 'casino' == request.form['place'] :
            session['gold'] += random.randint(-25,25)
    print (session['gold'])
    return redirect ('/' )

@app.route('/reset')
def reset():
    session.clear()
    return redirect ('/')


if __name__=='__main__':
    app.run(debug=True)