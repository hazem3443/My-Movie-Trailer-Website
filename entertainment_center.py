import fresh_tomatoes  # import file that pass the movies to the website
import media  # import file that contains class variables & functions

# list of Movies with all it's information that will be
# used to display the data on the website this data include
# the movie name , description , photo URL , youtube trailer URL
toy_story = media.Movie(
    "Toy story",
    "a story of a boy and his toys that comes to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=JcpWXaA2qeg")
avatar = media.Movie(
    "AVATAR",
    "a story of a marine on other planet",
    "https://goo.gl/r81gRv",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")
intersteller = media.Movie(
    "INTERSTELLER",
    "a story of a pilot travel throw space",
    "https://goo.gl/pDVNBG",
    "https://www.youtube.com/watch?v=zSWdZVtXT7E")
hunger_games = media.Movie(
    "Hunger Games",
    "a story of a players play a dangrous game that reflect on thier life",
    "https://goo.gl/VHZQtI",
    "https://www.youtube.com/watch?v=mfmrPu43DF8")
mother = media.Movie(
    "mother",
    "a story of a heaven and hell",
    "https://upload.wikimedia.org/wikipedia/en/9/94/Mother%212017.jpg",
    "https://www.youtube.com/watch?v=XpICoc65uh0")
i_am_a_legend = media.Movie(
    "I am a legend",
    "a story of a man live on his own between zombies",
    "https://goo.gl/7l4m8W",
    "https://www.youtube.com/watch?v=HW8l2Yj1ZK8")
# create a list of all movies in the database of a website
movies = [toy_story, avatar, intersteller, hunger_games, mother, i_am_a_legend]
# calling the opening function that is going to display this data
# in such a style with all of the information we put in the list variables
fresh_tomatoes.open_movies_page(movies)
