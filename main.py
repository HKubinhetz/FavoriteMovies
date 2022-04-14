# ---------------------------------- IMPORTS ----------------------------------
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import tmdbAPI


# ---------------------------- FLASK SERVER CONFIG ----------------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


# ---------------------------------- DATABASE ---------------------------------
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(500), unique=True, nullable=False)
    img_url = db.Column(db.String(500), unique=True, nullable=False)

# DB Creation, should only ran once.
# db.create_all()


# --------------------------------- CONSTANTS ---------------------------------
global tmdb_movielist


# --------------------------------- FUNCTIONS ---------------------------------
def query_movies():
    # This function finds all movies in the Database, if any, and returns them.
    all_movies = []
    movies = db.session.query(Movie).order_by("rating").all()
    for movie in movies:
        movies_info = {
            "id": movie.id,
            "title": movie.title,
            "year": movie.year,
            "description": movie.description,
            "rating": movie.rating,
            "ranking": movie.ranking,
            "review": movie.review,
            "img_url": movie.img_url,
        }
        all_movies.append(movies_info)
        print(all_movies)
    return all_movies


# ----------------------------------- FORMS -----------------------------------
class ReviewMovieForm(FlaskForm):
    rating = StringField('Your rating', validators=[DataRequired()])
    review = StringField('Your movie review', validators=[DataRequired()])
    submit = SubmitField('Done!')


class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Search!')


# ---------------------------------- ROUTING ----------------------------------
@app.route("/", methods=['GET', 'POST'])
def home():
    moviedata = query_movies()
    return render_template("index.html", movies=moviedata)


@app.route("/add", methods=['GET', 'POST'])
def add():
    global tmdb_movielist
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        tmdb_movielist = tmdbAPI.search_movie(movie_title)
        return render_template("select.html", movies=tmdb_movielist)
    return render_template("add.html", form=form)


@app.route("/edit/<movieid>", methods=['GET', 'POST'])
def edit(movieid):
    form = ReviewMovieForm()
    moviedata = query_movies()
    if form.validate_on_submit():
        movie_rating = form.rating.data
        movie_review = form.review.data
        movie_to_update = Movie.query.filter_by(id=movieid).first()           # Finds the movie in the DB
        movie_to_update.rating = movie_rating                                 # Updates the rating
        movie_to_update.review = movie_review                                 # Updates the review
        db.session.commit()                                                   # Commits the update
        return redirect(url_for('home'))                                      # Redirects the user to home
    return render_template("edit.html", movies=moviedata, id=movieid, form=form)


@app.route("/selected/<movieid>", methods=['GET', 'POST'])
def selected(movieid):

    form = ReviewMovieForm()
    if form.validate_on_submit():
        global tmdb_movielist
        movie = tmdb_movielist[int(movieid)]
        movie_rating = form.rating.data
        movie_review = form.review.data

        selected_movie = Movie(
            title=movie['title'],
            year=movie['release_date'].split('-')[0],
            description=movie['overview'],
            rating=movie_rating,
            ranking=0,
            review=movie_review,
            img_url=f"https://image.tmdb.org/t/p/w500{movie['poster_path']}",
        )

        db.session.add(selected_movie)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", form=form)
    # return render_template("edit.html", movies=moviedata, id=movieid, form=form)


@app.route("/delete/<movieid>")
def delete(movieid):
    movie_to_delete = Movie.query.filter_by(id=movieid).first()  # Finds the movie in the DB
    db.session.delete(movie_to_delete)                           # Deletes the movie
    db.session.commit()                                          # Commits the update
    return redirect(url_for('home'))


# --------------------------------- EXECUTION ---------------------------------
if __name__ == '__main__':
    app.run(debug=True)
