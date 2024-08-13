from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for, jsonify
from markupsafe import escape
import json
import urllib.request

app = Flask(__name__)


@app.route("/fetch-data", methods=['GET', 'POST'])
def fetch_data():
    # global input_data
    # input_data = {}
    if request.method == "POST":
        return redirect(url_for('get_processed_data'))
    external_api_url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = urllib.request.urlopen(external_api_url)
    data = response.read()
    dict_d = json.loads(data)
    with open("raw_data.json", "w") as file:
        json.dump(dict_d, file)
    return render_template('home.html', input_data=dict_d)


@app.route("/get-processed-data", methods=['GET'])
def get_processed_data():
    # global input_data
    output_data = {}
    if request.method == "GET":
        file1 = open("raw_data.json")
        input_data = json.load(file1)
        for key in input_data.keys():
            if key == "title" or key == "body":
                output_data[key] = str(input_data[key]).upper()
            else:
                output_data[key] = input_data[key]
        # Store the processed data in a new file
        with open("processed_data.json", "w") as file:
            json.dump(output_data, file)
        return render_template('home.html', input_data=input_data, output_data=output_data)
    else:
        return render_template('home.html')
