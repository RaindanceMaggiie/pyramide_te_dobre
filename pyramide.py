# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from static import board

app = Flask(__name__)

class Plansza:
    def __init__(self):
        self.t = board.p

    def __call__(self):
        return self.t
class Zaznaczenie:
    def __init__(self):
        self.x = ['x','o']
    def __call__(self):
        return self.x
class Gracz1:
    def __init__(self):
        self.pierwszy = gracz.pierwszy

    def __call__(self):
        return self.pierwszy
class Gracz2:
    def __init__(self):
        self.drugi = gracz.drugi

    def __call__(self):
        return self.drugi
class Wygrana:
    def __init__(self):
        self.wygra = [
        'Wygrał Gracz 1', 
        'Wygrał Gracz 2'
        ]

    def __call__(self):
        return self.wygra

@app.route('/', methods=['POST', 'GET'])
def main():
    board.p = [[1],
    [2, 3],
    [4, 5, 6],
    [7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20, 21]]
    punkty.gracz1 = 0
    punkty.gracz2 = 0
    wolne.pola = 21
    wybor.tura = 'gracz1'
    return render_template('main.html')

@app.route("/start", methods=['POST', 'GET'])
def start():
    plansza = Plansza()
    return render_template('plansza.html', plansza=plansza(), tura=wybor.tura)

@app.route('/ruch' , methods=['POST', 'GET'])
def ruch():
    plansza = Plansza()
    gracz1 = Gracz1()
    gracz2 = Gracz2()
    zazn = Zaznaczenie()
    wygrana = Wygrana()
    zmiana = 0
    z = None
    m = None

    if wybor.tura == 'gracz1':
        if request_method == 'POST':
                wolne.pola = wolne.pola - 1
                z = zazn.x[0]
                x = int(request.form['x'])
                y = int(request.form['y'])
                if plansza.t[x][y] == 1:
                    punkty.gracz1 += 1
                elif plansza.t[x][y] == 2 or plansza.t[x][y] == 3:
                    punkty.gracz1 += 2
                elif plansza.t[x][y] >= 4 and plansza.t[x][y] <= 6:
                    punkty.gracz1 += 3
                elif plansza.t[x][y] >= 7 and plansza.t[x][y] <= 10:
                    punkty.gracz1 += 4
                elif plansza.t[x][y] >= 11 and plansza.t[x][y] <= 15:
                    punkty.gracz1 += 5
                else:
                    punkty.gracz1 += 6
                if z == zazn.x[0]: plansza.t[x][y] = zazn.x[0]

    if wybor.tura == 'gracz2':
        if request_method == 'POST':
                wolne.pola = wolne.pola - 1
                z = zazn.x[1]
                x = int(request.form['x'])
                y = int(request.form['y'])
                zmiana = 1
                if plansza.t[x][y] == 1:
                    punkty.gracz2 += 1
                elif plansza.t[x][y] == 2 or plansza.t[x][y] == 3:
                    punkty.gracz2 += 2
                elif plansza.t[x][y] >= 4 and plansza.t[x][y] <= 6:
                    punkty.gracz2 += 3
                elif plansza.t[x][y] >= 7 and plansza.t[x][y] <= 10:
                    punkty.gracz2 += 4
                elif plansza.t[x][y] >= 11 and plansza.t[x][y] <= 15:
                    punkty.gracz2 += 5
                else:
                    punkty.gracz2 += 6
                if z == zazn.x[1]: plansza.t[x][y] = zazn.x[1]

    board.p = plansza()
    gracz.pierwszy = gracz1()
    gracz.drugi = gracz2()

    if zmiana == 1:
        if wybor.tura == 'gracz1':
            wybor.tura = 'gracz2'
        else:
            wybor.tura = 'gracz1'

    if wolne.pola == 0:
        if punkty.gracz1 > punkty.gracz2:
            m = wygrana.wygra[0]
            return render_template('wygrana.html', m=m)
        else:
            m = wygrana.wygra[1]
            return render_template('wygrana.html', m=m)

    return render_template('index.html', plansza=plansza(), m = m, tura=wybor.tura)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000, debug=True)
