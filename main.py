# ---------------------------------- IMPORTS ----------------------------------
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

# ---------------------------- FLASK SERVER CONFIG ----------------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# ---------------------------------- DATABASE ---------------------------------

# DB Creation, should only ran once.
# engine = create_engine('sqlite:///movies.db', echo=True)
meta = MetaData()
db = SQLAlchemy(app)

movies = Table(
   'movies', meta,
   Column('id', Integer, primary_key=True),
   Column('title', String),
   Column('year', String),
   Column('description', String),
   Column('rating', String),
   Column('ranking', String),
   Column('img_url', String),
)

# DB Creation, should only run once.
# meta.create_all(engine)

# Creating a new data entry. Run just once!
new_movie = Table(
    'movies', meta,
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)

db.session.add(new_movie)
db.session.commit()


# ---------------------------------- ROUTING ----------------------------------
@app.route("/")
def home():
    return render_template("index.html")

# --------------------------------- EXECUTION ---------------------------------
if __name__ == '__main__':
    app.run(debug=True)
