from flask import Flask  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello Worlds!'  # Return the string 'Hello World!' as a response

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
