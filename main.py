# '''
# Metadata Exercise
#     -Use an endpoint from api.nasa.gov
#         --Goal: connect with the API using flask and display information
#     -Extra feature: Include a textbox that takes in an api key and generates the POD
#     -Extra extra feature: Include a textbox that lets you choose a date, then display's that day's picture

# https://flask.palletsprojects.com/en/1.1.x/quickstart/
# https: // realpython.com/flask-connexion-rest-api/


# Outline:

# 1.Make flask server, get it running.
# 2.Connect to the NASA api, test a response body
#     -How do we render it in the browser?
# 3.Make route that takes today's date and displays the img and title

# '''
# from flask import Flask,  # Import flask
# # Create an instance of a Flask obj The first arg is the name of the app(single module use __name__, otherwise we need to specify, so that flask can find templates, static files, etc).
# app = Flask(__name__)

# # Use the route decorator to tell flask what URL should trigger this function
# @app.route('/')
# # We then define a function
# def hello_world():
#     return 'hello, world'

# ## Let's build a url
# '''
# url_for() accepts the name of the function, and any number of keyword args. Unknown vars are appended as query params

# '''

# @app.route('/apic')
# # We then define a function
# def api_call():
#     return 'hello, world'


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return "Logged in"
#     else:
#         return "logged out"
