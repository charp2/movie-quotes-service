from utilities import formatSQLRowsForMovies, formatSQLRowsForQuotes

def findMovies(data, conn):
	year = -1
	name = ''
	if 'year' in data:
		year = data['year']
	if 'name' in data and len(data['name']) > 1:
		name = '%' + data['name'] + '%'

	with conn.cursor() as cur:
		sql = "SELECT * FROM Movies WHERE Year=%s OR Name LIKE %s"
		cur.execute(sql, (str(year), name))
		conn.commit()
	return formatSQLRowsForMovies(cur)

def createMovie(data, conn):
	if 'year' not in data or 'name' not in data:
		raise Exception('Malformed request body')
	year = data['year']
	name = data['name']

	with conn.cursor() as cur:
		sql = "insert into Movies (Name, Year) VALUES (%s, %s)"
		cur.execute(sql, (name, year))
		conn.commit()
	return { 'Message': 'Successully added movie to DB' }


def getRandomQuotes(data, conn):
	with conn.cursor() as cur:
		sql = "SELECT * FROM Quotes ORDER BY RAND() LIMIT %s"
		cur.execute(sql, int(data['limit']) if int(data['limit']) > 0 else 0)
		conn.commit()
	return formatSQLRowsForQuotes(cur)

def findQuotesForMovie(data, conn):
	movie = data['movie']
	with conn.cursor() as cur:
		sql = "SELECT * from Quotes inner join Movies on Quotes.movie_id = Movies.movie_id where Movies.Name=%s"
		cur.execute(sql, movie)
		conn.commit()
	return formatSQLRowsForQuotes(cur)

def createQuoteForMovie(data, conn):
	quote = data['quote']
	movie = data['movie']

	with conn.cursor() as cur:
		sql = "INSERT INTO Quotes (movie_id, Quote) SELECT movie_id, %s FROM Movies where Name = %s"
		cur.execute(sql, (quote, movie))
		conn.commit()
	return { 'Message': 'Successully added quote to DB' }
