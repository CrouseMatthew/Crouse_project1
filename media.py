import webbrowser

# Creates a movie with a title, storyline, poster image, and trailer link. 
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # public method of Movie() that opens the web-browser to the link stored in 
    # trailer_youtube_url 
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
