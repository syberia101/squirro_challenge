import requests
import json

def get_document_from_springer(keyword, number):
    keywords = {'q': keyword, 's': number}
    request_result = requests.get('http://api.springer.com/metadata/json?api_key=9188698f8c47d46fc33e66205c83c87d&', params=keywords).text
    request_result = json.loads(request_result)
    title = request_result['records'][0]['title']
    abstract = request_result['records'][0]['abstract']
    print(abstract)
    print(title)
    return title, abstract