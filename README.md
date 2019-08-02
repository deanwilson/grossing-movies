# grossing-movies

A small movie income guessing game

![Screenshot of the game](/highest-earner.png "Screenshot of the game")

## Development

Before you can run this locally you'll need to configure Python (and its
required dependencies) and then process the data and fetch the movie poster
images.

### Configure Python

Create the virtual environment our python will run in

    python3 -m venv venv

Activate it

    source venv/bin/activate

Install the dependencies

    pip3 install -r requirements.txt

### Prepare the data

Load the movie data. This script will create a sqlite database,
`database/file_incomes.db`, from the data in `data/film_incomes`.

    bin/data2sqlite.py

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

### Author

  [Dean Wilson](https://www.unixdaemon.net)

### License

 * Released under the GPLv2
