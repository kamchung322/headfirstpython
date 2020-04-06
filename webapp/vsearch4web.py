from flask import Flask, render_template, request, redirect, escape, copy_current_request_context
from vsearch import search4letters
from DBcm import UseDatabase
from threading import Thread
import time

app = Flask(__name__)
app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB'}

#  No need to use redirect, it costs 2 request
#  Flask can associate more than one URL to given function.
#  @app.route('/')
#  def hello() -> '302':
#      return redirect('/entry')


@app.route('/search4', methods=['Post'])
def do_search() -> 'html':

#  use @copy_current_request_context to preserve the data in request
    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        """ log information to vsearch.log """
        
        time.sleep(10)

        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """insert into log
                    (phrase, letters, ip, browser_string, results )
                    values
                    (%s, %s, %s, %s, %s)"""
            cursor.execute(_SQL, (req.form['phrase'],
                                req.form['letters'],
                                req.remote_addr,
                                req.user_agent.browser,
                                res))

    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    try:
        t = Thread(target=log_request, args=(request, results))
        t.start()
        #  log_request(request, results)
    except Exception as err:
        print("Some error in log_request :", err)
        
    return render_template('result.html', the_title='Here are your result',
        the_phrase=phrase, the_letters=letters, the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """SELECT phrase, letters, ip, browser_string, results 
                  from log"""
        print("SQL : ", _SQL)
        cursor.execute(_SQL)
        contents = cursor.fetchall()

    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', 
                            the_title='View log',
                            the_row_titles = titles,
                            the_data = contents)


if __name__ == '__main__':
    app.run(debug=True)