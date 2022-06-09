from turtle import color
from flask import Flask, render_template  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# # The "@" decorator associates this route with the function immediately following
# @app.route('/')
# def hello_world():
#     return 'Hello Worlds!'  # Return the string 'Hello World!' as a response

@app.route('/')                           
def hello_world():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html', phrase="hello", times=5)

@app.route('/play', defaults={'num':1, 'color':'lightskyblue'}) 
@app.route('/play/<num>', defaults={'color':'lightskyblue'}) 
@app.route('/play/<num>/<color>')                          
def playbox(num, color):
    print(num)
    print(color)
    return render_template('play.html', num=int(num), color=color)


@app.route('/Dojo!')
def success():
    return "Dojo!"

@app.route('/Hi/<saying>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def say(saying):
    print(saying)
    return "Hi, " + saying +"!"


@app.route('/repeat/<num>/<x>')
def repeat(x,num):
    print(x)
    print(num)
    numx=""
    for i in range(int(num)):
        numx+=x+"\n"
    return numx


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.