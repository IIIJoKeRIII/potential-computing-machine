from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newflask.db'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    family = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    old_name = db.Column(db.Text, nullable=False)
    mail = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text, nullable=False)
    txt = db.Column(db.Text, nullable=False)

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/create", methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        family = request.form['family']
        name = request.form['name']
        old_name = request.form['old_name']
        mail = request.form['mail']
        phone = request.form['phone']
        txt = request.form['txt']

        post = Post(family=family, name=name, old_name=old_name, mail=mail, phone=phone, txt=txt)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except:
            return "Произошла ошибка"
    else:
        return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)