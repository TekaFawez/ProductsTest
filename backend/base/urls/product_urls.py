#from base.views import getProducts,getProduct
from django.urls import path
from base.views import product_views as views


urlpatterns = [
    

    path('',views.getProducts),



    path('<str:pk>',views.getProduct),

]