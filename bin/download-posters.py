#!/usr/bin/env python
import os
import re
import sqlite3
import requests

import tmdbsimple as tmdb

def _get_api_key():
    """ Get the MovieDB API key or kill the process """
    try:
        "THE_MOVIE_DB_API_KEY" in os.environ
    except KeyError:
        print("Please set the environment variable THE_MOVIE_DB_API_KEY")
        exit(1)

    return os.environ["THE_MOVIE_DB_API_KEY"]


def _get_film_titles():
    sqlfile = 'database/file_incomes.db'
    conn = sqlite3.connect(sqlfile)
    cursor = conn.cursor()

    cursor.execute('SELECT title FROM films ORDER BY title')

    return cursor.fetchall()


def _build_base_url(tmdb_handle):
    config_info = tmdb_handle.Configuration().info()
    image_base = config_info["images"]["secure_base_url"]

    poster_width = 'w185' # chosen because it looks about right on the page

    return f"{image_base}{poster_width}"


def get_poster(poster_url, name):
    """ Construct the poster URL and download the poster to the local file system """
    # Only used for the side effect of downloading the image.
    # TODO: Skip get if file exists

    poster_file = f"static/images/{name}.jpg"

    print(f"Fetching {name} from {poster_url} and saving to {poster_file}")

    r = requests.get(poster_url)

    with open(poster_file, 'wb') as outfile:
        outfile.write(r.content)


def main():
    """ Main function to pull the downloading together """
    api_key = _get_api_key()
    tmdb.API_KEY = api_key
    search = tmdb.Search()

    titles = _get_film_titles()

    poster_base = _build_base_url(tmdb)

    for title in titles:
        movie_name = title[0]
        movie_poster = None
        print(movie_name)

        response = search.movie(query=movie_name)
        for result in search.results:
            movie_poster = result['poster_path']

            print("  ==  ", result['title'], result['id'], result['release_date'])
            break # TODO - fetch the first and hope it's the best match?

        sanitised_name = re.sub('[^A-Za-z0-9]+', '_', movie_name)

        get_poster(f"{poster_base}{movie_poster}", sanitised_name)


if __name__ == '__main__':
    main()
