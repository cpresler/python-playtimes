# Movie Data
movie_titles = ['Star Wars: A New Hope', 'Star Wars: The Empire Strikes Back', 'Star Wars: Return of the Jedi', 'Star Wars: The Phantom Menace', 'Star Wars: Attack of the Clones', 'Star Wars: Revenge of the Sith', 'Star Wars: The Force Awakens']
parental_rating = ['PG','PG','PG','PG','PG','PG-13','PG-13']
bechdel_rating = [1,0,1,3,3,1,3]
imdb_rating = [8.7,8.8,8.4,6.5,6.7,7.6,8.4]
genre = ['Action, Adventure, Fantasy','Action, Adventure, Fantasy','Action, Adventure, Fantasy','Action, Adventure, Fantasy','Action, Adventure, Fantasy','Action, Adventure, Fantasy','Action, Adventure, Fantasy',]

for title, pg_rating, bechdel, imdb, genre in zip(movie_titles,parental_rating,bechdel_rating,imdb_rating,genre):
	print "{0}, {1}, {2}, {3}, {4}".format(title, pg_rating, bechdel, imdb, genre)