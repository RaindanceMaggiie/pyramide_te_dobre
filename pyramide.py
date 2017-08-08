#flask/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
import board

app = Flask(__name__)

class Plansza:
    def __init__(self):
        self.tablica = board.p
        self.skreslenia = board.r
        self.slownik = board.s

    def skresl(self, skreslenie, gracz):
        w = self.slownik[skreslenie]
        if  self.skreslenia[w[0]][w[1]] == -1:
            self.skreslenia[w[0]][w[1]] = gracz
            return gracz
        else:
            return -2

    def czyje(self):
        slownik = {}
        i=1
        for wiersz in self.skreslenia:
            for kolumna in wiersz:
                slownik[i] = kolumna
                i+=1
        return slownik

    def nowa(self):
        from importlib import reload
        reload(board)
        self.tablica = board.p
        self.skreslenia = board.r
        self.slownik = board.s

    def __call__(self):
        return self.tablica

class Wiadomosc:
    def __init__(self):
        self.wypisz =[
        'Nie oszukuj!',
        'Koniec gry! wygrał gracz 1',
        'Koniec gry! wygrał gracz 2'
        ]

    def __call__(self):
        return self.wypisz

class Gracz:
    def __init__(self):
        self.punkty = 0

    def __dodaj__(self, punkty):
        self.punkty += punkty

    def __call__(self):
        return self.punkty

@app.route('/', methods=['POST', 'GET'])
def main():
    return render_template('index.html')

@app.route("/start", methods=['POST', 'GET'])
def start():
    global gracze, tura, plansza
    plansza = Plansza()
    plansza.nowa()
    gracze = list()
    gracze.append( Gracz() )
    gracze.append( Gracz() )
    tura = 0
    return render_template('plansza.html', plansza=plansza(), skreslenia=plansza.czyje(), tura=tura, g0=0, g1=0)

@app.route('/ruch/<int:skreslenie>' , methods=['POST', 'GET'])
def ruch(skreslenie):
    global gracze, tura, plansza
    wiadomosc = Wiadomosc()
    m = None 
    p0 = 0
    p1 = 0
    print(plansza.skreslenia)
    """
    warunki czy można skreślić dane pole
    """
    #plansza.skresl(skreslenie, tura)
    if plansza.skresl(skreslenie, tura) not in (0,1):
        m = wiadomosc.wypisz[0]
        return render_template('oszukista.html', m =m)
    print(plansza.skreslenia)
    """
    warunek stopu gry + zmiana templatki
    """
    znalezione = 0
    for w in plansza.skreslenia:
        for k in w:
            if(k == -1):
                znalezione = 1
    if znalezione == 0:
        """
        liczenie punktów graczy
        """

        #punkty gracza 0

        if plansza.skreslenia[0][0] == 0:
            p0 += 1
        if plansza.skreslenia[0][0] == 0 and plansza.skreslenia[1][0] == 0 and plansza.skreslenia[2][0] == 0 and plansza.skreslenia[3][0] == 0 and plansza.skreslenia[4][0] == 0 and plansza.skreslenia[5][0] == 0:
            p0 += 41
        if plansza.skreslenia[1][1] == 0 and plansza.skreslenia[2][1] == 0 and plansza.skreslenia[3][1] == 0 and plansza.skreslenia[4][1] == 0 and plansza.skreslenia[5][1] == 0:
            p0 += 45
        if plansza.skreslenia[2][2] == 0 and plansza.skreslenia[3][2] == 0 and plansza.skreslenia[4][2] == 0 and plansza.skreslenia[5][2] == 0:
            p0 += 46
        if plansza.skreslenia[3][3] ==0 and plansza.skreslenia[4][3] == 0 and plansza.skreslenia[5][3] == 0:
            p0 += 43
        if plansza.skreslenia[4][4] == 0 and plansza.skreslenia[5][4] == 0:
            p0 += 35
        if plansza.skreslenia[5][5] == 0:
            p0 += 21

        if plansza.skreslenia[0][0] == 0 and plansza.skreslenia[1][1] == 0 and plansza.skreslenia[2][2] == 0 and plansza.skreslenia[3][3] == 0 and plansza.skreslenia[4][4] == 0 and plansza.skreslenia[5][5] == 0:
            p0 += 56
        if plansza.skreslenia[1][0] == 0 and plansza.skreslenia[2][1] == 0 and plansza.skreslenia[3][2] == 0 and plansza.skreslenia[4][3] == 0 and plansza.skreslenia[5][4] == 0:
            p0 += 50
        if plansza.skreslenia[2][0] == 0 and plansza.skreslenia[3][1] == 0 and plansza.skreslenia[4][2] == 0 and plansza.skreslenia[5][3] ==0:
            p0 += 44
        if plansza.skreslenia[3][0] == 0 and plansza.skreslenia[4][1] ==0 and plansza.skreslenia[5][2] == 0:
            p0 += 37
        if plansza.skreslenia[4][0] == 0 and plansza.skreslenia[5][1] == 0:
            p0 += 28
        if plansza.skreslenia[5][0] == 0:
            p0 += 16

        if plansza.skreslenia[1][0] ==0 and plansza.skreslenia[1][1] == 0:
            p0 += 5
        if plansza.skreslenia[2][0] == 0 and plansza.skreslenia[2][1] == 0 and plansza.skreslenia[2][2] == 0:
            p0 += 15
        if plansza.skreslenia[3][0] == 0 and plansza.skreslenia[3][1] == 0 and plansza.skreslenia[3][2] == 0 and plansza.skreslenia[3][3] ==0:
            p0 += 34
        if plansza.skreslenia[4][0] == 0 and plansza.skreslenia[4][1] == 0 and plansza.skreslenia[4][2] == 0 and plansza.skreslenia[4][3] == 0 and plansza.skreslenia[4][4] == 0:
            p0 += 65
        if plansza.skreslenia[5][0] == 0 and plansza.skreslenia[5][1] == 0 and plansza.skreslenia[5][2] == 0 and plansza.skreslenia[5][3] == 0 and plansza.skreslenia[5][4] == 9 and plansza.skreslenia[5][5] == 0:
            p0 += 111

        #pukty gracza1 

        if plansza.skreslenia[0][0] == 1:
            p1 += 1
        if plansza.skreslenia[0][0] == 1 and plansza.skreslenia[1][0] == 1 and plansza.skreslenia[2][0] == 1 and plansza.skreslenia[3][0] == 1 and plansza.skreslenia[4][0] == 1 and plansza.skreslenia[5][0] == 1:
            p1 += 41
        if plansza.skreslenia[1][1] == 1 and plansza.skreslenia[2][1] == 1 and plansza.skreslenia[3][1] == 1 and plansza.skreslenia[4][1] == 1 and plansza.skreslenia[5][1] == 1:
            p1 += 45
        if plansza.skreslenia[2][2] == 1 and plansza.skreslenia[3][2] == 1 and plansza.skreslenia[4][2] == 1 and plansza.skreslenia[5][2] == 1:
            p1 += 46
        if plansza.skreslenia[3][3] == 1 and plansza.skreslenia[4][3] == 1 and plansza.skreslenia[5][3] == 1:
            p1 += 43
        if plansza.skreslenia[4][4] == 1 and plansza.skreslenia[5][4] == 1:
            p1 += 35
        if plansza.skreslenia[5][5] == 1:
            p1 += 21

        if plansza.skreslenia[0][0] == 1 and plansza.skreslenia[1][1] == 1 and plansza.skreslenia[2][2] == 1 and plansza.skreslenia[3][3] == 1 and plansza.skreslenia[4][4] == 1 and plansza.skreslenia[5][5] == 1:
            p1 += 56
        if plansza.skreslenia[1][0] == 1 and plansza.skreslenia[2][1] == 1 and plansza.skreslenia[3][2] == 1 and plansza.skreslenia[4][3] == 1 and plansza.skreslenia[5][4] == 1:
            p1 += 50
        if plansza.skreslenia[2][0] == 1 and plansza.skreslenia[3][1] == 1 and plansza.skreslenia[4][2] == 1 and plansza.skreslenia[5][3] == 1:
            p1 += 44
        if plansza.skreslenia[3][0] == 1 and plansza.skreslenia[4][1] == 1 and plansza.skreslenia[5][2] == 1:
            p1 += 37
        if plansza.skreslenia[4][0] == 1 and plansza.skreslenia[5][1] == 1:
            p1 += 28
        if plansza.skreslenia[5][0] == 1:
            p1 += 16

        if plansza.skreslenia[1][0] == 1 and plansza.skreslenia[1][1] == 1:
            p1 += 5
        if plansza.skreslenia[2][0] == 1 and plansza.skreslenia[2][1] == 1 and plansza.skreslenia[2][2] == 1:
            p1 += 15
        if plansza.skreslenia[3][0] == 1 and plansza.skreslenia[3][1] == 1 and plansza.skreslenia[3][2] == 1 and plansza.skreslenia[3][3] == 1:
            p1 += 34
        if plansza.skreslenia[4][0] == 1 and plansza.skreslenia[4][1] == 1 and plansza.skreslenia[4][2] == 1 and plansza.skreslenia[4][3] == 1 and plansza.skreslenia[4][4] == 1:
            p1 += 65
        if plansza.skreslenia[5][0] == 1 and plansza.skreslenia[5][1] == 1 and plansza.skreslenia[5][2] == 1 and plansza.skreslenia[5][3] == 1 and plansza.skreslenia[5][4] == 1 and plansza.skreslenia[5][5] == 1:
            p1 += 111

        #warunki wygranej

        if p0 > p1:
            m = wiadomosc.wypisz[1] 
        else:
            m = wiadomosc.wypisz[2]
        return render_template('plansza.html', plansza=plansza(),skreslenia=plansza.czyje(),tura =tura, m=m, g0=p0, g1=p1) 
    
    if tura == 0:
        tura = 1
    else:
        tura = 0
    return render_template('plansza.html', plansza=plansza(), skreslenia=plansza.czyje(), tura=tura, g0=p0, g1=p1, m=m)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=8000, debug=True)
