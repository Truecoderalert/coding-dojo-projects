from flask import Flask , render_template , request , session , redirect 
app = Flask(__name__)
app.secret_key = 'kgraham'


@app.route('/')
def addone():
    if 'count' in session:
        session['count'] += 1
    else: session['count'] = 0
    return render_template ('counter.html')

@app.route('/addtwo' , methods =['post'])
def addtwo():
    if 'count' in session:
        session['count'] += 1
    return redirect('/')



@app.route('/addone' , methods =['post'])
def showinfo():
    return redirect('/')

@app.route('/reset' , methods =['post'])
def clear():
    session.clear()
    return redirect('/')




if __name__=="__main__":      
    app.run(debug=True) 