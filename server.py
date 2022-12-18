from datetime import datetime
import logging
from flask import Flask

app = Flask(__name__)

from erp import *

today = datetime.now()
today_string = today.strftime("%d-%m-%Y")

logging.basicConfig(filename=f'/home/ec2-user/manual-81/{today_string}.log', level=logging.DEBUG)


@app.route('/')
def home():
    return "It works"


if __name__ == '__main__':
    # app.run(port='81', debug=True, host="0.0.0.0")
    app.run(port='1024', debug=True, host="0.0.0.0")
