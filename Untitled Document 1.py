from flask import Flask, render_template, request
import math
import random
from static import board
from static import wilk
from static import owce
from static import wybor

app = Flask(__name__)

class Plansza:
    def __init__(self):
        self.t = board.p

    def __call__(self):
        return self.t
class Wilk:
    def __init__(self):
        self.poz = wilk.wolf
    def __call__(self):
        return self.poz
class Error:
    def __init__(self):
        self.messages = [
        'Tylko jedno granatowe pole w przód lub w tył !',
        'To pole jest zajęte !',
        'Tylko jedno !',
        'Wygrałeś !',
        'Przegrałeś !',
        'Wygrał Gracz 1',
        'Nie możesz się cofać !',
        'Wygrał Gracz 2'
        ]
    def __call__(self):
        return self.messages
class Owca1:
    def __init__(self):
        self.poz = owce.owca1
    def __call__(self):
        return self.poz
class Owca2:
    def __init__(self):
        self.poz = owce.owca2
    def __call__(self):
        return self.poz
class Owca3:
    def __init__(self):
        self.poz = owce.owca3
    def __call__(self):
        return self.poz
class Gracz:
    def __init__(self):
        self.gracz = wybor.postac
    def __call__(self):
        return self.gracz

@app.route('/', methods=['POST', 'GET'])
def main():
     board.p = [[6, 1, 6, 1, 6, 1, 6, 1],
     [0, 6, 0, 6, 0, 6, 0, 6],
     [6, 0, 6, 0, 6, 0, 6, 0],
     [0, 6, 0, 6, 0, 6, 0, 6],
     [6, 0, 6, 0, 6, 0, 6, 0],
     [0, 6, 0, 6, 0, 6, 0, 6],
     [6, 0, 6, 0, 6, 0, 6, 0],
     [2, 6, 0, 6, 0, 6, 0, 6]]
     wilk.wolf = [7,0]
     owce.owca1 = [0,1]
     owce.owca2 = [0,3]
     owce.owca3 = [0,5]
     owce.owca4 = [0,7]
     wybor.tura = 'wilk'
     wybor.licznik = 0
     return render_template('start.html')
@app.route("/start", methods=['POST', 'GET'])
def start():
    if request.method == 'POST':
         wybor.postac = str(request.form['gracz'])
    plansza = Plansza()
    return render_template('index.html', plansza=plansza(), wybor = wybor.postac,
    tura= wybor.tura, biala=owce.owca1, czerwona=owce.owca2, niebieska=owce.owca3, czarna=owce.owca4
    )
@app.route('/ruch' , methods=['POST', 'GET'])
def ruch():
    plansza = Plansza()
    wilk = Wilk()
    error = Error()
    owca1 = Owca1()
    owca2 = Owca2()
    owca3 = Owca3()
    owca4 = Owca4()
    owieczki = [owca1,owca2,owca3,owca4]
    m = None
    c = None
    d = None
    zmiana = 0
   '''
    Wersja dla 2 graczy
    '''
    if wybor.postac == 'Dwoch':
        '''
        Tura wilka
        '''
        if wybor.tura == 'wilk':
            if request.method == 'POST':
                x = int(request.form['x'])
                y = int(request.form['y'])
                if plansza.t[x][y] == 6:
                    m = error.messages[0]
                elif plansza.t[x][y] == 1:
                    m = error.messages[1]
                elif x == 0:
                    m = error.messages[5]
                    return render_template('winner.html', m=m)
                elif math.fabs(wilk.poz[0] - x) != 1:
                    m = error.messages[2]
                else:
                    '''
                    Ruch wilka
                    '''
                    plansza.t[wilk.poz[0]][wilk.poz[1]] = 0
                    plansza.t[x][y] = 2
                    wilk.poz[0] = x
                    wilk.poz[1] = y
                    zmiana = 1
                    licznik = 0
                    for p in owieczki:
                        if p.poz[0] >= wilk.poz[0] :
                             licznik += 1
                    if licznik == 4:
                        m = error.messages[5]
                        return render_template('beaten.html', m=m)
       if wybor.tura == 'owca':
            '''
            Tura owiec
            '''
            if request.method == 'POST':
                owca_ktora = int(request.form['owca'])
                x = int(request.form['x'])
                y = int(request.form['y'])
                n = owieczki[owca_ktora]
                if plansza.t[x][y] == 6:
                    m = error.messages[0]
                elif plansza.t[x][y] == 1 or plansza.t[x][y] == 2:
                    m = error.messages[1]
                elif (n.poz[0] - x) != -1:
                    m = error.messages[2]
                else:
                    plansza.t[n.poz[0]][n.poz[1]] = 0
                    plansza.t[x][y] = 1
                    n.poz[0] = x
                    n.poz[1] = y
                    zmiana = 1
                    if wilk.poz[0]%2 != 0:
                        if wilk.poz[0] == 7:
                            if wilk.poz[1] == 0:
                                if plansza.t[6][1] != 0:
                                    m = error.messages[7]
                                    return render_template('beaten.html', m=m)
                            else:
                                if (plansza.t[wilk.poz[0]-1][wilk.poz[1]-1] != 0) and (plansza.t[wilk.poz[0]-1][wilk.poz[1]+1] != 0):
                                    m = error.messages[7]
                                    return render_template('beaten.html', m=m)
                        elif wilk.poz[1] == 0:
                            if (plansza.t[wilk.poz[0]-1][1]) and plansza.t[wilk.poz[0]+1][1] != 0:
                                 m = error.messages[7]
                                 return render_template('beaten.html', m=m)
 else:
                            if (plansza.t[wilk.poz[0]-1][wilk.poz[1]-1] != 0) and (plansza.t[wilk.poz[0]-1][wilk.poz[1]+1] != 0) and (plansza.t[wilk.poz[0]+1][wilk.poz[1]-1] != 0) and (plansza.t[wilk.poz[0]+1][wilk.poz[1]+1] != 0) :
                                m = error.messages[7]
                                return render_template('beaten.html', m=m)
                    else:
                        if wilk.poz[1] == 7:
                            if (plansza.t[wilk.poz[0]-1][6] != 0) and  (plansza.t[wilk.poz[0]+1][6] != 0):
                                m = error.messages[7]
                                return render_template('beaten.html', m=m)
                        else:
                            if (plansza.t[wilk.poz[0]-1][wilk.poz[1]-1] != 0) and (plansza.t[wilk.poz[0]-1][wilk.poz[1]+1] != 0) and (plansza.t[wilk.poz[0]+1][wilk.poz[1]-1] != 0) and (plansza.t[wilk.poz[0]+1][wilk.poz[1]+1] != 0) :
                                m = error.messages[7]
                                return render_template('beaten.html', m=m)
    board.p = plansza()
    wilk.wolf = wilk()
    owce.owca1 = owca1()
    owce.owca2 = owca2()
    owce.owca3 = owca3()
    owce.owca4 = owca4()
    if zmiana == 1:
        if wybor.tura == 'wilk':
            wybor.tura = 'owca'
        else:
            wybor.tura = 'wilk'
    return render_template('index.html', plansza=plansza(), m = m, wilk=wilk(),
    owca1 = owca1(), owca2 = owca2(), owca3 = owca3(), owca4 = owca4(), wybor = wybor.postac, tura=wybor.tura,
    biala=owce.owca1, czerwona=owce.owca2, niebieska=owce.owca3, czarna=owce.owca4)



if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5030,debug=True)
                                                                        





board.py:
p =[[6, 1, 6, 1, 6, 1, 6, 1],
[0, 6, 0, 6, 0, 6, 0, 6],
[6, 0, 6, 0, 6, 0, 6, 0],
[0, 6, 0, 6, 0, 6, 0, 6],
[6, 0, 6, 0, 6, 0, 6, 0],
[0, 6, 0, 6, 0, 6, 0, 6],
[6, 0, 6, 0, 6, 0, 6, 0],
[2, 6, 0, 6, 0, 6, 0, 6]]
                                                                        
wybor.py:
postac = ''
tura = 'wilk'
licznik = 0


index.html:
{% extends "main.html" %}
{% block body %}
<div id="board">
  <form action="/">
    <input type="submit" value="Nowa gra">
  </form>
  <table class="board">
    {% for row in range(8) %}
      <tr>
        {% for i in range(8) %}
          <td>
            {% if (plansza[row][i] == 1) and (row == biala[0]) and (i == biala[1])%}
            <img class="char" src="{{ url_for('static', filename='owca.png') }}">
            {% elif (plansza[row][i] == 1) and (row == czerwona[0]) and (i == czerwona[1])%}
            <img class="char" src="{{ url_for('static', filename='owca_czerwona.png') }}">
            {% elif (plansza[row][i] == 1) and (row == niebieska[0]) and (i == niebieska[1])%}
            <img class="char" src="{{ url_for('static', filename='owca_niebieska.png') }}">
            {% elif (plansza[row][i] == 1) and (row == czarna[0]) and (i == czarna[1])%}
            <img class="char" src="{{ url_for('static', filename='owca_czarna.png') }}">
            {% elif plansza[row][i] == 2 %}
              <img class="char" src="{{ url_for('static', filename='wilk.png') }}">
            {% else %}
              <span id = "pola">{{row}},{{i}}</span>
            {% endif %}
              </form>
          </td>
        {% endfor %}
      </tr>
    {% endfor %}
  </table>
  </div>
  <div id="wspolrzedne">
        {% if m %}
          <p id="alert">{{m}}</p>
        {% endif %}
        {% if wybor == 'Wilk' %}
        <form action="/ruch" method="post">
          <input type="text" id="x" name="x" pattern=[0-7]{1} required>
          <input type="text" id="y" name="y" pattern=[0-7]{1} required>
          <input type="submit" value="Ruch">
        </form>
        {% endif %}
        {% if wybor== 'Owce' %}
        <form action="/ruch" method="post">
          <input type="radio" name="owca" value="0" id="1" checked> Biała
          <input type="radio" name="owca" value="1" id="1"> Czerwona
          <input type="radio" name="owca" value="2" id="1"> Niebieska
          <input type="radio" name="owca" value="3" id="1"> Czarna <br>
          <input type="text" id="x" name="x" pattern=[0-7]{1} required>
          <input type="text" id="y" name="y" pattern=[0-7]{1} required>
          <input type="submit" value="Ruch">
        </form>
        {% endif %}
          {% if wybor== 'Dwoch' %}
          {% if tura == 'wilk' %}
          <p> Gracz 1 - Wilk</p>
          <form action="/ruch" method="post">
            <input type="text" id="x" name="x" pattern=[0-7]{1} required>
            <input type="text" id="y" name="y" pattern=[0-7]{1} required>
            <input type="submit" value="Ruch">
          </form>
          {% endif %}
          {% if tura =='owca' %}
            <p> Gracz 2 - Owce</p>
            <form action="/ruch" method="post">
              <input type="radio" name="owca" value="0" id="1" checked> Biała
              <input type="radio" name="owca" value="1" id="1"> Czerwona
              <input type="radio" name="owca" value="2" id="1"> Niebieska
              <input type="radio" name="owca" value="3" id="1"> Czarna <br>
              <input type="text" id="x" name="x" pattern=[0-7]{1} required>
              <input type="text" id="y" name="y" pattern=[0-7]{1} required>
              <input type="submit" value="Ruch">
            </form>
            {% endif %}
          {% endif %}
  </div>
{% endblock %}



MAIN:
<!DOCTYPE html>
  <html>
    <head>
      <link href='http://fonts.googleapis.com/css?family=Fauna+One&subset=latin,latin-ext'
      rel='stylesheet' type='text/css'>
            <link rel='stylesheet' type='text/css' href="{{ url_for('static', filename='style.css') }}">
      <link rel='shortcut icon' type='image/vnd.microsoft.icon' href="{{ url_for('static', filename='wilk.png.ico') }}" />
      <title>
        Wilk i owce
      </title>
    </head>
    <body>
      <div id="up-bar">
        <p id="title"> Wilk i owce <br>
      </div>
      {% block body %}{% endblock %}
    </body>
  </html>

START:
{% extends "main.html" %}
{% block body %}
<div id="wspolrzedne">
        <form action="/start" method="post">
                <p> Wybierz tryb gry: </p>
                <input type="radio" name="gracz" value="Wilk" id="2" checked> Wilk
                <input type="radio" name="gracz" value="Owce" id="1"> Owce
                <input type="radio" name="gracz" value="Dwoch" id="1"> Dwóch graczy <br><br>
                <input type="submit" value="start">
        </form>
</div>
{% endblock %}


WINNER:
{% extends "main.html" %}
{% block body %}
<div id="wspolrzedne">
  {% if m %}
    <p id="alert">{{m}}</p>
  {% endif %}
  <form action="/">
    <input type="submit" value="Nowa gra">
  </form>
</div>
{% endblock %}

css

body {
  margin: 0px;
  font-family: 'Fauna One', sans-serif;
}

#up-bar {
  width: auto; height: 100px;
  background-color: #CFBE8F;
  padding: 5px;
  font-weight: bold;
  font-size: 20px;
  color: #322E30;
  text-align: center;

}

#title {
  font-size: 40px;
  margin:20px;
}

table.board {
  margin: 0 auto; text-align: left; background-color: #636C8F;
  border: 5px solid #2F2742;
  border-collapse: collapse;
  border-cellpadding: 0px;
}
table.board td {
    cursor: pointer;
    font-size: 2em;
    width: 50px;
    height: 50px;
    border: 3px solid #2F2742;
    text-align: center;
}

table.board tr:nth-child(2n) td:nth-child(2n),
table.board tr:nth-child(2n+1) td:nth-child(2n+1) {
    background-color: #CBC4DB;
}

#board {
margin: 20px;
}

.char {
width: 50px; height: 40px;
margin: 0px;
}

#wspolrzedne{
  text-align: center; height: 100px; width: 100%;
}

#alert {
  color: red; font-weight: bold;
}

#pola {
  font-size: 10px;
}
