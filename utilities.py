def formatSQLRowsForMovies(rows):
	movies = []
	for x in rows:
		movie = {
		'movie_id': x[0],
		'name': x[1],
		'year': x[2]
		}
		movies.append(movie)
	return movies

def formatSQLRowsForQuotes(rows):
	quotes = []
	for x in rows:
		quote = {
		'quote_id': x[0],
		'quote': x[2]
		}
		quotes.append(quote)
	return quotes
