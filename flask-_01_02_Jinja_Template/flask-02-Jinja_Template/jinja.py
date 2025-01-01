from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def head():
     return render_template('index.html', number1=27, number2=15)

@app.route('/mult')
def number():
     x=85
     y=99
     return render_template('body.html', value1=x, value2=y, mult=x*y)

if __name__== "__main__":
     # app.run(debug=True, port=3000)
     app.run(host= '0.0.0.0', port=80)