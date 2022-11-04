from flask import Flask, render_template, request, url_for, flash, redirect
import psycopg2

# ...

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)


# ...

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))

    return render_template('create.html')


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='pingis',
                            user='pingis',
                            password='spela_pingis')
    return conn


@app.route('/books')
def books():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', books=books)
