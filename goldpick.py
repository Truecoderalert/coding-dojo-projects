
from flask import Flask ,  render_template,redirect,session,request
app = Flask(__name__)  
result = ''
app.secret_key = 'playingnow'
import random

@app.route('/')       
def choose_location():
    if 'gold' not in session:
        session['gold'] = 0
    if session.get("places") != None:

        return render_template ('goldpick.index.html'  ) 




@app.route('/process_money', methods=['POST'] )
def process_money():
    import random
    #read the location 
    location = request.form['building']
    #catorgorize the place with the point amount
    Low_Num = int(request.form['low'])
    High_num = int(request.form['high'])
    random_num = random.randint(Low_Num,High_num)
    session ['gold'] += random_num
    return redirect ('/')
    # print (farm_points)
    

        #randomize the returned number
        #identify if casino was used
        #add or subtract to total
        #hold it in session
        #hold message in session






if __name__=='__main__':
app.run(debug=True, host="localhost", port=3000)