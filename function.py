
import sys
import logging
import rds_config
import pymysql
import json
import traceback

from resources import findMovies, createMovie, getRandomQuotes, findQuotesForMovie, createQuoteForMovie

#rds settings
rds_host  = "moviesandquotes.czuutkom8pq9.us-east-1.rds.amazonaws.com"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
	conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except Exception as ex:
	logger.error(ex)
	sys.exit()
logger.info('SUCCESS: connection succeeded')

Routes = {
	'/movies/find': findMovies,
	'/movies/create': createMovie,
	'/quotes': getRandomQuotes,
	'/quotes/find': findQuotesForMovie,
	'/quotes/create': createQuoteForMovie
}

def response_proxy(data):
	response = {}
	response["isBase64Encoded"] = False
	response["statusCode"] = data["statusCode"]
	response["headers"] = {}
	if "headers" in data:
		response["headers"] = data["headers"]
	response["body"] = json.dumps(data["body"])
	return response

def request_proxy(data):
	request = {}
	request = data
	request["body"]=json.loads(data["body"])
	return request

def handler(event, context):
	response = {}
	try:
	  request = request_proxy(event)
	  response["statusCode"]=200
	  response["headers"]={}

	  data = {}
	  data = Routes[request['resource']](request['body'], conn)
	  response["body"]=data
	except Exception as e:
	  traceback.print_exc()
	  response["statusCode"]=500
	  response["body"]={'message': e}

	return response_proxy(response)
