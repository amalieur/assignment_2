from math import sin

#@app.route('/numericalintegralservice/<lower>/<upper>')
def integral(lower, upper):
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
        #print(results)
        return results

