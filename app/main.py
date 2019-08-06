# Full URL Call https://api.nasa.gov/planetary/apod?api_key=vZviPQHrjc3jDCPFQNvbWka45EEPIrRAgbepKmvZ

from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__, template_folder='.')


@app.route('/', methods=['GET','POST'])
def  homepage():
    #If the method is POST
    if(request.method ==  'POST'):
        text = request.form['text'] #flask will send us a request obj, adn from the form we can fish out the text
        r = requests.get(
            'https://api.nasa.gov/planetary/apod?api_key=vZviPQHrjc3jDCPFQNvbWka45EEPIrRAgbepKmvZ&date='
            + text)
        # Get the dict representation of the response
        res = r.json() # Decodes the response json to python dict
        isImg = False
        #If the date is an image
        if(res['media_type'] == 'image'):
            isImg = True
        return render_template("/templates/home.html", url=res['url'], title=res['title'],
         desc=res['explanation'], type=res['media_type'], isImg=isImg)

    #Otherwise it is a GET request
    r = requests.get(
        'https://api.nasa.gov/planetary/apod?api_key=vZviPQHrjc3jDCPFQNvbWka45EEPIrRAgbepKmvZ')
    # Get the dict representation of the response
    res = r.json()
    print(type(res))
    if(res['media_type'] == 'image'):
        isImg = True
    return render_template("/templates/home.html", url=res['url'], 
    title=res['title'], desc=res['explanation'], isImg=isImg)


if __name__ == '__main__':
    app.run( debug=True)
