from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

# TODO
# make this a param or fuzz to a given decade
@app.route('/films/<int:year>')
def films(year):
    sqlfile = 'database/file_incomes.db'

    conn = sqlite3.connect(sqlfile)
    c = conn.cursor()

    c.execute('''SELECT year_of_release,title,international_earning FROM films
          WHERE year_of_release=?
          ''', (year,))

    results = c.fetchall()
    conn.close()

    # debug
    #films = [r for r in results {'year': results[1], 'title': results[2], 'amount': results[3]}]

    return jsonify({'films': results})

@app.route('/')
def questions():
    return render_template('questions.html', appname='Movie Gross Guesser 27')
