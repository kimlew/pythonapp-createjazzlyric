from flask import Flask, render_template, request
from connVarsDict import connDict
import mysql.connector

app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    msg_params = {
        "need_vowel_msg" : "",
        "need_number_msg" : "",
        "need_consonant_msg" : ""
    }
    return render_template('entry.html', the_title='Create a Jazz Lyric', the_msg_params=msg_params,)


@app.route('/show_lyric', methods=['POST'])
def create_lyric() -> str:
    title = 'New Jazz Lyric'
    vowel_set = set('aeiouy')
    consonant_set = set('bcdfghijklmnpqrstvwxz')

    vowel1 = request.form['vowel1'].lower()
    vowel2 = request.form['vowel2'].lower()
    vowel2_amount = (int) (request.form['vowel2_amount'])
    consonant = request.form['consonant'].lower()

    need_vowel_msg = 'You must enter a vowel.'
    need_number_msg = 'You must enter a number from 3-9.'
    need_consonant_msg = 'You must enter a consonant.'

    msg_params = {
        "need_vowel_msg": need_vowel_msg,
        "need_number_msg": need_number_msg,
        "need_consonant_msg": need_consonant_msg
    }


    if vowel1 not in vowel_set:
        # Render entry page again & print('Enter a vowel.')
        msg_params["need_vowel_msg"] = need_vowel_msg

        #return render_template('entry.html', the_title='Create a Jazz Lyric', the_msg_params=msg_params,)
    if vowel2 not in vowel_set:
        # Render entry page again & print('Enter a vowel.')
        return render_template('entry.html', the_title='Create a Jazz Lyric', the_msg_params=msg_params,)

    if vowel2_amount < 3 or vowel2_amount > 9:
        # Render entry page again & print('Enter a number from 3-9.')
        return render_template('entry.html', the_title='Create a Jazz Lyric', the_msg_params=msg_params,)

    if consonant != consonant_set:
        # Render entry page again & print('Enter a consonant.')
        return render_template('entry.html', the_title='Create a Jazz Lyric', the_msg_params=msg_params,)

    return render_template('entry.html', the_title='Create a Jazz Lyric', the_msg_params=msg_params, )


    # Shoo dap ba diii *eeeeeee...
    lyric = " Shooo" +\
            " d" + (vowel1) + "p" +\
            " b" + (vowel1 * 2) + " " +\
            consonant + (vowel2 * int(vowel2_amount)) +\
            " z" + ("e" * 8) + "... "

    conn = mysql.connector.connect(**connDict)
    cursor = conn.cursor()

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

    # Put in main() temporarily - so runs immediately to see if MySQL works.
    # If I put in Flask handler function that handles it for the page,
    # I would have to run so it goes to the show_lyric page.

    # conn = mysql.connector.connect(**connDict)
    # cursor = conn.cursor()

    # _SQL = """SHOW DATABASES"""
    # cursor.execute(_SQL)
    # res = cursor.fetchall()
    # for row in res:
    #     print(row)

    app.run(debug=True)
