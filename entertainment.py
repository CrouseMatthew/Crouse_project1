# Movie Trailer Project
# Crouse, Matthew
# 
# Creates an array of movies that are then passed to fresh_tomatoes.py which generates server-side html
# and produces a working movie trailer page.
# 
# @uses class Movie() defined in media.py

import media
import fresh_tomatoes

# create an instance of Movie called guard_galaxy
guard_galaxy = media.Movie ( 
    "Guardians Of The Galaxy",
    "A group of intergalactic criminals are forced to work together to stop a fanatical warrior "+
        "from taking control of the universe.",
    "http://t2.gstatic.com/images?q=tbn:ANd9GcQW3LbpT94mtUG1PZIIzJNxmFX399wr_NcvoppJ82k7z99Hx6in",
    "www.youtube.com/watch?v=B16Bo47KS2g"
    )

# create an instance of Movie called avatar
avatar = media.Movie (
    "Avatar",
    "A Paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between "+
        "following his orders and protecting the world he feels is his home..",
    "http://ecx.images-amazon.com/images/I/91N1lG%2BLBIS._SL1500_.jpg",
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ"
    )

# create an instance of Movie called school_of_rock
school_of_rock = media.Movie(
    "School of Rock",
    "Overly enthusiastic guitarist Dewey Finn (Jack Black) Poses as a substitute music"+
        " teacher at an elite private elementary school, he exposes his students to the hard "+
        "rock gods he idolizes and emulates.",
    "http://americanvideostore.com/wp-content/uploads/2014/07/School-of-Rock.jpg",
    "http://www.youtube.com/watch?v=XCwy6lW5Ixc"
    )

# create an instance of Movie called shawshank
shawshank = media.Movie(
    "Shawshanke Redemption",
    "Adapted from the Stephen King novella Rita Hayworth and Shawshank Redemption, the film "+
        "tells the story of Andy Dufresne, a banker who is sentenced to life in Shawshank State "+
        "Prison for the murder of his wife and her lover despite his claims of innocence.",
    "http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@"+
        "._V1_SX214_AL_.jpg",
    "https://www.youtube.com/watch?v=NmzuHjWmXOc")

# create an instance of Movie called fith
fith = media.Movie( 
    "The Fifth Element",
    "In the 23rd century, a New York City cabbie, Korben Dallas, finds the fate of the world "+
        "in his hands when Leeloo falls into his cab. As the embodiment of the fifth element, "+
        "Leeloo needs to keep the approaching Great Evil from destroying the world.",
    "http://ia.media-imdb.com/images/M/MV5BMTkzOTkwNTI4N15BMl5BanBnXkFtZTYwMDIzNzI5._V1_"+
    "SY317_CR6,0,214,317_AL_.jpg",
    "www.youtube.com/watch?v=VkX7dHjL-aY"
                    )

# create an instance of Movie called exam
exam = media.Movie( 
    "Exam",
    "The final candidates for a highly desirable corporate job are locked together in an "+
        "exam room and given a test so simple and confusing that tension begins to unravel.",
    "http://ia.media-imdb.com/images/M/MV5BNDg2NzM2NzIwNF5BMl5BanBnXkFtZTcwODE2ODc1Mg@@._V1_"+
        "SY317_CR0,0,214,317_AL_.jpg",
    "www.youtube.com/watch?v=bkdt2Sygew0")

# store an array of movie instances in a variable called movies
movies =[guard_galaxy, avatar, school_of_rock, shawshank, fith, exam]

# pass the array of movies to another file called fresh_tomatoes.
fresh_tomatoes.open_movies_page(movies)
