from flask import Flask, render_template, request
from api import APICountrys

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    
    
    api = APICountrys()
    countries_select = []
    country = {}
    
    if request.method == 'POST':
        country_name = request.form.get('country_name')
        country = api.get_search_pais(pais=country_name)
        return render_template('index.html', country_info= country, countries=countries_select)
    
    countries_select = api.list_paises
    
    
    return render_template('index.html', country_info= country, countries=countries_select)

if __name__ == "__main__":
    app.run()