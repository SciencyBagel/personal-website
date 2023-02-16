import flask
import json

app = flask.Flask(__name__)
posts = {}  # global variable to store posts

# Routes
@app.route('/')
def home():
    # get posts from json file
    global posts
    json_file = open("data/posts.json", mode='r')
    posts = json.load(json_file)
    json_file.close()
    
    return flask.render_template('index.html.j2', posts=posts)

@app.route('/about')
def about():
    return flask.render_template('about.html.j2')

@app.route('/contact')
def contact():
    return flask.render_template('contact.html.j2')

@app.route('/post/#<post_id>')
def post(post_id):
    
    return flask.render_template('post.html.j2', post=posts[post_id])

# driver
if __name__ == '__main__':
    app.run(debug=True)
