from flask import Flask, render_template, url_for, session, redirect, flash

from flask_bootstrap import Bootstrap

from flask_moment import Moment

from datetime import datetime

from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired

from flask_sqlalchemy import SQLAlchemy
import os


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    date = DateField("date is ", validators=[DataRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ozbb:qwer1234@localhost:3307/ozbb?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


class A():
    def print(self):
        return "hahahha"


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/404')
def error():
    print(url_for('error', _external=True))
    return render_template('404.html'), 404


if __name__ == "__main__":
    print("?")
    db.drop_all()
    db.create_all()
    u = User(username="hanmeimei2222")
    u2 = User(username="lilei222")
    db.session.add(u)
    db.session.add(u2)
    db.session.commit()
    print(User.query.all())
