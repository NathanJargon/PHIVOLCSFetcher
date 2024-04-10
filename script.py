from flask import Flask, render_template_string
import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://earthquake.phivolcs.dost.gov.ph', verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    classes = ['auto-style99', 'auto-style90', 'auto-style77', 'auto-style56', 'auto-style52']
    earthquake = {}

    for class_name in classes:
        elements = soup.select('.' + class_name)
        for i, element in enumerate(elements):
            text = element.text.replace('\n', '').replace('\t', '').replace('\u00c2', '').replace('\u00b0', '')
            if i not in earthquake:
                earthquake[i] = text
            else:
                earthquake[i] += text

    return jsonify(earthquake)

if __name__ == '__main__':
    app.run(debug=True)