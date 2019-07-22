#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

movies = ("movie1", "movie2", "movie3", "movie4", "movie1")
 # CTM: Now we can't add, remove, or delete any item from movies
 # we can use del to delete movies as a whole

print ("movies = ", movies)
print ("movies lenght = ", len(movies))
print ("count of 'movie1' = ", movies.count("movie1"))
print ("index of 'movie1' = ", movies.index("movie4"))

movies1 = tuple(movies)
print ("movies1 = ", movies1)



