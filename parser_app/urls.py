from django.urls import path
from . import views

urlpatterns = [
    path("start_parsing/", views.ParserFormView.as_view(), name="parser"),
    path("film_parser/", views.FilmListView.as_view(), name="film_list"),
    # path('search_parser/', views.SearchParse.as_view(), name='search_parser')
]
