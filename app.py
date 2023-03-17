import smtplib
import ssl
import flask
from flask import url_for
from flask_ckeditor import CKEditor
import datetime as dt

from blogdb import DBManager, Post
import config
from config import Email, Host
import myforms

# database setup
db = DBManager(config.CONNECTION_STRING)  # create dataio object to communicate with database

# app setup
app = flask.Flask(__name__)
ckeditor = CKEditor(app)  # needed for creating fancy text box
app.config['SECRET_KEY'] = config.SECRET_KEY


# View handlers
@app.route('/')
def index():
    posts = db.get_posts()
    return flask.render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return flask.render_template('about.html')


@app.route('/contact', methods=["POST", "GET"])
def contact():
    # if user is loading up the page
    if flask.request.method == "GET":
        return flask.render_template('contact.html', msg_sent=False)

    # if user submitted contact information
    elif flask.request.method == "POST":
        # used to process the data from the form located in /contact

        # get user info
        subject = "New Message"
        sender_name = flask.request.form["name"]
        sender_email = flask.request.form["email"]
        sender_tel = flask.request.form["tel"]
        sender_input = flask.request.form["message"]

        # format message
        message = f"Subject: {subject}\n\nName: {sender_name}\nEmail: {sender_email}\nPhone: {sender_tel}\nMessage: {sender_input}"

        # send message
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", Email.PORT, context=context) as server:
            server.login(Email.ID, Email.PASSWORD)
            server.sendmail(from_addr=sender_email, to_addrs=Email.ID, msg=message)

        return flask.render_template('contact.html', msg_sent=True)
    else:
        return "error"


@app.route('/post/#<post_id>')
def post(post_id):
    post = db.get_post(post_id)
    return flask.render_template('post.html', post=post)

@app.route('/new-post', methods=["GET", "POST"])
def new_post():
    form = myforms.PostForm()
    
    if form.validate_on_submit():
        now = dt.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        post = Post(
            title=form.title.data,
            date=now,
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data,
            subtitle=form.subtitle.data
        )
        db.add_post(post)
        return flask.redirect(url_for("index"))
    
    return flask.render_template('new_post.html', form=form)


# API
@app.route('/api/get_post', methods=["GET"])
def api_get_post():
    args = flask.request.args.to_dict()
    
    if flask.request.method == "GET":
        post_id = int(args["id"])
        
        # get object from database
        post = db.get_post(post_id)
        
        if not post:
            return flask.jsonify(error="Not Found"), 404
        
        return flask.jsonify(result=post.__dict__), 200
    else:
        return flask.jsonify(error="Bad Request"), 400
    
@app.route('/api/add_post', methods=["POST"])
def api_add_post():
    args = flask.request.args.to_dict()
    
    if flask.request.method == "POST":
        new_post = Post(**args)
        db.add_post(new_post)
        
        return flask.jsonify(status="Success"), 201
    else:
        return flask.jsonify(error="Bad Request"), 400
        
    

# driver
if __name__ == '__main__':
    # global posts
    app.run(debug=True, host=Host.HOST, port=Host.PORT)
