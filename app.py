from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, Hero

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

@app.route('/')
def index():
    heroes = Hero.query.all()
    return render_template('index.html', heroes=heroes)

@app.route('/add_hero', methods=['GET', 'POST'])
def add_hero():
    if request.method == 'POST':
        name = request.form.get('name')
        role = request.form.get('role')
        win_rate = request.form.get('win_rate')
        
        if name and role and win_rate:
            new_hero = Hero(name=name, role=role, win_rate=float(win_rate))
            db.session.add(new_hero)
            db.session.commit()
            return redirect(url_for('index'))
    
    return render_template('add_hero.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
