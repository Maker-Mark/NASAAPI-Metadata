# Full URL Call https://api.nasa.gov/planetary/apod?api_key=vZviPQHrjc3jDCPFQNvbWka45EEPIrRAgbepKmvZ

from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__, template_folder='.')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text'] #flask will send us a request obj, adn from the form we can fish out the text
    r = requests.get(
        'https://api.nasa.gov/planetary/apod?api_key=vZviPQHrjc3jDCPFQNvbWka45EEPIrRAgbepKmvZ&date='+ text)
    # Get the dict representation of the response
    res = r.json() # Decodes the response json to python dict
    isImg = False
    #If the date is an image
    if(res['media_type'] == 'image'):
        isImg = True
    print(isImg)     
    return render_template('home.html', url=res['url'], title=res['title'], desc=res['explanation'], type=res['media_type'], isImg=isImg)

@app.route('/')
def  homepage():
    params = {
        'api_key': 'vZviPQHrjc3jDCPFQNvbWka45EEPIrRAgbepKmvZ'
    }
    isCool = "kinda"
    r = requests.get(
        'https://api.nasa.gov/planetary/apod?api_key=vZviPQHrjc3jDCPFQNvbWka45EEPIrRAgbepKmvZ')
    # Get the dict representation of the response
    res = r.json()
    if(res['media_type'] == 'image'):
        isImg = True
    return render_template('home.html', url=res['url'], title=res['title'], desc=res['explanation'], isImg=isImg)


if __name__ == '__main__':
    app.run( debug=True)
