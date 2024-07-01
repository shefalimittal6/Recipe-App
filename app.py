from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'APIKEYTOBEADDED'
BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

@app.route('/', methods=['GET', 'POST'])
def index():
    recipes = []
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            response = requests.get(BASE_URL, params={'query': query, 'apiKey': API_KEY})
            if response.status_code == 200:
                data = response.json()
                recipes = data.get('results', [])
    return render_template('index.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True)
