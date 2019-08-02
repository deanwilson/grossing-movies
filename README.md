# grossing-movies
A small movie income guessing game


## Development

Create the virtual environment our python will run in

    python3 -m venv venv

Activate it

    source venv/bin/activate

Install the dependencies

    pip3 install -r requirements.txt

### Data sources

Load the movie data

   // TODO

Fetch the movie posters

    export THE_MOVIE_DB_API_KEY=fg645678jgde7899jgfdesfd6535a276

    bin/download-posters.py

You can see the downloaded images in `static/images/` on your local file system.

And as required by the data provider:

 * "This product uses the [TMDb](https://www.themoviedb.org/) API but is not endorsed or certified by TMDb."

### Running the flask application

Once you've set up your environment as above run the flask application

    FLASK_APP=films.py flask run

If you want to enable the debugger add the `FLASK_ENV` variable

    FLASK_ENV=development FLASK_APP=films.py flask run

You can then test the response with curl

    curl http://127.0.0.1:5000/films/2017

Open the [page locally](http://127.0.0.1:5000)
