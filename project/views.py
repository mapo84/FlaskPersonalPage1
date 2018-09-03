from project import app
from flask import render_template


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    return render_template('contact.html')
