import flask

app = flask.Flask(__name__)

# Routes
@app.route('/')
def home():
    return flask.render_template('index.html.j2')

@app.route('/about')
def about():
    return flask.render_template('about.html.j2')

@app.route('/contact')
def contact():
    return flask.render_template('contact.html.j2')

# driver
if __name__ == '__main__':
    app.run(debug=True)
