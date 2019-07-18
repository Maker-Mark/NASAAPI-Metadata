# Full URL Call https://api.nasa.gov/planetary/apod?api_key=vZviPQHrjc3jDCPFQNvbWka45EEPIrRAgbepKmvZ

from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__, template_folder='.')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    print(processed_text)
    r = requests.get(
        'https://api.nasa.gov/planetary/apod?api_key=vZviPQHrjc3jDCPFQNvbWka45EEPIrRAgbepKmvZ&date='+processed_text)
    # Get the dict representation of the response
    res = r.json()
    return render_template('home.html', img=res['url'], title=res['title'], desc=res['explanation'])

@app.route('/')
def homepage():
    params = {
        'api_key': 'vZviPQHrjc3jDCPFQNvbWka45EEPIrRAgbepKmvZ'
    }
    r = requests.get(
        'https://api.nasa.gov/planetary/apod?api_key=vZviPQHrjc3jDCPFQNvbWka45EEPIrRAgbepKmvZ')
    # Get the dict representation of the response
    res = r.json()

    return render_template('home.html', img=res['url'], title=res['title'], desc=res['explanation'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
