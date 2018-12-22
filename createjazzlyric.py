from flask import Flask, render_template, request
from connVarsDict import connDict
import mysql.connector

app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    if request.method == 'POST':
        vowel = request.form['vowel']
        # return redirect(url_for('show_lyric'))
        return render_template('entry.html',
                           the_title='Create a Jazz Lyric')
    else:
        return render_template('entry.html',
                           the_title='Create a Jazz Lyric')


@app.route('/show_lyric', methods=['POST'])
def create_lyric() -> str:
    title = 'New Jazz Lyric'
    vowel1 = request.form['vowel1']
    vowel2 = request.form['vowel2']
    vowel2_amount = request.form['vowel2_amount']
    consonant = request.form['consonant']

    # Shoo dap ba diii *eeeeeee...
    lyric = " Shooo" +\
            " d" + (vowel1) + "p" +\
            " b" + (vowel1 * 2) + " " +\
            consonant + (vowel2 * int(vowel2_amount)) +\
            " z" + ("e" * 8) + "... "

    vowel_count = count_vowels(lyric)

    lyric_params = {
        "the_title" :  title,
        "the_vowel1" : vowel1,
        "the_vowel2" : vowel2,
        "the_vowel2_amount" : vowel2_amount,
        "the_consonant" : consonant,
        "the_lyric" : lyric,
        "the_vowel_count" : vowel_count
    }

    return render_template('results.html', the_lyric_params=lyric_params,)


def count_vowels(lyric) -> str:
    vowels = set('aeiouy')
    vowel_count = 0

    for item in lyric:
        if item in vowels:
            vowel_count = vowel_count + 1

    return vowel_count


def add_lyric_to_db() -> str:
    # Establish connection & create cursor.
    conn = mysql.connector.connect(**connDict)
    cursor = conn.cursor()

    
if __name__ == '__main__':
    #  app.config['dbconfig'] = connDict

    # Test with:
    # Import driver, establish connection & create cursor.

    conn = mysql.connector.connect(**connDict)
    cursor = conn.cursor()

    _SQL = """SHOW DATABASES"""
    cursor.execute(_SQL)
    res = cursor.fetchall()
    for row in res:
        print(row)

    app.run(debug=True)
