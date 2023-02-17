import requests

request_ = requests.get('https://www.jsonkeeper.com/b/2IV8')
list_questions = request_.json()
