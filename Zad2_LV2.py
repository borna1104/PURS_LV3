from flask import Flask, request, redirect, url_for, render_template

app = Flask("Prva flask aplikacija")

temperature_lista = []

@app.get('/')
def index():
    return render_template('index.html'), 200

@app.get('/login')
def login_str():
    return render_template('login.html'), 200

@app.get('/logout')
def logout():
    return redirect(url_for('login_str'))

@app.post('/login') 
def login(): 
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'PURS' and password == '1234':
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login_str'))

@app.post('/temperatura')
def add_temperatura():
    temp = request.json.get('temperatura')
    if temp is None:
        return 'nije upisana temperatura.',404
    
    temperature_lista.append(temp)
    return 'temperatura dodana',201

@app.get('/temperatura')
def temperatura_str():
    if len(temperature_lista) == 0: 
        return 'nema temperatura',404

    return {'temperatura' : temperature_lista[-1]}

@app.delete('/temperatura')
def obrisi_temp():
    id = request.args.get('id', type=int)
    if id is None or id < 0 or id >=len(temperature_lista):
        return 'neispravan kljuc',404
    
    temperature_lista.pop(id)
    return 'Temperatura obrisana',202

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)