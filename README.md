# movies-and-quotes
Python service for interacting with a movie and movie-quotes MySql database

This library contains code for a lambda function which gets invoked by an AWS API-Gateway.
`function.py` contains the handler for the https event that invokes the lambda.

The updateFunction script contains a series of bash commands which will update the lambda on aws.
In order for this script to work, you must have installed PyMySql by following the instructions below:

`~/movies-and-quotes$ virtualenv v-env`
`~/movies-and-quotes$ source v-env/bin/activate`
`~/movies-and-quotes$ pip3 install PyMySql`

Then, configure your aws client and ensure that the last command in the `updateFunction` script points to the correct lambda: for example: `aws lambda update-function-code --function-name test --zip-file fileb://function.zip`

Now you can run `~/movies-and-quotes$ ./updateFunction` anytime code is updated.

# API
The base_uri for the API (which invokes this lambda) is https://bhfv7s8zka.execute-api.us-east-1.amazonaws.com/beta/

  Route                    |   Example Request Body
  -------------------------------------------------------------------

	POST '/movies/find'          { "name": "example", "year": 2003 }

  -------------------------------------------------------------------

	POST '/movies/create'        { "name": "example", "year": 2003 }

    -------------------------------------------------------------------

	POST '/quotes'               { "limit": 3 }

    -------------------------------------------------------------------

	POST '/quotes/find'          { "movie": "example" }

    -------------------------------------------------------------------

	POST '/quotes/create'        { "quote": "example", "movie": "example" }

    -------------------------------------------------------------------
