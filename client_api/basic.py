import requests 

endpoint = "http://127.0.0.1:8081/product" #permet de rendre a httpbin.org
response = requests.post(endpoint, json={'name':'patate', 'content':'feculent', 'price':150}) #params={'abc':124},  json={'query':'hi'}) # recupere les données , param permet d'envoyer les donnee par l'url post permet d'envoyer les données dans la bd
print(response.json())  
print(response.status_code)
#http requeste renvoi les donnés sous forme de html
# rest api http  renvoi le JSON