from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    # path('message/<slug:category>/<slug:subcategory>/<slug:theme>/<int:number>/', views.message),
]