from django.urls import path

from index import views

urlpatterns=[
    path(r"",views.get_index),
    path(r"index",views.get_index),
    path(r"news",views.get_news),
    path(r"service",views.get_service),
    path(r"about",views.get_about),
    path(r"solve",views.get_solve),
    path(r"construction",views.get_pmcon),
]