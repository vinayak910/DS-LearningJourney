from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")   #------> home route - automatically excecute when hit the server
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/hello_world1")
def hello_world1():
    return "<h1>Hello, World1!</h1>"

@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hello, World2!</h1>"

@app.route("/security")
def security():
    return "YO Kakashi okkkk {}".format(60 + 9)

@app.route("/test")
def test():
    data = request.args.get('m')
    return """ This is my data , hello {}""".format(data)


if __name__=="__main__":
    app.run(host="0.0.0.0")
