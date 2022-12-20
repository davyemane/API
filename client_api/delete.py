import requests 

id = input('enter the id of product that you want to delete')
endpoint = f"http://127.0.0.1:8081/product/{id}/delete/" #permet de rendre a httpbin.org
response = requests.delete(endpoint) #params={'abc':124},  json={'query':'hi'}) # recupere les données , param permet d'envoyer les donnee par l'url post permet d'envoyer les données dans la bd
print(response.status_code, response.status_code==204)
#http requeste renvoi les donnés sous forme de html
# rest api http  renvoi le JSON