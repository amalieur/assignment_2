from numpy import sin
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulations, it's a web app!"


@app.route('/numericalintegralservice/<lower>/<upper>')
def numerical_integration(lower, upper):
    n = [10, 100, 100, 1000, 10000, 100000, 1000000]

    for i in n:
        dx = (float(upper) - float(lower)) / i
        integral = 0.0
        results = {}
        for p in range(i):
            xp = dx * (p + 0.5)
            dI = abs(sin(xp)) * dx
            integral += dI
            results[p] = integral
        print(results)
        return results


if __name__ == '__main__':
    numerical_integration(0, 3.14159)
    app.run(host="127.0.0.1", port=5000, debug=True)
