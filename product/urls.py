from django.urls import path
from product.views import * 
urlpatterns = [
    #path('<int:pk>/', DetailProductView.as_view()),
    path('create-list/', CreateProductView.as_view()),
    #path('list/', ListProduct.as_view()),
    #path('<int:pk>/update/', UpdateProductView.as_view()),
    #path('<int:pk>/delete/', DeletePreoductView.as_view()),
    path('create/', ProductMixinsView.as_view()),
    path('<int:pk>/detail/', ProductMixinsView.as_view()),
    path('<int:pk>/update/', ProductMixinsView.as_view()),
    path('list/', ProductMixinsView.as_view()),
    path('<int:pk>/delete/', ProductMixinsView.as_view()),

]
