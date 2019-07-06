# grossing-movies
A small movie income guessing game


## Development

Create the virtual environment our python will run in

    python3 -m venv venv

Activate it

    source venv/bin/activate

Install the dependencies

    pip3 install -r requirements.txt


### Running the flask application

Once you've set up your environment as above run the flask application

    FLASK_APP=films.py flask run

If you want to enable the debugger add the `FLASK_ENV` variable

    FLASK_ENV=development FLASK_APP=films.py flask run

You can then test the response with curl

    curl http://127.0.0.1:5000/films/2017

## Client

### 

    cd html

    python3 -m http.server 8000

Open the [page locally](http://127.0.0.1:8000)
