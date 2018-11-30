from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Make a Jazz Lyric Web App')

if __name__ == '__main__':
    #  app.config['dbconfig'] = connDict
    app.run(debug=True)
