from flask import Flask, render_template, request
from datetime import datetime
from connVarsDict import connDict
import mysql.connector

app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'str':
    msg_params = {
        "need_vowel1_msg": "",
        "need_vowel2_msg": "",
        "need_number_msg": "",
        "need_consonant_msg": ""
    }
    return render_template('create_lyric.html',
                           the_title='Create a Jazz Lyric',
                           the_msg_params=msg_params,)


@app.route('/show_lyric', methods=['POST'])
def create_lyric() -> str:
    page_title = 'See Jazz Lyric'
    vowel_set = list('aeiouy')
    consonant_set = list('bcdfghijklmnpqrstvwxz')

    need_vowel_msg = 'You must enter a vowel.'
    need_number_msg = 'You must enter a number from 3-9.'
    need_consonant_msg = 'You must enter a consonant.'

    vowel1 = request.form['vowel1'].lower()
    vowel2 = request.form['vowel2'].lower()
    vowel2_amount = 0

    # try-catch block for when vowel2_amount field is empty string, ''.
    try:
        vowel2_amount = int(request.form['vowel2_amount'])
    except Exception as e:
        print(e)

    consonant = request.form['consonant'].lower()

    error_count = 0

    msg_params = {
        "need_vowel1_msg": "",
        "need_vowel2_msg": "",
        "need_number_msg": "",
        "need_consonant_msg": ""
    }

    if vowel1 not in vowel_set:
        # Render entry page again & show, 'Enter a vowel.'
        error_count += 1
        msg_params["need_vowel1_msg"] = need_vowel_msg

    if vowel2 not in vowel_set:
        # Render entry page again & show, 'Enter a vowel.'
        error_count += 1
        msg_params["need_vowel2_msg"] = need_vowel_msg

    if vowel2_amount < 3 or vowel2_amount > 9:
        # Render entry page again & show, 'Enter a number from 3-9.'
        error_count += 1
        msg_params["need_number_msg"] = need_number_msg

    if consonant not in consonant_set:
        # Render entry page again & show, 'Enter a consonant.'
        error_count += 1
        msg_params["need_consonant_msg"] = need_consonant_msg

    if error_count > 0:
        return render_template('create_lyric.html',
                               the_title='Create a Jazz Lyric',
                               the_msg_params=msg_params, )

    lyric = " Shooo d%sp b%s %s z%s..." % (
        vowel1,
        vowel1 * 2,
        consonant + (vowel2 * int(vowel2_amount)),
        "e" * 8)

    conn = mysql.connector.connect(**connDict)
    cursor = conn.cursor()

    try:
        nowdatetime = datetime.now()

        sql = """INSERT INTO lyric(lyric, date_created) VALUES (%s, %s)"""
        cursor.execute(sql, (lyric, nowdatetime))

        conn.commit()
    finally:
        conn.close()

    vowel_count = count_vowels(lyric)
    lyric_params = {
        "the_page_title":  page_title,
        "the_vowel1": vowel1,
        "the_vowel2": vowel2,
        "the_vowel2_amount": vowel2_amount,
        "the_consonant": consonant,
        "the_lyric": lyric,
        "the_vowel_count": vowel_count
    }

    return render_template('show_lyric.html', the_lyric_params=lyric_params,)


def count_vowels(lyric) -> str:
    vowels = set('aeiouy')
    vowel_count = 0

    for item in lyric:
        if item in vowels:
            vowel_count = vowel_count + 1

    return vowel_count


@app.route('/show_song', methods=['GET'])
def create_song() -> str:
    conn = mysql.connector.connect(**connDict)
    cursor = conn.cursor()

    try:
        sql = """SELECT lyric, date_created
            FROM lyric WHERE date_deactivated IS NULL
            ORDER BY date_created DESC"""
        cursor.execute(sql)
        all_lyrics = cursor.fetchall()
    finally:
        conn.close()

    page_title = 'See Jazz Song'

    return render_template('show_song.html', page_title=page_title,
                           all_lyrics=all_lyrics)


if __name__ == '__main__':
    app.run(debug=True)
