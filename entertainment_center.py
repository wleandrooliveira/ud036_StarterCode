# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 12:42:46 2019
@author: Wanderson
"""
import movie  # calls the contents of meda.py to define the class Movie.
import fresh_tomatoes  # takes in list of movies and output them in a websitet 

captain_marvel = movie.Movie("Captain Marvel (2019)", 
                        "Captain Marvel is an extraterrestrial Kree warrior" 
                        "who finds herself caught in the middle of an intergalactic battle between her"
                        "people and the Skrulls. Living on Earth in 1995, she keeps having recurring memories"
                        "of another life as U.S. Air Force pilot Carol Danvers. With help from Nick Fury,"
                        "Captain Marvel tries to uncover the secrets of her past while harnessing her special"
                        "superpowers to end the war with the evil Skrulls",
                        "https://nerdgeistdotcom.files.wordpress.com/2019/01/captain-marvel-poster-brie-larson-411x600.jpg",
                        "https://www.youtube.com/watch?v=Z1BCujX3pw8")
iron_man_3 = movie.Movie("Iron Man 3 (2013)", 
                        "Plagued with worry and insomnia since saving New York from destruction,"
                        "Tony Stark (Robert Downey Jr.), now, is more dependent on the suits that give him his Iron Man persona"
                        "-- so much so that every aspect of his life is affected, including his relationship with"
                        "Pepper (Gwyneth Paltrow). After a malevolent enemy known as the Mandarin (Ben Kingsley)"
                        "reduces his personal world to rubble, Tony must rely solely on instinct and ingenuity"
                        "to avenge his losses and protect the people he loves.",
                        "http://www.movienewsletters.net/photos/156876R1.jpg",
                        "https://www.youtube.com/watch?v=Ke1Y3P9D0Bc")
avengers = movie.Movie("The Avengers", "When Thor's evil brother, Loki (Tom Hiddleston), gains access to the unlimited power"
                        "of the energy cube called the Tesseract, Nick Fury (Samuel L. Jackson), director of S.H.I.E.L.D.,"
                        "initiates a superhero recruitment effort to defeat the unprecedented threat to Earth. Joining Fury's"
                        "dream team are Iron Man (Robert Downey Jr.), Captain America (Chris Evans), the Hulk (Mark Ruffalo),"
                        "Thor (Chris Hemsworth), the Black Widow (Scarlett Johansson) and Hawkeye (Jeremy Renner)",
                        "http://www.movienewsletters.net/photos/130835R1.jpg",
                        "https://www.youtube.com/watch?v=8AZ0LUafEAg")
robocop = movie.Movie("Robocop (2014)", "In 2028, OmniCorp is at the center of robot technology." 
                        "While its drones have long been used by the military overseas, their use is forbidden in American law enforcement."
                        "However, OmniCorp gets a golden opportunity to crack that market"
                        "when Detroit cop Alex Murphy (Joel Kinnaman) is critically injured in the line of duty."
                        "By transforming Murphy into a cyborg, OmniCorp executives hope to rake in billions for their shareholders,"
                        "but they forget one thing: There's still a man inside the machine.",
                        "https://m.media-amazon.com/images/M/MV5BMjQwODJkZmUtNjgwNy00ZmNhLWJlMjktNmFjNDVhOTMyZmRjXkEyXkFqcGdeQXVyODA4ODk5NTU@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=pWvI2nr_YQw")
hulk = movie.Movie("The Incredible Hulk(2008)", 
                        "Scientist Bruce Banner (Edward Norton) desperately seeks a cure for the gamma radiation"
                        "that contaminated his cells and turned him into The Hulk. Cut off from his true love Betty Ross (Liv Tyler)"
                        "and forced to hide from his nemesis, Gen. Thunderbolt Ross (William Hurt), Banner soon comes face-to-face with"
                        "a new threat: a supremely powerful enemy known as The Abomination (Tim Roth).",
                        "http://www.movienewsletters.net/photos/277217R1.jpg",
                        "https://www.youtube.com/watch?v=xbqNb2PFKKA") 
thor = movie.Movie("Thor (2011)", 
                        "As the son of Odin (Anthony Hopkins), king of the Norse gods, Thor (Chris Hemsworth)"
                        "will soon inherit the throne of Asgard from his aging father. However, on the day that he is to be crowned,"
                        "Thor reacts with brutality when the gods' enemies, the Frost Giants, enter the palace in violation of their treaty."
                        "As punishment, Odin banishes Thor to Earth. While Loki (Tom Hiddleston), Thor's brother, plots mischief in Asgard,"
                        "Thor, now stripped of his powers, faces his greatest threat.",
                        "http://www.movienewsletters.net/photos/113522R1.jpg",
                        "https://www.youtube.com/watch?v=Kk8HYCRZxRs")                 
movies = [captain_marvel, iron_man_3, avengers,robocop,hulk,thor]
fresh_tomatoes.open_movies_page(movies)
print(movie.Movie.VALID_RATINGS)  # calls the rating valid_rating in media.py
print(movie.Movie.__doc__)  # calls the document contained in the class Media()
                      
