import os
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort


app = Flask(__name__)
app.secret_key = os.urandom(24) 


def get_db_connection():
    #conn = sqlite3.connect('./database/database.db')
    conn = sqlite3.connect('./app/database/database.db') # Para o Docker Container
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts ORDER BY created DESC').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

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
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()

            flash('Novo Post !', 'green')
            return redirect(url_for('index'))
    
    return render_template('create.html')

@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')

        elif not content:
            flash('Content is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Post Deletado !', 'red')
    return redirect(url_for('index'))

@app.route('/about/', methods=('GET',))
def about():
    return render_template('about.html')

"""
if __name__ == '__main__':
    app.run(host='192.168.10.184', port=8501)
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8501)
