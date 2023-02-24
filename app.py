from flask import Flask, render_template, url_for, redirect, flash, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import AddArticle, UpdateArticle

app = Flask(__name__)
SECRET_KEY = 'juicy-pussy-money-money-pussy-juicy'
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog2.db'
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Article {self.id}>"


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html', title='About this site')


@app.route('/add-article', methods=["POST", "GET"])
def add_article():
    form = AddArticle()
    if form.validate_on_submit():
        try:
            article = Article(title=form.title.data, intro=form.intro.data, text=form.text.data)
            db.session.add(article)
            db.session.flush()
            db.session.commit()
            return redirect('/articles')
        except:
            db.session.rollback()
            print("Ошибка добавления в БД")

    return render_template('add-article.html', title='Create new article', form=form)


@app.route('/articles/<int:id>')
def get_article(id):
    try:
        article = Article.query.get(id)
    except:
        print("Ошибка получения  из БД")
        return redirect('/articles')

    return render_template('get_article.html', article=article)


@app.route('/articles/<int:id>/update', methods=["POST", "GET"])
def update_article(id):
    article = Article.query.get(id)

    form = UpdateArticle()
    if form.validate_on_submit():
        try:
            article.title = form.title.data
            article.intro = form.intro.data
            article.text = form.text.data

            db.session.commit()
            return redirect('/articles')
        except:
            db.session.rollback()
            print("Ошибка обновления в БД")

    return render_template('update_article.html', article=article, title='Update this article', form=form)


@app.route('/articles/<int:id>/delete')
def delete_article(id):
    try:
        article = Article.query.get_or_404(id)
        db.session.delete(article)
        db.session.flush()
        db.session.commit()
    except:
        print("Ошибка удаления из БД")

    return redirect('/articles')


@app.route('/articles')
def get_articles():
    articles = []
    try:
        articles = Article.query.order_by(Article.date.desc()).all()
    except:
        print("Ошибка получения  из БД")

    return render_template('get_articles.html', title='List of articles', articles=articles)


if __name__ == '__main__':
    app.run(debug=True)
