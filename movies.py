import webbrowser

#Creates a class Movie with 4 arguments, including self to invoke a variable.
class Movie():
    movieRatings = ["G","PG","PG-13","R"]
    def __init__(self, movieTitle, movieStoryline, posterImage, trailerYouTube):
        self.title = movieTitle
        self.storyline = movieStoryline
        self.poster_image_url = posterImage
        self.trailer_youtube_url = trailerYouTube

    #Shows trailer on YouTube
    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)