# FavoriteMovies
A project about the best that Cinema has to offer (aka my favorite movies of all time!).  
This is a Flask-based application that uses SQLAlchemy, APIs and Bootstrap to build an awesome movie list.

![Home](https://user-images.githubusercontent.com/31540553/163634641-1763bcda-3489-4c86-a652-ac9a27e32685.gif)


## Adding a Movie
A great functionality of this application is the "Add Movie". It fetches the search query into an API and allows the user to select exactly the movie they want.
As soon as a movie is selected, the user inputs a rating and a comment. Then it is displayed on the homepage with the others, according to the highest ratings.
This was all made possible thanks to the awesome TMDB, also known as [The Movie Database](https://www.themoviedb.org/).

![Add](https://user-images.githubusercontent.com/31540553/163640145-7833166e-5f81-4f98-b6d4-9589f6528687.gif)


## Editing a Movie
The same comment and review fields are available to the user if they want to change any of these. 

![Edit](https://user-images.githubusercontent.com/31540553/163639161-208cde4b-ab03-46b8-83b3-ad332ab78139.gif)



## Deleting a Movie
If the user wants to delete a movie, it is easily possible through the simple press of a button on the back of a movie card.

![Delete](https://user-images.githubusercontent.com/31540553/163639258-9bf346db-d964-4686-a7d6-f3f96f19545f.gif)



## Code
Feel free to visit the main.py code and check for comments on execution there! I made an effort to be as thorough as possible with the documentation.
Here's a quick example of what you can expect.

      selected_movie = Movie(
            # Movie structure just like the database requires.
            title=movie['title'],
            year=movie['release_date'].split('-')[0],
            description=movie['overview'],
            rating=movie_rating,
            ranking=0,
            review=movie_review,
            img_url=f"https://image.tmdb.org/t/p/w500{movie['poster_path']}",
        )

      db.session.add(selected_movie)              # Adding the movie to the DB
      db.session.commit()                         # Commiting the changes
      return redirect(url_for("home"))            # Redirecting the user to the homepage.

    # If the page is first loading (GET Method),
    # the form with the rating and review fields will be created.
    return render_template("edit.html", form=form)


## Important
If you have any doubts, please visit the code as it is very well documented. Besides that, feel free to contact me, it will be a pleasure to talk and learn with you! I'm also available for helping in your own projects!
