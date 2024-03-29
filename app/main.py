from flask import Flask, render_template, request
from requests import post
import logging
import configparser
import os

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('./token.ini')
token = config['default']['token']

logging.basicConfig(filename='info.log', level=logging.INFO)


@app.route('/hello')
def hello():
    return 'Hello World!'


@app.route('/station', methods=['GET', 'POST'])
def station_id():
    data = None
    if request.method == 'POST':
        keyword = request.form['keyword']
        logging.info(keyword)
        msg = post(f'https://api.waqi.info/search/?keyword={keyword}&token={token}', verify=False)
        logging.info(msg.json()['data'])
        data = [f"name: {x['station']['name']}, station id: @{x['uid']}"
                for x in msg.json()['data']]

    return render_template('station.html', data=data)


if __name__ == "__main__":
    print("starting web server on port", os.environ['PORT'])
    logging.info("starting web server on port " + os.environ['PORT'])
    app.run(host="0.0.0.0", port=int(os.environ['PORT']), debug=True)
    print("stopped web server")
    logging.info("stopped web server")
