import movies
import freshtomatoes

#Initialize 6 movies with the variables defined in the Movie class.
sully = movies.Movie("Sully", "Captain Sully who saved 155 lives aboard the disabled Airbus A320 jet",
                    "https://upload.wikimedia.org/wikipedia/commons/e/ee/Sully_Movie_Logo.png",
                    "https://www.youtube.com/watch?v=ofDzbPXBxP4")

#print(sully.storyline) #Debug statement, test to print storyline

fateOfTheFurious = movies.Movie("The Fate of the Furious", "A mysterious woman seduces Dom to betray the globe-trotting team",
                      "https://upload.wikimedia.org/wikipedia/en/2/2d/The_Fate_of_The_Furious_Theatrical_Poster.jpg",
                      "https://www.youtube.com/watch?v=9GvX2uexGkA")

#print(fateOfTheFurious.storyline) #Debug statement, tested to print storyline of movie

#fateOfTheFurious.showTrailer() #Debug statement, tested to open browser and play trailer.

theEmojiMovie = movies.Movie("The Emoji Movie", "Gene, an emoji embarks on a journey to become a real emoji",
                     "https://upload.wikimedia.org/wikipedia/en/6/63/The_Emoji_Movie_film_poster.jpg",
                     "https://www.youtube.com/watch?v=o_nfdzMhmrA")

loganLucky = movies.Movie("Logan Lucky", "Two brothers plan a robbery during Memorial Day Weekend at NASCAR Race in North Carolina",
                          "https://upload.wikimedia.org/wikipedia/en/e/e6/Logan_Lucky.png",
                          "https://www.youtube.com/watch?v=wsOIuzxMplA")

babyDriver = movies.Movie("Baby Driver", "A young driver is coerced to perform a robbery that later fails.",
                          "https://upload.wikimedia.org/wikipedia/en/8/8e/Baby_Driver_poster.jpg",
                          "https://www.youtube.com/watch?v=RWC3uA7YWg8")

kingsmanTheGoldenCircle = movies.Movie("Kingsman: The Golden Circle","Two secret organizations fight to defeat a common enemy",
                                       "https://upload.wikimedia.org/wikipedia/en/7/73/Kingsman_The_Golden_Circle.jpg",
                                       "https://www.youtube.com/watch?v=6reo6h7h1wk")

#Creates an array of all movies, uses new Python file to open movie page.
movies = [sully,fateOfTheFurious, theEmojiMovie, loganLucky, babyDriver, kingsmanTheGoldenCircle]
freshtomatoes.open_movies_page(movies)