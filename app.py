from flask import Flask, redirect, url_for, request, render_template, session    # render_template utilizamos para retornar o HTML
import requests, os, uuid, json
from dotenv import load_dotenv      # carrega os valores de .env
load_dotenv()

app = Flask(__name__)

# usando @app.route, indicamos a rota que queremos criar
# caminho será /, que é a rota padrão. Indicamos que ele será usado para GET
# se uma solicitação GET chegar para /, o Flask chamará de forma automática a função index 
# no corpo de index, indicamos que retornaremos um modelo HTML chamado index.html para o usuário
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')       # por padrão utilizamos index ou default

@app.route('/', methods=['POST'])
def index_post():
    # Read the values from the form
    original_text = request.form['text']
    target_language = request.form['language']

    # Load the values from .env
    key = os.environ['KEY']
    endpoint = os.environ['ENDPOINT']
    location = os.environ['LOCATION']

    # Indicate that we want to translate and the API version (3.0) and the target language
    path = '/translate?api-version=3.0'
    # Add the target language parameter
    target_language_parameter = '&to=' + target_language
    # Create the full URL
    constructed_url = endpoint + path + target_language_parameter

    # Set up the header information, which includes our subscription key
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # Create the body of the request with the text to be translated
    body = [{ 'text': original_text }]

    # Make the call using post
    translator_request = requests.post(constructed_url, headers=headers, json=body)
    # Retrieve the JSON response
    translator_response = translator_request.json()
    # Retrieve the translation
    translated_text = translator_response[0]['translations'][0]['text']

    # Call render template, passing the translated text,
    # original text, and target language to the template
    return render_template(
        'results.html',
        translated_text=translated_text,
        original_text=original_text,
        target_language=target_language
    )