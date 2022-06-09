from flask import Flask, render_template  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# # The "@" decorator associates this route with the function immediately following
# @app.route('/')
# def hello_world():
#     return 'Hello Worlds!'  # Return the string 'Hello World!' as a response

@app.route('/', defaults={'x':4, 'y':4, 'color1':'red', 'color2':'black'})
@app.route('/<y>', defaults={'x': 4, 'color1':'red', 'color2':'black'})
@app.route('/<x>/<y>', defaults={'color1':'red', 'color2':'black'})
@app.route('/<x>/<y>/<color1>/<color2>')
def cb(x,y,color1,color2):
    print(x)
    print(y)
    print(color1)
    print(color2)
    return render_template('index.html', x=int(x), y=int(y), color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)