# Movie-Trailer Website :star:
it is a **Server side** code that interact with the data base that is been collected and show it in such a manner
## How you run this code ?:point_down:
first you need to open and run **entertainment_center.py** that will open the default web browser with this page loaded
and you can run it directly by openeing **fresh_tomatoes.html** with any web browser you like such as ***_Chrome_*** :running:

## the files contained :cyclone:
### entertainment_center.py 
which contains the movies with all of the information that the code will use to show the movies
and containig ***List*** of movies and initialize the 
'''fresh_tomatoes.open_movies_page(movies)''' 
that will show the database on the webpage

### media.py
this file contain the class that will construct the variables that will be used as input data to the webpage,
first it containes the _**constructor**_ 
'''class Movie(object):"""Movie class for the data we are going to pass and
    all of it's operations whick is openeing the url"""

    # constructor
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):

        # instance variables
        self.title = movie_title  # movie name
        self.storyline = movie_storyline  # movie description
        self.poster_image_url = poster_image  # movie poster
        self.trailer_youtube_url = trailer_youtube  # youtube trailer link
'''
the it call a function from **webbrowser** python package to open the URL using the default browser

###fresh_tomatoes.py
this file contain the code that blug the server side code to the .html file in the same directory 

## Follow me on **Facebook** :gift_heart:
[here](https://www.facebook.com/hazem.khaled.3386585)
