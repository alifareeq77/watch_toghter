from django.urls import path

from party_app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create-party', views.create_party, name='create_party')
]
