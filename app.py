from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import os, sys

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])

def index():
    try:
        raise Exception("We are testing custiom exception")
    except Exception as e:
        housing = HousingException(e, sys)
        logging.info(housing.error_message)
        logging.info("We are tesing logging module")
    return "Staring Machine Learning Project"

if __name__=="__main__":
    app.run(debug=True)
