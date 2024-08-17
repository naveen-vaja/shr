from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "om"

@app.route('/siva')
def love():
    return "om namah shivaya"

@app.route('/rama')
def ram():
    a = input("enter you name:")
    b= input("enter your lover name:")
    return a+b


if __name__=='__main__':
    app.run()