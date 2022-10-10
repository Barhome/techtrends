import sqlite3

from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from flask.wrappers import Response
from werkzeug.exceptions import abort
import logging

# Define db_connection_counter
db_connection_counter = 0 
# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    #global counter 
    global db_connection_counter
    db_connection_counter +=1
    print(db_connection_counter)
    return connection

# Function to get a post using its ID
def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    connection.close()
    return post

# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# Define the main route of the web application 
@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

# Define how each individual article is rendered 
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
      #adding logger with the message '404 page access denied' to show on the console
      app.logger.info('404 Page Access Denied')
      return render_template('404.html'), 404
    else:
      #adding logger with the message 'post title retrieved' to show on the console
      app.logger.info(post['title']+ ' retrieved')
      return render_template('post.html', post=post)

# Define the About Us page
@app.route('/about')
def about():
    #adding logger with the message 'The "About Us" page is retrieved.' to show on the console
    app.logger.info('The "About Us" page is retrieved')
    return render_template('about.html')

# Define the post creation functionality 
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            connection.commit()
            connection.close()
            #adding logger with the message 'New article was created' to show on the console
            app.logger.info(title + 'New article was created')
            return redirect(url_for('index'))

    return render_template('create.html')

# Building healthz endpoint for techtrends
@app.route('/healthz')
# define status function to handle healthz endpoint
def status():
    response = app.response_class(
        response = json.dumps({'result':'OK - Healthy'}),
        status = 200,
        mimetype ='application/json'
    )
    return response 

# Building metrics endpoint for techtrends
@app.route('/metrics')
# Define metrics function to handle metrics endpoint 
def metrics():
    # Getting posts count
    connection = get_db_connection()
    post_count = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    # global counter
    global db_connection_counter
    response = app.response_class(
        response = json.dumps({'db_connection_count':db_connection_counter,'post_count':len(post_count)}),
        mimetype = "application/json"

    )
    return response
  
# start the application on port 3111
if __name__ == '__main__':
   logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%A, %d/%b/%Y at, %H:%M:%S %p', level=logging.DEBUG)
   app.run(host='0.0.0.0', port='3111')
