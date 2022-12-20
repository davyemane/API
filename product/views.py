from product.models import Product
from django.http import JsonResponse
from django.forms.models import model_to_dict #creer automatiq les dictio grace au formulaire
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *
from rest_framework import generics, mixins, permissions, authentication

#recupere les donne en bd en fonction de l'id
class DetailProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class= ProductSerializers

#créer un nouvelle objet 
class CreateProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class= ProductSerializers
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

#mise a jour des données
class UpdateProductView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class= ProductSerializers
    lookup_field = 'pk'

#suppression des données
class DeletePreoductView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class= ProductSerializers
    lookup_field = 'pk'

class ListProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class= ProductSerializers




class  ProductMixinsView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class= ProductSerializers
    lookup_field= 'pk'
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)












































#SERIALIZATION : mettre des donnée sous formes de dictionaire 

#@api_view(['POST'])#POUR ENVOYER LES DONNÉES NIVEAU BAKEND OU A LA BD IL FAUT UTILISER POST
#def api_view(request):
    #recuperation des données de la bd
    #query = Product.objects.all().order_by('?').first() # le ? c'est pour dire que c'est aleatoire

    #INSERTION DES DONNÉE
   # serializer =ProductSerializers(data= request.data)#recupere les donnee envoyer par le client
   # if serializer.is_valid(raise_exception=True):#si les données sont valide
    #    serializer.save()#on les enregistre dans la bd
    #    return Response(serializer.data)#ET ON LES AFFICHES 
   # else:
        #return Response({'details':'invalide data'})

    #if query:
        #data['name'] = query.name #c'est comme ca qu'on insert les données dans un dictionaire
        #data['content'] = query.content
        #data['price'] = query.price
        #data= ProductSerializers(query).data
         #data = model_to_dict(query, fields=('name', 'content', 'price', 'get_discount')) #il est plus pratique car il permet de creer automatiquement le dictionaire a partir du formulaire et y insere les données
    #return Response(data)
# Pour envoyer les données sous forme de json il faut créer un dictionaire