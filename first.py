from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/flask-blog'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(30))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)


@app.route('/')
def index():
    blogs = BlogPost.query.order_by(BlogPost.id.desc()).all()
    return render_template('index.html', blogs=blogs)


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    blog = BlogPost.query.filter_by(id=blog_id).one()
    date_posted = blog.date_posted.strftime('%B %d, %Y')

    return render_template('post.html', blog=blog, date_posted=date_posted)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/addBlog')
def add_blog():
    return render_template('add_blog.html')


@app.route('/store_blog', methods=['POST'])
def store_blog():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    date_posted = request.form['date_posted']
    content = request.form['content']

    post = BlogPost(title=title, subtitle=subtitle, author=author, date_posted=date_posted, content=content)
    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

