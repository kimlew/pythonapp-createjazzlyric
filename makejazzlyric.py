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
    vowel = request.form['vowel']
    return vowel


if __name__ == '__main__':
    #  app.config['dbconfig'] = connDict
    app.run(debug=True)
