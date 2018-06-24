"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

awesome_str = ""

for word in AWESOMENESS:
    awesome_str += "<option value='{}'>{}</option>".format(word, word)

DISSES = ['suck', 'are a chicken-face', 'stink', 'are dumb', 'are lame',
          'are a bad coder']

diss_str = ""

for word in DISSES:
    diss_str += "<option value='{}'>{}</option>".format(word, word)


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.<br>
    <a href='/hello'>Click here to go to Hello.</a></html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br>
          Pick a compliment:
          <select name='compliment-type'>
           {}
          </select><br>
          What's your favorite animal?<input type="text" name="animal"><br>
          <input type="submit" value="Submit">
        </form>
        <br>
        <form action="/diss">
        Random insults below. <br>
        What's your name? <input type="text" name="person"><br>
        Pick a diss: <select name='diss-type'>
        {}
        </select><br>
        What's your favorite animal?<input type="text" name="animal"><br>
        <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """.format(awesome_str, diss_str)


@app.route('/greet')
def greet_person():
    """Get user by name."""
    player = request.args.get("person")
    animal = request.args.get("animal")
    compliment = request.args.get("compliment-type")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}! Also, I love {}s.
      </body>
    </html>
    """.format(player, compliment, animal)


@app.route('/diss')
def diss_person():
    player = request.args.get("person")
    diss = request.args.get("diss-type")
    animal = request.args.get("animal")

    return"""
    <!doctype html>
    <html>
    <head>
      <title>You Get a Diss!</title>
    </head>
    <body>
      Yo, {}, I think you {}. Also, I hate {}s.
    </body>
    </html>
    """.format(player, diss, animal)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
