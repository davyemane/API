import json
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def api_view(request, *args, **kwargs):
    #request est une instance de HttpRequest
    print(request.body) #renvoi un byte string de tout ce qui se trouve dans l'appli
    data = json.loads(request.body)# json.loads transforme le byte string en dictionaire
    data = json.dumps(data) #renvoi les données dans leur formes d'origine
    print(data)
    data['headers'] = dict(request.headers)# contient tout ce qu'on envoi
    data['content_type'] = request.content_type #renvoi le type de donnée
    data['params'] = dict(request.GET) # recupere les données envoyés par l'url
    data['post-data'] = dict(request.POST)
    return JsonResponse(data)
