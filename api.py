import requests
import unicodedata

def remove_accents(input_str):
    # Normaliza el string a la forma compuesta
    normalized_str = unicodedata.normalize('NFD', input_str)
    # Filtra los caracteres que no son diacríticos
    return ''.join(char for char in normalized_str if unicodedata.category(char) != 'Mn')

class APICountrys:
    
    def __init__(self):
        self.url="https://restcountries.com/v3.1"
        self.paises = {}
        self.list_paises = []
        self.obtener_paises()
    
    
    def obtener_paises(self) -> None:
        response = requests.get(url=f"{self.url}/all")
        response.raise_for_status()


        if response.ok:
            dict_paises =  { remove_accents(pais['translations']['spa']['official']) : {
                'country': pais['translations']['spa']['official'],
                'prefix': pais.get('cioc'),
                'capital': pais.get('capital')[0] if pais.get('capital') else None,
                'domain': pais.get('tld')[0] if pais.get('tld') else None,
                'independent': pais.get('independent'),
                'currencie': pais.get('currencies')[list(pais.get('currencies').keys())[0]]['name'] if pais.get('currencies') else None,
                'currencie_symbol': pais.get('currencies')[list(pais.get('currencies').keys())[0]]['symbol'] if pais.get('currencies') else None,
                'languages': list(pais.get('languages').keys()) if pais.get('languages') else None,
                'region': pais.get('region'),
                'latitude': pais.get('latlng')[0],
                'longitude': pais.get('latlng')[1],
                'population': int(pais.get('population')),
                'maps': pais['maps']['googleMaps'],
                'timezone': pais['timezones'][0],
                'flag': pais['flags']['png'],
                'startOfWeek': pais['startOfWeek']
            } for pais in response.json()} 
        
        self.paises = dict_paises
    
        self.list_paises = list(dict_paises.keys())
    
    def get_search_pais(self, pais:str) -> dict:
        return self.paises[pais]
