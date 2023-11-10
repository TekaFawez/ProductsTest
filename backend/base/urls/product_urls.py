#from base.views import getProducts,getProduct
from django.urls import path
from base.views import product_views as views


urlpatterns = [
    

    path('',views.getProducts),
    path('create/', views.createProduct, name="product-create"),
    path('upload/', views.uploadImage, name="image-upload"),



 

    path('<str:pk>',views.getProduct),

    path('update/<str:pk>/', views.updateProduct, name="product-update"),
    path('delete/<str:pk>/', views.deleteProduct, name="product-delete"),

]