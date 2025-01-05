from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('test.html')

@app.route('/test_2')
def small_change():
    return render_template('test-2.html')

@app.route('/number/<int:num>')
def number(num):
    return f'What is your number? Mine is {num}'

if __name__ == '__main__':
    # app.run(debug=True, port=3000)
    app.run(host='0.0.0.0', port=80)