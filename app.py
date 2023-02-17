import flask
import json
import smtplib, ssl

from config import Email, Host
import data_io

# app setup
app = flask.Flask(__name__)
posts = {}  # global variable to store posts

@app.before_first_request
def initialize_posts():
    global posts
    posts = data_io.load_posts()

# Routes
@app.route('/')
def home():
    
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
    post = posts[post_id]
    return flask.render_template('post.html', post=post)
    
# driver
if __name__ == '__main__':
    app.run(debug=True, host=Host.HOST, port=Host.PORT)
