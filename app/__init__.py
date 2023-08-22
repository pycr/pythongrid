from flask import Flask
from flask_session import Session
import logging
from config import Config

app = Flask(__name__)

# start Flask session
app.config['SECRET_KEY'] = "<REPLACE WITH YOUR OWN SECRET KEY HERE>"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.debug = True
app.config.from_object(Config)

# logging in terminal display (no log file)
logging.basicConfig(level=logging.DEBUG)

# logging to file
# logging.basicConfig(filename='log1.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

from app import routes #, models