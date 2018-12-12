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

    lyric = "Sh" + (vowel1 * 2) +\
            " b" + ("oop") + \
            " d" + (vowel2 * 2) + \
            " z" + "eeee" +\
            " d" + (vowel1 * 7) + "..."
    return render_template('results.html', the_title=title, the_vowel1=vowel1, the_vowel2=vowel2, the_lyric=lyric,)


if __name__ == '__main__':
    #  app.config['dbconfig'] = connDict
    app.run(debug=True)
