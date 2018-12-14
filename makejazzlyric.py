from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    if request.method == 'POST':
        vowel = request.form['vowel']
        # return redirect(url_for('show_lyric'))
        return render_template('entry.html',
                           the_title='Make a Jazz Lyric Web App')
    else:
        return render_template('entry.html',
                           the_title='Make a Jazz Lyric Web App')


@app.route('/show_lyric', methods=['POST'])
def create_lyric() -> str:
    title = 'New Jazz Lyric'
    vowel1 = request.form['vowel1']
    vowel2 = request.form['vowel2']
    vowel2_amount = request.form['vowel2_amount']
    consonant = request.form['consonant']

    # Shoo dap ba diii *eeeeeee...
    lyric = " Shoo" +\
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


def count_vowels(str) -> str:
    vowel_count = 0
    return vowel_count


if __name__ == '__main__':
    #  app.config['dbconfig'] = connDict
    app.run(debug=True)
