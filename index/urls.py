from django.urls import path

from index import views

urlpatterns=[
    path(r"",views.index),
    path(r"news",views.get_news),
]