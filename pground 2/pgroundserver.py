from flask import Flask , render_template
app = Flask(__name__)



@app.route ('/play')
def play():
    return render_template('pground.html' , num = 3 , color = 'blue')

@app.route ('/play/<int:num>')
def play_times(num):
    return render_template('pground.html' , num=num , color='blue')


@app.route('/play/<int:num>/<string:color>')
def play_times_color(num,color ):
    return render_template('pground.html' , num=num , color=color ) 


    if __name__=="__main__":      
        app.run(debug=True) 





















if __name__=="__main__":    
    app.run(debug=True) 