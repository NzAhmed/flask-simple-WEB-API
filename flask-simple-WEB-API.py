"""
1- install python, pip
2- pip install flask
"""

from flask import Flask
app = Flask(__name__)

@app.route('/api/simple/')
def hello():
    return "Hello World!"

@app.route('/api/simple/<name>')
def hello_name(name):
    return "Hello {}" . format(name)

if __name__ == '__main__':
    app.run()

"""
run the app:
>python flask-simple-WEB-API.py
"""