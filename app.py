# Project 1 - Fibonacci Generator

from flask import Flask, render_template, request

app = Flask(__name__)

def generate_fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        n = int(request.form['number'])
        fibonacci_series = generate_fibonacci(n)
        return render_template('index.html', fibonacci_series=fibonacci_series, n=n)
    return render_template('index.html', fibonacci_series=[], n=0)

if __name__ == '__main__':
    app.run(debug=True)
