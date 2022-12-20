import requests 

endpoint = "http://127.0.0.1:8081/product/9/update/" #permet de rendre a httpbin.org
response = requests.put(endpoint, json={'name':'pomme du ciel', 'content':'le reve des blancs', 'price':2000 }) #params={'abc':124},  json={'query':'hi'}) # recupere les données , param permet d'envoyer les donnee par l'url post permet d'envoyer les données dans la bd
print(response.json())  
print(response.status_code)
#http requeste renvoi les donnés sous forme de html
# rest api http  renvoi le JSON