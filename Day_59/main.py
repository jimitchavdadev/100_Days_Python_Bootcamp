from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

# Blog API URL
BLOG_API_URL = "https://api.npoint.io/674f5423f73deab1e9a7"
response = requests.get(BLOG_API_URL)
blog_posts = response.json()

@app.route('/')
def home():
    return render_template("index.html", posts=blog_posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:post_id>')
def post(post_id):
    post_data = next((post for post in blog_posts if post["id"] == post_id), None)
    return render_template("post.html", post=post_data)

if __name__ == "__main__":
    app.run(debug=True)
