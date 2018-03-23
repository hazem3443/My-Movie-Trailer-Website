import webbrowser  # this import the webbrowser package from the main packages


class Movie(object):
    """Movie class for the data we are going to pass and
    all of it's operations whick is openeing the url"""

    # constructor
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):

        # instance variables
        self.title = movie_title  # movie name
        self.storyline = movie_storyline  # movie description
        self.poster_image_url = poster_image  # movie poster
        self.trailer_youtube_url = trailer_youtube  # youtube trailer link

    # functions going to be performes on that class
    # show the trailer of the movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
