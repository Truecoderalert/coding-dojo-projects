from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/<say>/<name>')
def say_flask(say , name):
    print (say)

    return    say +  name 

@app.route('/repeat/<int:num>/<phrase>')
def repeat(num , phrase):
    for x in phrase:
        while num > 0:
            
            phrase = 'hello'
            phrase = 'bye'
            phrase = 'dogs'
            break
        return (phrase * num)




















