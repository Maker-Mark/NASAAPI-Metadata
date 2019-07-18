# Full URL Call https://api.nasa.gov/planetary/apod?api_key=vZviPQHrjc3jDCPFQNvbWka45EEPIrRAgbepKmvZ

from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='.')


@app.route('/')
def homepage():
    params = {
        'api_key': 'vZviPQHrjc3jDCPFQNvbWka45EEPIrRAgbepKmvZ',
    }
    r = requests.get(
        'https://api.nasa.gov/planetary/apod?api_key=vZviPQHrjc3jDCPFQNvbWka45EEPIrRAgbepKmvZ&date=2018-11-9')
    # date = json.loads(r["date"])
    # Get the dict representation of the response
    res = r.json()

    return render_template('home.html', img=res['url'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
